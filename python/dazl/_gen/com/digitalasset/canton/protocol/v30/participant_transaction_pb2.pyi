# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from . import common_pb2 as _common_pb2
from . import merkle_pb2 as _merkle_pb2
from . import quorum_pb2 as _quorum_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
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
    def __init__(self, duration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., offset: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("root_hash", "physical_synchronizer_id", "view_type", "submission_topology_time", "payload")
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_TOPOLOGY_TIME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    root_hash: bytes
    physical_synchronizer_id: str
    view_type: _common_pb2.ViewType
    submission_topology_time: int
    payload: bytes
    def __init__(self, root_hash: _Optional[bytes] = ..., physical_synchronizer_id: _Optional[str] = ..., view_type: _Optional[_Union[_common_pb2.ViewType, str]] = ..., submission_topology_time: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

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
    contract: bytes
    consumed_in_core: bool
    rolled_back: bool
    def __init__(self, contract: _Optional[bytes] = ..., consumed_in_core: _Optional[bool] = ..., rolled_back: _Optional[bool] = ...) -> None: ...

class InputContract(_message.Message):
    __slots__ = ("contract", "consumed")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_FIELD_NUMBER: _ClassVar[int]
    contract: bytes
    consumed: bool
    def __init__(self, contract: _Optional[bytes] = ..., consumed: _Optional[bool] = ...) -> None: ...

class CommonMetadata(_message.Message):
    __slots__ = ("salt", "physical_synchronizer_id", "uuid", "mediator_group")
    SALT_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    physical_synchronizer_id: str
    uuid: str
    mediator_group: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., physical_synchronizer_id: _Optional[str] = ..., uuid: _Optional[str] = ..., mediator_group: _Optional[int] = ...) -> None: ...

class ActionDescription(_message.Message):
    __slots__ = ()
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
        def __init__(self, input_contract_id: _Optional[str] = ..., choice: _Optional[str] = ..., chosen_value: _Optional[bytes] = ..., actors: _Optional[_Iterable[str]] = ..., by_key: _Optional[bool] = ..., node_seed: _Optional[bytes] = ..., failed: _Optional[bool] = ..., interface_id: _Optional[str] = ..., template_id: _Optional[str] = ..., package_preference: _Optional[_Iterable[str]] = ...) -> None: ...
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
        def __init__(self, input_contract_id: _Optional[str] = ..., actors: _Optional[_Iterable[str]] = ..., by_key: _Optional[bool] = ..., template_id: _Optional[str] = ..., interface_id: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class ViewParticipantData(_message.Message):
    __slots__ = ()
    class RollbackContext(_message.Message):
        __slots__ = ("rollback_scope", "next_child")
        ROLLBACK_SCOPE_FIELD_NUMBER: _ClassVar[int]
        NEXT_CHILD_FIELD_NUMBER: _ClassVar[int]
        rollback_scope: _containers.RepeatedScalarFieldContainer[int]
        next_child: int
        def __init__(self, rollback_scope: _Optional[_Iterable[int]] = ..., next_child: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class ExternalPartyAuthorization(_message.Message):
    __slots__ = ("party", "signatures")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    party: str
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    def __init__(self, party: _Optional[str] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...
