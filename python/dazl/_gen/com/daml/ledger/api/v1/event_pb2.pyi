# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import contract_metadata_pb2 as _contract_metadata_pb2
from . import value_pb2 as _value_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ["created", "archived"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    created: CreatedEvent
    archived: ArchivedEvent
    def __init__(self, created: _Optional[_Union[CreatedEvent, _Mapping]] = ..., archived: _Optional[_Union[ArchivedEvent, _Mapping]] = ...) -> None: ...

class CreatedEvent(_message.Message):
    __slots__ = ["event_id", "contract_id", "template_id", "contract_key", "create_arguments", "create_arguments_blob", "interface_views", "witness_parties", "signatories", "observers", "agreement_text", "metadata"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_KEY_FIELD_NUMBER: _ClassVar[int]
    CREATE_ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_ARGUMENTS_BLOB_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_VIEWS_FIELD_NUMBER: _ClassVar[int]
    WITNESS_PARTIES_FIELD_NUMBER: _ClassVar[int]
    SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    contract_id: str
    template_id: _value_pb2.Identifier
    contract_key: _value_pb2.Value
    create_arguments: _value_pb2.Record
    create_arguments_blob: _any_pb2.Any
    interface_views: _containers.RepeatedCompositeFieldContainer[InterfaceView]
    witness_parties: _containers.RepeatedScalarFieldContainer[str]
    signatories: _containers.RepeatedScalarFieldContainer[str]
    observers: _containers.RepeatedScalarFieldContainer[str]
    agreement_text: _wrappers_pb2.StringValue
    metadata: _contract_metadata_pb2.ContractMetadata
    def __init__(self, event_id: _Optional[str] = ..., contract_id: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., contract_key: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., create_arguments: _Optional[_Union[_value_pb2.Record, _Mapping]] = ..., create_arguments_blob: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., interface_views: _Optional[_Iterable[_Union[InterfaceView, _Mapping]]] = ..., witness_parties: _Optional[_Iterable[str]] = ..., signatories: _Optional[_Iterable[str]] = ..., observers: _Optional[_Iterable[str]] = ..., agreement_text: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Union[_contract_metadata_pb2.ContractMetadata, _Mapping]] = ...) -> None: ...

class InterfaceView(_message.Message):
    __slots__ = ["interface_id", "view_status", "view_value"]
    INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    interface_id: _value_pb2.Identifier
    view_status: _status_pb2.Status
    view_value: _value_pb2.Record
    def __init__(self, interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., view_status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., view_value: _Optional[_Union[_value_pb2.Record, _Mapping]] = ...) -> None: ...

class ArchivedEvent(_message.Message):
    __slots__ = ["event_id", "contract_id", "template_id", "witness_parties"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    WITNESS_PARTIES_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    contract_id: str
    template_id: _value_pb2.Identifier
    witness_parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, event_id: _Optional[str] = ..., contract_id: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., witness_parties: _Optional[_Iterable[str]] = ...) -> None: ...

class ExercisedEvent(_message.Message):
    __slots__ = ["event_id", "contract_id", "template_id", "interface_id", "choice", "choice_argument", "acting_parties", "consuming", "witness_parties", "child_event_ids", "exercise_result"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    CHOICE_FIELD_NUMBER: _ClassVar[int]
    CHOICE_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    ACTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    CONSUMING_FIELD_NUMBER: _ClassVar[int]
    WITNESS_PARTIES_FIELD_NUMBER: _ClassVar[int]
    CHILD_EVENT_IDS_FIELD_NUMBER: _ClassVar[int]
    EXERCISE_RESULT_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    contract_id: str
    template_id: _value_pb2.Identifier
    interface_id: _value_pb2.Identifier
    choice: str
    choice_argument: _value_pb2.Value
    acting_parties: _containers.RepeatedScalarFieldContainer[str]
    consuming: bool
    witness_parties: _containers.RepeatedScalarFieldContainer[str]
    child_event_ids: _containers.RepeatedScalarFieldContainer[str]
    exercise_result: _value_pb2.Value
    def __init__(self, event_id: _Optional[str] = ..., contract_id: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., interface_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., choice: _Optional[str] = ..., choice_argument: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., acting_parties: _Optional[_Iterable[str]] = ..., consuming: bool = ..., witness_parties: _Optional[_Iterable[str]] = ..., child_event_ids: _Optional[_Iterable[str]] = ..., exercise_result: _Optional[_Union[_value_pb2.Value, _Mapping]] = ...) -> None: ...
