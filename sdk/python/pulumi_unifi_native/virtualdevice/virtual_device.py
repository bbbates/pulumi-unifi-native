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

__all__ = ['VirtualDeviceArgs', 'VirtualDevice']

@pulumi.input_type
class VirtualDeviceArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_hidden: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_hidden_id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_no_delete: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_no_edit: Optional[pulumi.Input[builtins.bool]] = None,
                 height_in_meters: Optional[pulumi.Input[builtins.float]] = None,
                 locked: Optional[pulumi.Input[builtins.bool]] = None,
                 map_id: Optional[pulumi.Input[builtins.str]] = None,
                 site_id: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None,
                 x: Optional[pulumi.Input[builtins.str]] = None,
                 y: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a VirtualDevice resource.
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
        if height_in_meters is not None:
            pulumi.set(__self__, "height_in_meters", height_in_meters)
        if locked is not None:
            pulumi.set(__self__, "locked", locked)
        if map_id is not None:
            pulumi.set(__self__, "map_id", map_id)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if x is not None:
            pulumi.set(__self__, "x", x)
        if y is not None:
            pulumi.set(__self__, "y", y)

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
    @pulumi.getter(name="heightInMeters")
    def height_in_meters(self) -> Optional[pulumi.Input[builtins.float]]:
        return pulumi.get(self, "height_in_meters")

    @height_in_meters.setter
    def height_in_meters(self, value: Optional[pulumi.Input[builtins.float]]):
        pulumi.set(self, "height_in_meters", value)

    @property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "locked")

    @locked.setter
    def locked(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "locked", value)

    @property
    @pulumi.getter(name="mapId")
    def map_id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "map_id")

    @map_id.setter
    def map_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "map_id", value)

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "site_id")

    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "site_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def x(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "x")

    @x.setter
    def x(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "x", value)

    @property
    @pulumi.getter
    def y(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "y")

    @y.setter
    def y(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "y", value)


@pulumi.type_token("unifi-native:virtualdevice:VirtualDevice")
class VirtualDevice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_hidden: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_hidden_id: Optional[pulumi.Input[builtins.str]] = None,
                 attr_no_delete: Optional[pulumi.Input[builtins.bool]] = None,
                 attr_no_edit: Optional[pulumi.Input[builtins.bool]] = None,
                 height_in_meters: Optional[pulumi.Input[builtins.float]] = None,
                 locked: Optional[pulumi.Input[builtins.bool]] = None,
                 map_id: Optional[pulumi.Input[builtins.str]] = None,
                 site_id: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None,
                 x: Optional[pulumi.Input[builtins.str]] = None,
                 y: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Create a VirtualDevice resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VirtualDeviceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a VirtualDevice resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param VirtualDeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualDeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 height_in_meters: Optional[pulumi.Input[builtins.float]] = None,
                 locked: Optional[pulumi.Input[builtins.bool]] = None,
                 map_id: Optional[pulumi.Input[builtins.str]] = None,
                 site_id: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None,
                 x: Optional[pulumi.Input[builtins.str]] = None,
                 y: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualDeviceArgs.__new__(VirtualDeviceArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["attr_hidden"] = attr_hidden
            __props__.__dict__["attr_hidden_id"] = attr_hidden_id
            __props__.__dict__["attr_no_delete"] = attr_no_delete
            __props__.__dict__["attr_no_edit"] = attr_no_edit
            __props__.__dict__["height_in_meters"] = height_in_meters
            __props__.__dict__["locked"] = locked
            __props__.__dict__["map_id"] = map_id
            __props__.__dict__["site_id"] = site_id
            __props__.__dict__["type"] = type
            __props__.__dict__["x"] = x
            __props__.__dict__["y"] = y
        super(VirtualDevice, __self__).__init__(
            'unifi-native:virtualdevice:VirtualDevice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualDevice':
        """
        Get an existing VirtualDevice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualDeviceArgs.__new__(VirtualDeviceArgs)

        __props__.__dict__["id"] = None
        __props__.__dict__["attr_hidden"] = None
        __props__.__dict__["attr_hidden_id"] = None
        __props__.__dict__["attr_no_delete"] = None
        __props__.__dict__["attr_no_edit"] = None
        __props__.__dict__["height_in_meters"] = None
        __props__.__dict__["locked"] = None
        __props__.__dict__["map_id"] = None
        __props__.__dict__["site_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["x"] = None
        __props__.__dict__["y"] = None
        return VirtualDevice(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter(name="heightInMeters")
    def height_in_meters(self) -> pulumi.Output[Optional[builtins.float]]:
        return pulumi.get(self, "height_in_meters")

    @property
    @pulumi.getter
    def locked(self) -> pulumi.Output[Optional[builtins.bool]]:
        return pulumi.get(self, "locked")

    @property
    @pulumi.getter(name="mapId")
    def map_id(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "map_id")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def x(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "x")

    @property
    @pulumi.getter
    def y(self) -> pulumi.Output[Optional[builtins.str]]:
        return pulumi.get(self, "y")

