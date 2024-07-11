# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from . import common_pb2 as _common_pb2
from . import merkle_pb2 as _merkle_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EncryptedViewMessage(_message.Message):
    __slots__ = ["view_tree", "submitter_participant_signature", "view_hash", "randomness", "domain_id", "view_type"]
    VIEW_TREE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    VIEW_HASH_FIELD_NUMBER: _ClassVar[int]
    RANDOMNESS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    view_tree: bytes
    submitter_participant_signature: _crypto_pb2.Signature
    view_hash: bytes
    randomness: _containers.RepeatedCompositeFieldContainer[ParticipantRandomnessLookup]
    domain_id: str
    view_type: _common_pb2.ViewType
    def __init__(self, view_tree: _Optional[bytes] = ..., submitter_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., view_hash: _Optional[bytes] = ..., randomness: _Optional[_Iterable[_Union[ParticipantRandomnessLookup, _Mapping]]] = ..., domain_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ...) -> None: ...

class LightTransactionViewTree(_message.Message):
    __slots__ = ["tree"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _merkle_pb2.GenTransactionTree
    def __init__(self, tree: _Optional[_Union[_merkle_pb2.GenTransactionTree, _Mapping]] = ...) -> None: ...

class SubmitterMetadata(_message.Message):
    __slots__ = ["salt", "act_as", "application_id", "command_id", "submitter_participant", "submission_id", "dedup_period"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUP_PERIOD_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    act_as: _containers.RepeatedScalarFieldContainer[str]
    application_id: str
    command_id: str
    submitter_participant: str
    submission_id: str
    dedup_period: DeduplicationPeriod
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., act_as: _Optional[_Iterable[str]] = ..., application_id: _Optional[str] = ..., command_id: _Optional[str] = ..., submitter_participant: _Optional[str] = ..., submission_id: _Optional[str] = ..., dedup_period: _Optional[_Union[DeduplicationPeriod, _Mapping]] = ...) -> None: ...

class DeduplicationPeriod(_message.Message):
    __slots__ = ["duration", "offset"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    duration: _duration_pb2.Duration
    offset: bytes
    def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., offset: _Optional[bytes] = ...) -> None: ...

class CommonMetadata(_message.Message):
    __slots__ = ["salt", "confirmation_policy", "domain_id", "uuid", "mediator_id"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_ID_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    confirmation_policy: bytes
    domain_id: str
    uuid: str
    mediator_id: str
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., confirmation_policy: _Optional[bytes] = ..., domain_id: _Optional[str] = ..., uuid: _Optional[str] = ..., mediator_id: _Optional[str] = ...) -> None: ...

class ParticipantMetadata(_message.Message):
    __slots__ = ["salt", "ledger_time", "submission_time", "workflow_id"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    LEDGER_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_TIME_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    ledger_time: _timestamp_pb2.Timestamp
    submission_time: _timestamp_pb2.Timestamp
    workflow_id: str
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., ledger_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., submission_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., workflow_id: _Optional[str] = ...) -> None: ...

class ViewNode(_message.Message):
    __slots__ = ["view_common_data", "view_participant_data", "subviews"]
    VIEW_COMMON_DATA_FIELD_NUMBER: _ClassVar[int]
    VIEW_PARTICIPANT_DATA_FIELD_NUMBER: _ClassVar[int]
    SUBVIEWS_FIELD_NUMBER: _ClassVar[int]
    view_common_data: _merkle_pb2.BlindableNode
    view_participant_data: _merkle_pb2.BlindableNode
    subviews: _containers.RepeatedCompositeFieldContainer[_merkle_pb2.BlindableNode]
    def __init__(self, view_common_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ..., view_participant_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ..., subviews: _Optional[_Iterable[_Union[_merkle_pb2.BlindableNode, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ["party", "weight"]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    party: str
    weight: int
    def __init__(self, party: _Optional[str] = ..., weight: _Optional[int] = ...) -> None: ...

class ViewParticipantData(_message.Message):
    __slots__ = ["salt", "core_inputs", "created_core", "created_in_subview_archived_in_core", "resolved_keys", "action_description", "rollback_context"]
    class CreatedContract(_message.Message):
        __slots__ = ["contract", "consumed_in_core", "rolled_back"]
        CONTRACT_FIELD_NUMBER: _ClassVar[int]
        CONSUMED_IN_CORE_FIELD_NUMBER: _ClassVar[int]
        ROLLED_BACK_FIELD_NUMBER: _ClassVar[int]
        contract: _common_pb2.SerializableContract
        consumed_in_core: bool
        rolled_back: bool
        def __init__(self, contract: _Optional[_Union[_common_pb2.SerializableContract, _Mapping]] = ..., consumed_in_core: bool = ..., rolled_back: bool = ...) -> None: ...
    class InputContract(_message.Message):
        __slots__ = ["contract", "consumed"]
        CONTRACT_FIELD_NUMBER: _ClassVar[int]
        CONSUMED_FIELD_NUMBER: _ClassVar[int]
        contract: _common_pb2.SerializableContract
        consumed: bool
        def __init__(self, contract: _Optional[_Union[_common_pb2.SerializableContract, _Mapping]] = ..., consumed: bool = ...) -> None: ...
    class ResolvedKey(_message.Message):
        __slots__ = ["key", "contract_id", "free"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        FREE_FIELD_NUMBER: _ClassVar[int]
        key: _common_pb2.GlobalKey
        contract_id: str
        free: ViewParticipantData.FreeKey
        def __init__(self, key: _Optional[_Union[_common_pb2.GlobalKey, _Mapping]] = ..., contract_id: _Optional[str] = ..., free: _Optional[_Union[ViewParticipantData.FreeKey, _Mapping]] = ...) -> None: ...
    class FreeKey(_message.Message):
        __slots__ = ["maintainers"]
        MAINTAINERS_FIELD_NUMBER: _ClassVar[int]
        maintainers: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, maintainers: _Optional[_Iterable[str]] = ...) -> None: ...
    class RollbackContext(_message.Message):
        __slots__ = ["rollback_scope", "next_child"]
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
    core_inputs: _containers.RepeatedCompositeFieldContainer[ViewParticipantData.InputContract]
    created_core: _containers.RepeatedCompositeFieldContainer[ViewParticipantData.CreatedContract]
    created_in_subview_archived_in_core: _containers.RepeatedScalarFieldContainer[str]
    resolved_keys: _containers.RepeatedCompositeFieldContainer[ViewParticipantData.ResolvedKey]
    action_description: ActionDescription
    rollback_context: ViewParticipantData.RollbackContext
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., core_inputs: _Optional[_Iterable[_Union[ViewParticipantData.InputContract, _Mapping]]] = ..., created_core: _Optional[_Iterable[_Union[ViewParticipantData.CreatedContract, _Mapping]]] = ..., created_in_subview_archived_in_core: _Optional[_Iterable[str]] = ..., resolved_keys: _Optional[_Iterable[_Union[ViewParticipantData.ResolvedKey, _Mapping]]] = ..., action_description: _Optional[_Union[ActionDescription, _Mapping]] = ..., rollback_context: _Optional[_Union[ViewParticipantData.RollbackContext, _Mapping]] = ...) -> None: ...

class ActionDescription(_message.Message):
    __slots__ = ["create", "exercise", "fetch", "lookup_by_key"]
    class CreateActionDescription(_message.Message):
        __slots__ = ["contract_id", "node_seed", "version"]
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_SEED_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        contract_id: str
        node_seed: bytes
        version: str
        def __init__(self, contract_id: _Optional[str] = ..., node_seed: _Optional[bytes] = ..., version: _Optional[str] = ...) -> None: ...
    class ExerciseActionDescription(_message.Message):
        __slots__ = ["input_contract_id", "choice", "chosen_value", "actors", "by_key", "node_seed", "version", "failed"]
        INPUT_CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        CHOICE_FIELD_NUMBER: _ClassVar[int]
        CHOSEN_VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTORS_FIELD_NUMBER: _ClassVar[int]
        BY_KEY_FIELD_NUMBER: _ClassVar[int]
        NODE_SEED_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        input_contract_id: str
        choice: str
        chosen_value: bytes
        actors: _containers.RepeatedScalarFieldContainer[str]
        by_key: bool
        node_seed: bytes
        version: str
        failed: bool
        def __init__(self, input_contract_id: _Optional[str] = ..., choice: _Optional[str] = ..., chosen_value: _Optional[bytes] = ..., actors: _Optional[_Iterable[str]] = ..., by_key: bool = ..., node_seed: _Optional[bytes] = ..., version: _Optional[str] = ..., failed: bool = ...) -> None: ...
    class FetchActionDescription(_message.Message):
        __slots__ = ["input_contract_id", "actors", "by_key", "version"]
        INPUT_CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        ACTORS_FIELD_NUMBER: _ClassVar[int]
        BY_KEY_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        input_contract_id: str
        actors: _containers.RepeatedScalarFieldContainer[str]
        by_key: bool
        version: str
        def __init__(self, input_contract_id: _Optional[str] = ..., actors: _Optional[_Iterable[str]] = ..., by_key: bool = ..., version: _Optional[str] = ...) -> None: ...
    class LookupByKeyActionDescription(_message.Message):
        __slots__ = ["key"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        key: _common_pb2.GlobalKey
        def __init__(self, key: _Optional[_Union[_common_pb2.GlobalKey, _Mapping]] = ...) -> None: ...
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    create: ActionDescription.CreateActionDescription
    exercise: ActionDescription.ExerciseActionDescription
    fetch: ActionDescription.FetchActionDescription
    lookup_by_key: ActionDescription.LookupByKeyActionDescription
    def __init__(self, create: _Optional[_Union[ActionDescription.CreateActionDescription, _Mapping]] = ..., exercise: _Optional[_Union[ActionDescription.ExerciseActionDescription, _Mapping]] = ..., fetch: _Optional[_Union[ActionDescription.FetchActionDescription, _Mapping]] = ..., lookup_by_key: _Optional[_Union[ActionDescription.LookupByKeyActionDescription, _Mapping]] = ...) -> None: ...

class ParticipantRandomnessLookup(_message.Message):
    __slots__ = ["participant", "randomness"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    RANDOMNESS_FIELD_NUMBER: _ClassVar[int]
    participant: str
    randomness: bytes
    def __init__(self, participant: _Optional[str] = ..., randomness: _Optional[bytes] = ...) -> None: ...

class InformeeMessage(_message.Message):
    __slots__ = ["full_informee_tree"]
    FULL_INFORMEE_TREE_FIELD_NUMBER: _ClassVar[int]
    full_informee_tree: FullInformeeTree
    def __init__(self, full_informee_tree: _Optional[_Union[FullInformeeTree, _Mapping]] = ...) -> None: ...

class FullInformeeTree(_message.Message):
    __slots__ = ["tree"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: _merkle_pb2.GenTransactionTree
    def __init__(self, tree: _Optional[_Union[_merkle_pb2.GenTransactionTree, _Mapping]] = ...) -> None: ...

class RootHashMessage(_message.Message):
    __slots__ = ["root_hash", "domain_id", "view_type", "payload"]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    root_hash: bytes
    domain_id: str
    view_type: _common_pb2.ViewType
    payload: bytes
    def __init__(self, root_hash: _Optional[bytes] = ..., domain_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ..., payload: _Optional[bytes] = ...) -> None: ...
