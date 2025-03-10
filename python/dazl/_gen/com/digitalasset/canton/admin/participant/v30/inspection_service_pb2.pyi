# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReceivedCommitmentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECEIVED_COMMITMENT_STATE_UNSPECIFIED: _ClassVar[ReceivedCommitmentState]
    RECEIVED_COMMITMENT_STATE_MATCH: _ClassVar[ReceivedCommitmentState]
    RECEIVED_COMMITMENT_STATE_MISMATCH: _ClassVar[ReceivedCommitmentState]
    RECEIVED_COMMITMENT_STATE_BUFFERED: _ClassVar[ReceivedCommitmentState]
    RECEIVED_COMMITMENT_STATE_OUTSTANDING: _ClassVar[ReceivedCommitmentState]

class SentCommitmentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SENT_COMMITMENT_STATE_UNSPECIFIED: _ClassVar[SentCommitmentState]
    SENT_COMMITMENT_STATE_MATCH: _ClassVar[SentCommitmentState]
    SENT_COMMITMENT_STATE_MISMATCH: _ClassVar[SentCommitmentState]
    SENT_COMMITMENT_STATE_NOT_COMPARED: _ClassVar[SentCommitmentState]
RECEIVED_COMMITMENT_STATE_UNSPECIFIED: ReceivedCommitmentState
RECEIVED_COMMITMENT_STATE_MATCH: ReceivedCommitmentState
RECEIVED_COMMITMENT_STATE_MISMATCH: ReceivedCommitmentState
RECEIVED_COMMITMENT_STATE_BUFFERED: ReceivedCommitmentState
RECEIVED_COMMITMENT_STATE_OUTSTANDING: ReceivedCommitmentState
SENT_COMMITMENT_STATE_UNSPECIFIED: SentCommitmentState
SENT_COMMITMENT_STATE_MATCH: SentCommitmentState
SENT_COMMITMENT_STATE_MISMATCH: SentCommitmentState
SENT_COMMITMENT_STATE_NOT_COMPARED: SentCommitmentState

