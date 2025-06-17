# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v30 import crypto_pb2 as _crypto_pb2
from ....protocol.v30 import common_stable_pb2 as _common_stable_pb2
from ....protocol.v30 import traffic_control_parameters_pb2 as _traffic_control_parameters_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerSnapshot(_message.Message):
    __slots__ = ("latest_timestamp", "last_block_height", "status", "additional", "in_flight_aggregations", "traffic_purchased", "traffic_consumed", "member_previous_timestamps")
    class MemberPreviousTimestamp(_message.Message):
        __slots__ = ("member", "previous_timestamp")
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        member: str
        previous_timestamp: int
        def __init__(self, member: _Optional[str] = ..., previous_timestamp: _Optional[int] = ...) -> None: ...
    class InFlightAggregationWithId(_message.Message):
        __slots__ = ("aggregation_id", "aggregation_rule", "max_sequencing_time", "aggregated_senders")
        AGGREGATION_ID_FIELD_NUMBER: _ClassVar[int]
        AGGREGATION_RULE_FIELD_NUMBER: _ClassVar[int]
        MAX_SEQUENCING_TIME_FIELD_NUMBER: _ClassVar[int]
        AGGREGATED_SENDERS_FIELD_NUMBER: _ClassVar[int]
        aggregation_id: bytes
        aggregation_rule: _common_stable_pb2.AggregationRule
        max_sequencing_time: int
        aggregated_senders: _containers.RepeatedCompositeFieldContainer[SequencerSnapshot.AggregationBySender]
        def __init__(self, aggregation_id: _Optional[bytes] = ..., aggregation_rule: _Optional[_Union[_common_stable_pb2.AggregationRule, _Mapping]] = ..., max_sequencing_time: _Optional[int] = ..., aggregated_senders: _Optional[_Iterable[_Union[SequencerSnapshot.AggregationBySender, _Mapping]]] = ...) -> None: ...
    class AggregationBySender(_message.Message):
        __slots__ = ("sender", "sequencing_timestamp", "signatures_by_envelope")
        SENDER_FIELD_NUMBER: _ClassVar[int]
        SEQUENCING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SIGNATURES_BY_ENVELOPE_FIELD_NUMBER: _ClassVar[int]
        sender: str
        sequencing_timestamp: int
        signatures_by_envelope: _containers.RepeatedCompositeFieldContainer[SequencerSnapshot.SignaturesForEnvelope]
        def __init__(self, sender: _Optional[str] = ..., sequencing_timestamp: _Optional[int] = ..., signatures_by_envelope: _Optional[_Iterable[_Union[SequencerSnapshot.SignaturesForEnvelope, _Mapping]]] = ...) -> None: ...
    class SignaturesForEnvelope(_message.Message):
        __slots__ = ("signatures",)
        SIGNATURES_FIELD_NUMBER: _ClassVar[int]
        signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
        def __init__(self, signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...
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
    additional: ImplementationSpecificInfo
    in_flight_aggregations: _containers.RepeatedCompositeFieldContainer[SequencerSnapshot.InFlightAggregationWithId]
    traffic_purchased: _containers.RepeatedCompositeFieldContainer[_traffic_control_parameters_pb2.TrafficPurchased]
    traffic_consumed: _containers.RepeatedCompositeFieldContainer[_traffic_control_parameters_pb2.TrafficConsumed]
    member_previous_timestamps: _containers.RepeatedCompositeFieldContainer[SequencerSnapshot.MemberPreviousTimestamp]
    def __init__(self, latest_timestamp: _Optional[int] = ..., last_block_height: _Optional[int] = ..., status: _Optional[_Union[SequencerPruningStatus, _Mapping]] = ..., additional: _Optional[_Union[ImplementationSpecificInfo, _Mapping]] = ..., in_flight_aggregations: _Optional[_Iterable[_Union[SequencerSnapshot.InFlightAggregationWithId, _Mapping]]] = ..., traffic_purchased: _Optional[_Iterable[_Union[_traffic_control_parameters_pb2.TrafficPurchased, _Mapping]]] = ..., traffic_consumed: _Optional[_Iterable[_Union[_traffic_control_parameters_pb2.TrafficConsumed, _Mapping]]] = ..., member_previous_timestamps: _Optional[_Iterable[_Union[SequencerSnapshot.MemberPreviousTimestamp, _Mapping]]] = ...) -> None: ...

class SequencerMemberStatus(_message.Message):
    __slots__ = ("member", "registered_at", "last_acknowledged", "enabled")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    member: str
    registered_at: int
    last_acknowledged: int
    enabled: bool
    def __init__(self, member: _Optional[str] = ..., registered_at: _Optional[int] = ..., last_acknowledged: _Optional[int] = ..., enabled: bool = ...) -> None: ...

class SequencerPruningStatus(_message.Message):
    __slots__ = ("now", "earliest_event_timestamp", "members")
    NOW_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_EVENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    now: int
    earliest_event_timestamp: int
    members: _containers.RepeatedCompositeFieldContainer[SequencerMemberStatus]
    def __init__(self, now: _Optional[int] = ..., earliest_event_timestamp: _Optional[int] = ..., members: _Optional[_Iterable[_Union[SequencerMemberStatus, _Mapping]]] = ...) -> None: ...

class ImplementationSpecificInfo(_message.Message):
    __slots__ = ("implementation_name", "info")
    IMPLEMENTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    implementation_name: str
    info: bytes
    def __init__(self, implementation_name: _Optional[str] = ..., info: _Optional[bytes] = ...) -> None: ...
