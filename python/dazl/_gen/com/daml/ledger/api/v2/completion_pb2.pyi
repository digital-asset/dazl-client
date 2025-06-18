# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import offset_checkpoint_pb2 as _offset_checkpoint_pb2
from . import trace_context_pb2 as _trace_context_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Completion(_message.Message):
    __slots__ = ("command_id", "status", "update_id", "user_id", "act_as", "submission_id", "deduplication_offset", "deduplication_duration", "trace_context", "offset", "synchronizer_time")
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_TIME_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    status: _status_pb2.Status
    update_id: str
    user_id: str
    act_as: _containers.RepeatedScalarFieldContainer[str]
    submission_id: str
    deduplication_offset: int
    deduplication_duration: _duration_pb2.Duration
    trace_context: _trace_context_pb2.TraceContext
    offset: int
    synchronizer_time: _offset_checkpoint_pb2.SynchronizerTime
    def __init__(self, command_id: _Optional[str] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., update_id: _Optional[str] = ..., user_id: _Optional[str] = ..., act_as: _Optional[_Iterable[str]] = ..., submission_id: _Optional[str] = ..., deduplication_offset: _Optional[int] = ..., deduplication_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ..., offset: _Optional[int] = ..., synchronizer_time: _Optional[_Union[_offset_checkpoint_pb2.SynchronizerTime, _Mapping]] = ...) -> None: ...
