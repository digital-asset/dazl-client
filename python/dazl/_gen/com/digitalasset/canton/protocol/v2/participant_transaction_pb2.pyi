# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from ..v0 import common_pb2 as _common_pb2
from ..v0 import participant_transaction_pb2 as _participant_transaction_pb2
from ..v0 import quorum_pb2 as _quorum_pb2
from ..v1 import participant_transaction_pb2 as _participant_transaction_pb2_1
from . import common_pb2 as _common_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewCommonData(_message.Message):
    __slots__ = ("salt", "informees", "quorums")
    SALT_FIELD_NUMBER: _ClassVar[int]
    INFORMEES_FIELD_NUMBER: _ClassVar[int]
    QUORUMS_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    informees: _containers.RepeatedCompositeFieldContainer[_quorum_pb2.TrustParty]
    quorums: _containers.RepeatedCompositeFieldContainer[_quorum_pb2.Quorum]
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., informees: _Optional[_Iterable[_Union[_quorum_pb2.TrustParty, _Mapping]]] = ..., quorums: _Optional[_Iterable[_Union[_quorum_pb2.Quorum, _Mapping]]] = ...) -> None: ...

class SessionKeyLookup(_message.Message):
    __slots__ = ("session_key_randomness", "fingerprint")
    SESSION_KEY_RANDOMNESS_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    session_key_randomness: bytes
    fingerprint: str
    def __init__(self, session_key_randomness: _Optional[bytes] = ..., fingerprint: _Optional[str] = ...) -> None: ...

class EncryptedViewMessage(_message.Message):
    __slots__ = ("view_tree", "encryption_scheme", "submitter_participant_signature", "view_hash", "randomness", "session_key_randomness", "domain_id", "view_type")
    VIEW_TREE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SCHEME_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    VIEW_HASH_FIELD_NUMBER: _ClassVar[int]
    RANDOMNESS_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_RANDOMNESS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    view_tree: bytes
    encryption_scheme: _crypto_pb2.SymmetricKeyScheme
    submitter_participant_signature: _crypto_pb2.Signature
    view_hash: bytes
    randomness: bytes
    session_key_randomness: _containers.RepeatedCompositeFieldContainer[SessionKeyLookup]
    domain_id: str
    view_type: _common_pb2.ViewType
    def __init__(self, view_tree: _Optional[bytes] = ..., encryption_scheme: _Optional[_Union[_crypto_pb2.SymmetricKeyScheme, str]] = ..., submitter_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., view_hash: _Optional[bytes] = ..., randomness: _Optional[bytes] = ..., session_key_randomness: _Optional[_Iterable[_Union[SessionKeyLookup, _Mapping]]] = ..., domain_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ...) -> None: ...

class ViewParticipantData(_message.Message):
    __slots__ = ("salt", "core_inputs", "created_core", "created_in_subview_archived_in_core", "resolved_keys", "action_description", "rollback_context")
    SALT_FIELD_NUMBER: _ClassVar[int]
    CORE_INPUTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_CORE_FIELD_NUMBER: _ClassVar[int]
    CREATED_IN_SUBVIEW_ARCHIVED_IN_CORE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_KEYS_FIELD_NUMBER: _ClassVar[int]
    ACTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    core_inputs: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2_1.InputContract]
    created_core: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2_1.CreatedContract]
    created_in_subview_archived_in_core: _containers.RepeatedScalarFieldContainer[str]
    resolved_keys: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2.ViewParticipantData.ResolvedKey]
    action_description: _participant_transaction_pb2_1.ActionDescription
    rollback_context: _participant_transaction_pb2.ViewParticipantData.RollbackContext
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., core_inputs: _Optional[_Iterable[_Union[_participant_transaction_pb2_1.InputContract, _Mapping]]] = ..., created_core: _Optional[_Iterable[_Union[_participant_transaction_pb2_1.CreatedContract, _Mapping]]] = ..., created_in_subview_archived_in_core: _Optional[_Iterable[str]] = ..., resolved_keys: _Optional[_Iterable[_Union[_participant_transaction_pb2.ViewParticipantData.ResolvedKey, _Mapping]]] = ..., action_description: _Optional[_Union[_participant_transaction_pb2_1.ActionDescription, _Mapping]] = ..., rollback_context: _Optional[_Union[_participant_transaction_pb2.ViewParticipantData.RollbackContext, _Mapping]] = ...) -> None: ...

class ActionDescription(_message.Message):
    __slots__ = ("create", "exercise", "fetch", "lookup_by_key")
    class ExerciseActionDescription(_message.Message):
        __slots__ = ("input_contract_id", "choice", "chosen_value", "actors", "by_key", "node_seed", "version", "failed", "interface_id", "template_id")
        INPUT_CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        CHOICE_FIELD_NUMBER: _ClassVar[int]
        CHOSEN_VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTORS_FIELD_NUMBER: _ClassVar[int]
        BY_KEY_FIELD_NUMBER: _ClassVar[int]
        NODE_SEED_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        input_contract_id: str
        choice: str
        chosen_value: bytes
        actors: _containers.RepeatedScalarFieldContainer[str]
        by_key: bool
        node_seed: bytes
        version: str
        failed: bool
        interface_id: str
        template_id: str
        def __init__(self, input_contract_id: _Optional[str] = ..., choice: _Optional[str] = ..., chosen_value: _Optional[bytes] = ..., actors: _Optional[_Iterable[str]] = ..., by_key: bool = ..., node_seed: _Optional[bytes] = ..., version: _Optional[str] = ..., failed: bool = ..., interface_id: _Optional[str] = ..., template_id: _Optional[str] = ...) -> None: ...
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    create: _participant_transaction_pb2.ActionDescription.CreateActionDescription
    exercise: ActionDescription.ExerciseActionDescription
    fetch: _participant_transaction_pb2.ActionDescription.FetchActionDescription
    lookup_by_key: _participant_transaction_pb2.ActionDescription.LookupByKeyActionDescription
    def __init__(self, create: _Optional[_Union[_participant_transaction_pb2.ActionDescription.CreateActionDescription, _Mapping]] = ..., exercise: _Optional[_Union[ActionDescription.ExerciseActionDescription, _Mapping]] = ..., fetch: _Optional[_Union[_participant_transaction_pb2.ActionDescription.FetchActionDescription, _Mapping]] = ..., lookup_by_key: _Optional[_Union[_participant_transaction_pb2.ActionDescription.LookupByKeyActionDescription, _Mapping]] = ...) -> None: ...

class CreatedContract(_message.Message):
    __slots__ = ("contract", "consumed_in_core", "rolled_back")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_IN_CORE_FIELD_NUMBER: _ClassVar[int]
    ROLLED_BACK_FIELD_NUMBER: _ClassVar[int]
    contract: _common_pb2_1.SerializableContract
    consumed_in_core: bool
    rolled_back: bool
    def __init__(self, contract: _Optional[_Union[_common_pb2_1.SerializableContract, _Mapping]] = ..., consumed_in_core: bool = ..., rolled_back: bool = ...) -> None: ...

class InputContract(_message.Message):
    __slots__ = ("contract", "consumed")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_FIELD_NUMBER: _ClassVar[int]
    contract: _common_pb2_1.SerializableContract
    consumed: bool
    def __init__(self, contract: _Optional[_Union[_common_pb2_1.SerializableContract, _Mapping]] = ..., consumed: bool = ...) -> None: ...
