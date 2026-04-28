# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from . import acs_import_pb2 as _acs_import_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParticipantPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARTICIPANT_PERMISSION_UNSPECIFIED: _ClassVar[ParticipantPermission]
    PARTICIPANT_PERMISSION_SUBMISSION: _ClassVar[ParticipantPermission]
    PARTICIPANT_PERMISSION_CONFIRMATION: _ClassVar[ParticipantPermission]
    PARTICIPANT_PERMISSION_OBSERVATION: _ClassVar[ParticipantPermission]
PARTICIPANT_PERMISSION_UNSPECIFIED: ParticipantPermission
PARTICIPANT_PERMISSION_SUBMISSION: ParticipantPermission
PARTICIPANT_PERMISSION_CONFIRMATION: ParticipantPermission
PARTICIPANT_PERMISSION_OBSERVATION: ParticipantPermission

class AddPartyAsyncRequest(_message.Message):
    __slots__ = ("arguments",)
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    arguments: AddPartyArguments
    def __init__(self, arguments: _Optional[_Union[AddPartyArguments, _Mapping]] = ...) -> None: ...

class AddPartyArguments(_message.Message):
    __slots__ = ("party_id", "synchronizer_id", "source_participant_uid", "topology_serial", "participant_permission")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    synchronizer_id: str
    source_participant_uid: str
    topology_serial: int
    participant_permission: ParticipantPermission
    def __init__(self, party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., source_participant_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ..., participant_permission: _Optional[_Union[ParticipantPermission, str]] = ...) -> None: ...

class AddPartyAsyncResponse(_message.Message):
    __slots__ = ("add_party_request_id",)
    ADD_PARTY_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    add_party_request_id: str
    def __init__(self, add_party_request_id: _Optional[str] = ...) -> None: ...

class AddPartyWithAcsAsyncRequest(_message.Message):
    __slots__ = ("acs_snapshot", "arguments")
    ACS_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    acs_snapshot: bytes
    arguments: AddPartyArguments
    def __init__(self, acs_snapshot: _Optional[bytes] = ..., arguments: _Optional[_Union[AddPartyArguments, _Mapping]] = ...) -> None: ...

class AddPartyWithAcsAsyncResponse(_message.Message):
    __slots__ = ("add_party_request_id",)
    ADD_PARTY_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    add_party_request_id: str
    def __init__(self, add_party_request_id: _Optional[str] = ...) -> None: ...

class GetAddPartyStatusRequest(_message.Message):
    __slots__ = ("add_party_request_id",)
    ADD_PARTY_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    add_party_request_id: str
    def __init__(self, add_party_request_id: _Optional[str] = ...) -> None: ...

class GetAddPartyStatusResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: PartyReplicationStatus
    def __init__(self, status: _Optional[_Union[PartyReplicationStatus, _Mapping]] = ...) -> None: ...

