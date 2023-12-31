# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import event_pb2 as _event_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionTree(_message.Message):
    __slots__ = ["transaction_id", "command_id", "workflow_id", "effective_at", "offset", "events_by_id", "root_event_ids"]
    class EventsByIdEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TreeEvent
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TreeEvent, _Mapping]] = ...) -> None: ...
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    EVENTS_BY_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_EVENT_IDS_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    command_id: str
    workflow_id: str
    effective_at: _timestamp_pb2.Timestamp
    offset: str
    events_by_id: _containers.MessageMap[str, TreeEvent]
    root_event_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, transaction_id: _Optional[str] = ..., command_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., effective_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., offset: _Optional[str] = ..., events_by_id: _Optional[_Mapping[str, TreeEvent]] = ..., root_event_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class TreeEvent(_message.Message):
    __slots__ = ["created", "exercised"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    EXERCISED_FIELD_NUMBER: _ClassVar[int]
    created: _event_pb2.CreatedEvent
    exercised: _event_pb2.ExercisedEvent
    def __init__(self, created: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ..., exercised: _Optional[_Union[_event_pb2.ExercisedEvent, _Mapping]] = ...) -> None: ...

class Transaction(_message.Message):
    __slots__ = ["transaction_id", "command_id", "workflow_id", "effective_at", "events", "offset"]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    command_id: str
    workflow_id: str
    effective_at: _timestamp_pb2.Timestamp
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    offset: str
    def __init__(self, transaction_id: _Optional[str] = ..., command_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., effective_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ..., offset: _Optional[str] = ...) -> None: ...
