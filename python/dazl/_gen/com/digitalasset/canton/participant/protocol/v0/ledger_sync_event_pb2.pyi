# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v0 import participant_transaction_pb2 as _participant_transaction_pb2
from ....protocol.v0 import participant_transfer_pb2 as _participant_transfer_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    Transaction: _ClassVar[CommandKind]
    TransferOut: _ClassVar[CommandKind]
    TransferIn: _ClassVar[CommandKind]
Transaction: CommandKind
TransferOut: CommandKind
TransferIn: CommandKind

class LedgerSyncEvent(_message.Message):
    __slots__ = ["configuration_changed", "configuration_change_rejected", "party_added_to_participant", "public_package_upload", "transaction_accepted", "command_rejected", "party_allocation_rejected", "public_package_upload_rejected", "transferred_out", "transferred_in"]
    CONFIGURATION_CHANGED_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_CHANGE_REJECTED_FIELD_NUMBER: _ClassVar[int]
    PARTY_ADDED_TO_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_PACKAGE_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    COMMAND_REJECTED_FIELD_NUMBER: _ClassVar[int]
    PARTY_ALLOCATION_REJECTED_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_PACKAGE_UPLOAD_REJECTED_FIELD_NUMBER: _ClassVar[int]
    TRANSFERRED_OUT_FIELD_NUMBER: _ClassVar[int]
    TRANSFERRED_IN_FIELD_NUMBER: _ClassVar[int]
    configuration_changed: ConfigurationChanged
    configuration_change_rejected: ConfigurationChangeRejected
    party_added_to_participant: PartyAddedToParticipant
    public_package_upload: PublicPackageUpload
    transaction_accepted: TransactionAccepted
    command_rejected: CommandRejected
    party_allocation_rejected: PartyAllocationRejected
    public_package_upload_rejected: PublicPackageUploadRejected
    transferred_out: TransferredOut
    transferred_in: TransferredIn
    def __init__(self, configuration_changed: _Optional[_Union[ConfigurationChanged, _Mapping]] = ..., configuration_change_rejected: _Optional[_Union[ConfigurationChangeRejected, _Mapping]] = ..., party_added_to_participant: _Optional[_Union[PartyAddedToParticipant, _Mapping]] = ..., public_package_upload: _Optional[_Union[PublicPackageUpload, _Mapping]] = ..., transaction_accepted: _Optional[_Union[TransactionAccepted, _Mapping]] = ..., command_rejected: _Optional[_Union[CommandRejected, _Mapping]] = ..., party_allocation_rejected: _Optional[_Union[PartyAllocationRejected, _Mapping]] = ..., public_package_upload_rejected: _Optional[_Union[PublicPackageUploadRejected, _Mapping]] = ..., transferred_out: _Optional[_Union[TransferredOut, _Mapping]] = ..., transferred_in: _Optional[_Union[TransferredIn, _Mapping]] = ...) -> None: ...

