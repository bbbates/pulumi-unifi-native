import pulumi
import pulumi_unifi_native as unifi

config = pulumi.Config()

# User network, vlan 2, no IPv6, DHCP enabled
personal_devices = unifi.networkconf.Network("users",
                                             name="users",
                                             vlan=2,
                                             vlan_enabled=True, # this must be set otherwise the creation of the network won't succeed

                                             purpose="corporate",
                                             ip_subnet=f"192.168.2.1/24", # Note the incorrect subnet specification (final segment at 1, not 0)- this is what the API expects

                                             domain_name=f"users.internal",
                                             network_isolation_enabled=False,
                                             dhcpd_enabled=True,
                                             dhcpd_start="192.168.2.1",
                                             dhcpd_stop="192.168.2.254",
                                             ipv6_interface_type="none")

