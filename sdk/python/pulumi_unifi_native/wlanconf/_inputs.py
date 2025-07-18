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
    'WLANCapabArgs',
    'WLANCapabArgsDict',
    'WLANCellularNetworkListArgs',
    'WLANCellularNetworkListArgsDict',
    'WLANFriendlyNameArgs',
    'WLANFriendlyNameArgsDict',
    'WLANHotspot2Args',
    'WLANHotspot2ArgsDict',
    'WLANNaiRealmListArgs',
    'WLANNaiRealmListArgsDict',
    'WLANPrivatePresharedKeysArgs',
    'WLANPrivatePresharedKeysArgsDict',
    'WLANRoamingConsortiumListArgs',
    'WLANRoamingConsortiumListArgsDict',
    'WLANSaePskArgs',
    'WLANSaePskArgsDict',
    'WLANScheduleWithDurationArgs',
    'WLANScheduleWithDurationArgsDict',
    'WLANVenueNameArgs',
    'WLANVenueNameArgsDict',
]

MYPY = False

if not MYPY:
    class WLANCapabArgsDict(TypedDict):
        port: NotRequired[pulumi.Input[builtins.int]]
        protocol: NotRequired[pulumi.Input[builtins.str]]
        status: NotRequired[pulumi.Input[builtins.str]]
elif False:
    WLANCapabArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANCapabArgs:
    def __init__(__self__, *,
                 port: Optional[pulumi.Input[builtins.int]] = None,
                 protocol: Optional[pulumi.Input[builtins.str]] = None,
                 status: Optional[pulumi.Input[builtins.str]] = None):
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "status", value)


if not MYPY:
    class WLANCellularNetworkListArgsDict(TypedDict):
        country_code: NotRequired[pulumi.Input[builtins.int]]
        mcc: NotRequired[pulumi.Input[builtins.int]]
        mnc: NotRequired[pulumi.Input[builtins.int]]
        name: NotRequired[pulumi.Input[builtins.str]]
elif False:
    WLANCellularNetworkListArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANCellularNetworkListArgs:
    def __init__(__self__, *,
                 country_code: Optional[pulumi.Input[builtins.int]] = None,
                 mcc: Optional[pulumi.Input[builtins.int]] = None,
                 mnc: Optional[pulumi.Input[builtins.int]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        if country_code is not None:
            pulumi.set(__self__, "country_code", country_code)
        if mcc is not None:
            pulumi.set(__self__, "mcc", mcc)
        if mnc is not None:
            pulumi.set(__self__, "mnc", mnc)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "country_code")

    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "country_code", value)

    @property
    @pulumi.getter
    def mcc(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "mcc")

    @mcc.setter
    def mcc(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "mcc", value)

    @property
    @pulumi.getter
    def mnc(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "mnc")

    @mnc.setter
    def mnc(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "mnc", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


if not MYPY:
    class WLANFriendlyNameArgsDict(TypedDict):
        language: NotRequired[pulumi.Input[builtins.str]]
        text: NotRequired[pulumi.Input[builtins.str]]
elif False:
    WLANFriendlyNameArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANFriendlyNameArgs:
    def __init__(__self__, *,
                 language: Optional[pulumi.Input[builtins.str]] = None,
                 text: Optional[pulumi.Input[builtins.str]] = None):
        if language is not None:
            pulumi.set(__self__, "language", language)
        if text is not None:
            pulumi.set(__self__, "text", text)

    @property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "language")

    @language.setter
    def language(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "language", value)

    @property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "text")

    @text.setter
    def text(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "text", value)


