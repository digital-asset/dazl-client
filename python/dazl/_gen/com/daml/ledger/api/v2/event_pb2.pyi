# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import value_pb2 as _value_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ("created", "archived", "exercised")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    EXERCISED_FIELD_NUMBER: _ClassVar[int]
    created: CreatedEvent
    archived: ArchivedEvent
    exercised: ExercisedEvent
    def __init__(self, created: _Optional[_Union[CreatedEvent, _Mapping]] = ..., archived: _Optional[_Union[ArchivedEvent, _Mapping]] = ..., exercised: _Optional[_Union[ExercisedEvent, _Mapping]] = ...) -> None: ...

class CreatedEvent(_message.Message):
    __slots__ = ("offset", "node_id", "contract_id", "template_id", "contract_key", "create_arguments", "created_event_blob", "interface_views", "witness_parties", "signatories", "observers", "created_at", "package_name")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATE_ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_EVENT_BLOB_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VIEWS_FIELD_NUMBER: _ClassVar[int]
    WITNESS_PARTIES_FIELD_NUMBER: _ClassVar[int]
    SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    offset: int
    node_id: int
    contract_id: str
    template_id: _value_pb2.Identifier
    contract_key: _value_pb2.Value
    create_arguments: _value_pb2.Record
    created_event_blob: bytes
    interface_views: _containers.RepeatedCompositeFieldContainer[InterfaceView]
    witness_parties: _containers.RepeatedScalarFieldContainer[str]
    signatories: _containers.RepeatedScalarFieldContainer[str]
    observers: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    package_name: str
    def __init__(self, offset: _Optional[int] = ..., node_id: _Optional[int] = ..., contract_id: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., contract_key: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., create_arguments: _Optional[_Union[_value_pb2.Record, _Mapping]] = ..., created_event_blob: _Optional[bytes] = ..., interface_views: _Optional[_Iterable[_Union[InterfaceView, _Mapping]]] = ..., witness_parties: _Optional[_Iterable[str]] = ..., signatories: _Optional[_Iterable[str]] = ..., observers: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., package_name: _Optional[str] = ...) -> None: ...

class InterfaceView(_message.Message):
    __slots__ = ("interface_id", "view_status", "view_value")
    INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    interface_id: _value_pb2.Identifier
    view_status: _status_pb2.Status
    view_value: _value_pb2.Record
    def __init__(self, interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., view_status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., view_value: _Optional[_Union[_value_pb2.Record, _Mapping]] = ...) -> None: ...

class ArchivedEvent(_message.Message):
    __slots__ = ("offset", "node_id", "contract_id", "template_id", "witness_parties", "package_name", "implemented_interfaces")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    WITNESS_PARTIES_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTED_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    offset: int
    node_id: int
    contract_id: str
    template_id: _value_pb2.Identifier
    witness_parties: _containers.RepeatedScalarFieldContainer[str]
    package_name: str
    implemented_interfaces: _containers.RepeatedCompositeFieldContainer[_value_pb2.Identifier]
    def __init__(self, offset: _Optional[int] = ..., node_id: _Optional[int] = ..., contract_id: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., witness_parties: _Optional[_Iterable[str]] = ..., package_name: _Optional[str] = ..., implemented_interfaces: _Optional[_Iterable[_Union[_value_pb2.Identifier, _Mapping]]] = ...) -> None: ...

class ExercisedEvent(_message.Message):
    __slots__ = ("offset", "node_id", "contract_id", "template_id", "interface_id", "choice", "choice_argument", "acting_parties", "consuming", "witness_parties", "last_descendant_node_id", "exercise_result", "package_name", "implemented_interfaces")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHOICE_FIELD_NUMBER: _ClassVar[int]
    CHOICE_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    ACTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    CONSUMING_FIELD_NUMBER: _ClassVar[int]
    WITNESS_PARTIES_FIELD_NUMBER: _ClassVar[int]
    LAST_DESCENDANT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_RESULT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTED_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    offset: int
    node_id: int
    contract_id: str
    template_id: _value_pb2.Identifier
    interface_id: _value_pb2.Identifier
    choice: str
    choice_argument: _value_pb2.Value
    acting_parties: _containers.RepeatedScalarFieldContainer[str]
    consuming: bool
    witness_parties: _containers.RepeatedScalarFieldContainer[str]
    last_descendant_node_id: int
    exercise_result: _value_pb2.Value
    package_name: str
    implemented_interfaces: _containers.RepeatedCompositeFieldContainer[_value_pb2.Identifier]
    def __init__(self, offset: _Optional[int] = ..., node_id: _Optional[int] = ..., contract_id: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., choice: _Optional[str] = ..., choice_argument: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., acting_parties: _Optional[_Iterable[str]] = ..., consuming: bool = ..., witness_parties: _Optional[_Iterable[str]] = ..., last_descendant_node_id: _Optional[int] = ..., exercise_result: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., package_name: _Optional[str] = ..., implemented_interfaces: _Optional[_Iterable[_Union[_value_pb2.Identifier, _Mapping]]] = ...) -> None: ...
