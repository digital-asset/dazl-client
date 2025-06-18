# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import active_contract_pb2 as _active_contract_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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

class LookupOffsetByTimeRequest(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class LookupOffsetByTimeResponse(_message.Message):
    __slots__ = ("offset",)
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: int
    def __init__(self, offset: _Optional[int] = ...) -> None: ...

class OpenCommitmentRequest(_message.Message):
    __slots__ = ("commitment", "synchronizer_id", "computed_for_counter_participant_uid", "period_end_tick")
    COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    COMPUTED_FOR_COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_TICK_FIELD_NUMBER: _ClassVar[int]
    commitment: bytes
    synchronizer_id: str
    computed_for_counter_participant_uid: str
    period_end_tick: _timestamp_pb2.Timestamp
    def __init__(self, commitment: _Optional[bytes] = ..., synchronizer_id: _Optional[str] = ..., computed_for_counter_participant_uid: _Optional[str] = ..., period_end_tick: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OpenCommitmentResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class CommitmentContractMeta(_message.Message):
    __slots__ = ("cid", "reassignment_counter")
    CID_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    cid: bytes
    reassignment_counter: int
    def __init__(self, cid: _Optional[bytes] = ..., reassignment_counter: _Optional[int] = ...) -> None: ...

class InspectCommitmentContractsRequest(_message.Message):
    __slots__ = ("cids", "expected_synchronizer_id", "timestamp", "download_payload")
    CIDS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    cids: _containers.RepeatedScalarFieldContainer[bytes]
    expected_synchronizer_id: str
    timestamp: _timestamp_pb2.Timestamp
    download_payload: bool
    def __init__(self, cids: _Optional[_Iterable[bytes]] = ..., expected_synchronizer_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., download_payload: bool = ...) -> None: ...

class InspectCommitmentContractsResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class CommitmentContract(_message.Message):
    __slots__ = ("cid", "active_on_expected_synchronizer", "serialized_contract", "states")
    CID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ON_EXPECTED_SYNCHRONIZER_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    cid: bytes
    active_on_expected_synchronizer: bool
    serialized_contract: _active_contract_pb2.Contract
    states: _containers.RepeatedCompositeFieldContainer[ContractState.SynchronizerState]
    def __init__(self, cid: _Optional[bytes] = ..., active_on_expected_synchronizer: bool = ..., serialized_contract: _Optional[_Union[_active_contract_pb2.Contract, _Mapping]] = ..., states: _Optional[_Iterable[_Union[ContractState.SynchronizerState, _Mapping]]] = ...) -> None: ...

class ContractState(_message.Message):
    __slots__ = ()
    class SynchronizerState(_message.Message):
        __slots__ = ("synchronizer_id", "created", "archived", "unassigned", "assigned", "unknown")
        SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        UNASSIGNED_FIELD_NUMBER: _ClassVar[int]
        ASSIGNED_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        synchronizer_id: str
        created: ContractState.Created
        archived: ContractState.Archived
        unassigned: ContractState.Unassigned
        assigned: ContractState.Assigned
        unknown: ContractState.Unknown
        def __init__(self, synchronizer_id: _Optional[str] = ..., created: _Optional[_Union[ContractState.Created, _Mapping]] = ..., archived: _Optional[_Union[ContractState.Archived, _Mapping]] = ..., unassigned: _Optional[_Union[ContractState.Unassigned, _Mapping]] = ..., assigned: _Optional[_Union[ContractState.Assigned, _Mapping]] = ..., unknown: _Optional[_Union[ContractState.Unknown, _Mapping]] = ...) -> None: ...
    class Created(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Assigned(_message.Message):
        __slots__ = ("reassignment_counter_target", "reassignment_id")
        REASSIGNMENT_COUNTER_TARGET_FIELD_NUMBER: _ClassVar[int]
        REASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
        reassignment_counter_target: int
        reassignment_id: ContractState.ReassignmentId
        def __init__(self, reassignment_counter_target: _Optional[int] = ..., reassignment_id: _Optional[_Union[ContractState.ReassignmentId, _Mapping]] = ...) -> None: ...
    class Archived(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Unassigned(_message.Message):
        __slots__ = ("target_synchronizer_id", "reassignment_counter_src", "reassignment_id")
        TARGET_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        REASSIGNMENT_COUNTER_SRC_FIELD_NUMBER: _ClassVar[int]
        REASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
        target_synchronizer_id: str
        reassignment_counter_src: int
        reassignment_id: ContractState.ReassignmentId
        def __init__(self, target_synchronizer_id: _Optional[str] = ..., reassignment_counter_src: _Optional[int] = ..., reassignment_id: _Optional[_Union[ContractState.ReassignmentId, _Mapping]] = ...) -> None: ...
    class Unknown(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ReassignmentId(_message.Message):
        __slots__ = ("source_synchronizer_id", "unassign_timestamp")
        SOURCE_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        UNASSIGN_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        source_synchronizer_id: str
        unassign_timestamp: _timestamp_pb2.Timestamp
        def __init__(self, source_synchronizer_id: _Optional[str] = ..., unassign_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LookupReceivedAcsCommitmentsRequest(_message.Message):
    __slots__ = ("time_ranges", "counter_participant_uids", "commitment_state", "verbose")
    TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    time_ranges: _containers.RepeatedCompositeFieldContainer[SynchronizerTimeRange]
    counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    commitment_state: _containers.RepeatedScalarFieldContainer[ReceivedCommitmentState]
    verbose: bool
    def __init__(self, time_ranges: _Optional[_Iterable[_Union[SynchronizerTimeRange, _Mapping]]] = ..., counter_participant_uids: _Optional[_Iterable[str]] = ..., commitment_state: _Optional[_Iterable[_Union[ReceivedCommitmentState, str]]] = ..., verbose: bool = ...) -> None: ...

class LookupReceivedAcsCommitmentsResponse(_message.Message):
    __slots__ = ("received",)
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    received: _containers.RepeatedCompositeFieldContainer[ReceivedAcsCommitmentPerSynchronizer]
    def __init__(self, received: _Optional[_Iterable[_Union[ReceivedAcsCommitmentPerSynchronizer, _Mapping]]] = ...) -> None: ...

class TimeRange(_message.Message):
    __slots__ = ("from_exclusive", "to_inclusive")
    FROM_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    from_exclusive: _timestamp_pb2.Timestamp
    to_inclusive: _timestamp_pb2.Timestamp
    def __init__(self, from_exclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., to_inclusive: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SynchronizerTimeRange(_message.Message):
    __slots__ = ("synchronizer_id", "interval")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    interval: TimeRange
    def __init__(self, synchronizer_id: _Optional[str] = ..., interval: _Optional[_Union[TimeRange, _Mapping]] = ...) -> None: ...

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

class ReceivedAcsCommitmentPerSynchronizer(_message.Message):
    __slots__ = ("synchronizer_id", "received")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    received: _containers.RepeatedCompositeFieldContainer[ReceivedAcsCommitment]
    def __init__(self, synchronizer_id: _Optional[str] = ..., received: _Optional[_Iterable[_Union[ReceivedAcsCommitment, _Mapping]]] = ...) -> None: ...

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

class SentAcsCommitmentPerSynchronizer(_message.Message):
    __slots__ = ("synchronizer_id", "sent")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SENT_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    sent: _containers.RepeatedCompositeFieldContainer[SentAcsCommitment]
    def __init__(self, synchronizer_id: _Optional[str] = ..., sent: _Optional[_Iterable[_Union[SentAcsCommitment, _Mapping]]] = ...) -> None: ...

class LookupSentAcsCommitmentsRequest(_message.Message):
    __slots__ = ("time_ranges", "counter_participant_uids", "commitment_state", "verbose")
    TIME_RANGES_FIELD_NUMBER: _ClassVar[int]
    COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    time_ranges: _containers.RepeatedCompositeFieldContainer[SynchronizerTimeRange]
    counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    commitment_state: _containers.RepeatedScalarFieldContainer[SentCommitmentState]
    verbose: bool
    def __init__(self, time_ranges: _Optional[_Iterable[_Union[SynchronizerTimeRange, _Mapping]]] = ..., counter_participant_uids: _Optional[_Iterable[str]] = ..., commitment_state: _Optional[_Iterable[_Union[SentCommitmentState, str]]] = ..., verbose: bool = ...) -> None: ...

class LookupSentAcsCommitmentsResponse(_message.Message):
    __slots__ = ("sent",)
    SENT_FIELD_NUMBER: _ClassVar[int]
    sent: _containers.RepeatedCompositeFieldContainer[SentAcsCommitmentPerSynchronizer]
    def __init__(self, sent: _Optional[_Iterable[_Union[SentAcsCommitmentPerSynchronizer, _Mapping]]] = ...) -> None: ...

class SlowCounterParticipantSynchronizerConfig(_message.Message):
    __slots__ = ("synchronizer_ids", "distinguished_participant_uids", "threshold_distinguished", "threshold_default", "participant_uids_metrics")
    SYNCHRONIZER_IDS_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHED_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_DISTINGUISHED_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_UIDS_METRICS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_ids: _containers.RepeatedScalarFieldContainer[str]
    distinguished_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    threshold_distinguished: int
    threshold_default: int
    participant_uids_metrics: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, synchronizer_ids: _Optional[_Iterable[str]] = ..., distinguished_participant_uids: _Optional[_Iterable[str]] = ..., threshold_distinguished: _Optional[int] = ..., threshold_default: _Optional[int] = ..., participant_uids_metrics: _Optional[_Iterable[str]] = ...) -> None: ...

class SetConfigForSlowCounterParticipantsRequest(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[SlowCounterParticipantSynchronizerConfig]
    def __init__(self, configs: _Optional[_Iterable[_Union[SlowCounterParticipantSynchronizerConfig, _Mapping]]] = ...) -> None: ...

class SetConfigForSlowCounterParticipantsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConfigForSlowCounterParticipantsRequest(_message.Message):
    __slots__ = ("synchronizer_ids",)
    SYNCHRONIZER_IDS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, synchronizer_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetConfigForSlowCounterParticipantsResponse(_message.Message):
    __slots__ = ("configs",)
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[SlowCounterParticipantSynchronizerConfig]
    def __init__(self, configs: _Optional[_Iterable[_Union[SlowCounterParticipantSynchronizerConfig, _Mapping]]] = ...) -> None: ...

class CounterParticipantInfo(_message.Message):
    __slots__ = ("counter_participant_uid", "synchronizer_id", "intervals_behind", "behind_since", "as_of_sequencing_timestamp")
    COUNTER_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    INTERVALS_BEHIND_FIELD_NUMBER: _ClassVar[int]
    BEHIND_SINCE_FIELD_NUMBER: _ClassVar[int]
    AS_OF_SEQUENCING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    counter_participant_uid: str
    synchronizer_id: str
    intervals_behind: int
    behind_since: _duration_pb2.Duration
    as_of_sequencing_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, counter_participant_uid: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., intervals_behind: _Optional[int] = ..., behind_since: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., as_of_sequencing_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetIntervalsBehindForCounterParticipantsRequest(_message.Message):
    __slots__ = ("counter_participant_uids", "synchronizer_ids", "threshold")
    COUNTER_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_IDS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    counter_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    synchronizer_ids: _containers.RepeatedScalarFieldContainer[str]
    threshold: int
    def __init__(self, counter_participant_uids: _Optional[_Iterable[str]] = ..., synchronizer_ids: _Optional[_Iterable[str]] = ..., threshold: _Optional[int] = ...) -> None: ...

class GetIntervalsBehindForCounterParticipantsResponse(_message.Message):
    __slots__ = ("intervals_behind",)
    INTERVALS_BEHIND_FIELD_NUMBER: _ClassVar[int]
    intervals_behind: _containers.RepeatedCompositeFieldContainer[CounterParticipantInfo]
    def __init__(self, intervals_behind: _Optional[_Iterable[_Union[CounterParticipantInfo, _Mapping]]] = ...) -> None: ...

class CountInFlightRequest(_message.Message):
    __slots__ = ("synchronizer_id",)
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    def __init__(self, synchronizer_id: _Optional[str] = ...) -> None: ...

class CountInFlightResponse(_message.Message):
    __slots__ = ("pending_submissions", "pending_transactions")
    PENDING_SUBMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PENDING_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    pending_submissions: int
    pending_transactions: int
    def __init__(self, pending_submissions: _Optional[int] = ..., pending_transactions: _Optional[int] = ...) -> None: ...