if not MYPY:
    class WLANHotspot2ArgsDict(TypedDict):
        capab: NotRequired[pulumi.Input[Sequence[pulumi.Input['WLANCapabArgsDict']]]]
        cellular_network_list: NotRequired[pulumi.Input[Sequence[pulumi.Input['WLANCellularNetworkListArgsDict']]]]
        domain_name_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]
        friendly_name: NotRequired[pulumi.Input[Sequence[pulumi.Input['WLANFriendlyNameArgsDict']]]]
        ipaddr_type_avail_v4: NotRequired[pulumi.Input[builtins.int]]
        ipaddr_type_avail_v6: NotRequired[pulumi.Input[builtins.int]]
        metrics_downlink_load: NotRequired[pulumi.Input[builtins.int]]
        metrics_downlink_load_set: NotRequired[pulumi.Input[builtins.bool]]
        metrics_downlink_speed: NotRequired[pulumi.Input[builtins.int]]
        metrics_downlink_speed_set: NotRequired[pulumi.Input[builtins.bool]]
        metrics_info_at_capacity: NotRequired[pulumi.Input[builtins.bool]]
        metrics_info_link_status: NotRequired[pulumi.Input[builtins.str]]
        metrics_info_symmetric: NotRequired[pulumi.Input[builtins.bool]]
        metrics_measurement: NotRequired[pulumi.Input[builtins.int]]
        metrics_measurement_set: NotRequired[pulumi.Input[builtins.bool]]
        metrics_status: NotRequired[pulumi.Input[builtins.bool]]
        metrics_uplink_load: NotRequired[pulumi.Input[builtins.int]]
        metrics_uplink_load_set: NotRequired[pulumi.Input[builtins.bool]]
        metrics_uplink_speed: NotRequired[pulumi.Input[builtins.int]]
        metrics_uplink_speed_set: NotRequired[pulumi.Input[builtins.bool]]
        nai_realm_list: NotRequired[pulumi.Input[Sequence[pulumi.Input['WLANNaiRealmListArgsDict']]]]
        network_type: NotRequired[pulumi.Input[builtins.int]]
        roaming_consortium_list: NotRequired[pulumi.Input[Sequence[pulumi.Input['WLANRoamingConsortiumListArgsDict']]]]
        venue_group: NotRequired[pulumi.Input[builtins.int]]
        venue_name: NotRequired[pulumi.Input[Sequence[pulumi.Input['WLANVenueNameArgsDict']]]]
        venue_type: NotRequired[pulumi.Input[builtins.int]]
