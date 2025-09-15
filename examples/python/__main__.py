import pulumi
import pulumi_unifi_native as unifi

config = pulumi.Config()

# User network, vlan 2, no IPv6, DHCP enabled
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
                                                     ipv6_interface_type="none")

# IOT Network, vlan 3, IPv6 enabled, DHCP enabled with DHCP guard enabled
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
                                                dhcpd_ip1="192.168.1.1", # The first acceptable DHCP server address
                                                dhcpd_ip2="192.168.2.1", # The second acceptable DHCP server address

                                                # IPv6 settings
                                                ipv6_interface_type="static",
                                                ipv6_client_address_assignment="slaac",
                                                ipv6_setting_preference="auto",
                                                ipv6_subnet="fd00::/64")

# "ipv6_client_address_assignment":"slaac","ipv6_interface_type":"static","ipv6_ra_enabled":true,"ipv6_ra_preferred_lifetime":"14400","ipv6_ra_priority":"high","ipv6_setting_preference":"auto","ipv6_subnet":"fd00::/64","dhcpd_ip_1":"192.168.2.1","gateway_type":"default"}
