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

__all__ = ['SettingEtherLightingArgs', 'SettingEtherLighting']

@pulumi.input_type
class SettingEtherLightingArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_hidden: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_hidden_id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_no_delete: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_no_edit: Optional[pulumi.Input[builtins.bool]] = None,
                 key: Optional[pulumi.Input[builtins.str]] = None,
                 network_overrides: Optional[pulumi.Input[Sequence[pulumi.Input['SettingEtherLightingNetworkOverridesArgs']]]] = None,
                 site_id: Optional[pulumi.Input[builtins.str]] = None,
                 speed_overrides: Optional[pulumi.Input[Sequence[pulumi.Input['SettingEtherLightingSpeedOverridesArgs']]]] = None):
        """
        The set of arguments for constructing a SettingEtherLighting resource.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if attr_hidden is not None:
            pulumi.set(__self__, "attr_hidden", attr_hidden)
        if attr_hidden_id is not None:
            pulumi.set(__self__, "attr_hidden_id", attr_hidden_id)
        if attr_no_delete is not None:
            pulumi.set(__self__, "attr_no_delete", attr_no_delete)
        if attr_no_edit is not None:
            pulumi.set(__self__, "attr_no_edit", attr_no_edit)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if network_overrides is not None:
            pulumi.set(__self__, "network_overrides", network_overrides)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)
        if speed_overrides is not None:
            pulumi.set(__self__, "speed_overrides", speed_overrides)

    @property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

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
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="networkOverrides")
    def network_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SettingEtherLightingNetworkOverridesArgs']]]]:
        return pulumi.get(self, "network_overrides")

    @network_overrides.setter
    def network_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SettingEtherLightingNetworkOverridesArgs']]]]):
        pulumi.set(self, "network_overrides", value)

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "site_id")

    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "site_id", value)

    @property
    @pulumi.getter(name="speedOverrides")
    def speed_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SettingEtherLightingSpeedOverridesArgs']]]]:
        return pulumi.get(self, "speed_overrides")

    @speed_overrides.setter
    def speed_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SettingEtherLightingSpeedOverridesArgs']]]]):
        pulumi.set(self, "speed_overrides", value)


@pulumi.type_token("unifi-native:ether_lighting:SettingEtherLighting")
class SettingEtherLighting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_hidden: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_hidden_id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_no_delete: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_no_edit: Optional[pulumi.Input[builtins.bool]] = None,
                 key: Optional[pulumi.Input[builtins.str]] = None,
                 network_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingEtherLightingNetworkOverridesArgs', 'SettingEtherLightingNetworkOverridesArgsDict']]]]] = None,
                 site_id: Optional[pulumi.Input[builtins.str]] = None,
                 speed_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingEtherLightingSpeedOverridesArgs', 'SettingEtherLightingSpeedOverridesArgsDict']]]]] = None,
                 __props__=None):
        """
        Create a SettingEtherLighting resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SettingEtherLightingArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SettingEtherLighting resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SettingEtherLightingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SettingEtherLightingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_hidden: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_hidden_id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_no_delete: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_no_edit: Optional[pulumi.Input[builtins.bool]] = None,
                 key: Optional[pulumi.Input[builtins.str]] = None,
                 network_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingEtherLightingNetworkOverridesArgs', 'SettingEtherLightingNetworkOverridesArgsDict']]]]] = None,
                 site_id: Optional[pulumi.Input[builtins.str]] = None,
                 speed_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingEtherLightingSpeedOverridesArgs', 'SettingEtherLightingSpeedOverridesArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SettingEtherLightingArgs.__new__(SettingEtherLightingArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["attr_hidden"] = attr_hidden
            __props__.__dict__["attr_hidden_id"] = attr_hidden_id
            __props__.__dict__["attr_no_delete"] = attr_no_delete
            __props__.__dict__["attr_no_edit"] = attr_no_edit
            __props__.__dict__["key"] = key
            __props__.__dict__["network_overrides"] = network_overrides
            __props__.__dict__["site_id"] = site_id
            __props__.__dict__["speed_overrides"] = speed_overrides
        super(SettingEtherLighting, __self__).__init__(
            'unifi-native:ether_lighting:SettingEtherLighting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SettingEtherLighting':
        """
        Get an existing SettingEtherLighting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SettingEtherLightingArgs.__new__(SettingEtherLightingArgs)

        __props__.__dict__["id"] = None
        __props__.__dict__["attr_hidden"] = None
        __props__.__dict__["attr_hidden_id"] = None
        __props__.__dict__["attr_no_delete"] = None
        __props__.__dict__["attr_no_edit"] = None
        __props__.__dict__["key"] = None
        __props__.__dict__["network_overrides"] = None
        __props__.__dict__["site_id"] = None
        __props__.__dict__["speed_overrides"] = None
        return SettingEtherLighting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="Id")
    def id(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "id")

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
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="networkOverrides")
    def network_overrides(self) -> pulumi.Output[Optional[Sequence['outputs.SettingEtherLightingNetworkOverrides']]]:
        return pulumi.get(self, "network_overrides")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter(name="speedOverrides")
    def speed_overrides(self) -> pulumi.Output[Optional[Sequence['outputs.SettingEtherLightingSpeedOverrides']]]:
        return pulumi.get(self, "speed_overrides")