elif False:
    WLANHotspot2ArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANHotspot2Args:
    def __init__(__self__, *,
                 capab: Optional[pulumi.Input[Sequence[pulumi.Input['WLANCapabArgs']]]] = None,
                 cellular_network_list: Optional[pulumi.Input[Sequence[pulumi.Input['WLANCellularNetworkListArgs']]]] = None,
                 domain_name_list: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 friendly_name: Optional[pulumi.Input[Sequence[pulumi.Input['WLANFriendlyNameArgs']]]] = None,
                 ipaddr_type_avail_v4: Optional[pulumi.Input[builtins.int]] = None,
                 ipaddr_type_avail_v6: Optional[pulumi.Input[builtins.int]] = None,
                 metrics_downlink_load: Optional[pulumi.Input[builtins.int]] = None,
                 metrics_downlink_load_set: Optional[pulumi.Input[builtins.bool]] = None,
                 metrics_downlink_speed: Optional[pulumi.Input[builtins.int]] = None,
                 metrics_downlink_speed_set: Optional[pulumi.Input[builtins.bool]] = None,
                 metrics_info_at_capacity: Optional[pulumi.Input[builtins.bool]] = None,
                 metrics_info_link_status: Optional[pulumi.Input[builtins.str]] = None,
                 metrics_info_symmetric: Optional[pulumi.Input[builtins.bool]] = None,
                 metrics_measurement: Optional[pulumi.Input[builtins.int]] = None,
                 metrics_measurement_set: Optional[pulumi.Input[builtins.bool]] = None,
                 metrics_status: Optional[pulumi.Input[builtins.bool]] = None,
                 metrics_uplink_load: Optional[pulumi.Input[builtins.int]] = None,
                 metrics_uplink_load_set: Optional[pulumi.Input[builtins.bool]] = None,
                 metrics_uplink_speed: Optional[pulumi.Input[builtins.int]] = None,
                 metrics_uplink_speed_set: Optional[pulumi.Input[builtins.bool]] = None,
                 nai_realm_list: Optional[pulumi.Input[Sequence[pulumi.Input['WLANNaiRealmListArgs']]]] = None,
                 network_type: Optional[pulumi.Input[builtins.int]] = None,
                 roaming_consortium_list: Optional[pulumi.Input[Sequence[pulumi.Input['WLANRoamingConsortiumListArgs']]]] = None,
                 venue_group: Optional[pulumi.Input[builtins.int]] = None,
                 venue_name: Optional[pulumi.Input[Sequence[pulumi.Input['WLANVenueNameArgs']]]] = None,
                 venue_type: Optional[pulumi.Input[builtins.int]] = None):
        if capab is not None:
            pulumi.set(__self__, "capab", capab)
        if cellular_network_list is not None:
            pulumi.set(__self__, "cellular_network_list", cellular_network_list)
        if domain_name_list is not None:
            pulumi.set(__self__, "domain_name_list", domain_name_list)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if ipaddr_type_avail_v4 is not None:
            pulumi.set(__self__, "ipaddr_type_avail_v4", ipaddr_type_avail_v4)
        if ipaddr_type_avail_v6 is not None:
            pulumi.set(__self__, "ipaddr_type_avail_v6", ipaddr_type_avail_v6)
        if metrics_downlink_load is not None:
            pulumi.set(__self__, "metrics_downlink_load", metrics_downlink_load)
        if metrics_downlink_load_set is not None:
            pulumi.set(__self__, "metrics_downlink_load_set", metrics_downlink_load_set)
        if metrics_downlink_speed is not None:
            pulumi.set(__self__, "metrics_downlink_speed", metrics_downlink_speed)
        if metrics_downlink_speed_set is not None:
            pulumi.set(__self__, "metrics_downlink_speed_set", metrics_downlink_speed_set)
        if metrics_info_at_capacity is not None:
            pulumi.set(__self__, "metrics_info_at_capacity", metrics_info_at_capacity)
        if metrics_info_link_status is not None:
            pulumi.set(__self__, "metrics_info_link_status", metrics_info_link_status)
        if metrics_info_symmetric is not None:
            pulumi.set(__self__, "metrics_info_symmetric", metrics_info_symmetric)
        if metrics_measurement is not None:
            pulumi.set(__self__, "metrics_measurement", metrics_measurement)
        if metrics_measurement_set is not None:
            pulumi.set(__self__, "metrics_measurement_set", metrics_measurement_set)
        if metrics_status is not None:
            pulumi.set(__self__, "metrics_status", metrics_status)
        if metrics_uplink_load is not None:
            pulumi.set(__self__, "metrics_uplink_load", metrics_uplink_load)
        if metrics_uplink_load_set is not None:
            pulumi.set(__self__, "metrics_uplink_load_set", metrics_uplink_load_set)
        if metrics_uplink_speed is not None:
            pulumi.set(__self__, "metrics_uplink_speed", metrics_uplink_speed)
        if metrics_uplink_speed_set is not None:
            pulumi.set(__self__, "metrics_uplink_speed_set", metrics_uplink_speed_set)
        if nai_realm_list is not None:
            pulumi.set(__self__, "nai_realm_list", nai_realm_list)
        if network_type is not None:
            pulumi.set(__self__, "network_type", network_type)
        if roaming_consortium_list is not None:
            pulumi.set(__self__, "roaming_consortium_list", roaming_consortium_list)
        if venue_group is not None:
            pulumi.set(__self__, "venue_group", venue_group)
        if venue_name is not None:
            pulumi.set(__self__, "venue_name", venue_name)
        if venue_type is not None:
            pulumi.set(__self__, "venue_type", venue_type)

    @property
    @pulumi.getter
    def capab(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WLANCapabArgs']]]]:
        return pulumi.get(self, "capab")

    @capab.setter
    def capab(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WLANCapabArgs']]]]):
        pulumi.set(self, "capab", value)

    @property
    @pulumi.getter(name="cellularNetworkList")
    def cellular_network_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WLANCellularNetworkListArgs']]]]:
        return pulumi.get(self, "cellular_network_list")

    @cellular_network_list.setter
    def cellular_network_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WLANCellularNetworkListArgs']]]]):
        pulumi.set(self, "cellular_network_list", value)

    @property
    @pulumi.getter(name="domainNameList")
    def domain_name_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "domain_name_list")

    @domain_name_list.setter
    def domain_name_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "domain_name_list", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WLANFriendlyNameArgs']]]]:
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WLANFriendlyNameArgs']]]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="ipaddrTypeAvailV4")
    def ipaddr_type_avail_v4(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "ipaddr_type_avail_v4")

    @ipaddr_type_avail_v4.setter
    def ipaddr_type_avail_v4(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "ipaddr_type_avail_v4", value)

    @property
    @pulumi.getter(name="ipaddrTypeAvailV6")
    def ipaddr_type_avail_v6(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "ipaddr_type_avail_v6")

    @ipaddr_type_avail_v6.setter
    def ipaddr_type_avail_v6(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "ipaddr_type_avail_v6", value)

    @property
    @pulumi.getter(name="metricsDownlinkLoad")
    def metrics_downlink_load(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "metrics_downlink_load")

    @metrics_downlink_load.setter
    def metrics_downlink_load(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "metrics_downlink_load", value)

    @property
    @pulumi.getter(name="metricsDownlinkLoadSet")
    def metrics_downlink_load_set(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "metrics_downlink_load_set")

    @metrics_downlink_load_set.setter
    def metrics_downlink_load_set(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "metrics_downlink_load_set", value)

    @property
    @pulumi.getter(name="metricsDownlinkSpeed")
    def metrics_downlink_speed(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "metrics_downlink_speed")

    @metrics_downlink_speed.setter
    def metrics_downlink_speed(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "metrics_downlink_speed", value)

    @property
    @pulumi.getter(name="metricsDownlinkSpeedSet")
    def metrics_downlink_speed_set(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "metrics_downlink_speed_set")

    @metrics_downlink_speed_set.setter
    def metrics_downlink_speed_set(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "metrics_downlink_speed_set", value)

    @property
    @pulumi.getter(name="metricsInfoAtCapacity")
    def metrics_info_at_capacity(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "metrics_info_at_capacity")

    @metrics_info_at_capacity.setter
    def metrics_info_at_capacity(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "metrics_info_at_capacity", value)

    @property
    @pulumi.getter(name="metricsInfoLinkStatus")
    def metrics_info_link_status(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "metrics_info_link_status")

    @metrics_info_link_status.setter
    def metrics_info_link_status(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "metrics_info_link_status", value)

    @property
    @pulumi.getter(name="metricsInfoSymmetric")
    def metrics_info_symmetric(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "metrics_info_symmetric")

    @metrics_info_symmetric.setter
    def metrics_info_symmetric(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "metrics_info_symmetric", value)

    @property
    @pulumi.getter(name="metricsMeasurement")
    def metrics_measurement(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "metrics_measurement")

    @metrics_measurement.setter
    def metrics_measurement(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "metrics_measurement", value)

    @property
    @pulumi.getter(name="metricsMeasurementSet")
    def metrics_measurement_set(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "metrics_measurement_set")

    @metrics_measurement_set.setter
    def metrics_measurement_set(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "metrics_measurement_set", value)

    @property
    @pulumi.getter(name="metricsStatus")
    def metrics_status(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "metrics_status")

    @metrics_status.setter
    def metrics_status(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "metrics_status", value)

    @property
    @pulumi.getter(name="metricsUplinkLoad")
    def metrics_uplink_load(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "metrics_uplink_load")

    @metrics_uplink_load.setter
    def metrics_uplink_load(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "metrics_uplink_load", value)

    @property
    @pulumi.getter(name="metricsUplinkLoadSet")
    def metrics_uplink_load_set(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "metrics_uplink_load_set")

    @metrics_uplink_load_set.setter
    def metrics_uplink_load_set(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "metrics_uplink_load_set", value)

    @property
    @pulumi.getter(name="metricsUplinkSpeed")
    def metrics_uplink_speed(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "metrics_uplink_speed")

    @metrics_uplink_speed.setter
    def metrics_uplink_speed(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "metrics_uplink_speed", value)

    @property
    @pulumi.getter(name="metricsUplinkSpeedSet")
    def metrics_uplink_speed_set(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "metrics_uplink_speed_set")

    @metrics_uplink_speed_set.setter
    def metrics_uplink_speed_set(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "metrics_uplink_speed_set", value)

    @property
    @pulumi.getter(name="naiRealmList")
    def nai_realm_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WLANNaiRealmListArgs']]]]:
        return pulumi.get(self, "nai_realm_list")

    @nai_realm_list.setter
    def nai_realm_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WLANNaiRealmListArgs']]]]):
        pulumi.set(self, "nai_realm_list", value)

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "network_type")

    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "network_type", value)

    @property
    @pulumi.getter(name="roamingConsortiumList")
    def roaming_consortium_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WLANRoamingConsortiumListArgs']]]]:
        return pulumi.get(self, "roaming_consortium_list")

    @roaming_consortium_list.setter
    def roaming_consortium_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WLANRoamingConsortiumListArgs']]]]):
        pulumi.set(self, "roaming_consortium_list", value)

    @property
    @pulumi.getter(name="venueGroup")
    def venue_group(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "venue_group")

    @venue_group.setter
    def venue_group(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "venue_group", value)

    @property
    @pulumi.getter(name="venueName")
    def venue_name(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WLANVenueNameArgs']]]]:
        return pulumi.get(self, "venue_name")

    @venue_name.setter
    def venue_name(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WLANVenueNameArgs']]]]):
        pulumi.set(self, "venue_name", value)

    @property
    @pulumi.getter(name="venueType")
    def venue_type(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "venue_type")

    @venue_type.setter
    def venue_type(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "venue_type", value)


if not MYPY:
    class WLANNaiRealmListArgsDict(TypedDict):
        auth_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[builtins.int]]]]
        auth_vals: NotRequired[pulumi.Input[Sequence[pulumi.Input[builtins.int]]]]
        eap_method: NotRequired[pulumi.Input[builtins.int]]
        encoding: NotRequired[pulumi.Input[builtins.int]]
        name: NotRequired[pulumi.Input[builtins.str]]
        status: NotRequired[pulumi.Input[builtins.bool]]
