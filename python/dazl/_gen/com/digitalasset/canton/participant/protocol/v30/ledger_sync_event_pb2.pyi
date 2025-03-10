# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import participant_transaction_pb2 as _participant_transaction_pb2
from ....protocol.v30 import participant_transfer_pb2 as _participant_transfer_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_KIND_TRANSACTION_UNSPECIFIED: _ClassVar[CommandKind]
    COMMAND_KIND_TRANSFER_OUT: _ClassVar[CommandKind]
    COMMAND_KIND_TRANSFER_IN: _ClassVar[CommandKind]
COMMAND_KIND_TRANSACTION_UNSPECIFIED: CommandKind
COMMAND_KIND_TRANSFER_OUT: CommandKind
COMMAND_KIND_TRANSFER_IN: CommandKind

class LedgerSyncEvent(_message.Message):
    __slots__ = ("party_added_to_participant", "transaction_accepted", "command_rejected", "party_allocation_rejected", "transferred_out", "transferred_in", "contracts_added", "contracts_purged", "parties_added", "parties_removed", "init")
    PARTY_ADDED_TO_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    COMMAND_REJECTED_FIELD_NUMBER: _ClassVar[int]
    PARTY_ALLOCATION_REJECTED_FIELD_NUMBER: _ClassVar[int]
    TRANSFERRED_OUT_FIELD_NUMBER: _ClassVar[int]
    TRANSFERRED_IN_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_ADDED_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_PURGED_FIELD_NUMBER: _ClassVar[int]
    PARTIES_ADDED_FIELD_NUMBER: _ClassVar[int]
    PARTIES_REMOVED_FIELD_NUMBER: _ClassVar[int]
    INIT_FIELD_NUMBER: _ClassVar[int]
    party_added_to_participant: PartyAddedToParticipant
    transaction_accepted: TransactionAccepted
    command_rejected: CommandRejected
    party_allocation_rejected: PartyAllocationRejected
    transferred_out: TransferredOut
    transferred_in: TransferredIn
    contracts_added: ContractsAdded
    contracts_purged: ContractsPurged
    parties_added: PartiesAddedToParticipant
    parties_removed: PartiesRemovedFromParticipant
    init: Init
    def __init__(self, party_added_to_participant: _Optional[_Union[PartyAddedToParticipant, _Mapping]] = ..., transaction_accepted: _Optional[_Union[TransactionAccepted, _Mapping]] = ..., command_rejected: _Optional[_Union[CommandRejected, _Mapping]] = ..., party_allocation_rejected: _Optional[_Union[PartyAllocationRejected, _Mapping]] = ..., transferred_out: _Optional[_Union[TransferredOut, _Mapping]] = ..., transferred_in: _Optional[_Union[TransferredIn, _Mapping]] = ..., contracts_added: _Optional[_Union[ContractsAdded, _Mapping]] = ..., contracts_purged: _Optional[_Union[ContractsPurged, _Mapping]] = ..., parties_added: _Optional[_Union[PartiesAddedToParticipant, _Mapping]] = ..., parties_removed: _Optional[_Union[PartiesRemovedFromParticipant, _Mapping]] = ..., init: _Optional[_Union[Init, _Mapping]] = ...) -> None: ...

class PartyAddedToParticipant(_message.Message):
    __slots__ = ("party", "display_name", "participant_id", "record_time", "submission_id")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    party: str
    display_name: str
    participant_id: str
    record_time: int
    submission_id: str
    def __init__(self, party: _Optional[str] = ..., display_name: _Optional[str] = ..., participant_id: _Optional[str] = ..., record_time: _Optional[int] = ..., submission_id: _Optional[str] = ...) -> None: ...

class PartyAllocationRejected(_message.Message):
    __slots__ = ("submission_id", "participant_id", "record_time", "rejection_reason")
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    participant_id: str
    record_time: int
    rejection_reason: str
    def __init__(self, submission_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., record_time: _Optional[int] = ..., rejection_reason: _Optional[str] = ...) -> None: ...

class TransactionAccepted(_message.Message):
    __slots__ = ("completion_info", "transaction_meta", "transaction", "transaction_id", "record_time", "divulged_contracts", "blinding_info", "contract_metadata", "hosted_witnesses", "domain_id")
    class ContractMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
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
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    completion_info: CompletionInfo
    transaction_meta: TransactionMeta
    transaction: bytes
    transaction_id: str
    record_time: int
    divulged_contracts: _containers.RepeatedCompositeFieldContainer[DivulgedContract]
    blinding_info: BlindingInfo
    contract_metadata: _containers.ScalarMap[str, bytes]
    hosted_witnesses: _containers.RepeatedScalarFieldContainer[str]
    domain_id: str
    def __init__(self, completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., transaction_meta: _Optional[_Union[TransactionMeta, _Mapping]] = ..., transaction: _Optional[bytes] = ..., transaction_id: _Optional[str] = ..., record_time: _Optional[int] = ..., divulged_contracts: _Optional[_Iterable[_Union[DivulgedContract, _Mapping]]] = ..., blinding_info: _Optional[_Union[BlindingInfo, _Mapping]] = ..., contract_metadata: _Optional[_Mapping[str, bytes]] = ..., hosted_witnesses: _Optional[_Iterable[str]] = ..., domain_id: _Optional[str] = ...) -> None: ...

