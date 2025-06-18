# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from .... import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Fetch(_message.Message):
    __slots__ = ("lf_version", "contract_id", "package_name", "template_id", "signatories", "stakeholders", "acting_parties", "interface_id")
    LF_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    ACTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    lf_version: str
    contract_id: str
    package_name: str
    template_id: _value_pb2.Identifier
    signatories: _containers.RepeatedScalarFieldContainer[str]
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    acting_parties: _containers.RepeatedScalarFieldContainer[str]
    interface_id: _value_pb2.Identifier
    def __init__(self, lf_version: _Optional[str] = ..., contract_id: _Optional[str] = ..., package_name: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., signatories: _Optional[_Iterable[str]] = ..., stakeholders: _Optional[_Iterable[str]] = ..., acting_parties: _Optional[_Iterable[str]] = ..., interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ...) -> None: ...

class Exercise(_message.Message):
    __slots__ = ("lf_version", "contract_id", "package_name", "template_id", "signatories", "stakeholders", "acting_parties", "interface_id", "choice_id", "chosen_value", "consuming", "children", "exercise_result", "choice_observers")
    LF_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    ACTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHOICE_ID_FIELD_NUMBER: _ClassVar[int]
    CHOSEN_VALUE_FIELD_NUMBER: _ClassVar[int]
    CONSUMING_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_RESULT_FIELD_NUMBER: _ClassVar[int]
    CHOICE_OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    lf_version: str
    contract_id: str
    package_name: str
    template_id: _value_pb2.Identifier
    signatories: _containers.RepeatedScalarFieldContainer[str]
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    acting_parties: _containers.RepeatedScalarFieldContainer[str]
    interface_id: _value_pb2.Identifier
    choice_id: str
    chosen_value: _value_pb2.Value
    consuming: bool
    children: _containers.RepeatedScalarFieldContainer[str]
    exercise_result: _value_pb2.Value
    choice_observers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lf_version: _Optional[str] = ..., contract_id: _Optional[str] = ..., package_name: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., signatories: _Optional[_Iterable[str]] = ..., stakeholders: _Optional[_Iterable[str]] = ..., acting_parties: _Optional[_Iterable[str]] = ..., interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., choice_id: _Optional[str] = ..., chosen_value: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., consuming: bool = ..., children: _Optional[_Iterable[str]] = ..., exercise_result: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., choice_observers: _Optional[_Iterable[str]] = ...) -> None: ...

class Create(_message.Message):
    __slots__ = ("lf_version", "contract_id", "package_name", "template_id", "argument", "signatories", "stakeholders")
    LF_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    lf_version: str
    contract_id: str
    package_name: str
    template_id: _value_pb2.Identifier
    argument: _value_pb2.Value
    signatories: _containers.RepeatedScalarFieldContainer[str]
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lf_version: _Optional[str] = ..., contract_id: _Optional[str] = ..., package_name: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., argument: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., signatories: _Optional[_Iterable[str]] = ..., stakeholders: _Optional[_Iterable[str]] = ...) -> None: ...

class Rollback(_message.Message):
    __slots__ = ("children",)
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, children: _Optional[_Iterable[str]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("create", "fetch", "exercise", "rollback")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    FETCH_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_FIELD_NUMBER: _ClassVar[int]
    create: Create
    fetch: Fetch
    exercise: Exercise
    rollback: Rollback
    def __init__(self, create: _Optional[_Union[Create, _Mapping]] = ..., fetch: _Optional[_Union[Fetch, _Mapping]] = ..., exercise: _Optional[_Union[Exercise, _Mapping]] = ..., rollback: _Optional[_Union[Rollback, _Mapping]] = ...) -> None: ...
