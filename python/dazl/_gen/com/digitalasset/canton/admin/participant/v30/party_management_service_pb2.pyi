# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
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

class GetAddPartyStatusRequest(_message.Message):
    __slots__ = ("add_party_request_id",)
    ADD_PARTY_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    add_party_request_id: str
    def __init__(self, add_party_request_id: _Optional[str] = ...) -> None: ...

class GetAddPartyStatusResponse(_message.Message):
    __slots__ = ("party_id", "synchronizer_id", "source_participant_uid", "target_participant_uid", "topology_serial", "participant_permission", "status")
    class Status(_message.Message):
        __slots__ = ("proposal_processed", "agreement_accepted", "topology_authorized", "connection_established", "replicating_acs", "fully_replicated_acs", "completed", "error", "disconnected")
        class ProposalProcessed(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AgreementAccepted(_message.Message):
            __slots__ = ("sequencer_uid",)
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            def __init__(self, sequencer_uid: _Optional[str] = ...) -> None: ...
        class TopologyAuthorized(_message.Message):
            __slots__ = ("sequencer_uid", "timestamp")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            timestamp: _timestamp_pb2.Timestamp
            def __init__(self, sequencer_uid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class ConnectionEstablished(_message.Message):
            __slots__ = ("sequencer_uid", "timestamp")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            timestamp: _timestamp_pb2.Timestamp
            def __init__(self, sequencer_uid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class ReplicatingAcs(_message.Message):
            __slots__ = ("sequencer_uid", "timestamp", "contracts_replicated")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            CONTRACTS_REPLICATED_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            timestamp: _timestamp_pb2.Timestamp
            contracts_replicated: int
            def __init__(self, sequencer_uid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., contracts_replicated: _Optional[int] = ...) -> None: ...
        class FullyReplicatedAcs(_message.Message):
            __slots__ = ("sequencer_uid", "timestamp", "contracts_replicated")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            CONTRACTS_REPLICATED_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            timestamp: _timestamp_pb2.Timestamp
            contracts_replicated: int
            def __init__(self, sequencer_uid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., contracts_replicated: _Optional[int] = ...) -> None: ...
        class Completed(_message.Message):
            __slots__ = ("sequencer_uid", "timestamp", "contracts_replicated")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            CONTRACTS_REPLICATED_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            timestamp: _timestamp_pb2.Timestamp
            contracts_replicated: int
            def __init__(self, sequencer_uid: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., contracts_replicated: _Optional[int] = ...) -> None: ...
        class Error(_message.Message):
            __slots__ = ("error_message", "status_prior_to_error")
            ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            STATUS_PRIOR_TO_ERROR_FIELD_NUMBER: _ClassVar[int]
            error_message: str
            status_prior_to_error: GetAddPartyStatusResponse.Status
            def __init__(self, error_message: _Optional[str] = ..., status_prior_to_error: _Optional[_Union[GetAddPartyStatusResponse.Status, _Mapping]] = ...) -> None: ...
        class Disconnected(_message.Message):
            __slots__ = ("disconnect_message", "status_prior_to_disconnect")
            DISCONNECT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            STATUS_PRIOR_TO_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
            disconnect_message: str
            status_prior_to_disconnect: GetAddPartyStatusResponse.Status
            def __init__(self, disconnect_message: _Optional[str] = ..., status_prior_to_disconnect: _Optional[_Union[GetAddPartyStatusResponse.Status, _Mapping]] = ...) -> None: ...
        PROPOSAL_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        AGREEMENT_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
        TOPOLOGY_AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_ESTABLISHED_FIELD_NUMBER: _ClassVar[int]
        REPLICATING_ACS_FIELD_NUMBER: _ClassVar[int]
        FULLY_REPLICATED_ACS_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
        proposal_processed: GetAddPartyStatusResponse.Status.ProposalProcessed
        agreement_accepted: GetAddPartyStatusResponse.Status.AgreementAccepted
        topology_authorized: GetAddPartyStatusResponse.Status.TopologyAuthorized
        connection_established: GetAddPartyStatusResponse.Status.ConnectionEstablished
        replicating_acs: GetAddPartyStatusResponse.Status.ReplicatingAcs
        fully_replicated_acs: GetAddPartyStatusResponse.Status.FullyReplicatedAcs
        completed: GetAddPartyStatusResponse.Status.Completed
        error: GetAddPartyStatusResponse.Status.Error
        disconnected: GetAddPartyStatusResponse.Status.Disconnected
        def __init__(self, proposal_processed: _Optional[_Union[GetAddPartyStatusResponse.Status.ProposalProcessed, _Mapping]] = ..., agreement_accepted: _Optional[_Union[GetAddPartyStatusResponse.Status.AgreementAccepted, _Mapping]] = ..., topology_authorized: _Optional[_Union[GetAddPartyStatusResponse.Status.TopologyAuthorized, _Mapping]] = ..., connection_established: _Optional[_Union[GetAddPartyStatusResponse.Status.ConnectionEstablished, _Mapping]] = ..., replicating_acs: _Optional[_Union[GetAddPartyStatusResponse.Status.ReplicatingAcs, _Mapping]] = ..., fully_replicated_acs: _Optional[_Union[GetAddPartyStatusResponse.Status.FullyReplicatedAcs, _Mapping]] = ..., completed: _Optional[_Union[GetAddPartyStatusResponse.Status.Completed, _Mapping]] = ..., error: _Optional[_Union[GetAddPartyStatusResponse.Status.Error, _Mapping]] = ..., disconnected: _Optional[_Union[GetAddPartyStatusResponse.Status.Disconnected, _Mapping]] = ...) -> None: ...
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    synchronizer_id: str
    source_participant_uid: str
    target_participant_uid: str
    topology_serial: int
    participant_permission: ParticipantPermission
    status: GetAddPartyStatusResponse.Status
    def __init__(self, party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., source_participant_uid: _Optional[str] = ..., target_participant_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ..., participant_permission: _Optional[_Union[ParticipantPermission, str]] = ..., status: _Optional[_Union[GetAddPartyStatusResponse.Status, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("acs_snapshot", "workflow_id_prefix", "contract_import_mode", "representative_package_id_override")
    ACS_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IMPORT_MODE_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATIVE_PACKAGE_ID_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    acs_snapshot: bytes
    workflow_id_prefix: str
    contract_import_mode: _acs_import_pb2.ContractImportMode
    representative_package_id_override: _acs_import_pb2.RepresentativePackageIdOverride
    def __init__(self, acs_snapshot: _Optional[bytes] = ..., workflow_id_prefix: _Optional[str] = ..., contract_import_mode: _Optional[_Union[_acs_import_pb2.ContractImportMode, str]] = ..., representative_package_id_override: _Optional[_Union[_acs_import_pb2.RepresentativePackageIdOverride, _Mapping]] = ...) -> None: ...

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
