package gen

import (
	"fmt"
	"github.com/cloudy-sky-software/pulschema/pkg"
	"github.com/getkin/kin-openapi/openapi3"
)

// FixOpenAPIDoc applies patches to the raw OpenAPI spec
// before passing it to pulschema and validating it
// TODO: remove null types, maybe fix default -> 200s?
// TODO: make the server URLs relative and remove the host and port vars
func FixOpenAPIDoc(openAPIDoc *openapi3.T) error {
	// So the hosts can be configured, change the server URLs to relative paths.
	// This will satisfy the Router.FindRoute method

	return nil
}

var V2PathsToRemove = []string{
	"/api/site/{siteName}/alert",
	"/api/site/{siteName}/wireguard/{networkId}/users/batch",
	"/api/site/{siteName}/wifiman/{clientIp}/feedback/{feedbackId}/wifi_experience",
	"/api/device_info",
	"/api/alarm-manager/reset-alarms",
	"/api/site/{siteName}/wifi-stats/details",
	"/api/site/{siteName}/wifi-stats/channelization",
	"/api/site/{siteName}/visual-programming/virtual-network",
	"/api/site/{siteName}/traffic-flows/export",
	"/api/site/{siteName}/traffic-flows/filter-data",
	"/api/site/{siteName}/traffic-flows/alarm/{alarmId}",
	"/api/site/{siteName}/traffic-flows", // this might be needed, but ignore for now
	"/api/site/{siteName}/system-log/critical/mark-all-as-read",
	"/api/site/{siteName}/system-log/admin-activity",
	"/api/site/{siteName}/system-log/admin-access",
	"/api/site/{siteName}/speedtest/csv",
	"/api/site/{siteName}/settings/ips/advanced-filtering-defaults",
	"/api/site/{siteName}/settings/ips/advanced-filtering-auto-values",
	"/api/site/{siteName}/settings/global_switch/defaults",
	"/api/site/{siteName}/settings/guest-access/reset",
	"/api/site/{siteName}/next-ai/mark-all-as-read",
	"/api/site/{siteName}/lcm/wakeup",
	"/api/site/{siteName}/lan/enriched-configuration",
	"/api/site/{siteName}/lan/defaults",
	"/api/site/{siteName}/hotspot/clients",
	"/api/site/{siteName}/clients/history",
	"/api/fingerprint_devices/{imageFolder}",
	"/api/features/{featureName}/exists",
	"/api/site/{siteName}/vpn/openvpn/{networkId}/configuration", // this might be useful to someone, but doesn't parse correctly
	"/api/site/{siteName}/visual-programming/virtual-network/{networkId}",
	"/api/site/{siteName}/trafficroutes/{routeId}/enable",
	"/api/site/{siteName}/trafficroutes/{routeId}/disable",
	"/api/site/{siteName}/traffic-flows/{id}",
	"/api/site/{siteName}/system-log/critical/{alertId}/mark-as-read",
	"/api/site/{siteName}/system-log/admin-activity/{id}",
	"/api/site/{siteName}/next-ai/{category}/mark-all-as-read",
	"/api/site/{siteName}/next-ai/{alertId}/mark-as-read",
	"/api/site/{siteName}/lan/migrate-to-layer3/{networkConfId}",
	"/api/site/{siteName}/features/{featureName}/exists",
	"/api/site/{siteName}/device/{deviceMac}/24hr-tx-retries",
	"/api/site/{siteName}/device/{deviceMac}/24hr-satisfaction",
	"/api/site/{siteName}/client/{clientMac}/24hr-satisfaction",
	"/api/site/{siteName}/client/{clientMac}/24hr-activity",
	"/api/site/{siteName}/active-leases",
	"/api/site/{siteName}/active-leases/{networkId}",
	"/api/magicsitetositevpn/speedtest/start",
	"/api/site/{siteName}/wan/magic/speedtest",
	"/api/site/{siteName}/teleport/access-request",
	"/api/site/{siteName}/{mac}/acl-entry-count",
}

func FixV2OpenAPIDoc(openAPIDoc *openapi3.T) error {
	// remove license from header, just causes issues
	openAPIDoc.Info.License = nil

	// remove paths that don't belong in a pulumi provider
	for _, path := range V2PathsToRemove {
		openAPIDoc.Paths.Delete(path)
	}

	// Fix all the component schema names that have space in their names, convert these to CamelCase
	newSchemas := make(map[string]*openapi3.SchemaRef)
	for key, schema := range openAPIDoc.Components.Schemas {
		fmt.Printf("Fixing schema: %s -> %s\n", key, pkg.ToPascalCase(key))
		newSchemas[pkg.ToPascalCase(key)] = schema

	}

	openAPIDoc.Components.Schemas = newSchemas

	return nil
}