class CompletionInfo(_message.Message):
    __slots__ = ("act_as", "application_id", "command_id", "opt_deduplication_period", "submission_id")
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    OPT_DEDUPLICATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    act_as: _containers.RepeatedScalarFieldContainer[str]
    application_id: str
    command_id: str
    opt_deduplication_period: _participant_transaction_pb2.DeduplicationPeriod
    submission_id: str
    def __init__(self, act_as: _Optional[_Iterable[str]] = ..., application_id: _Optional[str] = ..., command_id: _Optional[str] = ..., opt_deduplication_period: _Optional[_Union[_participant_transaction_pb2.DeduplicationPeriod, _Mapping]] = ..., submission_id: _Optional[str] = ...) -> None: ...

class TransactionMeta(_message.Message):
    __slots__ = ("ledger_time", "workflow_id", "submission_time", "submission_seed", "used_packages", "node_seeds", "by_key_nodes")
    class ByKeyNodes(_message.Message):
        __slots__ = ("by_key_node",)
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
    ledger_time: int
    workflow_id: _wrappers_pb2.StringValue
    submission_time: int
    submission_seed: bytes
    used_packages: _containers.RepeatedScalarFieldContainer[str]
    node_seeds: _containers.RepeatedCompositeFieldContainer[NodeSeed]
    by_key_nodes: TransactionMeta.ByKeyNodes
    def __init__(self, ledger_time: _Optional[int] = ..., workflow_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., submission_time: _Optional[int] = ..., submission_seed: _Optional[bytes] = ..., used_packages: _Optional[_Iterable[str]] = ..., node_seeds: _Optional[_Iterable[_Union[NodeSeed, _Mapping]]] = ..., by_key_nodes: _Optional[_Union[TransactionMeta.ByKeyNodes, _Mapping]] = ...) -> None: ...

class NodeSeed(_message.Message):
    __slots__ = ("node_index", "node_seed")
    NODE_INDEX_FIELD_NUMBER: _ClassVar[int]
    NODE_SEED_FIELD_NUMBER: _ClassVar[int]
    node_index: int
    node_seed: bytes
    def __init__(self, node_index: _Optional[int] = ..., node_seed: _Optional[bytes] = ...) -> None: ...

class DivulgedContract(_message.Message):
    __slots__ = ("contract_id", "contract_inst")
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_INST_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    contract_inst: bytes
    def __init__(self, contract_id: _Optional[str] = ..., contract_inst: _Optional[bytes] = ...) -> None: ...

class BlindingInfo(_message.Message):
    __slots__ = ("disclosure", "divulgence")
    class DisclosureEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Parties
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Parties, _Mapping]] = ...) -> None: ...
    class DivulgenceEntry(_message.Message):
        __slots__ = ("key", "value")
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
    __slots__ = ("parties",)
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parties: _Optional[_Iterable[str]] = ...) -> None: ...

class CommandRejected(_message.Message):
    __slots__ = ("completion_info", "record_time", "rejection_reason", "command_kind", "domain_id")
    class GrpcRejectionReasonTemplate(_message.Message):
        __slots__ = ("status",)
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: bytes
        def __init__(self, status: _Optional[bytes] = ...) -> None: ...
    COMPLETION_INFO_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    COMMAND_KIND_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    completion_info: CompletionInfo
    record_time: int
    rejection_reason: CommandRejected.GrpcRejectionReasonTemplate
    command_kind: CommandKind
    domain_id: str
    def __init__(self, completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., record_time: _Optional[int] = ..., rejection_reason: _Optional[_Union[CommandRejected.GrpcRejectionReasonTemplate, _Mapping]] = ..., command_kind: _Optional[_Union[CommandKind, str]] = ..., domain_id: _Optional[str] = ...) -> None: ...

