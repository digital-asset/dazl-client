# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ....admin.participant.v30 import active_contract_pb2 as _active_contract_pb2
from ....protocol.v30 import topology_pb2 as _topology_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartyReplicationTargetParticipantMessage(_message.Message):
    __slots__ = ("initialize", "send_acs_up_to")
    class Initialize(_message.Message):
        __slots__ = ("initial_contract_ordinal_inclusive",)
        INITIAL_CONTRACT_ORDINAL_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        initial_contract_ordinal_inclusive: int
        def __init__(self, initial_contract_ordinal_inclusive: _Optional[int] = ...) -> None: ...
    class SendAcsUpTo(_message.Message):
        __slots__ = ("max_contract_ordinal_inclusive",)
        MAX_CONTRACT_ORDINAL_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        max_contract_ordinal_inclusive: int
        def __init__(self, max_contract_ordinal_inclusive: _Optional[int] = ...) -> None: ...
    INITIALIZE_FIELD_NUMBER: _ClassVar[int]
    SEND_ACS_UP_TO_FIELD_NUMBER: _ClassVar[int]
    initialize: PartyReplicationTargetParticipantMessage.Initialize
    send_acs_up_to: PartyReplicationTargetParticipantMessage.SendAcsUpTo
    def __init__(self, initialize: _Optional[_Union[PartyReplicationTargetParticipantMessage.Initialize, _Mapping]] = ..., send_acs_up_to: _Optional[_Union[PartyReplicationTargetParticipantMessage.SendAcsUpTo, _Mapping]] = ...) -> None: ...

