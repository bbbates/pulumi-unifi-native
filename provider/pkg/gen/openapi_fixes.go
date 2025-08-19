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
	//TODO

	// Prefix all paths with /proxy/network/api so they can be merged with the /v2 api
	for _, path := range openAPIDoc.Paths.InMatchingOrder() {
		openAPIDoc.Paths.Set("/proxy/network/api"+path, openAPIDoc.Paths.Find(path))
		openAPIDoc.Paths.Delete(path)
	}

	// replace the server list to support the mergeable api specs
	openAPIDoc.Servers = nil
	openAPIDoc.AddServer(&openapi3.Server{
		URL:         "https://unifi.ui.com/",
		Description: "Added by pulumi unifi native provider",
	})

	return nil
}

var V2PathsToRemove = []string{
	"/api/ai-fingerprint/site/{siteName}/station/{mac}/fingerprint_override",
	"/api/alarm-manager/publish-log",
	"/api/alarm-manager/reset-alarms",
	"/api/alarm-manager/scope/clients",
	"/api/alarm-manager/scope/devices",
	"/api/alarm-manager/scope/sites",
	"/api/cloud/application/event/{eventName}",
	"/api/device_info",
	"/api/features",
	"/api/features/{featureName}/exists",
	"/api/fingerprint_devices/{imageFolder}",
	"/api/log-levels/defaults",
	"/api/magicsitetositevpn/configs",
	"/api/magicsitetositevpn/speedtest/start",
	"/api/magicsitetositevpn/speedtest/stop",
	"/api/mfa/email/{id}/send",
	"/api/mfa/sms/{id}/send",
	"/api/notifications",
	"/api/notifications/dismiss-global",
	"/api/notifications/{name}",
	"/api/radio-ai/optimize/{calculationId}",
	"/api/settings/super-mgmt/defaults",
	"/api/sites",
	"/api/site/{siteName}/access-points/{apMac}/wifi-activity",
	"/api/site/{siteName}/access-points/{apMac}/wifi-stats",
	"/api/site/{siteName}/acl-rules/batch-delete",
	"/api/site/{siteName}/active-leases",
	"/api/site/{siteName}/active-leases/{networkId}",
	"/api/site/{siteName}/adopt-info/{deviceMac}",
	"/api/site/{siteName}/aggregated-dashboard",
	"/api/site/{siteName}/alert",
	"/api/site/{siteName}/alias",
	"/api/site/{siteName}/ap/{apMac}/last-scans",
	"/api/site/{siteName}/ap/{apMac}/neighbors",
	"/api/site/{siteName}/app-traffic-rate",
	"/api/site/{siteName}/bgp/config/all",
	"/api/site/{siteName}/client/{clientIp}/wifi_experience",
	"/api/site/{siteName}/client/{clientIp}/wifi_experience/incorrect",
	"/api/site/{siteName}/client/{clientMac}/24hr-activity",
	"/api/site/{siteName}/client/{clientMac}/24hr-satisfaction",
	"/api/site/{siteName}/client/{clientMac}/ap-stats",
	"/api/site/{siteName}/client/{clientMac}/experience",
	"/api/site/{siteName}/client/{clientMac}/experience/incorrect",
	"/api/site/{siteName}/client/{clientMac}/traffic-insights",
	"/api/site/{siteName}/clients/active",
	"/api/site/{siteName}/clients/history",
	"/api/site/{siteName}/clients/metadata",
	"/api/site/{siteName}/client/stats/fingerprint-os",
	"/api/site/{siteName}/clients/traffic-control",
	"/api/site/{siteName}/content-filtering/bulk",
	"/api/site/{siteName}/content-filtering/categories",
	"/api/site/{siteName}/content-filtering/create",
	"/api/site/{siteName}/country-traffic",
	"/api/site/{siteName}/dashboard",
	"/api/site/{siteName}/described-features",
	"/api/site/{siteName}/device/{deviceMac}/24hr-satisfaction",
	"/api/site/{siteName}/device/{deviceMac}/24hr-tx-retries",
	"/api/site/{siteName}/device/{deviceMac}/battery/action",
	"/api/site/{siteName}/device/{deviceMac}/clone-candidates",
	"/api/site/{siteName}/device/{deviceMac}/replace",
	"/api/site/{siteName}/device/{deviceMac}/replacement-candidates",
	"/api/site/{siteName}/device/{mac}/gateway/adopt-as-secondary",
	"/api/site/{siteName}/device/{mac}/wifi_experience/incorrect",
	"/api/site/{siteName}/device/{mac}/wireless-links",
	"/api/site/{siteName}/dhcp-import",
	"/api/site/{siteName}/dhcp/resolve-wan-subnet-conflict",
	"/api/site/{siteName}/downtime",
	"/api/site/{siteName}/downtime/{wanNetworkGroup}",
	"/api/site/{siteName}/dpi",
	"/api/site/{siteName}/features/{featureName}/exists",
	"/api/site/{siteName}/fingerprint/assets",
	"/api/site/{siteName}/fingerprint_override",
	"/api/site/{siteName}/firewall-app-blocks/create",
	"/api/site/{siteName}/firewall/migrate",
	"/api/site/{siteName}/firewall-policies/batch",
	"/api/site/{siteName}/firewall-policies/batch-delete",
	"/api/site/{siteName}/firewall-policies/batch-reorder",
	"/api/site/{siteName}/firewall-policies/defaults",
	"/api/site/{siteName}/firewall-rules/batch-delete",
	"/api/site/{siteName}/firewall-rules/combined-traffic-firewall-rules",
	"/api/site/{siteName}/firewall-rules/defaults",
	"/api/site/{siteName}/firewall/zone/batch-delete",
	"/api/site/{siteName}/firewall/zone/defaults",
	"/api/site/{siteName}/firewall/zone-matrix",
	"/api/site/{siteName}/floorplan/shape/batch",
	"/api/site/{siteName}/gateway/engine/features",
	"/api/site/{siteName}/gateway/engine/logs",
	"/api/site/{siteName}/gateway/engine/most-active-networks",
	"/api/site/{siteName}/gateway/engine/utilization",
	"/api/site/{siteName}/hotspot/clients",
	"/api/site/{siteName}/insights/filtering/overview",
	"/api/site/{siteName}/insights/filtering/watchlist",
	"/api/site/{siteName}/ips_alerts",
	"/api/site/{siteName}/isp/health",
	"/api/site/{siteName}/isp/health/compact",
	"/api/site/{siteName}/isp/status",
	"/api/site/{siteName}/lan/defaults",
	"/api/site/{siteName}/lan/enriched-configuration",
	"/api/site/{siteName}/lan/migrate-to-layer3/{networkConfId}",
	"/api/site/{siteName}/lcm/wakeup",
	"/api/site/{siteName}/loop-detection/info",
	"/api/site/{siteName}/loop-detection/recover-all-ports",
	"/api/site/{siteName}/{mac}/acl-entry-count",
	"/api/site/{siteName}/magicsitetositevpn/configs",
	"/api/site/{siteName}/mclag-groups/batch-delete",
	"/api/site/{siteName}/missing_fingerprint",
	"/api/site/{siteName}/network/generate-vlans",
	"/api/site/{siteName}/network/port-suggest",
	"/api/site/{siteName}/network_status",
	"/api/site/{siteName}/network/suggest",
	"/api/site/{siteName}/next-ai/{alertId}/mark-as-read",
	"/api/site/{siteName}/next-ai/{category}/mark-all-as-read",
	"/api/site/{siteName}/next-ai/logs",
	"/api/site/{siteName}/next-ai/mark-all-as-read",
	"/api/site/{siteName}/notifications",
	"/api/site/{siteName}/ospf/neighbors",
	"/api/site/{siteName}/pcap-get/{mac}",
	"/api/site/{siteName}/pcap-status/{mac}",
	"/api/site/{siteName}/pcap-stop/{mac}",
	"/api/site/{siteName}/pcap-upload/{mac}",
	"/api/site/{siteName}/ping/{mac}",
	"/api/site/{siteName}/ping-start/{mac}",
	"/api/site/{siteName}/ping-stop/{mac}",
	"/api/site/{siteName}/port-forward/batch-delete",
	"/api/site/{siteName}/port-profiles/defaults",
	"/api/site/{siteName}/qos-rules/batch",
	"/api/site/{siteName}/qos-rules/batch-delete",
	"/api/site/{siteName}/qos-rules/batch-reorder",
	"/api/site/{siteName}/radio-ai/optimize/{calculationId}",
	"/api/site/{siteName}/radio-ai/optimize/preview",
	"/api/site/{siteName}/radius/users",
	"/api/site/{siteName}/radius/users/batch_add",
	"/api/site/{siteName}/radius/users/batch_delete",
	"/api/site/{siteName}/radius/users/batch_update",
	"/api/site/{siteName}/score",
	"/api/site/{siteName}/score/details/{scoreId}",
	"/api/site/{siteName}/search",
	"/api/site/{siteName}/settings/connectivity/defaults",
	"/api/site/{siteName}/settings/doh/available-server-names",
	"/api/site/{siteName}/settings/doh/defaults",
	"/api/site/{siteName}/settings/element_adopt/defaults",
	"/api/site/{siteName}/settings/global_nat/defaults",
	"/api/site/{siteName}/settings/global_switch/defaults",
	"/api/site/{siteName}/settings/guest-access/reset",
	"/api/site/{siteName}/settings/ips/advanced-filtering-auto-values",
	"/api/site/{siteName}/settings/ips/advanced-filtering-defaults",
	"/api/site/{siteName}/settings/ips/available-categories",
	"/api/site/{siteName}/settings/mgmt/device_upgrade/disable",
	"/api/site/{siteName}/settings/mgmt/device_upgrade/enable",
	"/api/site/{siteName}/settings/mgmt/direct_connect/disable",
	"/api/site/{siteName}/settings/mgmt/direct_connect/enable",
	"/api/site/{siteName}/settings/netflow/defaults",
	"/api/site/{siteName}/settings/ntp/defaults",
	"/api/site/{siteName}/settings/roaming_assistant/defaults",
	"/api/site/{siteName}/settings/shortcuts",
	"/api/site/{siteName}/settings/traffic_flow/defaults",
	"/api/site/{siteName}/settings/usg/defaults",
	"/api/site/{siteName}/settings/wifiai/defaults",
	"/api/site/{siteName}/shadowmode/managed/begin-adoption",
	"/api/site/{siteName}/shadowmode/managed/check-vrrp",
	"/api/site/{siteName}/shadowmode/managed/complete-adoption",
	"/api/site/{siteName}/shadowmode/managed/rollback",
	"/api/site/{siteName}/shadowmode/override",
	"/api/site/{siteName}/shadowmode/rollback",
	"/api/site/{siteName}/shadowmode/status",
	"/api/site/{siteName}/site-feature-migration",
	"/api/site/{siteName}/smart-subnet",
	"/api/site/{siteName}/speedtest",
	"/api/site/{siteName}/speedtest/csv",
	"/api/site/{siteName}/speedtest/latest",
	"/api/site/{siteName}/speedtest/latest-per-wan",
	"/api/site/{siteName}/station/{mac}/missing_fingerprint",
	"/api/site/{siteName}/station/{mac}/wifi_experience/incorrect",
	"/api/site/{siteName}/system-log/admin-access",
	"/api/site/{siteName}/system-log/admin-activity",
	"/api/site/{siteName}/system-log/admin-activity/{id}",
	"/api/site/{siteName}/system-log/alarm/{alarmId}",
	"/api/site/{siteName}/system-log/all",
	"/api/site/{siteName}/system-log/ap-logs",
	"/api/site/{siteName}/system-log/ap-logs/display-options/aps",
	"/api/site/{siteName}/system-log/client-alert",
	"/api/site/{siteName}/system-log/client-connection/{clientMac}",
	"/api/site/{siteName}/system-log/critical",
	"/api/site/{siteName}/system-log/critical/{alertId}/mark-as-read",
	"/api/site/{siteName}/system-log/critical/mark-all-as-read",
	"/api/site/{siteName}/system-log/device-alert",
	"/api/site/{siteName}/system-log/display-options/admins",
	"/api/site/{siteName}/system-log/{id}/cef",
	"/api/site/{siteName}/system-log/ips_alert/{alertId}",
	"/api/site/{siteName}/system-log/network-ai/clear-all",
	"/api/site/{siteName}/system-log/network-ai/logs",
	"/api/site/{siteName}/system-log/next-ai-alert",
	"/api/site/{siteName}/system-log/remote-settings",
	"/api/site/{siteName}/system-log/setting/defaults",
	"/api/site/{siteName}/system-log/system-critical-alert",
	"/api/site/{siteName}/system-log/threat-alert",
	"/api/site/{siteName}/system-log/threat/display-options/clients",
	"/api/site/{siteName}/system-log/threats",
	"/api/site/{siteName}/system-log/triggers",
	"/api/site/{siteName}/system-log/triggers/display-options/hosts",
	"/api/site/{siteName}/system-log/update-alert",
	"/api/site/{siteName}/system-log/vpn-alert",
	"/api/site/{siteName}/teleport/access-request",
	"/api/site/{siteName}/teleport/disconnect-client/{clientId}",
	"/api/site/{siteName}/teleport/invitation-history",
	"/api/site/{siteName}/teleport/token",
	"/api/site/{siteName}/teleport/token/{tokenId}",
	"/api/site/{siteName}/topology",
	"/api/site/{siteName}/traffic",
	"/api/site/{siteName}/traffic-flow-latest-statistics",
	"/api/site/{siteName}/traffic-flows/alarm/{alarmId}",
	"/api/site/{siteName}/traffic-flows/export",
	"/api/site/{siteName}/traffic-flows/filter-data",
	"/api/site/{siteName}/traffic-flows/{id}",
	"/api/site/{siteName}/traffic-flows", // this might be needed, but ignore for now
	"/api/site/{siteName}/traffic/{mac}",
	"/api/site/{siteName}/traffic-rate",
	"/api/site/{siteName}/trafficroutes/{routeId}/disable",
	"/api/site/{siteName}/trafficroutes/{routeId}/enable",
	"/api/site/{siteName}/uid/client-info/{clientMac}",
	"/api/site/{siteName}/uid/vpn-server/kick/{username}",
	"/api/site/{siteName}/uid/wlan",
	"/api/site/{siteName}/uid/wlan/{wlanId}",
	"/api/site/{siteName}/utilization/last_days",
	"/api/site/{siteName}/utilization/time_range",
	"/api/site/{siteName}/vendor-ids",
	"/api/site/{siteName}/visual-programming/virtual-network",
	"/api/site/{siteName}/visual-programming/virtual-network/{networkId}",
	"/api/site/{siteName}/vpn/client-connections",
	"/api/site/{siteName}/vpn/l2tp/defaults",
	"/api/site/{siteName}/vpn/{networkId}/restart",
	"/api/site/{siteName}/vpn/openvpn/certificates",
	"/api/site/{siteName}/vpn/openvpn/{networkId}/configuration", // this might be useful to someone, but doesn't parse correctly
	"/api/site/{siteName}/wan/ddns",
	"/api/site/{siteName}/wan/defaults",
	"/api/site/{siteName}/wan/enriched-configuration",
	"/api/site/{siteName}/wan/load-balancing/status",
	"/api/site/{siteName}/wan/magic/speedtest",
	"/api/site/{siteName}/wan/magic/subscription",
	"/api/site/{siteName}/wan/provider-capabilities/legacy",
	"/api/site/{siteName}/wan-slas/batch-delete",
	"/api/site/{siteName}/wan/{wanNetworkGroup}/isp-status",
	"/api/site/{siteName}/warnings",
	"/api/site/{siteName}/wifi-connectivity",
	"/api/site/{siteName}/wifiman/{clientIp}",
	"/api/site/{siteName}/wifiman/{clientIp}/feedback",
	"/api/site/{siteName}/wifiman/{clientIp}/feedback/{feedbackId}/wifi_experience",
	"/api/site/{siteName}/wifi-stats/aps",
	"/api/site/{siteName}/wifi-stats/channelization",
	"/api/site/{siteName}/wifi-stats/details",
	"/api/site/{siteName}/wifi-stats/radios",
	"/api/site/{siteName}/wireguard/{networkId}/users",
	"/api/site/{siteName}/wireguard/{networkId}/users/batch",
	"/api/site/{siteName}/wireguard/{networkId}/users/batch_delete",
	"/api/site/{siteName}/wireguard/users",
	"/api/site/{siteName}/wireguard/users/existing-subnets",
	"/api/site/{siteName}/wlan/defaults",
	"/api/site/{siteName}/wlan/enriched-configuration",
	"/api/site/{siteName}/wlan/{wlanId}/statistics/hourly",
	"/api/system/event/{eventType}/first",
	"/api/timezones",
	"/api/ucore/backup-archive/export",
	"/api/ucore/backup-archive/import",
	"/api/ucore/backup/export",
	"/api/ucore/backup/import",
	"/api/ucore/devices/update",
	"/api/ucore/devices/update/all",
	"/api/ucore/support-dump",
	"/api/uisp/status",
	"/api/vpn/auto/sites",
	"/docs/system-log/events",
	"/docs/system-log/messages",
	"/docs/system-log/sections",
	"/api/site/{siteName}/device/{deviceMac}/battery/update",
	"/api/site/default/ips_alerts",
	"/api/site/{siteName}/shadowmode/managed/group",
	"/api/site/{siteName}/excluded-ips/{networkId}",
	"/api/site/{siteName}/vpn/connections",
	"/api/site/{siteName}/wan/magic/configuration",
	"/api/site/{siteName}/settings/teleport/defaults",
	"/api/site/{siteName}/bgp/config/{deviceMac}",
	"/api/site/{siteName}/bgp/config",
	"/api/site/{siteName}/vpn/openvpn/configuration",
}

