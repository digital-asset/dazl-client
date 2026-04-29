# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ....protocol.v30 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v30 import traffic_control_parameters_pb2 as _traffic_control_parameters_pb2
from . import sequencer_initialization_snapshot_pb2 as _sequencer_initialization_snapshot_pb2
from ....topology.admin.v30 import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateAuthenticationTokenRequest(_message.Message):
    __slots__ = ("member", "expires_in")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    member: str
    expires_in: _duration_pb2.Duration
    def __init__(self, member: _Optional[str] = ..., expires_in: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GenerateAuthenticationTokenResponse(_message.Message):
    __slots__ = ("token", "expires_at")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    token: bytes
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, token: _Optional[bytes] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TrafficControlStateRequest(_message.Message):
    __slots__ = ("members", "exact_timestamp", "relative_timestamp")
    class RelativeTimestamp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELATIVE_TIMESTAMP_LATEST_SAFE_UNSPECIFIED: _ClassVar[TrafficControlStateRequest.RelativeTimestamp]
        RELATIVE_TIMESTAMP_LAST_UPDATE_PER_MEMBER: _ClassVar[TrafficControlStateRequest.RelativeTimestamp]
        RELATIVE_TIMESTAMP_LATEST_APPROXIMATE: _ClassVar[TrafficControlStateRequest.RelativeTimestamp]
    RELATIVE_TIMESTAMP_LATEST_SAFE_UNSPECIFIED: TrafficControlStateRequest.RelativeTimestamp
    RELATIVE_TIMESTAMP_LAST_UPDATE_PER_MEMBER: TrafficControlStateRequest.RelativeTimestamp
    RELATIVE_TIMESTAMP_LATEST_APPROXIMATE: TrafficControlStateRequest.RelativeTimestamp
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    EXACT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedScalarFieldContainer[str]
    exact_timestamp: int
    relative_timestamp: TrafficControlStateRequest.RelativeTimestamp
    def __init__(self, members: _Optional[_Iterable[str]] = ..., exact_timestamp: _Optional[int] = ..., relative_timestamp: _Optional[_Union[TrafficControlStateRequest.RelativeTimestamp, str]] = ...) -> None: ...

class TrafficControlStateResponse(_message.Message):
    __slots__ = ("traffic_states",)
    class TrafficStatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _traffic_control_parameters_pb2.TrafficState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_traffic_control_parameters_pb2.TrafficState, _Mapping]] = ...) -> None: ...
    TRAFFIC_STATES_FIELD_NUMBER: _ClassVar[int]
    traffic_states: _containers.MessageMap[str, _traffic_control_parameters_pb2.TrafficState]
    def __init__(self, traffic_states: _Optional[_Mapping[str, _traffic_control_parameters_pb2.TrafficState]] = ...) -> None: ...

class SetTrafficPurchasedRequest(_message.Message):
    __slots__ = ("member", "serial", "total_traffic_purchased")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRAFFIC_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    member: str
    serial: int
    total_traffic_purchased: int
    def __init__(self, member: _Optional[str] = ..., serial: _Optional[int] = ..., total_traffic_purchased: _Optional[int] = ...) -> None: ...

class SetTrafficPurchasedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLsuTrafficControlStateRequest(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LsuTrafficState(_message.Message):
    __slots__ = ("lsu_traffic_states",)
    class LsuTrafficStatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _traffic_control_parameters_pb2.TrafficState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_traffic_control_parameters_pb2.TrafficState, _Mapping]] = ...) -> None: ...
    LSU_TRAFFIC_STATES_FIELD_NUMBER: _ClassVar[int]
    lsu_traffic_states: _containers.MessageMap[str, _traffic_control_parameters_pb2.TrafficState]
    def __init__(self, lsu_traffic_states: _Optional[_Mapping[str, _traffic_control_parameters_pb2.TrafficState]] = ...) -> None: ...

class GetLsuTrafficControlStateResponse(_message.Message):
    __slots__ = ("lsu_traffic_state",)
    LSU_TRAFFIC_STATE_FIELD_NUMBER: _ClassVar[int]
    lsu_traffic_state: bytes
    def __init__(self, lsu_traffic_state: _Optional[bytes] = ...) -> None: ...

class SetLsuTrafficControlStateRequest(_message.Message):
    __slots__ = ("lsu_traffic_state",)
    LSU_TRAFFIC_STATE_FIELD_NUMBER: _ClassVar[int]
    lsu_traffic_state: bytes
    def __init__(self, lsu_traffic_state: _Optional[bytes] = ...) -> None: ...

class SetLsuTrafficControlStateResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IndividualThroughputCapConfig(_message.Message):
    __slots__ = ("global_tps_cap", "global_kbps_cap", "per_client_tps_cap", "per_client_kbps_cap")
    GLOBAL_TPS_CAP_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_KBPS_CAP_FIELD_NUMBER: _ClassVar[int]
    PER_CLIENT_TPS_CAP_FIELD_NUMBER: _ClassVar[int]
    PER_CLIENT_KBPS_CAP_FIELD_NUMBER: _ClassVar[int]
    global_tps_cap: float
    global_kbps_cap: float
    per_client_tps_cap: float
    per_client_kbps_cap: float
    def __init__(self, global_tps_cap: _Optional[float] = ..., global_kbps_cap: _Optional[float] = ..., per_client_tps_cap: _Optional[float] = ..., per_client_kbps_cap: _Optional[float] = ...) -> None: ...

