package gen

import (
	"github.com/getkin/kin-openapi/openapi3"
)

// FixOpenAPIDoc applies patches to the raw OpenAPI spec
// before passing it to pulschema.
// TODO: remove null types, maybe fix default -> 200s?
// TODO: make the server URLs relative and remove the host and port vars
func FixOpenAPIDoc(openAPIDoc *openapi3.T) error {
	// So the hosts can be configured, change the server URLs to relative paths.
	// This will satisfy the Router.FindRoute method

	return nil
}
