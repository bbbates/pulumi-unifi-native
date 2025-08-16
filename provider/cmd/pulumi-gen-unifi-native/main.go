// Copyright 2022, Cloudy Sky Software LLC.

package main

import (
	"context"
	_ "embed"
	"github.com/getkin/kin-openapi/openapi3"

	"encoding/json"
	"flag"
	"fmt"
	"os"
	"path/filepath"

	"gopkg.in/yaml.v3"

	providerSchemaGen "github.com/bbbates/pulumi-unifi-native/provider/pkg/gen"
	providerVersion "github.com/bbbates/pulumi-unifi-native/provider/pkg/version"

	"github.com/pkg/errors"

	"github.com/pulumi/pulumi/pkg/v3/codegen/schema"

	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"
)

//go:embed openapi.yml
var openapiDocBytes []byte

//go:embed v2-openapi.yml
var v2openapiDocBytes []byte

// TemplateDir is the path to the base directory for code generator templates.
var TemplateDir string

// BaseDir is the path to the base pulumi-provider-template directory.
var BaseDir string

// Language is the SDK language.
type Language string

const (
	DotNet Language = "dotnet"
	Go     Language = "go"
	NodeJS Language = "nodejs"
	Python Language = "python"
	Schema Language = "schema"
)

func main() {
	flag.Usage = func() {
		const usageFormat = "Usage: %s <language>"
		_, err := fmt.Fprintf(flag.CommandLine.Output(), usageFormat, os.Args[0])
		contract.IgnoreError(err)
		flag.PrintDefaults()
	}

	var version string
	flag.StringVar(&version, "version", providerVersion.Version, "the provider version to record in the generated code")

	flag.Parse()
	args := flag.Args()
	if len(args) < 1 {
		flag.Usage()
		return
	}

	language := Language(args[0])

	switch language {
	case Schema:
		openAPIDoc := getOpenAPISpec(v2openapiDocBytes)

		err := providerSchemaGen.FixV2OpenAPIDoc(openAPIDoc)
		if err != nil {
			panic(err)
		}

		validateOpenAPISpec(openAPIDoc)

		schemaSpec, metadata, updatedOpenAPIDoc := providerSchemaGen.PulumiSchema(*openAPIDoc)
		providerDir := filepath.Join(".", "provider", "cmd", "pulumi-resource-unifi-native")
		mustWritePulumiSchema(schemaSpec, providerDir)

		// Write the metadata.json file as well.
		metadataBytes, _ := json.Marshal(metadata)
		mustWriteFile(providerDir, "metadata.json", metadataBytes)

		updatedOpenAPIDocBytes, _ := yaml.Marshal(updatedOpenAPIDoc)
		// Also copy the raw OpenAPI spec file to the provider dir.
		mustWriteFile(providerDir, "openapi_generated.yml", updatedOpenAPIDocBytes)
	default:
		panic(fmt.Sprintf("Unrecognized language '%s'", language))
	}
}

func getOpenAPISpec(data []byte) *openapi3.T {
	doc, err := openapi3.NewLoader().LoadFromData(data)
	if err != nil {
		contract.Failf("Failed to load openapi.yml: %v", err)
	}

	return doc
}

func validateOpenAPISpec(doc *openapi3.T) {
	ctx := context.Background()
	// For the purposes of building a Pulumi schema, we don't care about
	// examples that may have been added to the spec by the cloud provider,
	// ignore those as those tend to have errors.
	if err := doc.Validate(ctx, openapi3.DisableExamplesValidation()); err != nil {
		contract.Failf("OpenAPI spec failed validation: %v", err)
	}
}

func mustWritePulumiSchema(pkgSpec schema.PackageSpec, outdir string) {
	pkgSpec.Version = ""
	schemaJSON, err := json.MarshalIndent(pkgSpec, "", "    ")
	if err != nil {
		panic(errors.Wrap(err, "marshaling Pulumi schema"))
	}
	mustWriteFile(outdir, "schemav2.json", schemaJSON)
}

func mustWriteFile(rootDir, filename string, contents []byte) {
	outPath := filepath.Join(rootDir, filename)

	if err := os.MkdirAll(filepath.Dir(outPath), 0755); err != nil {
		panic(err)
	}
	// nolint: gosec
	err := os.WriteFile(outPath, contents, 0644)
	if err != nil {
		panic(err)
	}
}
