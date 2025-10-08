package provider

import (
	"bytes"
	"io"
	"net/http"
	"slices"
)

// Don't forget to add the matching path to provider/pkg/gen/openapi_fixes.go:338
var notIdentifiableResources = []string{
	"unifi-native:network:GlobalConfig",
}

func isNonIdentifiableResource(resourceType string) bool {
	return slices.Contains(notIdentifiableResources, resourceType)
}

func deleteNonIdentifiableResource(httpReq *http.Request) error {
	// non-identifiable resources (resources that do not have an ID)
	// are deleted by sending a PUT request with an empty JSON object body
	httpReq.Method = "PUT"

	var buf io.Reader
	buf = bytes.NewBuffer([]byte(`{}`))
	httpReq.Body = io.NopCloser(buf)

	return nil
}