class ConfigurationChanged(_message.Message):
    __slots__ = ["submission_id", "configuration", "participant_id", "record_time"]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    configuration: Configuration
    participant_id: str
    record_time: _timestamp_pb2.Timestamp
    def __init__(self, submission_id: _Optional[str] = ..., configuration: _Optional[_Union[Configuration, _Mapping]] = ..., participant_id: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Configuration(_message.Message):
    __slots__ = ["generation", "time_model", "max_deduplication_duration"]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    TIME_MODEL_FIELD_NUMBER: _ClassVar[int]
    MAX_DEDUPLICATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    generation: int
    time_model: TimeModel
    max_deduplication_duration: _duration_pb2.Duration
    def __init__(self, generation: _Optional[int] = ..., time_model: _Optional[_Union[TimeModel, _Mapping]] = ..., max_deduplication_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class TimeModel(_message.Message):
    __slots__ = ["avg_transaction_latency", "min_skew", "max_skew"]
    AVG_TRANSACTION_LATENCY_FIELD_NUMBER: _ClassVar[int]
    MIN_SKEW_FIELD_NUMBER: _ClassVar[int]
    MAX_SKEW_FIELD_NUMBER: _ClassVar[int]
    avg_transaction_latency: _duration_pb2.Duration
    min_skew: _duration_pb2.Duration
    max_skew: _duration_pb2.Duration
    def __init__(self, avg_transaction_latency: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., min_skew: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_skew: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ConfigurationChangeRejected(_message.Message):
    __slots__ = ["submission_id", "reason", "participant_id", "recordTime", "proposed_configuration"]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDTIME_FIELD_NUMBER: _ClassVar[int]
    PROPOSED_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    reason: str
    participant_id: str
    recordTime: _timestamp_pb2.Timestamp
    proposed_configuration: Configuration
    def __init__(self, submission_id: _Optional[str] = ..., reason: _Optional[str] = ..., participant_id: _Optional[str] = ..., recordTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., proposed_configuration: _Optional[_Union[Configuration, _Mapping]] = ...) -> None: ...

class PartyAddedToParticipant(_message.Message):
    __slots__ = ["party", "display_name", "participant_id", "record_time", "submission_id"]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    party: str
    display_name: str
    participant_id: str
    record_time: _timestamp_pb2.Timestamp
    submission_id: str
    def __init__(self, party: _Optional[str] = ..., display_name: _Optional[str] = ..., participant_id: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., submission_id: _Optional[str] = ...) -> None: ...

class PartyAllocationRejected(_message.Message):
    __slots__ = ["submission_id", "participant_id", "record_time", "rejection_reason"]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    participant_id: str
    record_time: _timestamp_pb2.Timestamp
    rejection_reason: str
    def __init__(self, submission_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejection_reason: _Optional[str] = ...) -> None: ...

class PublicPackageUpload(_message.Message):
    __slots__ = ["archives", "source_description", "record_time", "submission_id"]
    ARCHIVES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    archives: _containers.RepeatedScalarFieldContainer[bytes]
    source_description: _wrappers_pb2.StringValue
    record_time: _timestamp_pb2.Timestamp
    submission_id: str
    def __init__(self, archives: _Optional[_Iterable[bytes]] = ..., source_description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., submission_id: _Optional[str] = ...) -> None: ...

class PublicPackageUploadRejected(_message.Message):
    __slots__ = ["submission_id", "record_time", "rejection_reason"]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    record_time: _timestamp_pb2.Timestamp
    rejection_reason: str
    def __init__(self, submission_id: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejection_reason: _Optional[str] = ...) -> None: ...

class TransactionAccepted(_message.Message):
    __slots__ = ["completion_info", "transaction_meta", "transaction", "transaction_id", "record_time", "divulged_contracts", "blinding_info", "contract_metadata", "hosted_witnesses"]
    class ContractMetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    COMPLETION_INFO_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_META_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    DIVULGED_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    BLINDING_INFO_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_METADATA_FIELD_NUMBER: _ClassVar[int]
    HOSTED_WITNESSES_FIELD_NUMBER: _ClassVar[int]
    completion_info: CompletionInfo
    transaction_meta: TransactionMeta
    transaction: bytes
    transaction_id: str
    record_time: _timestamp_pb2.Timestamp
    divulged_contracts: _containers.RepeatedCompositeFieldContainer[DivulgedContract]
    blinding_info: BlindingInfo
    contract_metadata: _containers.ScalarMap[str, bytes]
    hosted_witnesses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., transaction_meta: _Optional[_Union[TransactionMeta, _Mapping]] = ..., transaction: _Optional[bytes] = ..., transaction_id: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., divulged_contracts: _Optional[_Iterable[_Union[DivulgedContract, _Mapping]]] = ..., blinding_info: _Optional[_Union[BlindingInfo, _Mapping]] = ..., contract_metadata: _Optional[_Mapping[str, bytes]] = ..., hosted_witnesses: _Optional[_Iterable[str]] = ...) -> None: ...

class CompletionInfo(_message.Message):
    __slots__ = ["act_as", "application_id", "command_id", "optDeduplicationPeriod", "submission_id"]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    OPTDEDUPLICATIONPERIOD_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    act_as: _containers.RepeatedScalarFieldContainer[str]
    application_id: str
    command_id: str
    optDeduplicationPeriod: _participant_transaction_pb2.DeduplicationPeriod
    submission_id: str
    def __init__(self, act_as: _Optional[_Iterable[str]] = ..., application_id: _Optional[str] = ..., command_id: _Optional[str] = ..., optDeduplicationPeriod: _Optional[_Union[_participant_transaction_pb2.DeduplicationPeriod, _Mapping]] = ..., submission_id: _Optional[str] = ...) -> None: ...

class TransactionMeta(_message.Message):
    __slots__ = ["ledger_time", "workflow_id", "submission_time", "submission_seed", "used_packages", "node_seeds", "by_key_nodes", "domain_id"]
    class ByKeyNodes(_message.Message):
        __slots__ = ["by_key_node"]
        BY_KEY_NODE_FIELD_NUMBER: _ClassVar[int]
        by_key_node: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, by_key_node: _Optional[_Iterable[int]] = ...) -> None: ...
    LEDGER_TIME_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_SEED_FIELD_NUMBER: _ClassVar[int]
    USED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    NODE_SEEDS_FIELD_NUMBER: _ClassVar[int]
    BY_KEY_NODES_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ledger_time: _timestamp_pb2.Timestamp
    workflow_id: _wrappers_pb2.StringValue
    submission_time: _timestamp_pb2.Timestamp
    submission_seed: bytes
    used_packages: _containers.RepeatedScalarFieldContainer[str]
    node_seeds: _containers.RepeatedCompositeFieldContainer[NodeSeed]
    by_key_nodes: TransactionMeta.ByKeyNodes
    domain_id: _wrappers_pb2.StringValue
    def __init__(self, ledger_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., workflow_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., submission_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., submission_seed: _Optional[bytes] = ..., used_packages: _Optional[_Iterable[str]] = ..., node_seeds: _Optional[_Iterable[_Union[NodeSeed, _Mapping]]] = ..., by_key_nodes: _Optional[_Union[TransactionMeta.ByKeyNodes, _Mapping]] = ..., domain_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class NodeSeed(_message.Message):
    __slots__ = ["node_index", "node_seed"]
    NODE_INDEX_FIELD_NUMBER: _ClassVar[int]
    NODE_SEED_FIELD_NUMBER: _ClassVar[int]
    node_index: int
    node_seed: bytes
    def __init__(self, node_index: _Optional[int] = ..., node_seed: _Optional[bytes] = ...) -> None: ...

class DivulgedContract(_message.Message):
    __slots__ = ["contract_id", "contract_inst"]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_INST_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    contract_inst: bytes
    def __init__(self, contract_id: _Optional[str] = ..., contract_inst: _Optional[bytes] = ...) -> None: ...

class BlindingInfo(_message.Message):
    __slots__ = ["disclosure", "divulgence"]
    class DisclosureEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Parties
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Parties, _Mapping]] = ...) -> None: ...
    class DivulgenceEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Parties
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Parties, _Mapping]] = ...) -> None: ...
    DISCLOSURE_FIELD_NUMBER: _ClassVar[int]
    DIVULGENCE_FIELD_NUMBER: _ClassVar[int]
    disclosure: _containers.MessageMap[int, Parties]
    divulgence: _containers.MessageMap[str, Parties]
    def __init__(self, disclosure: _Optional[_Mapping[int, Parties]] = ..., divulgence: _Optional[_Mapping[str, Parties]] = ...) -> None: ...

