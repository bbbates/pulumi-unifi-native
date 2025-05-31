package provider

import (
	"context"
	"crypto/tls"
	"fmt"
	"github.com/cloudy-sky-software/pulumi-provider-framework/state"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource/plugin"
	"net/http"
	"os"
	"time"

	"github.com/getkin/kin-openapi/openapi3"

	"github.com/pkg/errors"

	structpb "google.golang.org/protobuf/types/known/structpb"

	"github.com/pulumi/pulumi/pkg/v3/resource/provider"

	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/logging"
	pulumirpc "github.com/pulumi/pulumi/sdk/v3/proto/go"

	fwCallback "github.com/cloudy-sky-software/pulumi-provider-framework/callback"
	fwRest "github.com/cloudy-sky-software/pulumi-provider-framework/rest"
)

type unifiNativeProvider struct {
	name    string
	version string

	siteId        string
	apiKey        string
	apiHost       string
	allowInsecure bool
}

var (
	handler  *fwRest.Provider
	callback fwCallback.ProviderCallback
)

func makeProvider(host *provider.HostClient, name, version string, pulumiSchemaBytes, openapiDocBytes, metadataBytes []byte) (pulumirpc.ResourceProviderServer, error) {
	p := &unifiNativeProvider{
		name:    name,
		version: version,
	}

	callback = p
	rp, err := fwRest.MakeProvider(host, name, version, pulumiSchemaBytes, openapiDocBytes, metadataBytes, callback)

	handler = rp.(*fwRest.Provider)

	return rp, err
}

func (p *unifiNativeProvider) extractOutput(outputs interface{}, inputProperties *structpb.Struct) (map[string]interface{}, error) {
	// All create/read/update endpoints return the object under the top-level "data" object.

	var result = outputs.(map[string]interface{})
	if result["data"] != nil {
		logging.V(3).Infof("Data: %v", result["data"])
		var dataList = result["data"].([]interface{})
		if (dataList == nil) || (len(dataList) == 0) {
			logging.V(3).Infof("No data found in output")

			if inputProperties == nil {
				return nil, errors.New("output did not contain a 'data' object and no input properties were provided (not an update operation?)")
			} else {
				// Unifi API will return an empty data array for an update if nothing has changed.
				// This is usually because something has gone wrong in the state mgmt for the Pulumi provider,
				// but failing the entire update because of it is usually not desired.
				// Return the existing input properties to ensure the resource still has state
				logging.V(3).Infof("Marshalled input properties: %v", inputProperties.AsMap())
				inputs, err := plugin.UnmarshalProperties(inputProperties, state.DefaultUnmarshalOpts)
				if err != nil {
					return nil, errors.Wrap(err, "unmarshaling new inputs in check method")
				}
				return inputs.Mappable(), nil
			}
		}

		var data = dataList[0].(map[string]interface{})
		if data["_id"] == nil {
			return nil, errors.New("output did not contain an '_id' field")
		}
		data["id"] = data["_id"] // need to massage the _id from unifi to match Pulumi's expectations
		data["siteId"] = p.siteId
		data["site_id"] = p.siteId
		return data, nil
	}

	return nil, errors.New("output did not contain a 'data' object")
}

func (p *unifiNativeProvider) GetAuthorizationHeader() string {
	return p.apiKey
}

func (p *unifiNativeProvider) OnPreInvoke(_ context.Context, _ *pulumirpc.InvokeRequest, _ *http.Request) error {
	return nil
}

func (p *unifiNativeProvider) OnPostInvoke(_ context.Context, _ *pulumirpc.InvokeRequest, outputs interface{}) (map[string]interface{}, error) {
	return p.extractOutput(outputs, nil)
}

