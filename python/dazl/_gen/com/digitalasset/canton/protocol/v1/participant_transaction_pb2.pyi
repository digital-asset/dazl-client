# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from ..v0 import common_pb2 as _common_pb2
from ..v0 import participant_transaction_pb2 as _participant_transaction_pb2
from ..v0 import topology_pb2 as _topology_pb2
from . import common_pb2 as _common_pb2_1
from . import merkle_pb2 as _merkle_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionDescription(_message.Message):
    __slots__ = ["create", "exercise", "fetch", "lookup_by_key"]
    class ExerciseActionDescription(_message.Message):
        __slots__ = ["input_contract_id", "choice", "chosen_value", "actors", "by_key", "node_seed", "version", "failed", "interface_id"]
        INPUT_CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        CHOICE_FIELD_NUMBER: _ClassVar[int]
        CHOSEN_VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTORS_FIELD_NUMBER: _ClassVar[int]
        BY_KEY_FIELD_NUMBER: _ClassVar[int]
        NODE_SEED_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
        input_contract_id: str
        choice: str
        chosen_value: bytes
        actors: _containers.RepeatedScalarFieldContainer[str]
        by_key: bool
        node_seed: bytes
        version: str
        failed: bool
        interface_id: str
        def __init__(self, input_contract_id: _Optional[str] = ..., choice: _Optional[str] = ..., chosen_value: _Optional[bytes] = ..., actors: _Optional[_Iterable[str]] = ..., by_key: bool = ..., node_seed: _Optional[bytes] = ..., version: _Optional[str] = ..., failed: bool = ..., interface_id: _Optional[str] = ...) -> None: ...
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    create: _participant_transaction_pb2.ActionDescription.CreateActionDescription
    exercise: ActionDescription.ExerciseActionDescription
    fetch: _participant_transaction_pb2.ActionDescription.FetchActionDescription
    lookup_by_key: _participant_transaction_pb2.ActionDescription.LookupByKeyActionDescription
    def __init__(self, create: _Optional[_Union[_participant_transaction_pb2.ActionDescription.CreateActionDescription, _Mapping]] = ..., exercise: _Optional[_Union[ActionDescription.ExerciseActionDescription, _Mapping]] = ..., fetch: _Optional[_Union[_participant_transaction_pb2.ActionDescription.FetchActionDescription, _Mapping]] = ..., lookup_by_key: _Optional[_Union[_participant_transaction_pb2.ActionDescription.LookupByKeyActionDescription, _Mapping]] = ...) -> None: ...

class ViewNode(_message.Message):
    __slots__ = ["view_common_data", "view_participant_data", "subviews"]
    VIEW_COMMON_DATA_FIELD_NUMBER: _ClassVar[int]
    VIEW_PARTICIPANT_DATA_FIELD_NUMBER: _ClassVar[int]
    SUBVIEWS_FIELD_NUMBER: _ClassVar[int]
    view_common_data: _merkle_pb2.BlindableNode
    view_participant_data: _merkle_pb2.BlindableNode
    subviews: _merkle_pb2.MerkleSeq
    def __init__(self, view_common_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ..., view_participant_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ..., subviews: _Optional[_Union[_merkle_pb2.MerkleSeq, _Mapping]] = ...) -> None: ...

class ViewCommonData(_message.Message):
    __slots__ = ["salt", "informees", "threshold"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    INFORMEES_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    informees: _containers.RepeatedCompositeFieldContainer[Informee]
    threshold: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., informees: _Optional[_Iterable[_Union[Informee, _Mapping]]] = ..., threshold: _Optional[int] = ...) -> None: ...

class Informee(_message.Message):
    __slots__ = ["party", "weight", "required_trust_level"]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_TRUST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    party: str
    weight: int
    required_trust_level: _topology_pb2.TrustLevel
    def __init__(self, party: _Optional[str] = ..., weight: _Optional[int] = ..., required_trust_level: _Optional[_Union[_topology_pb2.TrustLevel, str]] = ...) -> None: ...