class TransferredOut(_message.Message):
    __slots__ = ("update_id", "completion_info", "submitter", "record_time", "contract_id", "contract_stakeholders", "source_domain", "target_domain", "transfer_in_exclusivity", "workflow_id", "template_id", "is_transferring_participant", "hosted_stakeholders", "transfer_counter", "package_name")
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
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    completion_info: CompletionInfo
    submitter: str
    record_time: int
    contract_id: str
    contract_stakeholders: _containers.RepeatedScalarFieldContainer[str]
    source_domain: str
    target_domain: str
    transfer_in_exclusivity: _wrappers_pb2.Int64Value
    workflow_id: str
    template_id: str
    is_transferring_participant: bool
    hosted_stakeholders: _containers.RepeatedScalarFieldContainer[str]
    transfer_counter: int
    package_name: str
    def __init__(self, update_id: _Optional[str] = ..., completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., submitter: _Optional[str] = ..., record_time: _Optional[int] = ..., contract_id: _Optional[str] = ..., contract_stakeholders: _Optional[_Iterable[str]] = ..., source_domain: _Optional[str] = ..., target_domain: _Optional[str] = ..., transfer_in_exclusivity: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., workflow_id: _Optional[str] = ..., template_id: _Optional[str] = ..., is_transferring_participant: bool = ..., hosted_stakeholders: _Optional[_Iterable[str]] = ..., transfer_counter: _Optional[int] = ..., package_name: _Optional[str] = ...) -> None: ...

class TransferredIn(_message.Message):
    __slots__ = ("update_id", "completion_info", "submitter", "record_time", "ledger_create_time", "create_node", "creating_transaction_id", "contract_metadata", "transfer_out_id", "target_domain", "workflow_id", "is_transferring_participant", "hosted_stakeholders", "transfer_counter")
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
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TRANSFERRING_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    HOSTED_STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_COUNTER_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    completion_info: CompletionInfo
    submitter: str
    record_time: int
    ledger_create_time: int
    create_node: bytes
    creating_transaction_id: str
    contract_metadata: bytes
    transfer_out_id: _participant_transfer_pb2.TransferId
    target_domain: str
    workflow_id: str
    is_transferring_participant: bool
    hosted_stakeholders: _containers.RepeatedScalarFieldContainer[str]
    transfer_counter: int
    def __init__(self, update_id: _Optional[str] = ..., completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., submitter: _Optional[str] = ..., record_time: _Optional[int] = ..., ledger_create_time: _Optional[int] = ..., create_node: _Optional[bytes] = ..., creating_transaction_id: _Optional[str] = ..., contract_metadata: _Optional[bytes] = ..., transfer_out_id: _Optional[_Union[_participant_transfer_pb2.TransferId, _Mapping]] = ..., target_domain: _Optional[str] = ..., workflow_id: _Optional[str] = ..., is_transferring_participant: bool = ..., hosted_stakeholders: _Optional[_Iterable[str]] = ..., transfer_counter: _Optional[int] = ...) -> None: ...

class ContractsAdded(_message.Message):
    __slots__ = ("transaction_id", "contracts", "domain_id", "ledger_time", "record_time", "hosted_witnesses", "contract_metadata", "workflow_id")
    class ContractMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    LEDGER_TIME_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    HOSTED_WITNESSES_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_METADATA_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    contracts: _containers.RepeatedScalarFieldContainer[bytes]
    domain_id: str
    ledger_time: int
    record_time: int
    hosted_witnesses: _containers.RepeatedScalarFieldContainer[str]
    contract_metadata: _containers.ScalarMap[str, bytes]
    workflow_id: str
    def __init__(self, transaction_id: _Optional[str] = ..., contracts: _Optional[_Iterable[bytes]] = ..., domain_id: _Optional[str] = ..., ledger_time: _Optional[int] = ..., record_time: _Optional[int] = ..., hosted_witnesses: _Optional[_Iterable[str]] = ..., contract_metadata: _Optional[_Mapping[str, bytes]] = ..., workflow_id: _Optional[str] = ...) -> None: ...

class ContractsPurged(_message.Message):
    __slots__ = ("transaction_id", "contracts", "domain_id", "record_time", "hosted_witnesses")
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    HOSTED_WITNESSES_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    contracts: _containers.RepeatedScalarFieldContainer[bytes]
    domain_id: str
    record_time: int
    hosted_witnesses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, transaction_id: _Optional[str] = ..., contracts: _Optional[_Iterable[bytes]] = ..., domain_id: _Optional[str] = ..., record_time: _Optional[int] = ..., hosted_witnesses: _Optional[_Iterable[str]] = ...) -> None: ...

class PartiesAddedToParticipant(_message.Message):
    __slots__ = ("parties", "participant_id", "record_time", "effective_time")
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    participant_id: str
    record_time: int
    effective_time: int
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., participant_id: _Optional[str] = ..., record_time: _Optional[int] = ..., effective_time: _Optional[int] = ...) -> None: ...

class PartiesRemovedFromParticipant(_message.Message):
    __slots__ = ("parties", "participant_id", "record_time", "effective_time")
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    participant_id: str
    record_time: int
    effective_time: int
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., participant_id: _Optional[str] = ..., record_time: _Optional[int] = ..., effective_time: _Optional[int] = ...) -> None: ...

class Init(_message.Message):
    __slots__ = ("record_time",)
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    record_time: int
    def __init__(self, record_time: _Optional[int] = ...) -> None: ...
