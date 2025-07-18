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
from . import outputs
from ._inputs import *

__all__ = ['SettingIpsArgs', 'SettingIps']

@pulumi.input_type
class SettingIpsArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 ad_blocking_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['SettingIpsAdBlockingConfigurationsArgs']]]] = None,
                 ad_blocking_enabled: Optional[pulumi.Input[builtins.bool]] = None,
                 advanced_filtering_preference: Optional[pulumi.Input[builtins.str]] = None,
                 attr_hidden: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_hidden_id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_no_delete: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_no_edit: Optional[pulumi.Input[builtins.bool]] = None,
                 dns_filtering: Optional[pulumi.Input[builtins.bool]] = None,
                 dns_filters: Optional[pulumi.Input[Sequence[pulumi.Input['SettingIpsDNSFiltersArgs']]]] = None,
                 enabled_categories: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 enabled_networks: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 honeypot: Optional[pulumi.Input[Sequence[pulumi.Input['SettingIpsHoneypotArgs']]]] = None,
                 honeypot_enabled: Optional[pulumi.Input[builtins.bool]] = None,
                 ips_mode: Optional[pulumi.Input[builtins.str]] = None,
                 key: Optional[pulumi.Input[builtins.str]] = None,
                 memory_optimized: Optional[pulumi.Input[builtins.bool]] = None,
                 restrict_torrents: Optional[pulumi.Input[builtins.bool]] = None,
                 site_id: Optional[pulumi.Input[builtins.str]] = None,
                 suppression: Optional[pulumi.Input['SettingIpsSuppressionArgs']] = None):
        """
        The set of arguments for constructing a SettingIps resource.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if ad_blocking_configurations is not None:
            pulumi.set(__self__, "ad_blocking_configurations", ad_blocking_configurations)
        if ad_blocking_enabled is not None:
            pulumi.set(__self__, "ad_blocking_enabled", ad_blocking_enabled)
        if advanced_filtering_preference is not None:
            pulumi.set(__self__, "advanced_filtering_preference", advanced_filtering_preference)
        if attr_hidden is not None:
            pulumi.set(__self__, "attr_hidden", attr_hidden)
        if attr_hidden_id is not None:
            pulumi.set(__self__, "attr_hidden_id", attr_hidden_id)
        if attr_no_delete is not None:
            pulumi.set(__self__, "attr_no_delete", attr_no_delete)
        if attr_no_edit is not None:
            pulumi.set(__self__, "attr_no_edit", attr_no_edit)
        if dns_filtering is not None:
            pulumi.set(__self__, "dns_filtering", dns_filtering)
        if dns_filters is not None:
            pulumi.set(__self__, "dns_filters", dns_filters)
        if enabled_categories is not None:
            pulumi.set(__self__, "enabled_categories", enabled_categories)
        if enabled_networks is not None:
            pulumi.set(__self__, "enabled_networks", enabled_networks)
        if honeypot is not None:
            pulumi.set(__self__, "honeypot", honeypot)
        if honeypot_enabled is not None:
            pulumi.set(__self__, "honeypot_enabled", honeypot_enabled)
        if ips_mode is not None:
            pulumi.set(__self__, "ips_mode", ips_mode)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if memory_optimized is not None:
            pulumi.set(__self__, "memory_optimized", memory_optimized)
        if restrict_torrents is not None:
            pulumi.set(__self__, "restrict_torrents", restrict_torrents)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)
        if suppression is not None:
            pulumi.set(__self__, "suppression", suppression)

    @property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="adBlockingConfigurations")
    def ad_blocking_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SettingIpsAdBlockingConfigurationsArgs']]]]:
        return pulumi.get(self, "ad_blocking_configurations")

    @ad_blocking_configurations.setter
    def ad_blocking_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SettingIpsAdBlockingConfigurationsArgs']]]]):
        pulumi.set(self, "ad_blocking_configurations", value)

    @property
    @pulumi.getter(name="adBlockingEnabled")
    def ad_blocking_enabled(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "ad_blocking_enabled")

    @ad_blocking_enabled.setter
    def ad_blocking_enabled(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "ad_blocking_enabled", value)

    @property
    @pulumi.getter(name="advancedFilteringPreference")
    def advanced_filtering_preference(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "advanced_filtering_preference")

    @advanced_filtering_preference.setter
    def advanced_filtering_preference(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "advanced_filtering_preference", value)

    @property
    @pulumi.getter(name="attrHidden")
    def attr_hidden(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "attr_hidden")

    @attr_hidden.setter
    def attr_hidden(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "attr_hidden", value)

    @property
    @pulumi.getter(name="attrHiddenId")
    def attr_hidden_id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "attr_hidden_id")

    @attr_hidden_id.setter
    def attr_hidden_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "attr_hidden_id", value)

    @property
    @pulumi.getter(name="attrNoDelete")
    def attr_no_delete(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "attr_no_delete")

    @attr_no_delete.setter
    def attr_no_delete(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "attr_no_delete", value)

    @property
    @pulumi.getter(name="attrNoEdit")
    def attr_no_edit(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "attr_no_edit")

    @attr_no_edit.setter
    def attr_no_edit(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "attr_no_edit", value)

    @property
    @pulumi.getter(name="dnsFiltering")
    def dns_filtering(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "dns_filtering")

    @dns_filtering.setter
    def dns_filtering(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "dns_filtering", value)

    @property
    @pulumi.getter(name="dnsFilters")
    def dns_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SettingIpsDNSFiltersArgs']]]]:
        return pulumi.get(self, "dns_filters")

    @dns_filters.setter
    def dns_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SettingIpsDNSFiltersArgs']]]]):
        pulumi.set(self, "dns_filters", value)

    @property
    @pulumi.getter(name="enabledCategories")
    def enabled_categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "enabled_categories")

    @enabled_categories.setter
    def enabled_categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "enabled_categories", value)

    @property
    @pulumi.getter(name="enabledNetworks")
    def enabled_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "enabled_networks")

    @enabled_networks.setter
    def enabled_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "enabled_networks", value)

    @property
    @pulumi.getter
    def honeypot(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SettingIpsHoneypotArgs']]]]:
        return pulumi.get(self, "honeypot")

    @honeypot.setter
    def honeypot(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SettingIpsHoneypotArgs']]]]):
        pulumi.set(self, "honeypot", value)

    @property
    @pulumi.getter(name="honeypotEnabled")
    def honeypot_enabled(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "honeypot_enabled")

    @honeypot_enabled.setter
    def honeypot_enabled(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "honeypot_enabled", value)

    @property
    @pulumi.getter(name="ipsMode")
    def ips_mode(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "ips_mode")

    @ips_mode.setter
    def ips_mode(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "ips_mode", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="memoryOptimized")
    def memory_optimized(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "memory_optimized")

    @memory_optimized.setter
    def memory_optimized(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "memory_optimized", value)

    @property
    @pulumi.getter(name="restrictTorrents")
    def restrict_torrents(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "restrict_torrents")

    @restrict_torrents.setter
    def restrict_torrents(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "restrict_torrents", value)

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "site_id")

    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "site_id", value)

    @property
    @pulumi.getter
    def suppression(self) -> Optional[pulumi.Input['SettingIpsSuppressionArgs']]:
        return pulumi.get(self, "suppression")

    @suppression.setter
    def suppression(self, value: Optional[pulumi.Input['SettingIpsSuppressionArgs']]):
        pulumi.set(self, "suppression", value)


@pulumi.type_token("unifi-native:ips:SettingIps")
class SettingIps(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 ad_blocking_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingIpsAdBlockingConfigurationsArgs', 'SettingIpsAdBlockingConfigurationsArgsDict']]]]] = None,
                 ad_blocking_enabled: Optional[pulumi.Input[builtins.bool]] = None,
                 advanced_filtering_preference: Optional[pulumi.Input[builtins.str]] = None,
                 attr_hidden: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_hidden_id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_no_delete: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_no_edit: Optional[pulumi.Input[builtins.bool]] = None,
                 dns_filtering: Optional[pulumi.Input[builtins.bool]] = None,
                 dns_filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingIpsDNSFiltersArgs', 'SettingIpsDNSFiltersArgsDict']]]]] = None,
                 enabled_categories: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 enabled_networks: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 honeypot: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingIpsHoneypotArgs', 'SettingIpsHoneypotArgsDict']]]]] = None,
                 honeypot_enabled: Optional[pulumi.Input[builtins.bool]] = None,
                 ips_mode: Optional[pulumi.Input[builtins.str]] = None,
                 key: Optional[pulumi.Input[builtins.str]] = None,
                 memory_optimized: Optional[pulumi.Input[builtins.bool]] = None,
                 restrict_torrents: Optional[pulumi.Input[builtins.bool]] = None,
                 site_id: Optional[pulumi.Input[builtins.str]] = None,
                 suppression: Optional[pulumi.Input[Union['SettingIpsSuppressionArgs', 'SettingIpsSuppressionArgsDict']]] = None,
                 __props__=None):
        """
        Create a SettingIps resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SettingIpsArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SettingIps resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SettingIpsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SettingIpsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 ad_blocking_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingIpsAdBlockingConfigurationsArgs', 'SettingIpsAdBlockingConfigurationsArgsDict']]]]] = None,
                 ad_blocking_enabled: Optional[pulumi.Input[builtins.bool]] = None,
                 advanced_filtering_preference: Optional[pulumi.Input[builtins.str]] = None,
                 attr_hidden: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_hidden_id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_no_delete: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_no_edit: Optional[pulumi.Input[builtins.bool]] = None,
                 dns_filtering: Optional[pulumi.Input[builtins.bool]] = None,
                 dns_filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingIpsDNSFiltersArgs', 'SettingIpsDNSFiltersArgsDict']]]]] = None,
                 enabled_categories: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 enabled_networks: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 honeypot: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingIpsHoneypotArgs', 'SettingIpsHoneypotArgsDict']]]]] = None,
                 honeypot_enabled: Optional[pulumi.Input[builtins.bool]] = None,
                 ips_mode: Optional[pulumi.Input[builtins.str]] = None,
                 key: Optional[pulumi.Input[builtins.str]] = None,
                 memory_optimized: Optional[pulumi.Input[builtins.bool]] = None,
                 restrict_torrents: Optional[pulumi.Input[builtins.bool]] = None,
                 site_id: Optional[pulumi.Input[builtins.str]] = None,
                 suppression: Optional[pulumi.Input[Union['SettingIpsSuppressionArgs', 'SettingIpsSuppressionArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SettingIpsArgs.__new__(SettingIpsArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["ad_blocking_configurations"] = ad_blocking_configurations
            __props__.__dict__["ad_blocking_enabled"] = ad_blocking_enabled
            __props__.__dict__["advanced_filtering_preference"] = advanced_filtering_preference
            __props__.__dict__["attr_hidden"] = attr_hidden
            __props__.__dict__["attr_hidden_id"] = attr_hidden_id
            __props__.__dict__["attr_no_delete"] = attr_no_delete
            __props__.__dict__["attr_no_edit"] = attr_no_edit
            __props__.__dict__["dns_filtering"] = dns_filtering
            __props__.__dict__["dns_filters"] = dns_filters
            __props__.__dict__["enabled_categories"] = enabled_categories
            __props__.__dict__["enabled_networks"] = enabled_networks
            __props__.__dict__["honeypot"] = honeypot
            __props__.__dict__["honeypot_enabled"] = honeypot_enabled
            __props__.__dict__["ips_mode"] = ips_mode
            __props__.__dict__["key"] = key
            __props__.__dict__["memory_optimized"] = memory_optimized
            __props__.__dict__["restrict_torrents"] = restrict_torrents
            __props__.__dict__["site_id"] = site_id
            __props__.__dict__["suppression"] = suppression
        super(SettingIps, __self__).__init__(
            'unifi-native:ips:SettingIps',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SettingIps':
        """
        Get an existing SettingIps resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SettingIpsArgs.__new__(SettingIpsArgs)

        __props__.__dict__["id"] = None
        __props__.__dict__["ad_blocking_configurations"] = None
        __props__.__dict__["ad_blocking_enabled"] = None
        __props__.__dict__["advanced_filtering_preference"] = None
        __props__.__dict__["attr_hidden"] = None
        __props__.__dict__["attr_hidden_id"] = None
        __props__.__dict__["attr_no_delete"] = None
        __props__.__dict__["attr_no_edit"] = None
        __props__.__dict__["dns_filtering"] = None
        __props__.__dict__["dns_filters"] = None
        __props__.__dict__["enabled_categories"] = None
        __props__.__dict__["enabled_networks"] = None
        __props__.__dict__["honeypot"] = None
        __props__.__dict__["honeypot_enabled"] = None
        __props__.__dict__["ips_mode"] = None
        __props__.__dict__["key"] = None
        __props__.__dict__["memory_optimized"] = None
        __props__.__dict__["restrict_torrents"] = None
        __props__.__dict__["site_id"] = None
        __props__.__dict__["suppression"] = None
        return SettingIps(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="Id")
    def id(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="adBlockingConfigurations")
    def ad_blocking_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.SettingIpsAdBlockingConfigurations']]]:
        return pulumi.get(self, "ad_blocking_configurations")

    @property
    @pulumi.getter(name="adBlockingEnabled")
    def ad_blocking_enabled(self) -> pulumi.Output[Optional[builtins.bool]]:
        return pulumi.get(self, "ad_blocking_enabled")

    @property
    @pulumi.getter(name="advancedFilteringPreference")
    def advanced_filtering_preference(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "advanced_filtering_preference")

    @property
    @pulumi.getter(name="attrHidden")
    def attr_hidden(self) -> pulumi.Output[Optional[builtins.bool]]:
        return pulumi.get(self, "attr_hidden")

    @property
    @pulumi.getter(name="attrHiddenId")
    def attr_hidden_id(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "attr_hidden_id")

    @property
    @pulumi.getter(name="attrNoDelete")
    def attr_no_delete(self) -> pulumi.Output[Optional[builtins.bool]]:
        return pulumi.get(self, "attr_no_delete")

    @property
    @pulumi.getter(name="attrNoEdit")
    def attr_no_edit(self) -> pulumi.Output[Optional[builtins.bool]]:
        return pulumi.get(self, "attr_no_edit")

    @property
    @pulumi.getter(name="dnsFiltering")
    def dns_filtering(self) -> pulumi.Output[Optional[builtins.bool]]:
        return pulumi.get(self, "dns_filtering")

    @property
    @pulumi.getter(name="dnsFilters")
    def dns_filters(self) -> pulumi.Output[Optional[Sequence['outputs.SettingIpsDNSFilters']]]:
        return pulumi.get(self, "dns_filters")

    @property
    @pulumi.getter(name="enabledCategories")
    def enabled_categories(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        return pulumi.get(self, "enabled_categories")

    @property
    @pulumi.getter(name="enabledNetworks")
    def enabled_networks(self) -> pulumi.Output[Optional[Sequence[builtins.str]]]:
        return pulumi.get(self, "enabled_networks")

    @property
    @pulumi.getter
    def honeypot(self) -> pulumi.Output[Optional[Sequence['outputs.SettingIpsHoneypot']]]:
        return pulumi.get(self, "honeypot")

    @property
    @pulumi.getter(name="honeypotEnabled")
    def honeypot_enabled(self) -> pulumi.Output[Optional[builtins.bool]]:
        return pulumi.get(self, "honeypot_enabled")

    @property
    @pulumi.getter(name="ipsMode")
    def ips_mode(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "ips_mode")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="memoryOptimized")
    def memory_optimized(self) -> pulumi.Output[Optional[builtins.bool]]:
        return pulumi.get(self, "memory_optimized")

    @property
    @pulumi.getter(name="restrictTorrents")
    def restrict_torrents(self) -> pulumi.Output[Optional[builtins.bool]]:
        return pulumi.get(self, "restrict_torrents")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter
    def suppression(self) -> pulumi.Output[Optional['outputs.SettingIpsSuppression']]:
        return pulumi.get(self, "suppression")

