# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import value_pb2 as _value_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Command(_message.Message):
    __slots__ = ("create", "exercise", "exercise_by_key", "create_and_exercise")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATE_AND_EXERCISE_FIELD_NUMBER: _ClassVar[int]
    create: CreateCommand
    exercise: ExerciseCommand
    exercise_by_key: ExerciseByKeyCommand
    create_and_exercise: CreateAndExerciseCommand
    def __init__(self, create: _Optional[_Union[CreateCommand, _Mapping]] = ..., exercise: _Optional[_Union[ExerciseCommand, _Mapping]] = ..., exercise_by_key: _Optional[_Union[ExerciseByKeyCommand, _Mapping]] = ..., create_and_exercise: _Optional[_Union[CreateAndExerciseCommand, _Mapping]] = ...) -> None: ...

class CreateCommand(_message.Message):
    __slots__ = ("template_id", "create_arguments")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    create_arguments: _value_pb2.Record
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., create_arguments: _Optional[_Union[_value_pb2.Record, _Mapping]] = ...) -> None: ...

class ExerciseCommand(_message.Message):
    __slots__ = ("template_id", "contract_id", "choice", "choice_argument")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    CHOICE_FIELD_NUMBER: _ClassVar[int]
    CHOICE_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    contract_id: str
    choice: str
    choice_argument: _value_pb2.Value
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., contract_id: _Optional[str] = ..., choice: _Optional[str] = ..., choice_argument: _Optional[_Union[_value_pb2.Value, _Mapping]] = ...) -> None: ...

class ExerciseByKeyCommand(_message.Message):
    __slots__ = ("template_id", "contract_key", "choice", "choice_argument")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_KEY_FIELD_NUMBER: _ClassVar[int]
    CHOICE_FIELD_NUMBER: _ClassVar[int]
    CHOICE_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    contract_key: _value_pb2.Value
    choice: str
    choice_argument: _value_pb2.Value
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., contract_key: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., choice: _Optional[str] = ..., choice_argument: _Optional[_Union[_value_pb2.Value, _Mapping]] = ...) -> None: ...

class CreateAndExerciseCommand(_message.Message):
    __slots__ = ("template_id", "create_arguments", "choice", "choice_argument")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    CHOICE_FIELD_NUMBER: _ClassVar[int]
    CHOICE_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    create_arguments: _value_pb2.Record
    choice: str
    choice_argument: _value_pb2.Value
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., create_arguments: _Optional[_Union[_value_pb2.Record, _Mapping]] = ..., choice: _Optional[str] = ..., choice_argument: _Optional[_Union[_value_pb2.Value, _Mapping]] = ...) -> None: ...

class DisclosedContract(_message.Message):
    __slots__ = ("template_id", "contract_id", "created_event_blob", "synchronizer_id")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_EVENT_BLOB_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    contract_id: str
    created_event_blob: bytes
    synchronizer_id: str
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., contract_id: _Optional[str] = ..., created_event_blob: _Optional[bytes] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...

class Commands(_message.Message):
    __slots__ = ("workflow_id", "user_id", "command_id", "commands", "deduplication_duration", "deduplication_offset", "min_ledger_time_abs", "min_ledger_time_rel", "act_as", "read_as", "submission_id", "disclosed_contracts", "synchronizer_id", "package_id_selection_preference", "prefetch_contract_keys")
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_TIME_ABS_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_TIME_REL_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    READ_AS_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    DISCLOSED_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_SELECTION_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_CONTRACT_KEYS_FIELD_NUMBER: _ClassVar[int]
    workflow_id: str
    user_id: str
    command_id: str
    commands: _containers.RepeatedCompositeFieldContainer[Command]
    deduplication_duration: _duration_pb2.Duration
    deduplication_offset: int
    min_ledger_time_abs: _timestamp_pb2.Timestamp
    min_ledger_time_rel: _duration_pb2.Duration
    act_as: _containers.RepeatedScalarFieldContainer[str]
    read_as: _containers.RepeatedScalarFieldContainer[str]
    submission_id: str
    disclosed_contracts: _containers.RepeatedCompositeFieldContainer[DisclosedContract]
    synchronizer_id: str
    package_id_selection_preference: _containers.RepeatedScalarFieldContainer[str]
    prefetch_contract_keys: _containers.RepeatedCompositeFieldContainer[PrefetchContractKey]
    def __init__(self, workflow_id: _Optional[str] = ..., user_id: _Optional[str] = ..., command_id: _Optional[str] = ..., commands: _Optional[_Iterable[_Union[Command, _Mapping]]] = ..., deduplication_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., deduplication_offset: _Optional[int] = ..., min_ledger_time_abs: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., min_ledger_time_rel: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., act_as: _Optional[_Iterable[str]] = ..., read_as: _Optional[_Iterable[str]] = ..., submission_id: _Optional[str] = ..., disclosed_contracts: _Optional[_Iterable[_Union[DisclosedContract, _Mapping]]] = ..., synchronizer_id: _Optional[str] = ..., package_id_selection_preference: _Optional[_Iterable[str]] = ..., prefetch_contract_keys: _Optional[_Iterable[_Union[PrefetchContractKey, _Mapping]]] = ...) -> None: ...

class PrefetchContractKey(_message.Message):
    __slots__ = ("template_id", "contract_key")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_KEY_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    contract_key: _value_pb2.Value
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., contract_key: _Optional[_Union[_value_pb2.Value, _Mapping]] = ...) -> None: ...
