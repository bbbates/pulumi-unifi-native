import pulumi
import pulumi_unifi_native as unifi

config = pulumi.Config()

personal_devices = unifi.networkconf.Network("personal_device",
                                             name="personal_device",
                                             vlan=2,

                                             purpose="corporate",
                                             ip_subnet=f"192.168.2.0/24",

                                             domain_name=f"personal.internal",
                                             network_isolation_enabled=False,
                                             dhcpd_enabled=True,
                                             dhcpd_start="192.168.2.1/24",
                                             dhcpd_stop="192.168.2.253/24",
                                             ipv6_interface_type="none")
