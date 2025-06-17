# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from .. import commands_pb2 as _commands_pb2
from . import interactive_submission_common_data_pb2 as _interactive_submission_common_data_pb2
from .transaction.v1 import interactive_submission_data_pb2 as _interactive_submission_data_pb2
from .. import package_reference_pb2 as _package_reference_pb2
from .. import value_pb2 as _value_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HashingSchemeVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HASHING_SCHEME_VERSION_UNSPECIFIED: _ClassVar[HashingSchemeVersion]
    HASHING_SCHEME_VERSION_V2: _ClassVar[HashingSchemeVersion]

class SigningAlgorithmSpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNING_ALGORITHM_SPEC_UNSPECIFIED: _ClassVar[SigningAlgorithmSpec]
    SIGNING_ALGORITHM_SPEC_ED25519: _ClassVar[SigningAlgorithmSpec]
    SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256: _ClassVar[SigningAlgorithmSpec]
    SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384: _ClassVar[SigningAlgorithmSpec]

class SignatureFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_FORMAT_UNSPECIFIED: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_RAW: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_DER: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_CONCAT: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_SYMBOLIC: _ClassVar[SignatureFormat]
HASHING_SCHEME_VERSION_UNSPECIFIED: HashingSchemeVersion
HASHING_SCHEME_VERSION_V2: HashingSchemeVersion
SIGNING_ALGORITHM_SPEC_UNSPECIFIED: SigningAlgorithmSpec
SIGNING_ALGORITHM_SPEC_ED25519: SigningAlgorithmSpec
SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256: SigningAlgorithmSpec
SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384: SigningAlgorithmSpec
SIGNATURE_FORMAT_UNSPECIFIED: SignatureFormat
SIGNATURE_FORMAT_RAW: SignatureFormat
SIGNATURE_FORMAT_DER: SignatureFormat
SIGNATURE_FORMAT_CONCAT: SignatureFormat
SIGNATURE_FORMAT_SYMBOLIC: SignatureFormat

class PrepareSubmissionRequest(_message.Message):
    __slots__ = ("user_id", "command_id", "commands", "min_ledger_time", "act_as", "read_as", "disclosed_contracts", "synchronizer_id", "package_id_selection_preference", "verbose_hashing", "prefetch_contract_keys")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_TIME_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    READ_AS_FIELD_NUMBER: _ClassVar[int]
    DISCLOSED_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_SELECTION_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_HASHING_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_CONTRACT_KEYS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    command_id: str
    commands: _containers.RepeatedCompositeFieldContainer[_commands_pb2.Command]
    min_ledger_time: MinLedgerTime
    act_as: _containers.RepeatedScalarFieldContainer[str]
    read_as: _containers.RepeatedScalarFieldContainer[str]
    disclosed_contracts: _containers.RepeatedCompositeFieldContainer[_commands_pb2.DisclosedContract]
    synchronizer_id: str
    package_id_selection_preference: _containers.RepeatedScalarFieldContainer[str]
    verbose_hashing: bool
    prefetch_contract_keys: _containers.RepeatedCompositeFieldContainer[_commands_pb2.PrefetchContractKey]
    def __init__(self, user_id: _Optional[str] = ..., command_id: _Optional[str] = ..., commands: _Optional[_Iterable[_Union[_commands_pb2.Command, _Mapping]]] = ..., min_ledger_time: _Optional[_Union[MinLedgerTime, _Mapping]] = ..., act_as: _Optional[_Iterable[str]] = ..., read_as: _Optional[_Iterable[str]] = ..., disclosed_contracts: _Optional[_Iterable[_Union[_commands_pb2.DisclosedContract, _Mapping]]] = ..., synchronizer_id: _Optional[str] = ..., package_id_selection_preference: _Optional[_Iterable[str]] = ..., verbose_hashing: bool = ..., prefetch_contract_keys: _Optional[_Iterable[_Union[_commands_pb2.PrefetchContractKey, _Mapping]]] = ...) -> None: ...

class PrepareSubmissionResponse(_message.Message):
    __slots__ = ("prepared_transaction", "prepared_transaction_hash", "hashing_scheme_version", "hashing_details")
    PREPARED_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    PREPARED_TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    HASHING_SCHEME_VERSION_FIELD_NUMBER: _ClassVar[int]
    HASHING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    prepared_transaction: PreparedTransaction
    prepared_transaction_hash: bytes
    hashing_scheme_version: HashingSchemeVersion
    hashing_details: str
    def __init__(self, prepared_transaction: _Optional[_Union[PreparedTransaction, _Mapping]] = ..., prepared_transaction_hash: _Optional[bytes] = ..., hashing_scheme_version: _Optional[_Union[HashingSchemeVersion, str]] = ..., hashing_details: _Optional[str] = ...) -> None: ...

