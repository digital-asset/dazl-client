# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import traffic_control_parameters_pb2 as _traffic_control_parameters_pb2
from ..v30 import sequencer_initialization_snapshot_pb2 as _sequencer_initialization_snapshot_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerSnapshot(_message.Message):
    __slots__ = ("latest_timestamp", "last_block_height", "status", "additional", "in_flight_aggregations", "traffic_purchased", "traffic_consumed", "member_previous_timestamps")
    LATEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FIELD_NUMBER: _ClassVar[int]
    IN_FLIGHT_AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    MEMBER_PREVIOUS_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    latest_timestamp: int
    last_block_height: int
    status: SequencerPruningStatus
    additional: _sequencer_initialization_snapshot_pb2.ImplementationSpecificInfo
    in_flight_aggregations: _containers.RepeatedCompositeFieldContainer[_sequencer_initialization_snapshot_pb2.SequencerSnapshot.InFlightAggregationWithId]
    traffic_purchased: _containers.RepeatedCompositeFieldContainer[_traffic_control_parameters_pb2.TrafficPurchased]
    traffic_consumed: _containers.RepeatedCompositeFieldContainer[_traffic_control_parameters_pb2.TrafficConsumed]
    member_previous_timestamps: _containers.RepeatedCompositeFieldContainer[_sequencer_initialization_snapshot_pb2.SequencerSnapshot.MemberPreviousTimestamp]
    def __init__(self, latest_timestamp: _Optional[int] = ..., last_block_height: _Optional[int] = ..., status: _Optional[_Union[SequencerPruningStatus, _Mapping]] = ..., additional: _Optional[_Union[_sequencer_initialization_snapshot_pb2.ImplementationSpecificInfo, _Mapping]] = ..., in_flight_aggregations: _Optional[_Iterable[_Union[_sequencer_initialization_snapshot_pb2.SequencerSnapshot.InFlightAggregationWithId, _Mapping]]] = ..., traffic_purchased: _Optional[_Iterable[_Union[_traffic_control_parameters_pb2.TrafficPurchased, _Mapping]]] = ..., traffic_consumed: _Optional[_Iterable[_Union[_traffic_control_parameters_pb2.TrafficConsumed, _Mapping]]] = ..., member_previous_timestamps: _Optional[_Iterable[_Union[_sequencer_initialization_snapshot_pb2.SequencerSnapshot.MemberPreviousTimestamp, _Mapping]]] = ...) -> None: ...

class SequencerMemberStatus(_message.Message):
    __slots__ = ("member", "onboarding", "active", "disabled")
    class Onboarding(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Active(_message.Message):
        __slots__ = ("registered_at", "last_acknowledged")
        REGISTERED_AT_FIELD_NUMBER: _ClassVar[int]
        LAST_ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
        registered_at: int
        last_acknowledged: int
        def __init__(self, registered_at: _Optional[int] = ..., last_acknowledged: _Optional[int] = ...) -> None: ...
    class Disabled(_message.Message):
        __slots__ = ("registered_at", "last_acknowledged")
        REGISTERED_AT_FIELD_NUMBER: _ClassVar[int]
        LAST_ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
        registered_at: int
        last_acknowledged: int
        def __init__(self, registered_at: _Optional[int] = ..., last_acknowledged: _Optional[int] = ...) -> None: ...
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    ONBOARDING_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    member: str
    onboarding: SequencerMemberStatus.Onboarding
    active: SequencerMemberStatus.Active
    disabled: SequencerMemberStatus.Disabled
    def __init__(self, member: _Optional[str] = ..., onboarding: _Optional[_Union[SequencerMemberStatus.Onboarding, _Mapping]] = ..., active: _Optional[_Union[SequencerMemberStatus.Active, _Mapping]] = ..., disabled: _Optional[_Union[SequencerMemberStatus.Disabled, _Mapping]] = ...) -> None: ...

class SequencerPruningStatus(_message.Message):
    __slots__ = ("now", "earliest_event_timestamp", "members")
    NOW_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_EVENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    now: int
    earliest_event_timestamp: int
    members: _containers.RepeatedCompositeFieldContainer[SequencerMemberStatus]
    def __init__(self, now: _Optional[int] = ..., earliest_event_timestamp: _Optional[int] = ..., members: _Optional[_Iterable[_Union[SequencerMemberStatus, _Mapping]]] = ...) -> None: ...
