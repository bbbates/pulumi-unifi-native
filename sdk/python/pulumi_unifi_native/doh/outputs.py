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
    'Meta',
    'SettingDoh',
    'SettingDohCustomServers',
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
class SettingDoh(dict):
    def __init__(__self__, *,
                 id: Optional[builtins.str] = None,
                 attr_hidden: Optional[builtins.bool] = None,
                 attr_hidden_id: Optional[builtins.str] = None,
                 attr_no_delete: Optional[builtins.bool] = None,
                 attr_no_edit: Optional[builtins.bool] = None,
                 custom_servers: Optional[Sequence['outputs.SettingDohCustomServers']] = None,
                 key: Optional[builtins.str] = None,
                 server_names: Optional[Sequence[builtins.str]] = None,
                 site_id: Optional[builtins.str] = None,
                 state: Optional[builtins.str] = None):
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
        if custom_servers is not None:
            pulumi.set(__self__, "custom_servers", custom_servers)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if server_names is not None:
            pulumi.set(__self__, "server_names", server_names)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)
        if state is not None:
            pulumi.set(__self__, "state", state)

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
    @pulumi.getter(name="customServers")
    def custom_servers(self) -> Optional[Sequence['outputs.SettingDohCustomServers']]:
        return pulumi.get(self, "custom_servers")

    @property
    @pulumi.getter
    def key(self) -> Optional[builtins.str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="serverNames")
    def server_names(self) -> Optional[Sequence[builtins.str]]:
        return pulumi.get(self, "server_names")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[builtins.str]:
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[builtins.str]:
        return pulumi.get(self, "state")


@pulumi.output_type
class SettingDohCustomServers(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "sdnsStamp":
            suggest = "sdns_stamp"
        elif key == "serverName":
            suggest = "server_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SettingDohCustomServers. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SettingDohCustomServers.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SettingDohCustomServers.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[builtins.bool] = None,
                 sdns_stamp: Optional[builtins.str] = None,
                 server_name: Optional[builtins.str] = None):
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if sdns_stamp is not None:
            pulumi.set(__self__, "sdns_stamp", sdns_stamp)
        if server_name is not None:
            pulumi.set(__self__, "server_name", server_name)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[builtins.bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="sdnsStamp")
    def sdns_stamp(self) -> Optional[builtins.str]:
        return pulumi.get(self, "sdns_stamp")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[builtins.str]:
        return pulumi.get(self, "server_name")


