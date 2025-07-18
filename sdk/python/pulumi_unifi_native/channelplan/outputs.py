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

__all__ = [
    'ChannelPlan',
    'ChannelPlanApBlacklistedChannels',
    'ChannelPlanCoupling',
    'ChannelPlanRadioTable',
    'ChannelPlanSatisfactionTable',
    'ChannelPlanSiteBlacklistedChannels',
    'Meta',
]

@pulumi.output_type
class ChannelPlan(dict):
    def __init__(__self__, *,
                 id: Optional[builtins.str] = None,
                 ap_blacklisted_channels: Optional[Sequence['outputs.ChannelPlanApBlacklistedChannels']] = None,
                 attr_hidden: Optional[builtins.bool] = None,
                 attr_hidden_id: Optional[builtins.str] = None,
                 attr_no_delete: Optional[builtins.bool] = None,
                 attr_no_edit: Optional[builtins.bool] = None,
                 conf_source: Optional[builtins.str] = None,
                 coupling: Optional[Sequence['outputs.ChannelPlanCoupling']] = None,
                 date: Optional[builtins.str] = None,
                 fitness: Optional[builtins.float] = None,
                 note: Optional[builtins.str] = None,
                 radio: Optional[builtins.str] = None,
                 radio_table: Optional[Sequence['outputs.ChannelPlanRadioTable']] = None,
                 satisfaction: Optional[builtins.float] = None,
                 satisfaction_table: Optional[Sequence['outputs.ChannelPlanSatisfactionTable']] = None,
                 site_blacklisted_channels: Optional[Sequence['outputs.ChannelPlanSiteBlacklistedChannels']] = None,
                 site_id: Optional[builtins.str] = None):
        if id is not None:
            pulumi.set(__self__, "id", id)
        if ap_blacklisted_channels is not None:
            pulumi.set(__self__, "ap_blacklisted_channels", ap_blacklisted_channels)
        if attr_hidden is not None:
            pulumi.set(__self__, "attr_hidden", attr_hidden)
        if attr_hidden_id is not None:
            pulumi.set(__self__, "attr_hidden_id", attr_hidden_id)
        if attr_no_delete is not None:
            pulumi.set(__self__, "attr_no_delete", attr_no_delete)
        if attr_no_edit is not None:
            pulumi.set(__self__, "attr_no_edit", attr_no_edit)
        if conf_source is not None:
            pulumi.set(__self__, "conf_source", conf_source)
        if coupling is not None:
            pulumi.set(__self__, "coupling", coupling)
        if date is not None:
            pulumi.set(__self__, "date", date)
        if fitness is not None:
            pulumi.set(__self__, "fitness", fitness)
        if note is not None:
            pulumi.set(__self__, "note", note)
        if radio is not None:
            pulumi.set(__self__, "radio", radio)
        if radio_table is not None:
            pulumi.set(__self__, "radio_table", radio_table)
        if satisfaction is not None:
            pulumi.set(__self__, "satisfaction", satisfaction)
        if satisfaction_table is not None:
            pulumi.set(__self__, "satisfaction_table", satisfaction_table)
        if site_blacklisted_channels is not None:
            pulumi.set(__self__, "site_blacklisted_channels", site_blacklisted_channels)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)

    @property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="apBlacklistedChannels")
    def ap_blacklisted_channels(self) -> Optional[Sequence['outputs.ChannelPlanApBlacklistedChannels']]:
        return pulumi.get(self, "ap_blacklisted_channels")

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
    @pulumi.getter(name="confSource")
    def conf_source(self) -> Optional[builtins.str]:
        return pulumi.get(self, "conf_source")

    @property
    @pulumi.getter
    def coupling(self) -> Optional[Sequence['outputs.ChannelPlanCoupling']]:
        return pulumi.get(self, "coupling")

    @property
    @pulumi.getter
    def date(self) -> Optional[builtins.str]:
        return pulumi.get(self, "date")

    @property
    @pulumi.getter
    def fitness(self) -> Optional[builtins.float]:
        return pulumi.get(self, "fitness")

    @property
    @pulumi.getter
    def note(self) -> Optional[builtins.str]:
        return pulumi.get(self, "note")

    @property
    @pulumi.getter
    def radio(self) -> Optional[builtins.str]:
        return pulumi.get(self, "radio")

    @property
    @pulumi.getter(name="radioTable")
    def radio_table(self) -> Optional[Sequence['outputs.ChannelPlanRadioTable']]:
        return pulumi.get(self, "radio_table")

    @property
    @pulumi.getter
    def satisfaction(self) -> Optional[builtins.float]:
        return pulumi.get(self, "satisfaction")

    @property
    @pulumi.getter(name="satisfactionTable")
    def satisfaction_table(self) -> Optional[Sequence['outputs.ChannelPlanSatisfactionTable']]:
        return pulumi.get(self, "satisfaction_table")

    @property
    @pulumi.getter(name="siteBlacklistedChannels")
    def site_blacklisted_channels(self) -> Optional[Sequence['outputs.ChannelPlanSiteBlacklistedChannels']]:
        return pulumi.get(self, "site_blacklisted_channels")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "site_id")


