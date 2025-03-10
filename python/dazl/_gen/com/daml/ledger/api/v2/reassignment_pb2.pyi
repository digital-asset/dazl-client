# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import event_pb2 as _event_pb2
from . import trace_context_pb2 as _trace_context_pb2
from . import value_pb2 as _value_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Reassignment(_message.Message):
    __slots__ = ("update_id", "command_id", "workflow_id", "offset", "unassigned_event", "assigned_event", "trace_context", "record_time")
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNED_EVENT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_EVENT_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    command_id: str
    workflow_id: str
    offset: int
    unassigned_event: UnassignedEvent
    assigned_event: AssignedEvent
    trace_context: _trace_context_pb2.TraceContext
    record_time: _timestamp_pb2.Timestamp
    def __init__(self, update_id: _Optional[str] = ..., command_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., offset: _Optional[int] = ..., unassigned_event: _Optional[_Union[UnassignedEvent, _Mapping]] = ..., assigned_event: _Optional[_Union[AssignedEvent, _Mapping]] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UnassignedEvent(_message.Message):
    __slots__ = ("unassign_id", "contract_id", "template_id", "source", "target", "submitter", "reassignment_counter", "assignment_exclusivity", "witness_parties", "package_name")
    UNASSIGN_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    WITNESS_PARTIES_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    unassign_id: str
    contract_id: str
    template_id: _value_pb2.Identifier
    source: str
    target: str
    submitter: str
    reassignment_counter: int
    assignment_exclusivity: _timestamp_pb2.Timestamp
    witness_parties: _containers.RepeatedScalarFieldContainer[str]
    package_name: str
    def __init__(self, unassign_id: _Optional[str] = ..., contract_id: _Optional[str] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., source: _Optional[str] = ..., target: _Optional[str] = ..., submitter: _Optional[str] = ..., reassignment_counter: _Optional[int] = ..., assignment_exclusivity: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., witness_parties: _Optional[_Iterable[str]] = ..., package_name: _Optional[str] = ...) -> None: ...

class AssignedEvent(_message.Message):
    __slots__ = ("source", "target", "unassign_id", "submitter", "reassignment_counter", "created_event")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    UNASSIGN_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_EVENT_FIELD_NUMBER: _ClassVar[int]
    source: str
    target: str
    unassign_id: str
    submitter: str
    reassignment_counter: int
    created_event: _event_pb2.CreatedEvent
    def __init__(self, source: _Optional[str] = ..., target: _Optional[str] = ..., unassign_id: _Optional[str] = ..., submitter: _Optional[str] = ..., reassignment_counter: _Optional[int] = ..., created_event: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ...) -> None: ...