class PartyReplicationSourceParticipantMessage(_message.Message):
    __slots__ = ("acs_batch", "end_of_acs")
    class AcsBatch(_message.Message):
        __slots__ = ("contracts",)
        CONTRACTS_FIELD_NUMBER: _ClassVar[int]
        contracts: _containers.RepeatedCompositeFieldContainer[_active_contract_pb2.ActiveContract]
        def __init__(self, contracts: _Optional[_Iterable[_Union[_active_contract_pb2.ActiveContract, _Mapping]]] = ...) -> None: ...
    class EndOfAcs(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    ACS_BATCH_FIELD_NUMBER: _ClassVar[int]
    END_OF_ACS_FIELD_NUMBER: _ClassVar[int]
    acs_batch: PartyReplicationSourceParticipantMessage.AcsBatch
    end_of_acs: PartyReplicationSourceParticipantMessage.EndOfAcs
    def __init__(self, acs_batch: _Optional[_Union[PartyReplicationSourceParticipantMessage.AcsBatch, _Mapping]] = ..., end_of_acs: _Optional[_Union[PartyReplicationSourceParticipantMessage.EndOfAcs, _Mapping]] = ...) -> None: ...

class PartyReplicationStatus(_message.Message):
    __slots__ = ("parameters", "agreement", "authorization", "replication", "indexing", "has_completed", "error_message")
    class ReplicationParameters(_message.Message):
        __slots__ = ("request_id", "party_id", "synchronizer_id", "source_participant_uid", "target_participant_uid", "topology_serial", "participant_permission")
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        PARTY_ID_FIELD_NUMBER: _ClassVar[int]
        SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
        TARGET_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
        TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
        request_id: str
        party_id: str
        synchronizer_id: str
        source_participant_uid: str
        target_participant_uid: str
        topology_serial: int
        participant_permission: _topology_pb2.Enums.ParticipantPermission
        def __init__(self, request_id: _Optional[str] = ..., party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., source_participant_uid: _Optional[str] = ..., target_participant_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ..., participant_permission: _Optional[_Union[_topology_pb2.Enums.ParticipantPermission, str]] = ...) -> None: ...
    class SequencerChannelAgreement(_message.Message):
        __slots__ = ("contract_id", "sequencer_uid")
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
        contract_id: str
        sequencer_uid: str
        def __init__(self, contract_id: _Optional[str] = ..., sequencer_uid: _Optional[str] = ...) -> None: ...
    class PartyReplicationAuthorization(_message.Message):
        __slots__ = ("onboarding_at", "is_onboarding_flag_cleared")
        ONBOARDING_AT_FIELD_NUMBER: _ClassVar[int]
        IS_ONBOARDING_FLAG_CLEARED_FIELD_NUMBER: _ClassVar[int]
        onboarding_at: _timestamp_pb2.Timestamp
        is_onboarding_flag_cleared: bool
        def __init__(self, onboarding_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_onboarding_flag_cleared: bool = ...) -> None: ...
    class AcsReplicationProgress(_message.Message):
        __slots__ = ("processed_contract_count", "next_persistence_counter", "fully_processed_acs")
        PROCESSED_CONTRACT_COUNT_FIELD_NUMBER: _ClassVar[int]
        NEXT_PERSISTENCE_COUNTER_FIELD_NUMBER: _ClassVar[int]
        FULLY_PROCESSED_ACS_FIELD_NUMBER: _ClassVar[int]
        processed_contract_count: int
        next_persistence_counter: int
        fully_processed_acs: bool
        def __init__(self, processed_contract_count: _Optional[int] = ..., next_persistence_counter: _Optional[int] = ..., fully_processed_acs: bool = ...) -> None: ...
    class AcsIndexingProgress(_message.Message):
        __slots__ = ("indexed_contract_activation_change_count", "next_indexing_counter", "indexing_almost_done_watermark")
        INDEXED_CONTRACT_ACTIVATION_CHANGE_COUNT_FIELD_NUMBER: _ClassVar[int]
        NEXT_INDEXING_COUNTER_FIELD_NUMBER: _ClassVar[int]
        INDEXING_ALMOST_DONE_WATERMARK_FIELD_NUMBER: _ClassVar[int]
        indexed_contract_activation_change_count: int
        next_indexing_counter: int
        indexing_almost_done_watermark: int
        def __init__(self, indexed_contract_activation_change_count: _Optional[int] = ..., next_indexing_counter: _Optional[int] = ..., indexing_almost_done_watermark: _Optional[int] = ...) -> None: ...
    class PartyReplicationError(_message.Message):
        __slots__ = ("error_type", "error_message")
        class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ERROR_TYPE_UNSPECIFIED: _ClassVar[PartyReplicationStatus.PartyReplicationError.ErrorType]
            ERROR_TYPE_FAILED: _ClassVar[PartyReplicationStatus.PartyReplicationError.ErrorType]
            ERROR_TYPE_DISCONNECTED: _ClassVar[PartyReplicationStatus.PartyReplicationError.ErrorType]
        ERROR_TYPE_UNSPECIFIED: PartyReplicationStatus.PartyReplicationError.ErrorType
        ERROR_TYPE_FAILED: PartyReplicationStatus.PartyReplicationError.ErrorType
        ERROR_TYPE_DISCONNECTED: PartyReplicationStatus.PartyReplicationError.ErrorType
        ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        error_type: PartyReplicationStatus.PartyReplicationError.ErrorType
        error_message: str
        def __init__(self, error_type: _Optional[_Union[PartyReplicationStatus.PartyReplicationError.ErrorType, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FIELD_NUMBER: _ClassVar[int]
    INDEXING_FIELD_NUMBER: _ClassVar[int]
    HAS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    parameters: PartyReplicationStatus.ReplicationParameters
    agreement: PartyReplicationStatus.SequencerChannelAgreement
    authorization: PartyReplicationStatus.PartyReplicationAuthorization
    replication: PartyReplicationStatus.AcsReplicationProgress
    indexing: PartyReplicationStatus.AcsIndexingProgress
    has_completed: bool
    error_message: PartyReplicationStatus.PartyReplicationError
    def __init__(self, parameters: _Optional[_Union[PartyReplicationStatus.ReplicationParameters, _Mapping]] = ..., agreement: _Optional[_Union[PartyReplicationStatus.SequencerChannelAgreement, _Mapping]] = ..., authorization: _Optional[_Union[PartyReplicationStatus.PartyReplicationAuthorization, _Mapping]] = ..., replication: _Optional[_Union[PartyReplicationStatus.AcsReplicationProgress, _Mapping]] = ..., indexing: _Optional[_Union[PartyReplicationStatus.AcsIndexingProgress, _Mapping]] = ..., has_completed: bool = ..., error_message: _Optional[_Union[PartyReplicationStatus.PartyReplicationError, _Mapping]] = ...) -> None: ...
