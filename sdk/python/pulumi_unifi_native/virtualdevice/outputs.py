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
    'Meta',
    'VirtualDevice',
]

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


@pulumi.output_type
class VirtualDevice(dict):
    def __init__(__self__, *,
                 id: Optional[builtins.str] = None,
                 attr_hidden: Optional[builtins.bool] = None,
                 attr_hidden_id: Optional[builtins.str] = None,
                 attr_no_delete: Optional[builtins.bool] = None,
                 attr_no_edit: Optional[builtins.bool] = None,
                 height_in_meters: Optional[builtins.float] = None,
                 locked: Optional[builtins.bool] = None,
                 map_id: Optional[builtins.str] = None,
                 site_id: Optional[builtins.str] = None,
                 type: Optional[builtins.str] = None,
                 x: Optional[builtins.str] = None,
                 y: Optional[builtins.str] = None):
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
    def id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="heightInMeters")
    def height_in_meters(self) -> Optional[builtins.float]:
        return pulumi.get(self, "height_in_meters")

    @property
    @pulumi.getter
    def locked(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "locked")

    @property
    @pulumi.getter(name="mapId")
    def map_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "map_id")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[builtins.str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def x(self) -> Optional[builtins.str]:
        return pulumi.get(self, "x")

    @property
    @pulumi.getter
    def y(self) -> Optional[builtins.str]:
        return pulumi.get(self, "y")