elif False:
    WLANNaiRealmListArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANNaiRealmListArgs:
    def __init__(__self__, *,
                 auth_ids: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.int]]]] = None,
                 auth_vals: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.int]]]] = None,
                 eap_method: Optional[pulumi.Input[builtins.int]] = None,
                 encoding: Optional[pulumi.Input[builtins.int]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 status: Optional[pulumi.Input[builtins.bool]] = None):
        if auth_ids is not None:
            pulumi.set(__self__, "auth_ids", auth_ids)
        if auth_vals is not None:
            pulumi.set(__self__, "auth_vals", auth_vals)
        if eap_method is not None:
            pulumi.set(__self__, "eap_method", eap_method)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="authIds")
    def auth_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.int]]]]:
        return pulumi.get(self, "auth_ids")

    @auth_ids.setter
    def auth_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.int]]]]):
        pulumi.set(self, "auth_ids", value)

    @property
    @pulumi.getter(name="authVals")
    def auth_vals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.int]]]]:
        return pulumi.get(self, "auth_vals")

    @auth_vals.setter
    def auth_vals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.int]]]]):
        pulumi.set(self, "auth_vals", value)

    @property
    @pulumi.getter(name="eapMethod")
    def eap_method(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "eap_method")

    @eap_method.setter
    def eap_method(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "eap_method", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[builtins.bool]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "status", value)


