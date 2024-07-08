# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import contract_metadata_pb2 as _contract_metadata_pb2
from . import value_pb2 as _value_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Commands(_message.Message):
    __slots__ = ["ledger_id", "workflow_id", "application_id", "command_id", "party", "commands", "deduplication_time", "deduplication_duration", "deduplication_offset", "min_ledger_time_abs", "min_ledger_time_rel", "act_as", "read_as", "submission_id", "disclosed_contracts"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_TIME_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_TIME_ABS_FIELD_NUMBER: _ClassVar[int]
    MIN_LEDGER_TIME_REL_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    READ_AS_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    DISCLOSED_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    workflow_id: str
    application_id: str
    command_id: str
    party: str
    commands: _containers.RepeatedCompositeFieldContainer[Command]
    deduplication_time: _duration_pb2.Duration
    deduplication_duration: _duration_pb2.Duration
    deduplication_offset: str
    min_ledger_time_abs: _timestamp_pb2.Timestamp
    min_ledger_time_rel: _duration_pb2.Duration
    act_as: _containers.RepeatedScalarFieldContainer[str]
    read_as: _containers.RepeatedScalarFieldContainer[str]
    submission_id: str
    disclosed_contracts: _containers.RepeatedCompositeFieldContainer[DisclosedContract]
    def __init__(self, ledger_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., application_id: _Optional[str] = ..., command_id: _Optional[str] = ..., party: _Optional[str] = ..., commands: _Optional[_Iterable[_Union[Command, _Mapping]]] = ..., deduplication_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., deduplication_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., deduplication_offset: _Optional[str] = ..., min_ledger_time_abs: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., min_ledger_time_rel: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., act_as: _Optional[_Iterable[str]] = ..., read_as: _Optional[_Iterable[str]] = ..., submission_id: _Optional[str] = ..., disclosed_contracts: _Optional[_Iterable[_Union[DisclosedContract, _Mapping]]] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ["create", "exercise", "exerciseByKey", "createAndExercise"]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    EXERCISEBYKEY_FIELD_NUMBER: _ClassVar[int]
    CREATEANDEXERCISE_FIELD_NUMBER: _ClassVar[int]
    create: CreateCommand
    exercise: ExerciseCommand
    exerciseByKey: ExerciseByKeyCommand
    createAndExercise: CreateAndExerciseCommand
    def __init__(self, create: _Optional[_Union[CreateCommand, _Mapping]] = ..., exercise: _Optional[_Union[ExerciseCommand, _Mapping]] = ..., exerciseByKey: _Optional[_Union[ExerciseByKeyCommand, _Mapping]] = ..., createAndExercise: _Optional[_Union[CreateAndExerciseCommand, _Mapping]] = ...) -> None: ...

class CreateCommand(_message.Message):
    __slots__ = ["template_id", "create_arguments"]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    create_arguments: _value_pb2.Record
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., create_arguments: _Optional[_Union[_value_pb2.Record, _Mapping]] = ...) -> None: ...

class ExerciseCommand(_message.Message):
    __slots__ = ["template_id", "contract_id", "choice", "choice_argument"]
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
    __slots__ = ["template_id", "contract_key", "choice", "choice_argument"]
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
    __slots__ = ["template_id", "create_arguments", "choice", "choice_argument"]
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
    __slots__ = ["template_id", "contract_id", "create_arguments", "create_arguments_blob", "metadata"]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_ARGUMENTS_BLOB_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    contract_id: str
    create_arguments: _value_pb2.Record
    create_arguments_blob: _any_pb2.Any
    metadata: _contract_metadata_pb2.ContractMetadata
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., contract_id: _Optional[str] = ..., create_arguments: _Optional[_Union[_value_pb2.Record, _Mapping]] = ..., create_arguments_blob: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., metadata: _Optional[_Union[_contract_metadata_pb2.ContractMetadata, _Mapping]] = ...) -> None: ...
