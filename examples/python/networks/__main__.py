import pulumi
import pulumi_unifi_native as unifi

config = pulumi.Config()

# # User network, vlan 2, no IPv6, DHCP enabled
personal_devices_network = unifi.networkconf.Network("users",
                                                     name="users",
                                                     vlan=2,
                                                     vlan_enabled=True,
                                                     # this must be set otherwise the creation of the network won't succeed

                                                     purpose="corporate",
                                                     ip_subnet=f"192.168.2.1/24",
                                                     # Note the incorrect subnet specification (final segment at 1, not 0)- this is what the API expects

                                                     domain_name=f"users.internal",
                                                     network_isolation_enabled=False,
                                                     dhcpd_enabled=True,
                                                     dhcpd_start="192.168.2.1",
                                                     dhcpd_stop="192.168.2.254",
                                                     ipv6_interface_type="none",

                                                     wan_gateway="0.0.0.0")
#
# # IOT Network, vlan 3, IPv6 enabled, DHCP enabled with DHCP guard enabled
iot_devices_network = unifi.networkconf.Network("iot",
                                                name="iot",
                                                vlan=3,
                                                vlan_enabled=True,
                                                # this must be set otherwise the creation of the network won't succeed

                                                purpose="corporate",
                                                ip_subnet=f"192.168.3.1/24",
                                                # Note the incorrect subnet specification (final segment at 1, not 0)- this is what the API expects

                                                domain_name=f"iot.internal",
                                                network_isolation_enabled=True,

                                                dhcpd_enabled=True,
                                                dhcpd_start="192.168.3.1",
                                                dhcpd_stop="192.168.3.254",
                                                dhcpd_conflict_checking=True,
                                                dhcpguard_enabled=True,
                                                dhcpd_ip1="192.168.1.1",  # The first acceptable DHCP server address
                                                dhcpd_ip2="192.168.2.1",  # The second acceptable DHCP server address

                                                # IPv6 settings
                                                ipv6_interface_type="static",
                                                ipv6_client_address_assignment="slaac",
                                                ipv6_setting_preference="auto",
                                                ipv6_subnet="fd00::/64")

# Guest network, vlan 4, no IPv6, DHCP enabled
guest_network = unifi.networkconf.Network("guests",
                                          name="guests",
                                          vlan=4,
                                          vlan_enabled=True,
                                          # this must be set otherwise the creation of the network won't succeed

                                          purpose="guest",
                                          ip_subnet=f"192.168.4.1/24",
                                          # Note the incorrect subnet specification (final segment at 1, not 0)- this is what the API expects

                                          domain_name=f"guests.internal",
                                          dhcpd_enabled=True,
                                          dhcpd_start="192.168.4.1",
                                          dhcpd_stop="192.168.4.254",
                                          ipv6_interface_type="none")

# "Global" network settings - these are the settings you would see under the list of networks in the networks settings UI

## Switch settings - how switches in the network behave when routing traffic between VLANs
global_switch_settings = unifi.global_switch.SettingGlobalSwitch("network_global_switch",
                                                                 # ACL isolation rules - Only enable if a supported device is present (not present in test fixture)
                                                                 # isolate all devices in the following networks
                                                                 # acl_device_isolation=[guest_network.id],
                                                                 # isolate all devices in guest_network from personal and iot networks
                                                                 # acl_l3_isolation=[unifi.global_switch.SettingGlobalSwitchAclL3IsolationArgs(
                                                                 #     source_network=guest_network.id,
                                                                 #     destination_networks=[iot_devices_network.id, personal_devices_network.id]
                                                                 # )],
                                                                 dhcp_snoop=True,
                                                                 flood_known_protocols=True)

## Multicast network settings
multicast_settings = unifi.network.GlobalConfig("network_global_multicast",
                                                # IGMP snooping on
                                                igmp_snooping_for="some",
                                                igmp_snooping_for_network_ids=[personal_devices_network.id, iot_devices_network.id, guest_network.id],

                                                # forward mDNS traffic between the IoT and Personal device networks
                                                mdns_enabled_for="some",
                                                mdns_enabled_for_network_ids=[personal_devices_network.id, iot_devices_network.id])



# Wireless LANs
default_wlan_group = unifi.wlangroup.WLANGroup("default", name="default")
ap_groups = unifi.apgroups.list_ap_groups().items

personal_devices_wlan = unifi.wlanconf.Wlan("wifi_personal",
                                            name="wifi_personal",
                                            # You would normally pull a secret from pulumi config here
                                            x_passphrase="this_is_the_secret!",

                                            wlangroup_id=default_wlan_group.id,
                                            ap_group_ids=[g.id for g in ap_groups],  # add to all AP groups

                                            security="wpapsk",
                                            wpa3_support=True,
                                            wpa3_transition=True,

                                            pmf_mode="optional",
                                            vlan=personal_devices_network.vlan,
                                            mcastenhance_enabled=True,
                                            bss_transition=True,
                                            wlan_band="both",
                                            wlan_bands=["2g", "5g", "6g"])

# Static DNS entries

## A entry -> nas.users.internal
nas_dns_entry = unifi.static_dns.StaticDnsEntry("nas_dns",
                                                record_type="A",
                                                key="nas.users.internal",
                                                value="192.168.2.100",
                                                enabled=True,
                                                ttl=600)

txt_entry = unifi.static_dns.StaticDnsEntry("txt_dns",
                                            record_type="TXT",
                                            key="__DUMMY_RECORD",
                                            value="DUMMYDUMMYDUMMY",
                                            enabled=True)