if not MYPY:
    class WLANPrivatePresharedKeysArgsDict(TypedDict):
        networkconf_id: NotRequired[pulumi.Input[builtins.str]]
        password: NotRequired[pulumi.Input[builtins.str]]
elif False:
    WLANPrivatePresharedKeysArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANPrivatePresharedKeysArgs:
    def __init__(__self__, *,
                 networkconf_id: Optional[pulumi.Input[builtins.str]] = None,
                 password: Optional[pulumi.Input[builtins.str]] = None):
        if networkconf_id is not None:
            pulumi.set(__self__, "networkconf_id", networkconf_id)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter(name="networkconfId")
    def networkconf_id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "networkconf_id")

    @networkconf_id.setter
    def networkconf_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "networkconf_id", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "password", value)


if not MYPY:
    class WLANRoamingConsortiumListArgsDict(TypedDict):
        name: NotRequired[pulumi.Input[builtins.str]]
        oid: NotRequired[pulumi.Input[builtins.str]]
elif False:
    WLANRoamingConsortiumListArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANRoamingConsortiumListArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 oid: Optional[pulumi.Input[builtins.str]] = None):
        if name is not None:
            pulumi.set(__self__, "name", name)
        if oid is not None:
            pulumi.set(__self__, "oid", oid)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def oid(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "oid")

    @oid.setter
    def oid(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "oid", value)