class LookupContractDomain(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("contract_id",)
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        contract_id: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, contract_id: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("results",)
        class ResultsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        RESULTS_FIELD_NUMBER: _ClassVar[int]
        results: _containers.ScalarMap[str, str]
        def __init__(self, results: _Optional[_Mapping[str, str]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LookupTransactionDomain(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("transaction_id",)
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        transaction_id: str
        def __init__(self, transaction_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("domain_id",)
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        domain_id: str
        def __init__(self, domain_id: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class LookupOffsetByTime(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("timestamp",)
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: str
        def __init__(self, offset: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class LookupOffsetByIndex(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("index",)
        INDEX_FIELD_NUMBER: _ClassVar[int]
        index: int
        def __init__(self, index: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: str
        def __init__(self, offset: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class LookupReceivedAcsCommitments(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("time_ranges", "counter_participant_uids", "commitment_state", "verbose")
        TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
        COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
        COMMITMENT_STATE_FIELD_NUMBER: _ClassVar[int]
        VERBOSE_FIELD_NUMBER: _ClassVar[int]
        time_ranges: _containers.RepeatedCompositeFieldContainer[DomainTimeRange]
        counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
        commitment_state: _containers.RepeatedScalarFieldContainer[ReceivedCommitmentState]
        verbose: bool
        def __init__(self, time_ranges: _Optional[_Iterable[_Union[DomainTimeRange, _Mapping]]] = ..., counter_participant_uids: _Optional[_Iterable[str]] = ..., commitment_state: _Optional[_Iterable[_Union[ReceivedCommitmentState, str]]] = ..., verbose: bool = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("received",)
        RECEIVED_FIELD_NUMBER: _ClassVar[int]
        received: _containers.RepeatedCompositeFieldContainer[ReceivedAcsCommitmentPerDomain]
        def __init__(self, received: _Optional[_Iterable[_Union[ReceivedAcsCommitmentPerDomain, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class TimeRange(_message.Message):
    __slots__ = ("from_exclusive", "to_inclusive")
    FROM_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    from_exclusive: _timestamp_pb2.Timestamp
    to_inclusive: _timestamp_pb2.Timestamp
    def __init__(self, from_exclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., to_inclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DomainTimeRange(_message.Message):
    __slots__ = ("domain_id", "interval")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    interval: TimeRange
    def __init__(self, domain_id: _Optional[str] = ..., interval: _Optional[_Union[TimeRange, _Mapping]] = ...) -> None: ...

class Interval(_message.Message):
    __slots__ = ("start_tick_exclusive", "end_tick_inclusive")
    START_TICK_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    END_TICK_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    start_tick_exclusive: _timestamp_pb2.Timestamp
    end_tick_inclusive: _timestamp_pb2.Timestamp
    def __init__(self, start_tick_exclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_tick_inclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReceivedAcsCommitment(_message.Message):
    __slots__ = ("interval", "origin_counter_participant_uid", "received_commitment", "own_commitment", "state")
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    OWN_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    interval: Interval
    origin_counter_participant_uid: str
    received_commitment: bytes
    own_commitment: bytes
    state: ReceivedCommitmentState
    def __init__(self, interval: _Optional[_Union[Interval, _Mapping]] = ..., origin_counter_participant_uid: _Optional[str] = ..., received_commitment: _Optional[bytes] = ..., own_commitment: _Optional[bytes] = ..., state: _Optional[_Union[ReceivedCommitmentState, str]] = ...) -> None: ...

class ReceivedAcsCommitmentPerDomain(_message.Message):
    __slots__ = ("domain_id", "received")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    received: _containers.RepeatedCompositeFieldContainer[ReceivedAcsCommitment]
    def __init__(self, domain_id: _Optional[str] = ..., received: _Optional[_Iterable[_Union[ReceivedAcsCommitment, _Mapping]]] = ...) -> None: ...

class SentAcsCommitment(_message.Message):
    __slots__ = ("interval", "dest_counter_participant_uid", "own_commitment", "received_commitment", "state")
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DEST_COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    OWN_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    interval: Interval
    dest_counter_participant_uid: str
    own_commitment: bytes
    received_commitment: bytes
    state: SentCommitmentState
    def __init__(self, interval: _Optional[_Union[Interval, _Mapping]] = ..., dest_counter_participant_uid: _Optional[str] = ..., own_commitment: _Optional[bytes] = ..., received_commitment: _Optional[bytes] = ..., state: _Optional[_Union[SentCommitmentState, str]] = ...) -> None: ...

class SentAcsCommitmentPerDomain(_message.Message):
    __slots__ = ("domain_id", "sent")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    SENT_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    sent: _containers.RepeatedCompositeFieldContainer[SentAcsCommitment]
    def __init__(self, domain_id: _Optional[str] = ..., sent: _Optional[_Iterable[_Union[SentAcsCommitment, _Mapping]]] = ...) -> None: ...

class LookupSentAcsCommitments(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("time_ranges", "counter_participant_uids", "commitment_state", "verbose")
        TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
        COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
        COMMITMENT_STATE_FIELD_NUMBER: _ClassVar[int]
        VERBOSE_FIELD_NUMBER: _ClassVar[int]
        time_ranges: _containers.RepeatedCompositeFieldContainer[DomainTimeRange]
        counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
        commitment_state: _containers.RepeatedScalarFieldContainer[SentCommitmentState]
        verbose: bool
        def __init__(self, time_ranges: _Optional[_Iterable[_Union[DomainTimeRange, _Mapping]]] = ..., counter_participant_uids: _Optional[_Iterable[str]] = ..., commitment_state: _Optional[_Iterable[_Union[SentCommitmentState, str]]] = ..., verbose: bool = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("sent",)
        SENT_FIELD_NUMBER: _ClassVar[int]
        sent: _containers.RepeatedCompositeFieldContainer[SentAcsCommitmentPerDomain]
        def __init__(self, sent: _Optional[_Iterable[_Union[SentAcsCommitmentPerDomain, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class SlowCounterParticipantDomainConfig(_message.Message):
    __slots__ = ("domain_ids", "distinguished_participant_uids", "threshold_distinguished", "threshold_default", "participant_uids_metrics")
    DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHED_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_DISTINGUISHED_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_UIDS_METRICS_FIELD_NUMBER: _ClassVar[int]
    domain_ids: _containers.RepeatedScalarFieldContainer[str]
    distinguished_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    threshold_distinguished: int
    threshold_default: int
    participant_uids_metrics: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain_ids: _Optional[_Iterable[str]] = ..., distinguished_participant_uids: _Optional[_Iterable[str]] = ..., threshold_distinguished: _Optional[int] = ..., threshold_default: _Optional[int] = ..., participant_uids_metrics: _Optional[_Iterable[str]] = ...) -> None: ...

class SetConfigForSlowCounterParticipants(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("configs",)
        CONFIGS_FIELD_NUMBER: _ClassVar[int]
        configs: _containers.RepeatedCompositeFieldContainer[SlowCounterParticipantDomainConfig]
        def __init__(self, configs: _Optional[_Iterable[_Union[SlowCounterParticipantDomainConfig, _Mapping]]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    def __init__(self) -> None: ...

class GetConfigForSlowCounterParticipants(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("domain_ids",)
        DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
        domain_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, domain_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("configs",)
        CONFIGS_FIELD_NUMBER: _ClassVar[int]
        configs: _containers.RepeatedCompositeFieldContainer[SlowCounterParticipantDomainConfig]
        def __init__(self, configs: _Optional[_Iterable[_Union[SlowCounterParticipantDomainConfig, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...

class GetIntervalsBehindForCounterParticipants(_message.Message):
    __slots__ = ()
    class CounterParticipantInfo(_message.Message):
        __slots__ = ("counter_participant_uid", "domain_id", "intervals_behind", "as_of_sequencing_timestamp")
        COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        INTERVALS_BEHIND_FIELD_NUMBER: _ClassVar[int]
        AS_OF_SEQUENCING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        counter_participant_uid: str
        domain_id: str
        intervals_behind: int
        as_of_sequencing_timestamp: _timestamp_pb2.Timestamp
        def __init__(self, counter_participant_uid: _Optional[str] = ..., domain_id: _Optional[str] = ..., intervals_behind: _Optional[int] = ..., as_of_sequencing_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Request(_message.Message):
        __slots__ = ("counter_participant_uids", "domain_ids", "threshold")
        COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_IDS_FIELD_NUMBER: _ClassVar[int]
        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
        domain_ids: _containers.RepeatedScalarFieldContainer[str]
        threshold: int
        def __init__(self, counter_participant_uids: _Optional[_Iterable[str]] = ..., domain_ids: _Optional[_Iterable[str]] = ..., threshold: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("intervals_behind",)
        INTERVALS_BEHIND_FIELD_NUMBER: _ClassVar[int]
        intervals_behind: _containers.RepeatedCompositeFieldContainer[GetIntervalsBehindForCounterParticipants.CounterParticipantInfo]
        def __init__(self, intervals_behind: _Optional[_Iterable[_Union[GetIntervalsBehindForCounterParticipants.CounterParticipantInfo, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
