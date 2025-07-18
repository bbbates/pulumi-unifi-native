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
    'SettingMdnsCustomServicesArgs',
    'SettingMdnsCustomServicesArgsDict',
    'SettingMdnsPredefinedServicesArgs',
    'SettingMdnsPredefinedServicesArgsDict',
]

MYPY = False

if not MYPY:
    class SettingMdnsCustomServicesArgsDict(TypedDict):
        address: NotRequired[pulumi.Input[builtins.str]]
        name: NotRequired[pulumi.Input[builtins.str]]
elif False:
    SettingMdnsCustomServicesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SettingMdnsCustomServicesArgs:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        if address is not None:
            pulumi.set(__self__, "address", address)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


if not MYPY:
    class SettingMdnsPredefinedServicesArgsDict(TypedDict):
        code: NotRequired[pulumi.Input[builtins.str]]
elif False:
    SettingMdnsPredefinedServicesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SettingMdnsPredefinedServicesArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input[builtins.str]] = None):
        if code is not None:
            pulumi.set(__self__, "code", code)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "code", value)


