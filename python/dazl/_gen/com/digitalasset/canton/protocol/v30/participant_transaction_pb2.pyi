# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from . import common_pb2 as _common_pb2
from . import common_stable_pb2 as _common_stable_pb2
from . import merkle_pb2 as _merkle_pb2
from . import quorum_pb2 as _quorum_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeduplicationPeriod(_message.Message):
    __slots__ = ("duration", "offset")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    offset: int
    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., offset: _Optional[int] = ...) -> None: ...

class ParticipantMetadata(_message.Message):
    __slots__ = ("salt", "ledger_time", "preparation_time", "workflow_id")
    SALT_FIELD_NUMBER: _ClassVar[int]
    LEDGER_TIME_FIELD_NUMBER: _ClassVar[int]
    PREPARATION_TIME_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    ledger_time: int
    preparation_time: int
    workflow_id: str
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., ledger_time: _Optional[int] = ..., preparation_time: _Optional[int] = ..., workflow_id: _Optional[str] = ...) -> None: ...

class RootHashMessage(_message.Message):
    __slots__ = ("root_hash", "synchronizer_id", "view_type", "submission_topology_time", "payload")
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_TOPOLOGY_TIME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    root_hash: bytes
    synchronizer_id: str
    view_type: _common_pb2.ViewType
    submission_topology_time: int
    payload: bytes
    def __init__(self, root_hash: _Optional[bytes] = ..., synchronizer_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ..., submission_topology_time: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class ViewNode(_message.Message):
    __slots__ = ("view_common_data", "view_participant_data", "subviews")
    VIEW_COMMON_DATA_FIELD_NUMBER: _ClassVar[int]
    VIEW_PARTICIPANT_DATA_FIELD_NUMBER: _ClassVar[int]
    SUBVIEWS_FIELD_NUMBER: _ClassVar[int]
    view_common_data: _merkle_pb2.BlindableNode
    view_participant_data: _merkle_pb2.BlindableNode
    subviews: _merkle_pb2.MerkleSeq
    def __init__(self, view_common_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ..., view_participant_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ..., subviews: _Optional[_Union[_merkle_pb2.MerkleSeq, _Mapping]] = ...) -> None: ...

class ViewCommonData(_message.Message):
    __slots__ = ("salt", "informees", "quorums")
    SALT_FIELD_NUMBER: _ClassVar[int]
    INFORMEES_FIELD_NUMBER: _ClassVar[int]
    QUORUMS_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    informees: _containers.RepeatedScalarFieldContainer[str]
    quorums: _containers.RepeatedCompositeFieldContainer[_quorum_pb2.Quorum]
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., informees: _Optional[_Iterable[str]] = ..., quorums: _Optional[_Iterable[_Union[_quorum_pb2.Quorum, _Mapping]]] = ...) -> None: ...

class Informee(_message.Message):
    __slots__ = ("party", "weight")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    party: str
    weight: int
    def __init__(self, party: _Optional[str] = ..., weight: _Optional[int] = ...) -> None: ...

class ViewParticipantMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InformeeMessage(_message.Message):
    __slots__ = ("full_informee_tree", "submitting_participant_signature")
    FULL_INFORMEE_TREE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    full_informee_tree: FullInformeeTree
    submitting_participant_signature: _crypto_pb2.Signature
    def __init__(self, full_informee_tree: _Optional[_Union[FullInformeeTree, _Mapping]] = ..., submitting_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class LightTransactionViewTree(_message.Message):
    __slots__ = ("tree", "subview_hashes_and_keys")
    TREE_FIELD_NUMBER: _ClassVar[int]
    SUBVIEW_HASHES_AND_KEYS_FIELD_NUMBER: _ClassVar[int]
    tree: _merkle_pb2.GenTransactionTree
    subview_hashes_and_keys: _containers.RepeatedCompositeFieldContainer[ViewHashAndKey]
    def __init__(self, tree: _Optional[_Union[_merkle_pb2.GenTransactionTree, _Mapping]] = ..., subview_hashes_and_keys: _Optional[_Iterable[_Union[ViewHashAndKey, _Mapping]]] = ...) -> None: ...

class ViewHashAndKey(_message.Message):
    __slots__ = ("view_hash", "view_encryption_key_randomness")
    VIEW_HASH_FIELD_NUMBER: _ClassVar[int]
    VIEW_ENCRYPTION_KEY_RANDOMNESS_FIELD_NUMBER: _ClassVar[int]
    view_hash: bytes
    view_encryption_key_randomness: bytes
    def __init__(self, view_hash: _Optional[bytes] = ..., view_encryption_key_randomness: _Optional[bytes] = ...) -> None: ...

class FullInformeeTree(_message.Message):
    __slots__ = ("tree",)
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _merkle_pb2.GenTransactionTree
    def __init__(self, tree: _Optional[_Union[_merkle_pb2.GenTransactionTree, _Mapping]] = ...) -> None: ...

class CreatedContract(_message.Message):
    __slots__ = ("contract", "consumed_in_core", "rolled_back")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_IN_CORE_FIELD_NUMBER: _ClassVar[int]
    ROLLED_BACK_FIELD_NUMBER: _ClassVar[int]
    contract: _common_stable_pb2.SerializableContract
    consumed_in_core: bool
    rolled_back: bool
    def __init__(self, contract: _Optional[_Union[_common_stable_pb2.SerializableContract, _Mapping]] = ..., consumed_in_core: bool = ..., rolled_back: bool = ...) -> None: ...

class InputContract(_message.Message):
    __slots__ = ("contract", "consumed")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_FIELD_NUMBER: _ClassVar[int]
    contract: _common_stable_pb2.SerializableContract
    consumed: bool
    def __init__(self, contract: _Optional[_Union[_common_stable_pb2.SerializableContract, _Mapping]] = ..., consumed: bool = ...) -> None: ...

class CommonMetadata(_message.Message):
    __slots__ = ("salt", "synchronizer_id", "uuid", "mediator_group")
    SALT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    synchronizer_id: str
    uuid: str
    mediator_group: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., synchronizer_id: _Optional[str] = ..., uuid: _Optional[str] = ..., mediator_group: _Optional[int] = ...) -> None: ...

class SubmitterMetadata(_message.Message):
    __slots__ = ("salt", "act_as", "user_id", "command_id", "submitting_participant_uid", "submission_id", "dedup_period", "max_sequencing_time", "external_authorization")
    SALT_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUP_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MAX_SEQUENCING_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    act_as: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    command_id: str
    submitting_participant_uid: str
    submission_id: str
    dedup_period: DeduplicationPeriod
    max_sequencing_time: int
    external_authorization: ExternalAuthorization
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., act_as: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ..., command_id: _Optional[str] = ..., submitting_participant_uid: _Optional[str] = ..., submission_id: _Optional[str] = ..., dedup_period: _Optional[_Union[DeduplicationPeriod, _Mapping]] = ..., max_sequencing_time: _Optional[int] = ..., external_authorization: _Optional[_Union[ExternalAuthorization, _Mapping]] = ...) -> None: ...

class EncryptedViewMessage(_message.Message):
    __slots__ = ("view_tree", "encryption_scheme", "submitting_participant_signature", "view_hash", "session_key_lookup", "synchronizer_id", "view_type")
    VIEW_TREE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SCHEME_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    VIEW_HASH_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    view_tree: bytes
    encryption_scheme: _crypto_pb2.SymmetricKeyScheme
    submitting_participant_signature: _crypto_pb2.Signature
    view_hash: bytes
    session_key_lookup: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.AsymmetricEncrypted]
    synchronizer_id: str
    view_type: _common_pb2.ViewType
    def __init__(self, view_tree: _Optional[bytes] = ..., encryption_scheme: _Optional[_Union[_crypto_pb2.SymmetricKeyScheme, str]] = ..., submitting_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., view_hash: _Optional[bytes] = ..., session_key_lookup: _Optional[_Iterable[_Union[_crypto_pb2.AsymmetricEncrypted, _Mapping]]] = ..., synchronizer_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ...) -> None: ...