// OnConfigure is called by the provider framework when Pulumi calls Configure on
// the resource provider server.
func (p *unifiNativeProvider) OnConfigure(_ context.Context, req *pulumirpc.ConfigureRequest) (*pulumirpc.ConfigureResponse, error) {
	siteId, ok := req.GetVariables()["unifi-native:config:siteId"]
	if !ok {
		// Check if it's set as an env var.
		envVarNames := handler.GetSchemaSpec().Provider.InputProperties["siteId"].DefaultInfo.Environment
		for _, n := range envVarNames {
			v := os.Getenv(n)
			if v != "" {
				siteId = v
				ok = true
			}
		}

		// else use the default value
		if !ok {
			siteId = handler.GetSchemaSpec().Config.Variables["siteId"].Default.(string)
		}
	}

	logging.V(3).Infof("Configuring Site Id: %s", siteId)
	p.siteId = siteId
	if p.siteId != "" {
		handler.GetGlobalPathParams()["siteId"] = p.siteId
		handler.GetGlobalPathParams()["site_id"] = p.siteId
	}

	apiKey, ok := req.GetVariables()["unifi-native:config:apiKey"]
	if !ok {
		// Check if it's set as an env var.
		envVarNames := handler.GetSchemaSpec().Provider.InputProperties["apiKey"].DefaultInfo.Environment
		for _, n := range envVarNames {
			v := os.Getenv(n)
			if v != "" {
				apiKey = v
			}
		}

		// Return an error if the API key is still empty.
		if apiKey == "" {
			return nil, errors.New("apiKey is required")
		}
	}

	logging.V(3).Info("Configuring UnifiNative API key")
	p.apiKey = apiKey

	apiHost, ok := req.GetVariables()["unifi-native:config:apiHost"]
	if !ok {
		// Check if it's set as an env var.
		envVarNames := handler.GetSchemaSpec().Provider.InputProperties["apiHost"].DefaultInfo.Environment
		for _, n := range envVarNames {
			v := os.Getenv(n)
			if v != "" {
				apiHost = v
			}
		}

		// Return an error if the API URL is still empty.
		if apiHost == "" {
			return nil, errors.New("apiHost is required")
		}
	}

	logging.V(3).Info("Configuring Unifi API Host", apiHost)
	p.apiHost = apiHost

	logging.V(3).Infof("Fixing the base URL for the provider to use the configured API host: %s", p.apiHost)
	handler.SetBaseURL(fmt.Sprintf("https://%s%s", p.apiHost, handler.GetBaseURL()))
	logging.V(3).Infof("Base URL set to: %s", handler.GetBaseURL())

	allowInsecure, ok := req.GetVariables()["unifi-native:config:allowInsecure"]
	if !ok {
		// Check if it's set as an env var.
		envVarNames := handler.GetSchemaSpec().Provider.InputProperties["allowInsecure"].DefaultInfo.Environment
		for _, n := range envVarNames {
			v := os.Getenv(n)
			if v != "" {
				allowInsecure = v
			}
		}
	}

	logging.V(3).Info("Configuring AllowInsecure setting", allowInsecure)
	p.allowInsecure = allowInsecure == "true"

	// Need to override the HTTP Client Transport to ensure we can set the InsecureSkipVerify flag, if needed
	handler.GetHTTPClient().Transport = &http.Transport{
		Proxy:                 http.ProxyFromEnvironment,
		ForceAttemptHTTP2:     false,
		MaxIdleConns:          100,
		IdleConnTimeout:       90 * time.Second,
		TLSHandshakeTimeout:   10 * time.Second,
		ExpectContinueTimeout: 1 * time.Second,
		TLSClientConfig: &tls.Config{
			InsecureSkipVerify: p.allowInsecure,
		},
	}

	return &pulumirpc.ConfigureResponse{
		AcceptSecrets: true,
	}, nil
}

// OnDiff checks what impacts a hypothetical update will have on the resource's properties.
func (p *unifiNativeProvider) OnDiff(ctx context.Context, req *pulumirpc.DiffRequest, resourceTypeToken string, diff *resource.ObjectDiff, jsonReq *openapi3.MediaType) (*pulumirpc.DiffResponse, error) {
	return nil, nil
}

func (p *unifiNativeProvider) OnPreCreate(ctx context.Context, req *pulumirpc.CreateRequest, httpReq *http.Request) error {
	return nil
}

// OnPostCreate allocates a new instance of the provided resource and returns its unique ID afterwards.
func (p *unifiNativeProvider) OnPostCreate(ctx context.Context, req *pulumirpc.CreateRequest, outputs interface{}) (map[string]interface{}, error) {
	return p.extractOutput(outputs, nil)
}

func (p *unifiNativeProvider) OnPreRead(ctx context.Context, req *pulumirpc.ReadRequest, httpReq *http.Request) error {
	return nil
}

func (p *unifiNativeProvider) OnPostRead(ctx context.Context, req *pulumirpc.ReadRequest, outputs interface{}) (map[string]interface{}, error) {
	outputMap, err := p.extractOutput(outputs, nil)
	if err != nil {
		return nil, err
	}

	// transform the output map from the API names to the SDK names
	// because the Provider Framwork uses these values for the input map
	// as well, but does not transform them first, which ends up causing
	// the API-named properties to be stored in the input state, and the next `plumumi up` call will
	// try and update the resource again
	logging.V(3).Infof("Transforming output map from API names to SDK names: %v", outputMap)
	handler.TransformBody(ctx, outputMap, handler.GetMetadata().APIToSDKNameMap)
	logging.V(3).Infof("Transformed output map from API names to SDK names: %v", outputMap)
	return outputMap, nil
}

func (p *unifiNativeProvider) OnPreUpdate(ctx context.Context, req *pulumirpc.UpdateRequest, httpReq *http.Request) error {
	return nil
}

func (p *unifiNativeProvider) OnPostUpdate(ctx context.Context, req *pulumirpc.UpdateRequest, httpReq http.Request, outputs interface{}) (map[string]interface{}, error) {
	return p.extractOutput(outputs, req.News)
}

func (p *unifiNativeProvider) OnPreDelete(ctx context.Context, req *pulumirpc.DeleteRequest, httpReq *http.Request) error {
	return nil
}

func (p *unifiNativeProvider) OnPostDelete(ctx context.Context, req *pulumirpc.DeleteRequest) error {
	return nil
}