var V2ProblematicSchemasToRemove = []string{
	"WLAN Configuration",
	"UnifiDeviceDto",
}

func FixV2OpenAPIDoc(openAPIDoc *openapi3.T) error {
	// remove license from header, just causes issues
	openAPIDoc.Info.License = nil

	// remove paths that don't belong in a pulumi provider
	for _, path := range V2PathsToRemove {
		openAPIDoc.Paths.Delete(path)
	}

	// add the /v2 prefix to the start of each path
	for _, path := range openAPIDoc.Paths.InMatchingOrder() {
		openAPIDoc.Paths.Set("/v2"+path, openAPIDoc.Paths.Find(path))
		openAPIDoc.Paths.Delete(path)
	}

	// remove problematic schemas that aren't used and cause issues if left
	// TODO: this should be improved to remove all orphaned schemas, to tidy things up
	for _, schemaRef := range V2ProblematicSchemasToRemove {
		delete(openAPIDoc.Components.Schemas, schemaRef)
		fmt.Printf("Removing schema: %s\n", schemaRef)
		if openAPIDoc.Components.Schemas[schemaRef] != nil {
			fmt.Printf(">>>>> %s still exists!\n", schemaRef)
		}
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

// TODO Fixes v2:
/*
- "Configuration" Wlan Load balancing namespace?
-
*/