@pulumi.output_type
class ChannelPlanApBlacklistedChannels(dict):
    def __init__(__self__, *,
                 channel: Optional[builtins.int] = None,
                 mac: Optional[builtins.str] = None,
                 timestamp: Optional[builtins.int] = None):
        if channel is not None:
            pulumi.set(__self__, "channel", channel)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if timestamp is not None:
            pulumi.set(__self__, "timestamp", timestamp)

    @property
    @pulumi.getter
    def channel(self) -> Optional[builtins.int]:
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter
    def mac(self) -> Optional[builtins.str]:
        return pulumi.get(self, "mac")

    @property
    @pulumi.getter
    def timestamp(self) -> Optional[builtins.int]:
        return pulumi.get(self, "timestamp")


@pulumi.output_type
class ChannelPlanCoupling(dict):
    def __init__(__self__, *,
                 rssi: Optional[builtins.int] = None,
                 source: Optional[builtins.str] = None,
                 target: Optional[builtins.str] = None):
        if rssi is not None:
            pulumi.set(__self__, "rssi", rssi)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if target is not None:
            pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter
    def rssi(self) -> Optional[builtins.int]:
        return pulumi.get(self, "rssi")

    @property
    @pulumi.getter
    def source(self) -> Optional[builtins.str]:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def target(self) -> Optional[builtins.str]:
        return pulumi.get(self, "target")


@pulumi.output_type
class ChannelPlanRadioTable(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "backupChannel":
            suggest = "backup_channel"
        elif key == "deviceMac":
            suggest = "device_mac"
        elif key == "txPower":
            suggest = "tx_power"
        elif key == "txPowerMode":
            suggest = "tx_power_mode"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ChannelPlanRadioTable. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ChannelPlanRadioTable.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ChannelPlanRadioTable.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 backup_channel: Optional[builtins.str] = None,
                 channel: Optional[builtins.str] = None,
                 device_mac: Optional[builtins.str] = None,
                 name: Optional[builtins.str] = None,
                 tx_power: Optional[builtins.str] = None,
                 tx_power_mode: Optional[builtins.str] = None,
                 width: Optional[builtins.int] = None):
        if backup_channel is not None:
            pulumi.set(__self__, "backup_channel", backup_channel)
        if channel is not None:
            pulumi.set(__self__, "channel", channel)
        if device_mac is not None:
            pulumi.set(__self__, "device_mac", device_mac)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tx_power is not None:
            pulumi.set(__self__, "tx_power", tx_power)
        if tx_power_mode is not None:
            pulumi.set(__self__, "tx_power_mode", tx_power_mode)
        if width is not None:
            pulumi.set(__self__, "width", width)

    @property
    @pulumi.getter(name="backupChannel")
    def backup_channel(self) -> Optional[builtins.str]:
        return pulumi.get(self, "backup_channel")

    @property
    @pulumi.getter
    def channel(self) -> Optional[builtins.str]:
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter(name="deviceMac")
    def device_mac(self) -> Optional[builtins.str]:
        return pulumi.get(self, "device_mac")

    @property
    @pulumi.getter
    def name(self) -> Optional[builtins.str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="txPower")
    def tx_power(self) -> Optional[builtins.str]:
        return pulumi.get(self, "tx_power")

    @property
    @pulumi.getter(name="txPowerMode")
    def tx_power_mode(self) -> Optional[builtins.str]:
        return pulumi.get(self, "tx_power_mode")

    @property
    @pulumi.getter
    def width(self) -> Optional[builtins.int]:
        return pulumi.get(self, "width")


@pulumi.output_type
class ChannelPlanSatisfactionTable(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "deviceMac":
            suggest = "device_mac"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ChannelPlanSatisfactionTable. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ChannelPlanSatisfactionTable.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ChannelPlanSatisfactionTable.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 device_mac: Optional[builtins.str] = None,
                 satisfaction: Optional[builtins.float] = None):
        if device_mac is not None:
            pulumi.set(__self__, "device_mac", device_mac)
        if satisfaction is not None:
            pulumi.set(__self__, "satisfaction", satisfaction)

    @property
    @pulumi.getter(name="deviceMac")
    def device_mac(self) -> Optional[builtins.str]:
        return pulumi.get(self, "device_mac")

    @property
    @pulumi.getter
    def satisfaction(self) -> Optional[builtins.float]:
        return pulumi.get(self, "satisfaction")


@pulumi.output_type
class ChannelPlanSiteBlacklistedChannels(dict):
    def __init__(__self__, *,
                 channel: Optional[builtins.int] = None,
                 timestamp: Optional[builtins.int] = None):
        if channel is not None:
            pulumi.set(__self__, "channel", channel)
        if timestamp is not None:
            pulumi.set(__self__, "timestamp", timestamp)

    @property
    @pulumi.getter
    def channel(self) -> Optional[builtins.int]:
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter
    def timestamp(self) -> Optional[builtins.int]:
        return pulumi.get(self, "timestamp")


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


