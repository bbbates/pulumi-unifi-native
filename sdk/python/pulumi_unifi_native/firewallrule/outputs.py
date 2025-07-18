# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

__all__ = [
    'FirewallRule',
    'Meta',
]

@pulumi.output_type
class FirewallRule(dict):
    def __init__(__self__, *,
                 id: Optional[builtins.str] = None,
                 action: Optional[builtins.str] = None,
                 attr_hidden: Optional[builtins.bool] = None,
                 attr_hidden_id: Optional[builtins.str] = None,
                 attr_no_delete: Optional[builtins.bool] = None,
                 attr_no_edit: Optional[builtins.bool] = None,
                 dst_address: Optional[builtins.str] = None,
                 dst_address_ipv6: Optional[builtins.str] = None,
                 dst_firewallgroup_ids: Optional[Sequence[builtins.str]] = None,
                 dst_networkconf_id: Optional[builtins.str] = None,
                 dst_networkconf_type: Optional[builtins.str] = None,
                 dst_port: Optional[builtins.str] = None,
                 enabled: Optional[builtins.bool] = None,
                 icmp_typename: Optional[builtins.str] = None,
                 icmpv6_typename: Optional[builtins.str] = None,
                 ipsec: Optional[builtins.str] = None,
                 logging: Optional[builtins.bool] = None,
                 name: Optional[builtins.str] = None,
                 protocol: Optional[builtins.str] = None,
                 protocol_match_excepted: Optional[builtins.bool] = None,
                 protocol_v6: Optional[builtins.str] = None,
                 rule_index: Optional[builtins.int] = None,
                 ruleset: Optional[builtins.str] = None,
                 setting_preference: Optional[builtins.str] = None,
                 site_id: Optional[builtins.str] = None,
                 src_address: Optional[builtins.str] = None,
                 src_address_ipv6: Optional[builtins.str] = None,
                 src_firewallgroup_ids: Optional[Sequence[builtins.str]] = None,
                 src_mac_address: Optional[builtins.str] = None,
                 src_networkconf_id: Optional[builtins.str] = None,
                 src_networkconf_type: Optional[builtins.str] = None,
                 src_port: Optional[builtins.str] = None,
                 state_established: Optional[builtins.bool] = None,
                 state_invalid: Optional[builtins.bool] = None,
                 state_new: Optional[builtins.bool] = None,
                 state_related: Optional[builtins.bool] = None):
        if id is not None:
            pulumi.set(__self__, "id", id)
        if action is not None:
            pulumi.set(__self__, "action", action)
        if attr_hidden is not None:
            pulumi.set(__self__, "attr_hidden", attr_hidden)
        if attr_hidden_id is not None:
            pulumi.set(__self__, "attr_hidden_id", attr_hidden_id)
        if attr_no_delete is not None:
            pulumi.set(__self__, "attr_no_delete", attr_no_delete)
        if attr_no_edit is not None:
            pulumi.set(__self__, "attr_no_edit", attr_no_edit)
        if dst_address is not None:
            pulumi.set(__self__, "dst_address", dst_address)
        if dst_address_ipv6 is not None:
            pulumi.set(__self__, "dst_address_ipv6", dst_address_ipv6)
        if dst_firewallgroup_ids is not None:
            pulumi.set(__self__, "dst_firewallgroup_ids", dst_firewallgroup_ids)
        if dst_networkconf_id is not None:
            pulumi.set(__self__, "dst_networkconf_id", dst_networkconf_id)
        if dst_networkconf_type is not None:
            pulumi.set(__self__, "dst_networkconf_type", dst_networkconf_type)
        if dst_port is not None:
            pulumi.set(__self__, "dst_port", dst_port)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if icmp_typename is not None:
            pulumi.set(__self__, "icmp_typename", icmp_typename)
        if icmpv6_typename is not None:
            pulumi.set(__self__, "icmpv6_typename", icmpv6_typename)
        if ipsec is not None:
            pulumi.set(__self__, "ipsec", ipsec)
        if logging is not None:
            pulumi.set(__self__, "logging", logging)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if protocol_match_excepted is not None:
            pulumi.set(__self__, "protocol_match_excepted", protocol_match_excepted)
        if protocol_v6 is not None:
            pulumi.set(__self__, "protocol_v6", protocol_v6)
        if rule_index is not None:
            pulumi.set(__self__, "rule_index", rule_index)
        if ruleset is not None:
            pulumi.set(__self__, "ruleset", ruleset)
        if setting_preference is not None:
            pulumi.set(__self__, "setting_preference", setting_preference)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)
        if src_address is not None:
            pulumi.set(__self__, "src_address", src_address)
        if src_address_ipv6 is not None:
            pulumi.set(__self__, "src_address_ipv6", src_address_ipv6)
        if src_firewallgroup_ids is not None:
            pulumi.set(__self__, "src_firewallgroup_ids", src_firewallgroup_ids)
        if src_mac_address is not None:
            pulumi.set(__self__, "src_mac_address", src_mac_address)
        if src_networkconf_id is not None:
            pulumi.set(__self__, "src_networkconf_id", src_networkconf_id)
        if src_networkconf_type is not None:
            pulumi.set(__self__, "src_networkconf_type", src_networkconf_type)
        if src_port is not None:
            pulumi.set(__self__, "src_port", src_port)
        if state_established is not None:
            pulumi.set(__self__, "state_established", state_established)
        if state_invalid is not None:
            pulumi.set(__self__, "state_invalid", state_invalid)
        if state_new is not None:
            pulumi.set(__self__, "state_new", state_new)
        if state_related is not None:
            pulumi.set(__self__, "state_related", state_related)

    @property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def action(self) -> Optional[builtins.str]:
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="attrHidden")
    def attr_hidden(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "attr_hidden")

    @property
    @pulumi.getter(name="attrHiddenId")
    def attr_hidden_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "attr_hidden_id")

    @property
    @pulumi.getter(name="attrNoDelete")
    def attr_no_delete(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "attr_no_delete")

    @property
    @pulumi.getter(name="attrNoEdit")
    def attr_no_edit(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "attr_no_edit")

    @property
    @pulumi.getter(name="dstAddress")
    def dst_address(self) -> Optional[builtins.str]:
        return pulumi.get(self, "dst_address")

    @property
    @pulumi.getter(name="dstAddressIpv6")
    def dst_address_ipv6(self) -> Optional[builtins.str]:
        return pulumi.get(self, "dst_address_ipv6")

    @property
    @pulumi.getter(name="dstFirewallgroupIds")
    def dst_firewallgroup_ids(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "dst_firewallgroup_ids")

    @property
    @pulumi.getter(name="dstNetworkconfId")
    def dst_networkconf_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "dst_networkconf_id")

    @property
    @pulumi.getter(name="dstNetworkconfType")
    def dst_networkconf_type(self) -> Optional[builtins.str]:
        return pulumi.get(self, "dst_networkconf_type")

    @property
    @pulumi.getter(name="dstPort")
    def dst_port(self) -> Optional[builtins.str]:
        return pulumi.get(self, "dst_port")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="icmpTypename")
    def icmp_typename(self) -> Optional[builtins.str]:
        return pulumi.get(self, "icmp_typename")

    @property
    @pulumi.getter(name="icmpv6Typename")
    def icmpv6_typename(self) -> Optional[builtins.str]:
        return pulumi.get(self, "icmpv6_typename")

    @property
    @pulumi.getter
    def ipsec(self) -> Optional[builtins.str]:
        return pulumi.get(self, "ipsec")

    @property
    @pulumi.getter
    def logging(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[builtins.str]:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="protocolMatchExcepted")
    def protocol_match_excepted(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "protocol_match_excepted")

    @property
    @pulumi.getter(name="protocolV6")
    def protocol_v6(self) -> Optional[builtins.str]:
        return pulumi.get(self, "protocol_v6")

    @property
    @pulumi.getter(name="ruleIndex")
    def rule_index(self) -> Optional[builtins.int]:
        return pulumi.get(self, "rule_index")

    @property
    @pulumi.getter
    def ruleset(self) -> Optional[builtins.str]:
        return pulumi.get(self, "ruleset")

    @property
    @pulumi.getter(name="settingPreference")
    def setting_preference(self) -> Optional[builtins.str]:
        return pulumi.get(self, "setting_preference")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter(name="srcAddress")
    def src_address(self) -> Optional[builtins.str]:
        return pulumi.get(self, "src_address")

    @property
    @pulumi.getter(name="srcAddressIpv6")
    def src_address_ipv6(self) -> Optional[builtins.str]:
        return pulumi.get(self, "src_address_ipv6")

    @property
    @pulumi.getter(name="srcFirewallgroupIds")
    def src_firewallgroup_ids(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "src_firewallgroup_ids")

    @property
    @pulumi.getter(name="srcMacAddress")
    def src_mac_address(self) -> Optional[builtins.str]:
        return pulumi.get(self, "src_mac_address")

    @property
    @pulumi.getter(name="srcNetworkconfId")
    def src_networkconf_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "src_networkconf_id")

    @property
    @pulumi.getter(name="srcNetworkconfType")
    def src_networkconf_type(self) -> Optional[builtins.str]:
        return pulumi.get(self, "src_networkconf_type")

    @property
    @pulumi.getter(name="srcPort")
    def src_port(self) -> Optional[builtins.str]:
        return pulumi.get(self, "src_port")

    @property
    @pulumi.getter(name="stateEstablished")
    def state_established(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "state_established")

    @property
    @pulumi.getter(name="stateInvalid")
    def state_invalid(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "state_invalid")

    @property
    @pulumi.getter(name="stateNew")
    def state_new(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "state_new")

    @property
    @pulumi.getter(name="stateRelated")
    def state_related(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "state_related")


@pulumi.output_type
class Meta(dict):
    def __init__(__self__, *,
                 msg: Optional[builtins.str] = None,
                 rc: Optional[builtins.str] = None):
        if msg is not None:
            pulumi.set(__self__, "msg", msg)
        if rc is not None:
            pulumi.set(__self__, "rc", rc)

    @property
    @pulumi.getter
    def msg(self) -> Optional[builtins.str]:
        return pulumi.get(self, "msg")

    @property
    @pulumi.getter
    def rc(self) -> Optional[builtins.str]:
        return pulumi.get(self, "rc")


