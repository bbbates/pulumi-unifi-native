import pulumi
import pulumi_unifi_native as unifi

config = pulumi.Config()

# # User network, vlan 2, no IPv6, DHCP enabled
users_network = unifi.networkconf.Network("users",
                                          name="users",
                                          vlan=100,
                                          vlan_enabled=True,
                                          # this must be set otherwise the creation of the network won't succeed

                                          purpose="corporate",
                                          ip_subnet=f"192.168.100.1/24",
                                          # Note the incorrect subnet specification (final segment at 1, not 0)- this is what the API expects

                                          domain_name=f"users.internal",
                                          network_isolation_enabled=False,
                                          dhcpd_enabled=True,
                                          dhcpd_start="192.168.100.1",
                                          dhcpd_stop="192.168.100.254",
                                          ipv6_interface_type="none")

# Client devices (Users, or "Clients" in the Unifi UI)
nas_device = unifi.user.User("nas",
                             name="nas",
                             mac="2c:cc:66:55:33:33",
                             note="NAS",
                             fixed_ip="192.168.100.111",
                             use_fixedip=True,
                             network_id=users_network.id)

# Users can be grouped and have bandwidth limits applied
compute_group = unifi.usergroup.UserGroup("computeGroup",
                                          name="ComputeGroup",
                                          qos_rate_max_up=100000,
                                          qos_rate_max_down=100000)

compute_device_1 = unifi.user.User("compute1",
                                   name="compute1",
                                   mac="2c:cc:66:55:33:44",
                                   note="Compute1",
                                   usergroup_id=compute_group.id,
                                   network_id=users_network.id)

compute_device_2 = unifi.user.User("compute2",
                                   name="compute2",
                                   mac="2c:cc:66:55:33:55",
                                   note="Compute2",
                                   usergroup_id=compute_group.id,
                                   network_id=users_network.id)

# Users can be blocked
blocked_device = unifi.user.User("blockedDevice",
                                 name="blockedDevice",
                                 mac="2c:cc:66:55:33:66",
                                 note="Blocked Device",
                                 blocked=True,
                                 network_id=users_network.id)

# Users with DNS records
user_with_dns = unifi.user.User("user_with_dns",
                                name="user_with_dns",
                                mac="2c:cc:66:55:33:77",
                                note="User with DNS record",
                                network_id=users_network.id,
                                local_dns_record="with-dns",
                                local_dns_record_enabled=True,
                                fixed_ip="192.168.100.100",
                                use_fixedip=True)
