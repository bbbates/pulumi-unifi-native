import pulumi
import pulumi_unifi_native as unifi

config = pulumi.Config()

# # User network, vlan 2, no IPv6, DHCP enabled
base_network = unifi.networkconf.Network("base",
                                         name="base",
                                         vlan=200,
                                         vlan_enabled=True,
                                         # this must be set otherwise the creation of the network won't succeed

                                         purpose="corporate",
                                         ip_subnet=f"192.168.200.1/24",
                                         # Note the incorrect subnet specification (final segment at 1, not 0)- this is what the API expects

                                         network_isolation_enabled=False,
                                         dhcpd_enabled=True,
                                         dhcpd_start="192.168.200.1",
                                         dhcpd_stop="192.168.200.254",
                                         ipv6_interface_type="none")

# FIXME: currently, creating devices is not possible -
# As per the terraform providers, the device should be imported first and then
# adopted. If the device has been imported, adding the adopted arg to the resource
# will cause the device to be adopted.
usg_3p = unifi.device.Device("usg_3p",
                             name="usg_3p",
                             adopted=True,
                             mac="dc:9f:db:00:00:01")
