package gen

import (
	"bytes"
	"encoding/json"

	"github.com/getkin/kin-openapi/openapi3"

	pschema "github.com/pulumi/pulumi/pkg/v3/codegen/schema"

	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"

	openapigen "github.com/cloudy-sky-software/pulschema/pkg"

	"github.com/bbbates/pulumi-unifi-native/provider/pkg/gen/examples"
)

const packageName = "unifi-native"

// PulumiSchema will generate a Pulumi schema for the given k8s schema.
func PulumiSchema(openapiDoc openapi3.T) (pschema.PackageSpec, openapigen.ProviderMetadata, openapi3.T) {
	pkg := pschema.PackageSpec{
		Name:        packageName,
		Description: "A Pulumi package for creating and managing Unifi OS resources.",
		DisplayName: "Unifi",
		License:     "Apache-2.0",
		Keywords: []string{
			"pulumi",
			packageName,
			"category/network",
			"kind/native",
		},
		Homepage:  "https://github.com/bbbates/pulumi-unifi-native",
		Publisher: "bbbates",

		Config: pschema.ConfigSpec{
			Variables: map[string]pschema.PropertySpec{
				"siteId": {
					Description: "The Human readable Stack identifier (e.g. 'notDefault') for the Unifi site to manage. Defaults to 'default'",
					TypeSpec:    pschema.TypeSpec{Type: "string"},
					Language: map[string]pschema.RawMessage{
						"csharp": rawMessage(map[string]interface{}{
							"name": "SiteId",
						}),
					},
					Default: "default",
					Secret:  false,
				},
				"apiKey": {
					Description: "The API key for an admin user, generated from the Unifi admin console",
					TypeSpec:    pschema.TypeSpec{Type: "string"},
					Language: map[string]pschema.RawMessage{
						"csharp": rawMessage(map[string]interface{}{
							"name": "ApiKey",
						}),
					},
					Secret: true,
				},
				"apiHost": {
					Description: "The URL Host name or IP Address for the Unifi API, e.g. 10.1.1.1",
					TypeSpec:    pschema.TypeSpec{Type: "string"},
					Language: map[string]pschema.RawMessage{
						"csharp": rawMessage(map[string]interface{}{
							"name": "ApiHost",
						}),
					},
					Secret: false,
				},
				"allowInsecure": {
					Description: "Implicitly trust the Unifi API server's TLS certificate. This is useful for testing, but should not be used in production.",
					TypeSpec:    pschema.TypeSpec{Type: "boolean"},
					Language: map[string]pschema.RawMessage{
						"csharp": rawMessage(map[string]interface{}{
							"name": "AllowInsecure",
						}),
					},
					Secret: false,
				},
			},
		},

		Provider: pschema.ResourceSpec{
			ObjectTypeSpec: pschema.ObjectTypeSpec{
				Description: "The provider type for the Unifi package.",
				Type:        "object",
			},
			InputProperties: map[string]pschema.PropertySpec{
				"siteId": {
					DefaultInfo: &pschema.DefaultSpec{
						Environment: []string{
							"UNIFI_SITE",
						},
					},
					Description: "The Human readable Stack identifier (e.g. 'notDefault') for the Unifi site to manage. Defaults to 'default'",
					TypeSpec:    pschema.TypeSpec{Type: "string"},
					Language: map[string]pschema.RawMessage{
						"csharp": rawMessage(map[string]interface{}{
							"name": "SiteId",
						}),
					},
					Default: "default",
					Secret:  false,
				},
				"apiKey": {
					DefaultInfo: &pschema.DefaultSpec{
						Environment: []string{
							"UNIFI_APIKEY",
						},
					},
					Description: "The Unifi API key.",
					TypeSpec:    pschema.TypeSpec{Type: "string"},
					Language: map[string]pschema.RawMessage{
						"csharp": rawMessage(map[string]interface{}{
							"name": "ApiKey",
						}),
					},
					Secret: true,
				},
				"apiHost": {
					DefaultInfo: &pschema.DefaultSpec{
						Environment: []string{
							"UNIFI_API_HOST",
						},
					},
					Description: "The URL Host name or IP Address for the Unifi API, e.g. 10.1.1.1.",
					TypeSpec:    pschema.TypeSpec{Type: "string"},
					Language: map[string]pschema.RawMessage{
						"csharp": rawMessage(map[string]interface{}{
							"name": "ApiHost",
						}),
					},
					Secret: false,
				},
				"allowInsecure": {
					DefaultInfo: &pschema.DefaultSpec{
						Environment: []string{
							"UNIFI_ALLOW_INSECURE",
						},
					},
					Description: "Implicitly trust the Unifi API server's TLS certificate. This is useful for testing, but should not be used in production.",
					TypeSpec:    pschema.TypeSpec{Type: "boolean"},
					Language: map[string]pschema.RawMessage{
						"csharp": rawMessage(map[string]interface{}{
							"name": "AllowInsecure",
						}),
					},
					Secret: false,
				},
			},
		},

		PluginDownloadURL: "github://api.github.com/bbbates/pulumi-unifi-native",
		Types:             map[string]pschema.ComplexTypeSpec{},
		Resources:         map[string]pschema.ResourceSpec{},
		Functions:         map[string]pschema.FunctionSpec{},
		Language:          map[string]pschema.RawMessage{},
	}

	csharpNamespaces := map[string]string{
		"unifi": "UNIFI",
		// TODO: Is this needed?
		"": "Provider",
	}

	openAPICtx := &openapigen.OpenAPIContext{
		Doc:                       openapiDoc,
		Pkg:                       &pkg,
		ExcludedPaths:             []string{},
		UseParentResourceAsModule: true,
		AllowedPluralResources: []string{
			"Ips",
			"SettingIps",
		},
	}

	providerMetadata, updatedOpenAPIDoc, err := openAPICtx.GatherResourcesFromAPI(csharpNamespaces)
	if err != nil {
		contract.Failf("generating resources from OpenAPI spec: %v", err)
	}

	// Add examples to resources
	for k, v := range examples.ResourceExample {
		if r, ok := pkg.Resources[k]; ok {
			r.Description += "\n\n" + v
			pkg.Resources[k] = r
		}
	}

	pkg.Language["csharp"] = rawMessage(map[string]interface{}{
		"rootNamespace": "Pulumi",
		"packageReferences": map[string]string{
			"Pulumi": "3.*",
		},
		"namespaces": csharpNamespaces,
		// TODO: What does this enable?
		// "dictionaryConstructors": true,
	})

	pkg.Language["go"] = rawMessage(map[string]interface{}{
		"importBasePath": "github.com/bbbates/pulumi-unifi-native/sdk/go/unifi-native",
	})
	pkg.Language["nodejs"] = rawMessage(map[string]interface{}{
		"packageName": "@bbbates/pulumi-unifi-native",
	})
	pkg.Language["python"] = rawMessage(map[string]interface{}{
		"packageName": "pulumi_unifi_native",
		"requires": map[string]string{
			"pulumi": ">=3.0.0,<4.0.0",
		},
		"pyproject": map[string]bool{
			"enabled": true,
		},
	})

	metadata := openapigen.ProviderMetadata{
		ResourceCRUDMap:  providerMetadata.ResourceCRUDMap,
		AutoNameMap:      providerMetadata.AutoNameMap,
		SDKToAPINameMap:  providerMetadata.SDKToAPINameMap,
		APIToSDKNameMap:  providerMetadata.APIToSDKNameMap,
		PathParamNameMap: providerMetadata.PathParamNameMap,
	}
	return pkg, metadata, updatedOpenAPIDoc
}

func rawMessage(v interface{}) pschema.RawMessage {
	var out bytes.Buffer
	encoder := json.NewEncoder(&out)
	encoder.SetEscapeHTML(false)
	err := encoder.Encode(v)
	contract.Assert(err == nil)
	return out.Bytes()
}