if not MYPY:
    class WLANSaePskArgsDict(TypedDict):
        id: NotRequired[pulumi.Input[builtins.str]]
        mac: NotRequired[pulumi.Input[builtins.str]]
        psk: NotRequired[pulumi.Input[builtins.str]]
        vlan: NotRequired[pulumi.Input[builtins.int]]
elif False:
    WLANSaePskArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANSaePskArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[builtins.str]] = None,
                 mac: Optional[pulumi.Input[builtins.str]] = None,
                 psk: Optional[pulumi.Input[builtins.str]] = None,
                 vlan: Optional[pulumi.Input[builtins.int]] = None):
        if id is not None:
            pulumi.set(__self__, "id", id)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if psk is not None:
            pulumi.set(__self__, "psk", psk)
        if vlan is not None:
            pulumi.set(__self__, "vlan", vlan)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter
    def psk(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "psk")

    @psk.setter
    def psk(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "psk", value)

    @property
    @pulumi.getter
    def vlan(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "vlan")

    @vlan.setter
    def vlan(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "vlan", value)


if not MYPY:
    class WLANScheduleWithDurationArgsDict(TypedDict):
        duration_minutes: NotRequired[pulumi.Input[builtins.int]]
        name: NotRequired[pulumi.Input[builtins.str]]
        start_days_of_week: NotRequired[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]
        start_hour: NotRequired[pulumi.Input[builtins.int]]
        start_minute: NotRequired[pulumi.Input[builtins.int]]
elif False:
    WLANScheduleWithDurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANScheduleWithDurationArgs:
    def __init__(__self__, *,
                 duration_minutes: Optional[pulumi.Input[builtins.int]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 start_days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 start_hour: Optional[pulumi.Input[builtins.int]] = None,
                 start_minute: Optional[pulumi.Input[builtins.int]] = None):
        if duration_minutes is not None:
            pulumi.set(__self__, "duration_minutes", duration_minutes)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if start_days_of_week is not None:
            pulumi.set(__self__, "start_days_of_week", start_days_of_week)
        if start_hour is not None:
            pulumi.set(__self__, "start_hour", start_hour)
        if start_minute is not None:
            pulumi.set(__self__, "start_minute", start_minute)

    @property
    @pulumi.getter(name="durationMinutes")
    def duration_minutes(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "duration_minutes")

    @duration_minutes.setter
    def duration_minutes(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "duration_minutes", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="startDaysOfWeek")
    def start_days_of_week(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        return pulumi.get(self, "start_days_of_week")

    @start_days_of_week.setter
    def start_days_of_week(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "start_days_of_week", value)

    @property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "start_hour")

    @start_hour.setter
    def start_hour(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "start_hour", value)

    @property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[pulumi.Input[builtins.int]]:
        return pulumi.get(self, "start_minute")

    @start_minute.setter
    def start_minute(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "start_minute", value)


if not MYPY:
    class WLANVenueNameArgsDict(TypedDict):
        language: NotRequired[pulumi.Input[builtins.str]]
        name: NotRequired[pulumi.Input[builtins.str]]
        url: NotRequired[pulumi.Input[builtins.str]]
elif False:
    WLANVenueNameArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class WLANVenueNameArgs:
    def __init__(__self__, *,
                 language: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 url: Optional[pulumi.Input[builtins.str]] = None):
        if language is not None:
            pulumi.set(__self__, "language", language)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "language")

    @language.setter
    def language(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "language", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[builtins.str]]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "url", value)


