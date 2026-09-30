# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ....admin.participant.v30 import active_contract_pb2 as _active_contract_pb2
from ....crypto.v30 import crypto_pb2 as _crypto_pb2
from ....protocol.v30 import topology_pb2 as _topology_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcsReplicationStatus(_message.Message):
    __slots__ = ("parameters", "not_proposed", "proposed", "exists", "archived", "authorization", "replication", "has_completed", "error_message")
    class AcsReplicationParameters(_message.Message):
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
    class AgreementNotProposed(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AgreementProposed(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AgreementExists(_message.Message):
        __slots__ = ("contract_id", "agreed_at", "sequencer_uid")
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        AGREED_AT_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
        contract_id: str
        agreed_at: _timestamp_pb2.Timestamp
        sequencer_uid: str
        def __init__(self, contract_id: _Optional[str] = ..., agreed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sequencer_uid: _Optional[str] = ...) -> None: ...
    class AgreementArchived(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AcsReplicationProgress(_message.Message):
        __slots__ = ("processed_contract_count", "next_persistence_counter", "acs_hash", "fully_processed_acs")
        PROCESSED_CONTRACT_COUNT_FIELD_NUMBER: _ClassVar[int]
        NEXT_PERSISTENCE_COUNTER_FIELD_NUMBER: _ClassVar[int]
        ACS_HASH_FIELD_NUMBER: _ClassVar[int]
        FULLY_PROCESSED_ACS_FIELD_NUMBER: _ClassVar[int]
        processed_contract_count: int
        next_persistence_counter: int
        acs_hash: bytes
        fully_processed_acs: bool
        def __init__(self, processed_contract_count: _Optional[int] = ..., next_persistence_counter: _Optional[int] = ..., acs_hash: _Optional[bytes] = ..., fully_processed_acs: _Optional[bool] = ...) -> None: ...
    class AcsReplicationError(_message.Message):
        __slots__ = ("error_type", "error_message")
        class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ERROR_TYPE_UNSPECIFIED: _ClassVar[AcsReplicationStatus.AcsReplicationError.ErrorType]
            ERROR_TYPE_FAILED: _ClassVar[AcsReplicationStatus.AcsReplicationError.ErrorType]
            ERROR_TYPE_DISCONNECTED: _ClassVar[AcsReplicationStatus.AcsReplicationError.ErrorType]
        ERROR_TYPE_UNSPECIFIED: AcsReplicationStatus.AcsReplicationError.ErrorType
        ERROR_TYPE_FAILED: AcsReplicationStatus.AcsReplicationError.ErrorType
        ERROR_TYPE_DISCONNECTED: AcsReplicationStatus.AcsReplicationError.ErrorType
        ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        error_type: AcsReplicationStatus.AcsReplicationError.ErrorType
        error_message: str
        def __init__(self, error_type: _Optional[_Union[AcsReplicationStatus.AcsReplicationError.ErrorType, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
    class PartyReplicationAuthorization(_message.Message):
        __slots__ = ("onboarding_at", "is_onboarding_flag_cleared")
        ONBOARDING_AT_FIELD_NUMBER: _ClassVar[int]
        IS_ONBOARDING_FLAG_CLEARED_FIELD_NUMBER: _ClassVar[int]
        onboarding_at: _timestamp_pb2.Timestamp
        is_onboarding_flag_cleared: bool
        def __init__(self, onboarding_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_onboarding_flag_cleared: _Optional[bool] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    NOT_PROPOSED_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_FIELD_NUMBER: _ClassVar[int]
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FIELD_NUMBER: _ClassVar[int]
    HAS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    parameters: AcsReplicationStatus.AcsReplicationParameters
    not_proposed: AcsReplicationStatus.AgreementNotProposed
    proposed: AcsReplicationStatus.AgreementProposed
    exists: AcsReplicationStatus.AgreementExists
    archived: AcsReplicationStatus.AgreementArchived
    authorization: AcsReplicationStatus.PartyReplicationAuthorization
    replication: AcsReplicationStatus.AcsReplicationProgress
    has_completed: bool
    error_message: AcsReplicationStatus.AcsReplicationError
    def __init__(self, parameters: _Optional[_Union[AcsReplicationStatus.AcsReplicationParameters, _Mapping]] = ..., not_proposed: _Optional[_Union[AcsReplicationStatus.AgreementNotProposed, _Mapping]] = ..., proposed: _Optional[_Union[AcsReplicationStatus.AgreementProposed, _Mapping]] = ..., exists: _Optional[_Union[AcsReplicationStatus.AgreementExists, _Mapping]] = ..., archived: _Optional[_Union[AcsReplicationStatus.AgreementArchived, _Mapping]] = ..., authorization: _Optional[_Union[AcsReplicationStatus.PartyReplicationAuthorization, _Mapping]] = ..., replication: _Optional[_Union[AcsReplicationStatus.AcsReplicationProgress, _Mapping]] = ..., has_completed: _Optional[bool] = ..., error_message: _Optional[_Union[AcsReplicationStatus.AcsReplicationError, _Mapping]] = ...) -> None: ...

class AcsReplicationTargetParticipantMessage(_message.Message):
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
    initialize: AcsReplicationTargetParticipantMessage.Initialize
    send_acs_up_to: AcsReplicationTargetParticipantMessage.SendAcsUpTo
    def __init__(self, initialize: _Optional[_Union[AcsReplicationTargetParticipantMessage.Initialize, _Mapping]] = ..., send_acs_up_to: _Optional[_Union[AcsReplicationTargetParticipantMessage.SendAcsUpTo, _Mapping]] = ...) -> None: ...

class AcsReplicationSourceParticipantMessage(_message.Message):
    __slots__ = ("acs_batch", "end_of_acs")
    class AcsBatch(_message.Message):
        __slots__ = ("contracts",)
        CONTRACTS_FIELD_NUMBER: _ClassVar[int]
        contracts: _containers.RepeatedCompositeFieldContainer[_active_contract_pb2.ActiveContract]
        def __init__(self, contracts: _Optional[_Iterable[_Union[_active_contract_pb2.ActiveContract, _Mapping]]] = ...) -> None: ...
    class EndOfAcs(_message.Message):
        __slots__ = ("acs_digest", "signature")
        ACS_DIGEST_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        acs_digest: bytes
        signature: _crypto_pb2.Signature
        def __init__(self, acs_digest: _Optional[bytes] = ..., signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...
    ACS_BATCH_FIELD_NUMBER: _ClassVar[int]
    END_OF_ACS_FIELD_NUMBER: _ClassVar[int]
    acs_batch: AcsReplicationSourceParticipantMessage.AcsBatch
    end_of_acs: AcsReplicationSourceParticipantMessage.EndOfAcs
    def __init__(self, acs_batch: _Optional[_Union[AcsReplicationSourceParticipantMessage.AcsBatch, _Mapping]] = ..., end_of_acs: _Optional[_Union[AcsReplicationSourceParticipantMessage.EndOfAcs, _Mapping]] = ...) -> None: ...

class AcsDigest(_message.Message):
    __slots__ = ("acs_hash", "get_acs_args", "source_participant_uid", "agreed_at")
    ACS_HASH_FIELD_NUMBER: _ClassVar[int]
    GET_ACS_ARGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    AGREED_AT_FIELD_NUMBER: _ClassVar[int]
    acs_hash: bytes
    get_acs_args: GetAcsArguments
    source_participant_uid: str
    agreed_at: _timestamp_pb2.Timestamp
    def __init__(self, acs_hash: _Optional[bytes] = ..., get_acs_args: _Optional[_Union[GetAcsArguments, _Mapping]] = ..., source_participant_uid: _Optional[str] = ..., agreed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetAcsArguments(_message.Message):
    __slots__ = ("party_id", "synchronizer_id", "as_of", "excluded_stakeholders")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    AS_OF_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    synchronizer_id: str
    as_of: _timestamp_pb2.Timestamp
    excluded_stakeholders: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., as_of: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., excluded_stakeholders: _Optional[_Iterable[str]] = ...) -> None: ...
