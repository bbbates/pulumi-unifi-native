package provider

import (
	"context"
	"crypto/tls"
	"github.com/cloudy-sky-software/pulumi-provider-framework/state"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource/plugin"
	"net/http"
	"os"
	"reflect"
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
	fwCallback.UnimplementedProviderCallback
	name    string
	version string

	siteID        string
	apiKey        string
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

func (p *unifiNativeProvider) extractOutput(outputs interface{}, id string, resourceType string, inputProperties *structpb.Struct) (map[string]interface{}, error) {
	outputType := reflect.TypeOf(outputs)
	if outputType.Kind() == reflect.Map {
		result := outputs.(map[string]interface{})

		if result["meta"] != nil && result["data"] != nil {
			return p.v1ApiExtractOutput(result, id, resourceType, inputProperties)
		}
		return p.v2ApiExtractOutput(result)
	} else if outputType.Kind() == reflect.Slice {
		logging.V(3).Infof("API v2 Data: %v", outputs)
		// only v2 APIs return slices of results
		items := outputs.([]interface{})

		for _, itemIt := range items {
			item := itemIt.(map[string]interface{})
			item["id"] = item["_id"] // need to massage the _id from unifi to match Pulumi's expectations
			item["Id"] = item["_id"]
			delete(item, "_id") // leaving the API _id field in the results seems to cause trouble with the refresh operation
			item["siteName"] = p.siteID
			item["site_name"] = p.siteID
		}

		result := make(map[string]interface{})
		result["items"] = items

		return result, nil
	}

	// All create/read/update endpoints return the object under the top-level "data" object.

	return nil, errors.New("API version output type could not be determined")
}

func (p *unifiNativeProvider) v1ApiExtractOutput(result map[string]interface{}, id string, resourceType string, inputProperties *structpb.Struct) (map[string]interface{}, error) {
	logging.V(3).Infof("API v1 Data: %v", result["data"])

	var dataList = result["data"].([]interface{})
	if (dataList == nil) || (len(dataList) == 0) {
		logging.V(3).Infof("No data found in output")

		if inputProperties == nil {
			return nil, errors.New("output did not contain a 'data' object and no input properties were provided (not an update operation?)")
		}

		// Unifi API will return an empty data array for an update if nothing has changed.
		// This is usually because something has gone wrong in the state mgmt for the Pulumi provider,
		// but failing the entire update because of it is usually not desired.
		// Return the existing input properties to ensure the resource still has state
		logging.V(3).Infof("Marshalled input properties: %v", inputProperties.AsMap())
		inputs, err := plugin.UnmarshalProperties(inputProperties, state.DefaultUnmarshalOpts)
		if err != nil {
			return nil, errors.Wrap(err, "unmarshaling new inputs in check method")
		}
		inputsMap := inputs.Mappable()
		inputsMap["id"] = id // inputProperties will not contain the id, so we need to add it here
		return inputsMap, nil
	}

	var data = dataList[0].(map[string]interface{})
	if data["_id"] == nil {
		return nil, errors.New("output did not contain an '_id' field")
	}
	data["id"] = data["_id"] // need to massage the _id from unifi to match Pulumi's expectations
	delete(data, "_id")      // leaving the API _id field in the results seems to cause trouble with the refresh operation
	data["siteId"] = p.siteID
	data["site_id"] = p.siteID

	// If the resource type if provided, and the type is a Device, then remove the unnecessary fields
	// and change the ID field to use the mac field
	if resourceType == "unifi-native:device:Device" {
		statPropertiesForRemoval := []string{
			"active_geo_info",
			"config_network_lan",
			"dhcp_excluded_ip_list",
			"last_uplink",
			"system-stats",
			"sys_stats",
			"detailed_states",
			"geo_info",
			"ids_ips_signature",
			"ipv4_active_leases",
			"last_geo_info",
			"last_wan_interfaces",
			"led_state",
			"ruleset_interfaces",
			"speedtest-status",
			"stat",
			"switch_caps",
			"udapi_version",
			"uplink",
			"uptime_stats",
			"wan1",
			"wan2",
		}
		for _, prop := range statPropertiesForRemoval {
			if _, ok := data[prop]; ok {
				logging.V(3).Infof("Removing property %s from the output data", prop)
				delete(data, prop)
			}
		}
	}

	return data, nil
}

func (p *unifiNativeProvider) v2ApiExtractOutput(result map[string]interface{}) (map[string]interface{}, error) {
	logging.V(3).Infof("API v2 Data: %v", result)

	if result["_id"] == nil {
		return nil, errors.New("output did not contain an '_id' field")
	}
	result["id"] = result["_id"] // need to massage the _id from unifi to match Pulumi's expectations
	result["Id"] = result["_id"]
	delete(result, "_id") // leaving the API _id field in the results seems to cause trouble with the refresh operation
	result["siteName"] = p.siteID
	result["site_name"] = p.siteID

	return result, nil
}

func (p *unifiNativeProvider) GetAuthorizationHeader() string {
	return p.apiKey
}

func (p *unifiNativeProvider) OnPreInvoke(_ context.Context, _ *pulumirpc.InvokeRequest, _ *http.Request) error {
	return nil
}

func (p *unifiNativeProvider) OnPostInvoke(_ context.Context, _ *pulumirpc.InvokeRequest, outputs interface{}) (map[string]interface{}, error) {
	return p.extractOutput(outputs, "", "", nil)
}

// OnConfigure is called by the provider framework when Pulumi calls Configure on
// the resource provider server.
func (p *unifiNativeProvider) OnConfigure(_ context.Context, req *pulumirpc.ConfigureRequest) (*pulumirpc.ConfigureResponse, error) {
	siteID, ok := req.GetVariables()["unifi-native:config:siteId"]
	if !ok {
		// Check if it's set as an env var.
		envVarNames := handler.GetSchemaSpec().Provider.InputProperties["siteId"].DefaultInfo.Environment
		for _, n := range envVarNames {
			v := os.Getenv(n)
			if v != "" {
				siteID = v
				ok = true
			}
		}

		// else use the default value
		if !ok {
			siteID = handler.GetSchemaSpec().Config.Variables["siteId"].Default.(string)
		}
	}

	logging.V(3).Infof("Configuring Site Id: %s", siteID)
	p.siteID = siteID

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
			InsecureSkipVerify: p.allowInsecure, //nolint:gosec  // Insecure TLS is allowable for this provider, let the user assess the risk
		},
	}

	return nil, nil
}

