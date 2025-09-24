package provider

import (
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/logging"
	pulumirpc "github.com/pulumi/pulumi/sdk/v3/proto/go"
	"net/http"
	"regexp"
)

func readDevice(req *pulumirpc.ReadRequest, httpReq *http.Request) {
	// if the request is for a Device, and the ID is NOT a mac address (because the device has been previously imported)
	// change the last part of the URL path to use the mac address instead of the ID

	if req.Id != "" && len(req.Id) > 17 { // mac address is 17 characters long
		logging.V(3).Infof("Changing the ID in the request from %s to use the mac address", req.Id)
		re := regexp.MustCompile(`[^/]+$`)
		httpReq.URL.Path = re.ReplaceAllString(httpReq.URL.Path, req.Properties.Fields["mac"].GetStringValue())
		logging.V(3).Infof("New URL Path: %s", httpReq.URL.Path)
	} else {
		logging.V(3).Infof("Request ID is already a mac address or empty, no change needed")
	}
}

func cleanDeviceData(data map[string]interface{}) {
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