class Parties(_message.Message):
    __slots__ = ["parties"]
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parties: _Optional[_Iterable[str]] = ...) -> None: ...

class CommandRejected(_message.Message):
    __slots__ = ["completion_info", "record_time", "rejection_reason", "command_kind", "domain_id"]
    class GrpcRejectionReasonTemplate(_message.Message):
        __slots__ = ["status"]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: bytes
        def __init__(self, status: _Optional[bytes] = ...) -> None: ...
    COMPLETION_INFO_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    COMMAND_KIND_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    completion_info: CompletionInfo
    record_time: _timestamp_pb2.Timestamp
    rejection_reason: CommandRejected.GrpcRejectionReasonTemplate
    command_kind: CommandKind
    domain_id: _wrappers_pb2.StringValue
    def __init__(self, completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejection_reason: _Optional[_Union[CommandRejected.GrpcRejectionReasonTemplate, _Mapping]] = ..., command_kind: _Optional[_Union[CommandKind, str]] = ..., domain_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class TransferredOut(_message.Message):
    __slots__ = ["update_id", "completion_info", "submitter", "record_time", "contract_id", "contract_stakeholders", "source_domain", "target_domain", "transfer_in_exclusivity", "workflow_id", "template_id", "is_transferring_participant", "hosted_stakeholders", "transfer_counter"]
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_INFO_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_IN_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSFERRING_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    HOSTED_STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_COUNTER_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    completion_info: CompletionInfo
    submitter: str
    record_time: _timestamp_pb2.Timestamp
    contract_id: str
    contract_stakeholders: _containers.RepeatedScalarFieldContainer[str]
    source_domain: str
    target_domain: str
    transfer_in_exclusivity: _timestamp_pb2.Timestamp
    workflow_id: str
    template_id: str
    is_transferring_participant: bool
    hosted_stakeholders: _containers.RepeatedScalarFieldContainer[str]
    transfer_counter: int
    def __init__(self, update_id: _Optional[str] = ..., completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., submitter: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., contract_id: _Optional[str] = ..., contract_stakeholders: _Optional[_Iterable[str]] = ..., source_domain: _Optional[str] = ..., target_domain: _Optional[str] = ..., transfer_in_exclusivity: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., workflow_id: _Optional[str] = ..., template_id: _Optional[str] = ..., is_transferring_participant: bool = ..., hosted_stakeholders: _Optional[_Iterable[str]] = ..., transfer_counter: _Optional[int] = ...) -> None: ...

class TransferredIn(_message.Message):
    __slots__ = ["update_id", "completion_info", "submitter", "record_time", "ledger_create_time", "create_node", "creating_transaction_id", "contract_metadata", "transfer_out_id", "target_domain", "create_transaction_accepted", "workflow_id", "is_transferring_participant", "hosted_stakeholders", "transfer_counter"]
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_INFO_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    LEDGER_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_NODE_FIELD_NUMBER: _ClassVar[int]
    CREATING_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_METADATA_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OUT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CREATE_TRANSACTION_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSFERRING_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    HOSTED_STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_COUNTER_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    completion_info: CompletionInfo
    submitter: str
    record_time: _timestamp_pb2.Timestamp
    ledger_create_time: _timestamp_pb2.Timestamp
    create_node: bytes
    creating_transaction_id: str
    contract_metadata: bytes
    transfer_out_id: _participant_transfer_pb2.TransferId
    target_domain: str
    create_transaction_accepted: bool
    workflow_id: str
    is_transferring_participant: bool
    hosted_stakeholders: _containers.RepeatedScalarFieldContainer[str]
    transfer_counter: int
    def __init__(self, update_id: _Optional[str] = ..., completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., submitter: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ledger_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., create_node: _Optional[bytes] = ..., creating_transaction_id: _Optional[str] = ..., contract_metadata: _Optional[bytes] = ..., transfer_out_id: _Optional[_Union[_participant_transfer_pb2.TransferId, _Mapping]] = ..., target_domain: _Optional[str] = ..., create_transaction_accepted: bool = ..., workflow_id: _Optional[str] = ..., is_transferring_participant: bool = ..., hosted_stakeholders: _Optional[_Iterable[str]] = ..., transfer_counter: _Optional[int] = ...) -> None: ...