class PartyReplicationStatus(_message.Message):
    __slots__ = ("parameters", "agreement", "authorization", "replication", "indexing", "has_completed", "error_message")
    class ReplicationParameters(_message.Message):
        __slots__ = ("request_id", "party_id", "synchronizer_id", "source_participant_uid", "target_participant_uid", "topology_serial")
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        PARTY_ID_FIELD_NUMBER: _ClassVar[int]
        SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
        TARGET_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
        TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
        request_id: str
        party_id: str
        synchronizer_id: str
        source_participant_uid: str
        target_participant_uid: str
        topology_serial: int
        def __init__(self, request_id: _Optional[str] = ..., party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., source_participant_uid: _Optional[str] = ..., target_participant_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ...) -> None: ...
    class SequencerChannelAgreement(_message.Message):
        __slots__ = ("sequencer_uid",)
        SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
        sequencer_uid: str
        def __init__(self, sequencer_uid: _Optional[str] = ...) -> None: ...
    class PartyReplicationAuthorization(_message.Message):
        __slots__ = ("onboarding_at", "is_onboarding_flag_cleared")
        ONBOARDING_AT_FIELD_NUMBER: _ClassVar[int]
        IS_ONBOARDING_FLAG_CLEARED_FIELD_NUMBER: _ClassVar[int]
        onboarding_at: _timestamp_pb2.Timestamp
        is_onboarding_flag_cleared: bool
        def __init__(self, onboarding_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_onboarding_flag_cleared: bool = ...) -> None: ...
    class AcsReplicationProgress(_message.Message):
        __slots__ = ("processed_contract_count", "fully_processed_acs")
        PROCESSED_CONTRACT_COUNT_FIELD_NUMBER: _ClassVar[int]
        FULLY_PROCESSED_ACS_FIELD_NUMBER: _ClassVar[int]
        processed_contract_count: int
        fully_processed_acs: bool
        def __init__(self, processed_contract_count: _Optional[int] = ..., fully_processed_acs: bool = ...) -> None: ...
    class AcsIndexingProgress(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PartyReplicationError(_message.Message):
        __slots__ = ("error_message",)
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        error_message: str
        def __init__(self, error_message: _Optional[str] = ...) -> None: ...
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

class ExportPartyAcsRequest(_message.Message):
    __slots__ = ("party_id", "synchronizer_id", "target_participant_uid", "begin_offset_exclusive", "wait_for_activation_timeout")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_OFFSET_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_ACTIVATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    synchronizer_id: str
    target_participant_uid: str
    begin_offset_exclusive: int
    wait_for_activation_timeout: _duration_pb2.Duration
    def __init__(self, party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., target_participant_uid: _Optional[str] = ..., begin_offset_exclusive: _Optional[int] = ..., wait_for_activation_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ExportPartyAcsResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class ImportPartyAcsRequest(_message.Message):
    __slots__ = ("acs_snapshot", "synchronizer_id", "workflow_id_prefix", "contract_import_mode", "representative_package_id_override", "party_id")
    ACS_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IMPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATIVE_PACKAGE_ID_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    acs_snapshot: bytes
    synchronizer_id: str
    workflow_id_prefix: str
    contract_import_mode: _acs_import_pb2.ContractImportMode
    representative_package_id_override: _acs_import_pb2.RepresentativePackageIdOverride
    party_id: str
    def __init__(self, acs_snapshot: _Optional[bytes] = ..., synchronizer_id: _Optional[str] = ..., workflow_id_prefix: _Optional[str] = ..., contract_import_mode: _Optional[_Union[_acs_import_pb2.ContractImportMode, str]] = ..., representative_package_id_override: _Optional[_Union[_acs_import_pb2.RepresentativePackageIdOverride, _Mapping]] = ..., party_id: _Optional[str] = ...) -> None: ...

class ImportPartyAcsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetHighestOffsetByTimestampRequest(_message.Message):
    __slots__ = ("synchronizer_id", "timestamp", "force")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    timestamp: _timestamp_pb2.Timestamp
    force: bool
    def __init__(self, synchronizer_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., force: bool = ...) -> None: ...

class GetHighestOffsetByTimestampResponse(_message.Message):
    __slots__ = ("ledger_offset",)
    LEDGER_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ledger_offset: int
    def __init__(self, ledger_offset: _Optional[int] = ...) -> None: ...

class ClearPartyOnboardingFlagRequest(_message.Message):
    __slots__ = ("party_id", "synchronizer_id", "begin_offset_exclusive", "wait_for_activation_timeout")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_OFFSET_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_ACTIVATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    synchronizer_id: str
    begin_offset_exclusive: int
    wait_for_activation_timeout: _duration_pb2.Duration
    def __init__(self, party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., begin_offset_exclusive: _Optional[int] = ..., wait_for_activation_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ClearPartyOnboardingFlagResponse(_message.Message):
    __slots__ = ("onboarded", "earliest_retry_timestamp")
    ONBOARDED_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_RETRY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    onboarded: bool
    earliest_retry_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, onboarded: bool = ..., earliest_retry_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