class ActionDescription(_message.Message):
    __slots__ = ("create", "exercise", "fetch", "lookup_by_key")
    class CreateActionDescription(_message.Message):
        __slots__ = ("contract_id", "node_seed")
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_SEED_FIELD_NUMBER: _ClassVar[int]
        contract_id: str
        node_seed: bytes
        def __init__(self, contract_id: _Optional[str] = ..., node_seed: _Optional[bytes] = ...) -> None: ...
    class ExerciseActionDescription(_message.Message):
        __slots__ = ("input_contract_id", "choice", "chosen_value", "actors", "by_key", "node_seed", "failed", "interface_id", "template_id", "package_preference")
        INPUT_CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        CHOICE_FIELD_NUMBER: _ClassVar[int]
        CHOSEN_VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTORS_FIELD_NUMBER: _ClassVar[int]
        BY_KEY_FIELD_NUMBER: _ClassVar[int]
        NODE_SEED_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
        input_contract_id: str
        choice: str
        chosen_value: bytes
        actors: _containers.RepeatedScalarFieldContainer[str]
        by_key: bool
        node_seed: bytes
        failed: bool
        interface_id: str
        template_id: str
        package_preference: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, input_contract_id: _Optional[str] = ..., choice: _Optional[str] = ..., chosen_value: _Optional[bytes] = ..., actors: _Optional[_Iterable[str]] = ..., by_key: bool = ..., node_seed: _Optional[bytes] = ..., failed: bool = ..., interface_id: _Optional[str] = ..., template_id: _Optional[str] = ..., package_preference: _Optional[_Iterable[str]] = ...) -> None: ...
    class FetchActionDescription(_message.Message):
        __slots__ = ("input_contract_id", "actors", "by_key", "template_id", "interface_id")
        INPUT_CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        ACTORS_FIELD_NUMBER: _ClassVar[int]
        BY_KEY_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
        input_contract_id: str
        actors: _containers.RepeatedScalarFieldContainer[str]
        by_key: bool
        template_id: str
        interface_id: str
        def __init__(self, input_contract_id: _Optional[str] = ..., actors: _Optional[_Iterable[str]] = ..., by_key: bool = ..., template_id: _Optional[str] = ..., interface_id: _Optional[str] = ...) -> None: ...
    class LookupByKeyActionDescription(_message.Message):
        __slots__ = ("key",)
        KEY_FIELD_NUMBER: _ClassVar[int]
        key: _common_stable_pb2.GlobalKey
        def __init__(self, key: _Optional[_Union[_common_stable_pb2.GlobalKey, _Mapping]] = ...) -> None: ...
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    create: ActionDescription.CreateActionDescription
    exercise: ActionDescription.ExerciseActionDescription
    fetch: ActionDescription.FetchActionDescription
    lookup_by_key: ActionDescription.LookupByKeyActionDescription
    def __init__(self, create: _Optional[_Union[ActionDescription.CreateActionDescription, _Mapping]] = ..., exercise: _Optional[_Union[ActionDescription.ExerciseActionDescription, _Mapping]] = ..., fetch: _Optional[_Union[ActionDescription.FetchActionDescription, _Mapping]] = ..., lookup_by_key: _Optional[_Union[ActionDescription.LookupByKeyActionDescription, _Mapping]] = ...) -> None: ...

