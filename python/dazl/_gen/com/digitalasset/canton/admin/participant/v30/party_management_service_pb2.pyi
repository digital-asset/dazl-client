# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddPartyAsyncRequest(_message.Message):
    __slots__ = ("party_id", "synchronizer_id", "source_participant_uid", "serial")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    synchronizer_id: str
    source_participant_uid: str
    serial: int
    def __init__(self, party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., source_participant_uid: _Optional[str] = ..., serial: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("party_id", "synchronizer_id", "source_participant_uid", "target_participant_uid", "status")
    class Status(_message.Message):
        __slots__ = ("proposal_processed", "agreement_accepted", "topology_authorized", "connection_established", "replicating_acs", "completed", "error")
        class ProposalProcessed(_message.Message):
            __slots__ = ("topology_serial",)
            TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
            topology_serial: int
            def __init__(self, topology_serial: _Optional[int] = ...) -> None: ...
        class AgreementAccepted(_message.Message):
            __slots__ = ("sequencer_uid", "topology_serial")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            topology_serial: int
            def __init__(self, sequencer_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ...) -> None: ...
        class TopologyAuthorized(_message.Message):
            __slots__ = ("sequencer_uid", "topology_serial", "timestamp")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            topology_serial: int
            timestamp: _timestamp_pb2.Timestamp
            def __init__(self, sequencer_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class ConnectionEstablished(_message.Message):
            __slots__ = ("sequencer_uid", "topology_serial", "timestamp")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            topology_serial: int
            timestamp: _timestamp_pb2.Timestamp
            def __init__(self, sequencer_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
        class ReplicatingAcs(_message.Message):
            __slots__ = ("sequencer_uid", "topology_serial", "timestamp", "contracts_replicated")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            CONTRACTS_REPLICATED_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            topology_serial: int
            timestamp: _timestamp_pb2.Timestamp
            contracts_replicated: int
            def __init__(self, sequencer_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., contracts_replicated: _Optional[int] = ...) -> None: ...
        class Completed(_message.Message):
            __slots__ = ("sequencer_uid", "topology_serial", "timestamp", "contracts_replicated")
            SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
            TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            CONTRACTS_REPLICATED_FIELD_NUMBER: _ClassVar[int]
            sequencer_uid: str
            topology_serial: int
            timestamp: _timestamp_pb2.Timestamp
            contracts_replicated: int
            def __init__(self, sequencer_uid: _Optional[str] = ..., topology_serial: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., contracts_replicated: _Optional[int] = ...) -> None: ...
        class Error(_message.Message):
            __slots__ = ("error_message", "status_prior_to_error")
            ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
            STATUS_PRIOR_TO_ERROR_FIELD_NUMBER: _ClassVar[int]
            error_message: str
            status_prior_to_error: GetAddPartyStatusResponse.Status
            def __init__(self, error_message: _Optional[str] = ..., status_prior_to_error: _Optional[_Union[GetAddPartyStatusResponse.Status, _Mapping]] = ...) -> None: ...
        PROPOSAL_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        AGREEMENT_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
        TOPOLOGY_AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_ESTABLISHED_FIELD_NUMBER: _ClassVar[int]
        REPLICATING_ACS_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        proposal_processed: GetAddPartyStatusResponse.Status.ProposalProcessed
        agreement_accepted: GetAddPartyStatusResponse.Status.AgreementAccepted
        topology_authorized: GetAddPartyStatusResponse.Status.TopologyAuthorized
        connection_established: GetAddPartyStatusResponse.Status.ConnectionEstablished
        replicating_acs: GetAddPartyStatusResponse.Status.ReplicatingAcs
        completed: GetAddPartyStatusResponse.Status.Completed
        error: GetAddPartyStatusResponse.Status.Error
        def __init__(self, proposal_processed: _Optional[_Union[GetAddPartyStatusResponse.Status.ProposalProcessed, _Mapping]] = ..., agreement_accepted: _Optional[_Union[GetAddPartyStatusResponse.Status.AgreementAccepted, _Mapping]] = ..., topology_authorized: _Optional[_Union[GetAddPartyStatusResponse.Status.TopologyAuthorized, _Mapping]] = ..., connection_established: _Optional[_Union[GetAddPartyStatusResponse.Status.ConnectionEstablished, _Mapping]] = ..., replicating_acs: _Optional[_Union[GetAddPartyStatusResponse.Status.ReplicatingAcs, _Mapping]] = ..., completed: _Optional[_Union[GetAddPartyStatusResponse.Status.Completed, _Mapping]] = ..., error: _Optional[_Union[GetAddPartyStatusResponse.Status.Error, _Mapping]] = ...) -> None: ...
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    synchronizer_id: str
    source_participant_uid: str
    target_participant_uid: str
    status: GetAddPartyStatusResponse.Status
    def __init__(self, party_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., source_participant_uid: _Optional[str] = ..., target_participant_uid: _Optional[str] = ..., status: _Optional[_Union[GetAddPartyStatusResponse.Status, _Mapping]] = ...) -> None: ...

class ExportAcsTargetSynchronizer(_message.Message):
    __slots__ = ("target_synchronizer_id",)
    TARGET_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    target_synchronizer_id: str
    def __init__(self, target_synchronizer_id: _Optional[str] = ...) -> None: ...

class ExportAcsRequest(_message.Message):
    __slots__ = ("party_ids", "synchronizer_id", "ledger_offset", "contract_synchronizer_renames")
    class ContractSynchronizerRenamesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExportAcsTargetSynchronizer
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ExportAcsTargetSynchronizer, _Mapping]] = ...) -> None: ...
    PARTY_IDS_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    LEDGER_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SYNCHRONIZER_RENAMES_FIELD_NUMBER: _ClassVar[int]
    party_ids: _containers.RepeatedScalarFieldContainer[str]
    synchronizer_id: str
    ledger_offset: int
    contract_synchronizer_renames: _containers.MessageMap[str, ExportAcsTargetSynchronizer]
    def __init__(self, party_ids: _Optional[_Iterable[str]] = ..., synchronizer_id: _Optional[str] = ..., ledger_offset: _Optional[int] = ..., contract_synchronizer_renames: _Optional[_Mapping[str, ExportAcsTargetSynchronizer]] = ...) -> None: ...

class ExportAcsResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class ExportAcsAtTimestampRequest(_message.Message):
    __slots__ = ("party_ids", "synchronizer_id", "topology_transaction_effective_time")
    PARTY_IDS_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TRANSACTION_EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    party_ids: _containers.RepeatedScalarFieldContainer[str]
    synchronizer_id: str
    topology_transaction_effective_time: _timestamp_pb2.Timestamp
    def __init__(self, party_ids: _Optional[_Iterable[str]] = ..., synchronizer_id: _Optional[str] = ..., topology_transaction_effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExportAcsAtTimestampResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...