class SetThroughputCapRequest(_message.Message):
    __slots__ = ("type", "config")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    type: str
    config: IndividualThroughputCapConfig
    def __init__(self, type: _Optional[str] = ..., config: _Optional[_Union[IndividualThroughputCapConfig, _Mapping]] = ...) -> None: ...

class SetThroughputCapResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetThroughputCapRequest(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: str
    def __init__(self, type: _Optional[str] = ...) -> None: ...

class GetThroughputCapResponse(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: IndividualThroughputCapConfig
    def __init__(self, config: _Optional[_Union[IndividualThroughputCapConfig, _Mapping]] = ...) -> None: ...

class SnapshotRequest(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SnapshotResponse(_message.Message):
    __slots__ = ("success", "failure", "versioned_success")
    class Success(_message.Message):
        __slots__ = ("state",)
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: _sequencer_initialization_snapshot_pb2.SequencerSnapshot
        def __init__(self, state: _Optional[_Union[_sequencer_initialization_snapshot_pb2.SequencerSnapshot, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    class VersionedSuccess(_message.Message):
        __slots__ = ("snapshot",)
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        snapshot: bytes
        def __init__(self, snapshot: _Optional[bytes] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    VERSIONED_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: SnapshotResponse.Success
    failure: SnapshotResponse.Failure
    versioned_success: SnapshotResponse.VersionedSuccess
    def __init__(self, success: _Optional[_Union[SnapshotResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[SnapshotResponse.Failure, _Mapping]] = ..., versioned_success: _Optional[_Union[SnapshotResponse.VersionedSuccess, _Mapping]] = ...) -> None: ...

class OnboardingStateRequest(_message.Message):
    __slots__ = ("sequencer_uid", "timestamp")
    SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    sequencer_uid: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, sequencer_uid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OnboardingStateResponse(_message.Message):
    __slots__ = ("onboarding_state_for_sequencer",)
    ONBOARDING_STATE_FOR_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    onboarding_state_for_sequencer: bytes
    def __init__(self, onboarding_state_for_sequencer: _Optional[bytes] = ...) -> None: ...

class OnboardingStateForSequencer(_message.Message):
    __slots__ = ("topology_snapshot", "static_synchronizer_parameters", "sequencer_snapshot")
    TOPOLOGY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    STATIC_SYNCHRONIZER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    topology_snapshot: _common_pb2.TopologyTransactions
    static_synchronizer_parameters: _sequencing_pb2.StaticSynchronizerParameters
    sequencer_snapshot: _sequencer_initialization_snapshot_pb2.SequencerSnapshot
    def __init__(self, topology_snapshot: _Optional[_Union[_common_pb2.TopologyTransactions, _Mapping]] = ..., static_synchronizer_parameters: _Optional[_Union[_sequencing_pb2.StaticSynchronizerParameters, _Mapping]] = ..., sequencer_snapshot: _Optional[_Union[_sequencer_initialization_snapshot_pb2.SequencerSnapshot, _Mapping]] = ...) -> None: ...

class OnboardingStateV2Request(_message.Message):
    __slots__ = ("sequencer_uid", "timestamp")
    SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    sequencer_uid: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, sequencer_uid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OnboardingStateV2Response(_message.Message):
    __slots__ = ("onboarding_state_for_sequencer",)
    ONBOARDING_STATE_FOR_SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    onboarding_state_for_sequencer: bytes
    def __init__(self, onboarding_state_for_sequencer: _Optional[bytes] = ...) -> None: ...

class OnboardingStateForSequencerV2(_message.Message):
    __slots__ = ("topology_transaction", "static_synchronizer_parameters", "sequencer_snapshot")
    TOPOLOGY_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    STATIC_SYNCHRONIZER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    topology_transaction: bytes
    static_synchronizer_parameters: bytes
    sequencer_snapshot: _sequencer_initialization_snapshot_pb2.SequencerSnapshot
    def __init__(self, topology_transaction: _Optional[bytes] = ..., static_synchronizer_parameters: _Optional[bytes] = ..., sequencer_snapshot: _Optional[_Union[_sequencer_initialization_snapshot_pb2.SequencerSnapshot, _Mapping]] = ...) -> None: ...

class PruningStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PruningStatusResponse(_message.Message):
    __slots__ = ("pruning_status",)
    PRUNING_STATUS_FIELD_NUMBER: _ClassVar[int]
    pruning_status: _sequencer_initialization_snapshot_pb2.SequencerPruningStatus
    def __init__(self, pruning_status: _Optional[_Union[_sequencer_initialization_snapshot_pb2.SequencerPruningStatus, _Mapping]] = ...) -> None: ...

class DisableMemberRequest(_message.Message):
    __slots__ = ("member",)
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: str
    def __init__(self, member: _Optional[str] = ...) -> None: ...

class DisableMemberResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PerformLsuSequencingTestRequest(_message.Message):
    __slots__ = ("recipient_mediator_group",)
    RECIPIENT_MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    recipient_mediator_group: int
    def __init__(self, recipient_mediator_group: _Optional[int] = ...) -> None: ...

class PerformLsuSequencingTestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
