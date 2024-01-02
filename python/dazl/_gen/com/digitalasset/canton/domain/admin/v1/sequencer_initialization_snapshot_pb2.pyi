# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v0 import crypto_pb2 as _crypto_pb2
from ..v0 import sequencer_administration_service_pb2 as _sequencer_administration_service_pb2
from ..v0 import sequencer_initialization_snapshot_pb2 as _sequencer_initialization_snapshot_pb2
from ....protocol.v0 import sequencing_pb2 as _sequencing_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerSnapshot(_message.Message):
    __slots__ = ["latest_timestamp", "head_member_counters", "status", "additional", "in_flight_aggregations", "traffic_snapshots"]
    class MemberCounter(_message.Message):
        __slots__ = ["member", "sequencer_counter"]
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_COUNTER_FIELD_NUMBER: _ClassVar[int]
        member: str
        sequencer_counter: int
        def __init__(self, member: _Optional[str] = ..., sequencer_counter: _Optional[int] = ...) -> None: ...
    class InFlightAggregationWithId(_message.Message):
        __slots__ = ["aggregation_id", "aggregation_rule", "max_sequencing_time", "aggregated_senders"]
        AGGREGATION_ID_FIELD_NUMBER: _ClassVar[int]
        AGGREGATION_RULE_FIELD_NUMBER: _ClassVar[int]
        MAX_SEQUENCING_TIME_FIELD_NUMBER: _ClassVar[int]
        AGGREGATED_SENDERS_FIELD_NUMBER: _ClassVar[int]
        aggregation_id: bytes
        aggregation_rule: _sequencing_pb2.AggregationRule
        max_sequencing_time: _timestamp_pb2.Timestamp
        aggregated_senders: _containers.RepeatedCompositeFieldContainer[SequencerSnapshot.AggregationBySender]
        def __init__(self, aggregation_id: _Optional[bytes] = ..., aggregation_rule: _Optional[_Union[_sequencing_pb2.AggregationRule, _Mapping]] = ..., max_sequencing_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., aggregated_senders: _Optional[_Iterable[_Union[SequencerSnapshot.AggregationBySender, _Mapping]]] = ...) -> None: ...
    class AggregationBySender(_message.Message):
        __slots__ = ["sender", "sequencing_timestamp", "signatures_by_envelope"]
        SENDER_FIELD_NUMBER: _ClassVar[int]
        SEQUENCING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SIGNATURES_BY_ENVELOPE_FIELD_NUMBER: _ClassVar[int]
        sender: str
        sequencing_timestamp: _timestamp_pb2.Timestamp
        signatures_by_envelope: _containers.RepeatedCompositeFieldContainer[SequencerSnapshot.SignaturesForEnvelope]
        def __init__(self, sender: _Optional[str] = ..., sequencing_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., signatures_by_envelope: _Optional[_Iterable[_Union[SequencerSnapshot.SignaturesForEnvelope, _Mapping]]] = ...) -> None: ...
    class SignaturesForEnvelope(_message.Message):
        __slots__ = ["signatures"]
        SIGNATURES_FIELD_NUMBER: _ClassVar[int]
        signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
        def __init__(self, signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...
    class MemberTrafficSnapshot(_message.Message):
        __slots__ = ["member", "extra_traffic_remainder", "extra_traffic_consumed", "base_traffic_remainder", "sequencing_timestamp"]
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        EXTRA_TRAFFIC_REMAINDER_FIELD_NUMBER: _ClassVar[int]
        EXTRA_TRAFFIC_CONSUMED_FIELD_NUMBER: _ClassVar[int]
        BASE_TRAFFIC_REMAINDER_FIELD_NUMBER: _ClassVar[int]
        SEQUENCING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        member: str
        extra_traffic_remainder: int
        extra_traffic_consumed: int
        base_traffic_remainder: int
        sequencing_timestamp: _timestamp_pb2.Timestamp
        def __init__(self, member: _Optional[str] = ..., extra_traffic_remainder: _Optional[int] = ..., extra_traffic_consumed: _Optional[int] = ..., base_traffic_remainder: _Optional[int] = ..., sequencing_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    LATEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HEAD_MEMBER_COUNTERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_FIELD_NUMBER: _ClassVar[int]
    IN_FLIGHT_AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    latest_timestamp: _timestamp_pb2.Timestamp
    head_member_counters: _containers.RepeatedCompositeFieldContainer[SequencerSnapshot.MemberCounter]
    status: _sequencer_administration_service_pb2.SequencerPruningStatus
    additional: _sequencer_initialization_snapshot_pb2.ImplementationSpecificInfo
    in_flight_aggregations: _containers.RepeatedCompositeFieldContainer[SequencerSnapshot.InFlightAggregationWithId]
    traffic_snapshots: _containers.RepeatedCompositeFieldContainer[SequencerSnapshot.MemberTrafficSnapshot]
    def __init__(self, latest_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., head_member_counters: _Optional[_Iterable[_Union[SequencerSnapshot.MemberCounter, _Mapping]]] = ..., status: _Optional[_Union[_sequencer_administration_service_pb2.SequencerPruningStatus, _Mapping]] = ..., additional: _Optional[_Union[_sequencer_initialization_snapshot_pb2.ImplementationSpecificInfo, _Mapping]] = ..., in_flight_aggregations: _Optional[_Iterable[_Union[SequencerSnapshot.InFlightAggregationWithId, _Mapping]]] = ..., traffic_snapshots: _Optional[_Iterable[_Union[SequencerSnapshot.MemberTrafficSnapshot, _Mapping]]] = ...) -> None: ...