class EncryptedViewMessage(_message.Message):
    __slots__ = ["view_tree", "encryption_scheme", "submitter_participant_signature", "view_hash", "randomness", "domain_id", "view_type"]
    VIEW_TREE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SCHEME_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    VIEW_HASH_FIELD_NUMBER: _ClassVar[int]
    RANDOMNESS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    view_tree: bytes
    encryption_scheme: _crypto_pb2.SymmetricKeyScheme
    submitter_participant_signature: _crypto_pb2.Signature
    view_hash: bytes
    randomness: _containers.RepeatedCompositeFieldContainer[ParticipantRandomnessLookup]
    domain_id: str
    view_type: _common_pb2.ViewType
    def __init__(self, view_tree: _Optional[bytes] = ..., encryption_scheme: _Optional[_Union[_crypto_pb2.SymmetricKeyScheme, str]] = ..., submitter_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., view_hash: _Optional[bytes] = ..., randomness: _Optional[_Iterable[_Union[ParticipantRandomnessLookup, _Mapping]]] = ..., domain_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ...) -> None: ...

class ParticipantRandomnessLookup(_message.Message):
    __slots__ = ["randomness", "fingerprint"]
    RANDOMNESS_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    randomness: bytes
    fingerprint: str
    def __init__(self, randomness: _Optional[bytes] = ..., fingerprint: _Optional[str] = ...) -> None: ...

class ViewParticipantMessage(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class InformeeMessage(_message.Message):
    __slots__ = ["full_informee_tree", "protocol_version"]
    FULL_INFORMEE_TREE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    full_informee_tree: FullInformeeTree
    protocol_version: int
    def __init__(self, full_informee_tree: _Optional[_Union[FullInformeeTree, _Mapping]] = ..., protocol_version: _Optional[int] = ...) -> None: ...

class LightTransactionViewTree(_message.Message):
    __slots__ = ["tree", "subview_hashes"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    SUBVIEW_HASHES_FIELD_NUMBER: _ClassVar[int]
    tree: _merkle_pb2.GenTransactionTree
    subview_hashes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, tree: _Optional[_Union[_merkle_pb2.GenTransactionTree, _Mapping]] = ..., subview_hashes: _Optional[_Iterable[bytes]] = ...) -> None: ...

class FullInformeeTree(_message.Message):
    __slots__ = ["tree"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _merkle_pb2.GenTransactionTree
    def __init__(self, tree: _Optional[_Union[_merkle_pb2.GenTransactionTree, _Mapping]] = ...) -> None: ...

class CreatedContract(_message.Message):
    __slots__ = ["contract", "consumed_in_core", "rolled_back"]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_IN_CORE_FIELD_NUMBER: _ClassVar[int]
    ROLLED_BACK_FIELD_NUMBER: _ClassVar[int]
    contract: _common_pb2_1.SerializableContract
    consumed_in_core: bool
    rolled_back: bool
    def __init__(self, contract: _Optional[_Union[_common_pb2_1.SerializableContract, _Mapping]] = ..., consumed_in_core: bool = ..., rolled_back: bool = ...) -> None: ...

class InputContract(_message.Message):
    __slots__ = ["contract", "consumed"]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_FIELD_NUMBER: _ClassVar[int]
    contract: _common_pb2_1.SerializableContract
    consumed: bool
    def __init__(self, contract: _Optional[_Union[_common_pb2_1.SerializableContract, _Mapping]] = ..., consumed: bool = ...) -> None: ...

class CommonMetadata(_message.Message):
    __slots__ = ["salt", "confirmation_policy", "domain_id", "uuid", "mediator"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    confirmation_policy: bytes
    domain_id: str
    uuid: str
    mediator: str
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., confirmation_policy: _Optional[bytes] = ..., domain_id: _Optional[str] = ..., uuid: _Optional[str] = ..., mediator: _Optional[str] = ...) -> None: ...

class SubmitterMetadata(_message.Message):
    __slots__ = ["salt", "act_as", "application_id", "command_id", "submitter_participant", "submission_id", "dedup_period", "max_sequencing_time"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUP_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MAX_SEQUENCING_TIME_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    act_as: _containers.RepeatedScalarFieldContainer[str]
    application_id: str
    command_id: str
    submitter_participant: str
    submission_id: str
    dedup_period: _participant_transaction_pb2.DeduplicationPeriod
    max_sequencing_time: _timestamp_pb2.Timestamp
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., act_as: _Optional[_Iterable[str]] = ..., application_id: _Optional[str] = ..., command_id: _Optional[str] = ..., submitter_participant: _Optional[str] = ..., submission_id: _Optional[str] = ..., dedup_period: _Optional[_Union[_participant_transaction_pb2.DeduplicationPeriod, _Mapping]] = ..., max_sequencing_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
