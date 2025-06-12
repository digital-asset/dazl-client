# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from ..v0 import participant_transaction_pb2 as _participant_transaction_pb2
from ..v1 import participant_transaction_pb2 as _participant_transaction_pb2_1
from ..v2 import participant_transaction_pb2 as _participant_transaction_pb2_1_1
from ..v3 import participant_transaction_pb2 as _participant_transaction_pb2_1_1_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    core_inputs: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2_1_1.InputContract]
    created_core: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2_1_1.CreatedContract]
    created_in_subview_archived_in_core: _containers.RepeatedScalarFieldContainer[str]
    resolved_keys: _containers.RepeatedCompositeFieldContainer[_participant_transaction_pb2_1.ResolvedKey]
    action_description: _participant_transaction_pb2_1_1_1.ActionDescription
    rollback_context: _participant_transaction_pb2.ViewParticipantData.RollbackContext
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., core_inputs: _Optional[_Iterable[_Union[_participant_transaction_pb2_1_1.InputContract, _Mapping]]] = ..., created_core: _Optional[_Iterable[_Union[_participant_transaction_pb2_1_1.CreatedContract, _Mapping]]] = ..., created_in_subview_archived_in_core: _Optional[_Iterable[str]] = ..., resolved_keys: _Optional[_Iterable[_Union[_participant_transaction_pb2_1.ResolvedKey, _Mapping]]] = ..., action_description: _Optional[_Union[_participant_transaction_pb2_1_1_1.ActionDescription, _Mapping]] = ..., rollback_context: _Optional[_Union[_participant_transaction_pb2.ViewParticipantData.RollbackContext, _Mapping]] = ...) -> None: ...

class ActionDescription(_message.Message):
    __slots__ = ("create", "exercise", "fetch", "lookup_by_key")
    class FetchActionDescription(_message.Message):
        __slots__ = ("input_contract_id", "actors", "by_key", "version", "template_id", "interface_id")
        INPUT_CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        ACTORS_FIELD_NUMBER: _ClassVar[int]
        BY_KEY_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
        input_contract_id: str
        actors: _containers.RepeatedScalarFieldContainer[str]
        by_key: bool
        version: str
        template_id: str
        interface_id: str
        def __init__(self, input_contract_id: _Optional[str] = ..., actors: _Optional[_Iterable[str]] = ..., by_key: bool = ..., version: _Optional[str] = ..., template_id: _Optional[str] = ..., interface_id: _Optional[str] = ...) -> None: ...
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    create: _participant_transaction_pb2.ActionDescription.CreateActionDescription
    exercise: _participant_transaction_pb2_1_1_1.ActionDescription.ExerciseActionDescription
    fetch: ActionDescription.FetchActionDescription
    lookup_by_key: _participant_transaction_pb2_1.ActionDescription.LookupByKeyActionDescription
    def __init__(self, create: _Optional[_Union[_participant_transaction_pb2.ActionDescription.CreateActionDescription, _Mapping]] = ..., exercise: _Optional[_Union[_participant_transaction_pb2_1_1_1.ActionDescription.ExerciseActionDescription, _Mapping]] = ..., fetch: _Optional[_Union[ActionDescription.FetchActionDescription, _Mapping]] = ..., lookup_by_key: _Optional[_Union[_participant_transaction_pb2_1.ActionDescription.LookupByKeyActionDescription, _Mapping]] = ...) -> None: ...