func (p *unifiNativeProvider) GetGlobalPathParams(_ context.Context, _ *pulumirpc.ConfigureRequest) (map[string]string, error) {
	if p.siteID != "" {
		return map[string]string{
			"siteId":    p.siteID,
			"site_id":   p.siteID,
			"siteName":  p.siteID,
			"site_name": p.siteID,
		}, nil
	}
	return nil, nil
}

// OnDiff checks what impacts a hypothetical update will have on the resource's properties.
func (p *unifiNativeProvider) OnDiff(_ context.Context, _ *pulumirpc.DiffRequest, _ string, _ *resource.ObjectDiff, _ *openapi3.MediaType) (*pulumirpc.DiffResponse, error) {
	return nil, nil
}

func (p *unifiNativeProvider) OnPreCreate(_ context.Context, _ *pulumirpc.CreateRequest, _ *http.Request) error {
	return nil
}

// OnPostCreate allocates a new instance of the provided resource and returns its unique ID afterwards.
func (p *unifiNativeProvider) OnPostCreate(_ context.Context, req *pulumirpc.CreateRequest, outputs interface{}) (map[string]interface{}, error) {
	return p.extractOutput(outputs, "", req.Type, nil)
}

func (p *unifiNativeProvider) OnPreRead(_ context.Context, req *pulumirpc.ReadRequest, httpReq *http.Request) error {
	if req.Type == "unifi-native:device:Device" {
		readDevice(req, httpReq)
	}

	return nil
}

var (
	listResourceTypes = []string{
		"unifi:index:StaticDns",
	}
)

func (p *unifiNativeProvider) OnPostRead(_ context.Context, req *pulumirpc.ReadRequest, outputs interface{}) (map[string]interface{}, error) {
	output, err := p.extractOutput(outputs, "", req.Type, nil)
	if err != nil {
		return output, err
	}

	if isListResourceType(req.Type) {
		for _, item := range output["items"].([]map[string]interface{}) {
			if item["id"] == req.Id {
				return item, nil
			}
		}
	}

	return output, nil
}

func isListResourceType(resourceType string) bool {
	for _, t := range listResourceTypes {
		if t == resourceType {
			return true
		}
	}

	return false
}

func (p *unifiNativeProvider) OnPreUpdate(_ context.Context, _ *pulumirpc.UpdateRequest, _ *http.Request) error {
	return nil
}

func (p *unifiNativeProvider) OnPostUpdate(_ context.Context, req *pulumirpc.UpdateRequest, _ http.Request, outputs interface{}) (map[string]interface{}, error) {
	return p.extractOutput(outputs, req.Id, req.Type, req.News)
}

func (p *unifiNativeProvider) OnPreDelete(_ context.Context, deleteRequest *pulumirpc.DeleteRequest, httpReq *http.Request) error {
	resourceTypeToken := fwRest.GetResourceTypeToken(deleteRequest.GetUrn())
	logging.V(3).Infof("Deleting resource with token [%s]", resourceTypeToken)
	if resourceTypeToken == "unifi-native:user:User" {
		logging.V(3).Infof("Deleting a User resource, overriding request...")
		err := deleteUser(deleteRequest, httpReq, handler)
		if err != nil {
			return err
		}
	}
	return nil
}

func (p *unifiNativeProvider) OnPostDelete(_ context.Context, _ *pulumirpc.DeleteRequest) error {
	return nil
}