class ViewParticipantData(_message.Message):
    __slots__ = ("salt", "core_inputs", "created_core", "created_in_subview_archived_in_core", "resolved_keys", "action_description", "rollback_context")
    class FreeKey(_message.Message):
        __slots__ = ("maintainers",)
        MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
        maintainers: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, maintainers: _Optional[_Iterable[str]] = ...) -> None: ...
    class ResolvedKey(_message.Message):
        __slots__ = ("key", "contract_id", "free")
        KEY_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        FREE_FIELD_NUMBER: _ClassVar[int]
        key: _common_stable_pb2.GlobalKey
        contract_id: str
        free: ViewParticipantData.FreeKey
        def __init__(self, key: _Optional[_Union[_common_stable_pb2.GlobalKey, _Mapping]] = ..., contract_id: _Optional[str] = ..., free: _Optional[_Union[ViewParticipantData.FreeKey, _Mapping]] = ...) -> None: ...
    class RollbackContext(_message.Message):
        __slots__ = ("rollback_scope", "next_child")
        ROLLBACK_SCOPE_FIELD_NUMBER: _ClassVar[int]
        NEXT_CHILD_FIELD_NUMBER: _ClassVar[int]
        rollback_scope: _containers.RepeatedScalarFieldContainer[int]
        next_child: int
        def __init__(self, rollback_scope: _Optional[_Iterable[int]] = ..., next_child: _Optional[int] = ...) -> None: ...
    SALT_FIELD_NUMBER: _ClassVar[int]
    CORE_INPUTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_CORE_FIELD_NUMBER: _ClassVar[int]
    CREATED_IN_SUBVIEW_ARCHIVED_IN_CORE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_KEYS_FIELD_NUMBER: _ClassVar[int]
    ACTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    core_inputs: _containers.RepeatedCompositeFieldContainer[InputContract]
    created_core: _containers.RepeatedCompositeFieldContainer[CreatedContract]
    created_in_subview_archived_in_core: _containers.RepeatedScalarFieldContainer[str]
    resolved_keys: _containers.RepeatedCompositeFieldContainer[ViewParticipantData.ResolvedKey]
    action_description: ActionDescription
    rollback_context: ViewParticipantData.RollbackContext
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., core_inputs: _Optional[_Iterable[_Union[InputContract, _Mapping]]] = ..., created_core: _Optional[_Iterable[_Union[CreatedContract, _Mapping]]] = ..., created_in_subview_archived_in_core: _Optional[_Iterable[str]] = ..., resolved_keys: _Optional[_Iterable[_Union[ViewParticipantData.ResolvedKey, _Mapping]]] = ..., action_description: _Optional[_Union[ActionDescription, _Mapping]] = ..., rollback_context: _Optional[_Union[ViewParticipantData.RollbackContext, _Mapping]] = ...) -> None: ...

class ExternalPartyAuthorization(_message.Message):
    __slots__ = ("party", "signatures")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    party: str
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    def __init__(self, party: _Optional[str] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...

class ExternalAuthorization(_message.Message):
    __slots__ = ("authentications", "hashing_scheme_version")
    class HashingSchemeVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HASHING_SCHEME_VERSION_UNSPECIFIED: _ClassVar[ExternalAuthorization.HashingSchemeVersion]
        HASHING_SCHEME_VERSION_V2: _ClassVar[ExternalAuthorization.HashingSchemeVersion]
    HASHING_SCHEME_VERSION_UNSPECIFIED: ExternalAuthorization.HashingSchemeVersion
    HASHING_SCHEME_VERSION_V2: ExternalAuthorization.HashingSchemeVersion
    AUTHENTICATIONS_FIELD_NUMBER: _ClassVar[int]
    HASHING_SCHEME_VERSION_FIELD_NUMBER: _ClassVar[int]
    authentications: _containers.RepeatedCompositeFieldContainer[ExternalPartyAuthorization]
    hashing_scheme_version: ExternalAuthorization.HashingSchemeVersion
    def __init__(self, authentications: _Optional[_Iterable[_Union[ExternalPartyAuthorization, _Mapping]]] = ..., hashing_scheme_version: _Optional[_Union[ExternalAuthorization.HashingSchemeVersion, str]] = ...) -> None: ...