class Signature(_message.Message):
    __slots__ = ("format", "signature", "signed_by", "signing_algorithm_spec")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    SIGNING_ALGORITHM_SPEC_FIELD_NUMBER: _ClassVar[int]
    format: SignatureFormat
    signature: bytes
    signed_by: str
    signing_algorithm_spec: SigningAlgorithmSpec
    def __init__(self, format: _Optional[_Union[SignatureFormat, str]] = ..., signature: _Optional[bytes] = ..., signed_by: _Optional[str] = ..., signing_algorithm_spec: _Optional[_Union[SigningAlgorithmSpec, str]] = ...) -> None: ...

class SinglePartySignatures(_message.Message):
    __slots__ = ("party", "signatures")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    party: str
    signatures: _containers.RepeatedCompositeFieldContainer[Signature]
    def __init__(self, party: _Optional[str] = ..., signatures: _Optional[_Iterable[_Union[Signature, _Mapping]]] = ...) -> None: ...

class PartySignatures(_message.Message):
    __slots__ = ("signatures",)
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    signatures: _containers.RepeatedCompositeFieldContainer[SinglePartySignatures]
    def __init__(self, signatures: _Optional[_Iterable[_Union[SinglePartySignatures, _Mapping]]] = ...) -> None: ...

class ExecuteSubmissionRequest(_message.Message):
    __slots__ = ("prepared_transaction", "party_signatures", "deduplication_duration", "deduplication_offset", "submission_id", "user_id", "hashing_scheme_version", "min_ledger_time")
    PREPARED_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    PARTY_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    HASHING_SCHEME_VERSION_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_TIME_FIELD_NUMBER: _ClassVar[int]
    prepared_transaction: PreparedTransaction
    party_signatures: PartySignatures
    deduplication_duration: _duration_pb2.Duration
    deduplication_offset: int
    submission_id: str
    user_id: str
    hashing_scheme_version: HashingSchemeVersion
    min_ledger_time: MinLedgerTime
    def __init__(self, prepared_transaction: _Optional[_Union[PreparedTransaction, _Mapping]] = ..., party_signatures: _Optional[_Union[PartySignatures, _Mapping]] = ..., deduplication_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., deduplication_offset: _Optional[int] = ..., submission_id: _Optional[str] = ..., user_id: _Optional[str] = ..., hashing_scheme_version: _Optional[_Union[HashingSchemeVersion, str]] = ..., min_ledger_time: _Optional[_Union[MinLedgerTime, _Mapping]] = ...) -> None: ...

class ExecuteSubmissionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MinLedgerTime(_message.Message):
    __slots__ = ("min_ledger_time_abs", "min_ledger_time_rel")
    MIN_LEDGER_TIME_ABS_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_TIME_REL_FIELD_NUMBER: _ClassVar[int]
    min_ledger_time_abs: _timestamp_pb2.Timestamp
    min_ledger_time_rel: _duration_pb2.Duration
    def __init__(self, min_ledger_time_abs: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., min_ledger_time_rel: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class PreparedTransaction(_message.Message):
    __slots__ = ("transaction", "metadata")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    transaction: DamlTransaction
    metadata: Metadata
    def __init__(self, transaction: _Optional[_Union[DamlTransaction, _Mapping]] = ..., metadata: _Optional[_Union[Metadata, _Mapping]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("submitter_info", "synchronizer_id", "mediator_group", "transaction_uuid", "preparation_time", "input_contracts", "min_ledger_effective_time", "max_ledger_effective_time", "global_key_mapping")
    class SubmitterInfo(_message.Message):
        __slots__ = ("act_as", "command_id")
        ACT_AS_FIELD_NUMBER: _ClassVar[int]
        COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
        act_as: _containers.RepeatedScalarFieldContainer[str]
        command_id: str
        def __init__(self, act_as: _Optional[_Iterable[str]] = ..., command_id: _Optional[str] = ...) -> None: ...
    class GlobalKeyMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: _interactive_submission_common_data_pb2.GlobalKey
        value: _value_pb2.Value
        def __init__(self, key: _Optional[_Union[_interactive_submission_common_data_pb2.GlobalKey, _Mapping]] = ..., value: _Optional[_Union[_value_pb2.Value, _Mapping]] = ...) -> None: ...
    class InputContract(_message.Message):
        __slots__ = ("v1", "created_at", "event_blob")
        V1_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        EVENT_BLOB_FIELD_NUMBER: _ClassVar[int]
        v1: _interactive_submission_data_pb2.Create
        created_at: int
        event_blob: bytes
        def __init__(self, v1: _Optional[_Union[_interactive_submission_data_pb2.Create, _Mapping]] = ..., created_at: _Optional[int] = ..., event_blob: _Optional[bytes] = ...) -> None: ...
    SUBMITTER_INFO_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_UUID_FIELD_NUMBER: _ClassVar[int]
    PREPARATION_TIME_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_LEDGER_EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    submitter_info: Metadata.SubmitterInfo
    synchronizer_id: str
    mediator_group: int
    transaction_uuid: str
    preparation_time: int
    input_contracts: _containers.RepeatedCompositeFieldContainer[Metadata.InputContract]
    min_ledger_effective_time: int
    max_ledger_effective_time: int
    global_key_mapping: _containers.RepeatedCompositeFieldContainer[Metadata.GlobalKeyMappingEntry]
    def __init__(self, submitter_info: _Optional[_Union[Metadata.SubmitterInfo, _Mapping]] = ..., synchronizer_id: _Optional[str] = ..., mediator_group: _Optional[int] = ..., transaction_uuid: _Optional[str] = ..., preparation_time: _Optional[int] = ..., input_contracts: _Optional[_Iterable[_Union[Metadata.InputContract, _Mapping]]] = ..., min_ledger_effective_time: _Optional[int] = ..., max_ledger_effective_time: _Optional[int] = ..., global_key_mapping: _Optional[_Iterable[_Union[Metadata.GlobalKeyMappingEntry, _Mapping]]] = ...) -> None: ...

class DamlTransaction(_message.Message):
    __slots__ = ("version", "roots", "nodes", "node_seeds")
    class NodeSeed(_message.Message):
        __slots__ = ("node_id", "seed")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        SEED_FIELD_NUMBER: _ClassVar[int]
        node_id: int
        seed: bytes
        def __init__(self, node_id: _Optional[int] = ..., seed: _Optional[bytes] = ...) -> None: ...
    class Node(_message.Message):
        __slots__ = ("node_id", "v1")
        NODE_ID_FIELD_NUMBER: _ClassVar[int]
        V1_FIELD_NUMBER: _ClassVar[int]
        node_id: str
        v1: _interactive_submission_data_pb2.Node
        def __init__(self, node_id: _Optional[str] = ..., v1: _Optional[_Union[_interactive_submission_data_pb2.Node, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ROOTS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    NODE_SEEDS_FIELD_NUMBER: _ClassVar[int]
    version: str
    roots: _containers.RepeatedScalarFieldContainer[str]
    nodes: _containers.RepeatedCompositeFieldContainer[DamlTransaction.Node]
    node_seeds: _containers.RepeatedCompositeFieldContainer[DamlTransaction.NodeSeed]
    def __init__(self, version: _Optional[str] = ..., roots: _Optional[_Iterable[str]] = ..., nodes: _Optional[_Iterable[_Union[DamlTransaction.Node, _Mapping]]] = ..., node_seeds: _Optional[_Iterable[_Union[DamlTransaction.NodeSeed, _Mapping]]] = ...) -> None: ...

class GetPreferredPackageVersionRequest(_message.Message):
    __slots__ = ("parties", "package_name", "synchronizer_id", "vetting_valid_at")
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    VETTING_VALID_AT_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    package_name: str
    synchronizer_id: str
    vetting_valid_at: _timestamp_pb2.Timestamp
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., package_name: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., vetting_valid_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetPreferredPackageVersionResponse(_message.Message):
    __slots__ = ("package_preference",)
    PACKAGE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    package_preference: PackagePreference
    def __init__(self, package_preference: _Optional[_Union[PackagePreference, _Mapping]] = ...) -> None: ...

class PackagePreference(_message.Message):
    __slots__ = ("package_reference", "synchronizer_id")
    PACKAGE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    package_reference: _package_reference_pb2.PackageReference
    synchronizer_id: str
    def __init__(self, package_reference: _Optional[_Union[_package_reference_pb2.PackageReference, _Mapping]] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...
