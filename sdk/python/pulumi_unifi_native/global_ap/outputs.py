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
    'SettingGlobalAp',
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
class SettingGlobalAp(dict):
    def __init__(__self__, *,
                 id: Optional[builtins.str] = None,
                 _6e_channel_size: Optional[builtins.int] = None,
                 _6e_tx_power: Optional[builtins.int] = None,
                 _6e_tx_power_mode: Optional[builtins.str] = None,
                 ap_exclusions: Optional[Sequence[builtins.str]] = None,
                 attr_hidden: Optional[builtins.bool] = None,
                 attr_hidden_id: Optional[builtins.str] = None,
                 attr_no_delete: Optional[builtins.bool] = None,
                 attr_no_edit: Optional[builtins.bool] = None,
                 key: Optional[builtins.str] = None,
                 na_channel_size: Optional[builtins.int] = None,
                 na_tx_power: Optional[builtins.int] = None,
                 na_tx_power_mode: Optional[builtins.str] = None,
                 ng_channel_size: Optional[builtins.int] = None,
                 ng_tx_power: Optional[builtins.int] = None,
                 ng_tx_power_mode: Optional[builtins.str] = None,
                 site_id: Optional[builtins.str] = None):
        if id is not None:
            pulumi.set(__self__, "id", id)
        if _6e_channel_size is not None:
            pulumi.set(__self__, "_6e_channel_size", _6e_channel_size)
        if _6e_tx_power is not None:
            pulumi.set(__self__, "_6e_tx_power", _6e_tx_power)
        if _6e_tx_power_mode is not None:
            pulumi.set(__self__, "_6e_tx_power_mode", _6e_tx_power_mode)
        if ap_exclusions is not None:
            pulumi.set(__self__, "ap_exclusions", ap_exclusions)
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
        if na_channel_size is not None:
            pulumi.set(__self__, "na_channel_size", na_channel_size)
        if na_tx_power is not None:
            pulumi.set(__self__, "na_tx_power", na_tx_power)
        if na_tx_power_mode is not None:
            pulumi.set(__self__, "na_tx_power_mode", na_tx_power_mode)
        if ng_channel_size is not None:
            pulumi.set(__self__, "ng_channel_size", ng_channel_size)
        if ng_tx_power is not None:
            pulumi.set(__self__, "ng_tx_power", ng_tx_power)
        if ng_tx_power_mode is not None:
            pulumi.set(__self__, "ng_tx_power_mode", ng_tx_power_mode)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)

    @property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="_6eChannelSize")
    def _6e_channel_size(self) -> Optional[builtins.int]:
        return pulumi.get(self, "_6e_channel_size")

    @property
    @pulumi.getter(name="_6eTxPower")
    def _6e_tx_power(self) -> Optional[builtins.int]:
        return pulumi.get(self, "_6e_tx_power")

    @property
    @pulumi.getter(name="_6eTxPowerMode")
    def _6e_tx_power_mode(self) -> Optional[builtins.str]:
        return pulumi.get(self, "_6e_tx_power_mode")

    @property
    @pulumi.getter(name="apExclusions")
    def ap_exclusions(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "ap_exclusions")

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
    @pulumi.getter
    def key(self) -> Optional[builtins.str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="naChannelSize")
    def na_channel_size(self) -> Optional[builtins.int]:
        return pulumi.get(self, "na_channel_size")

    @property
    @pulumi.getter(name="naTxPower")
    def na_tx_power(self) -> Optional[builtins.int]:
        return pulumi.get(self, "na_tx_power")

    @property
    @pulumi.getter(name="naTxPowerMode")
    def na_tx_power_mode(self) -> Optional[builtins.str]:
        return pulumi.get(self, "na_tx_power_mode")

    @property
    @pulumi.getter(name="ngChannelSize")
    def ng_channel_size(self) -> Optional[builtins.int]:
        return pulumi.get(self, "ng_channel_size")

    @property
    @pulumi.getter(name="ngTxPower")
    def ng_tx_power(self) -> Optional[builtins.int]:
        return pulumi.get(self, "ng_tx_power")

    @property
    @pulumi.getter(name="ngTxPowerMode")
    def ng_tx_power_mode(self) -> Optional[builtins.str]:
        return pulumi.get(self, "ng_tx_power_mode")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "site_id")


