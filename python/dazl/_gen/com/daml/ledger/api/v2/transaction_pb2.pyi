# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import event_pb2 as _event_pb2
from . import trace_context_pb2 as _trace_context_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TreeEvent(_message.Message):
    __slots__ = ("created", "exercised")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    EXERCISED_FIELD_NUMBER: _ClassVar[int]
    created: _event_pb2.CreatedEvent
    exercised: _event_pb2.ExercisedEvent
    def __init__(self, created: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ..., exercised: _Optional[_Union[_event_pb2.ExercisedEvent, _Mapping]] = ...) -> None: ...

class TransactionTree(_message.Message):
    __slots__ = ("update_id", "command_id", "workflow_id", "effective_at", "offset", "events_by_id", "synchronizer_id", "trace_context", "record_time")
    class EventsByIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TreeEvent
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TreeEvent, _Mapping]] = ...) -> None: ...
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    EVENTS_BY_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    command_id: str
    workflow_id: str
    effective_at: _timestamp_pb2.Timestamp
    offset: int
    events_by_id: _containers.MessageMap[int, TreeEvent]
    synchronizer_id: str
    trace_context: _trace_context_pb2.TraceContext
    record_time: _timestamp_pb2.Timestamp
    def __init__(self, update_id: _Optional[str] = ..., command_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., effective_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., offset: _Optional[int] = ..., events_by_id: _Optional[_Mapping[int, TreeEvent]] = ..., synchronizer_id: _Optional[str] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Transaction(_message.Message):
    __slots__ = ("update_id", "command_id", "workflow_id", "effective_at", "events", "offset", "synchronizer_id", "trace_context", "record_time")
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    command_id: str
    workflow_id: str
    effective_at: _timestamp_pb2.Timestamp
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    offset: int
    synchronizer_id: str
    trace_context: _trace_context_pb2.TraceContext
    record_time: _timestamp_pb2.Timestamp
    def __init__(self, update_id: _Optional[str] = ..., command_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., effective_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]] = ..., offset: _Optional[int] = ..., synchronizer_id: _Optional[str] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
