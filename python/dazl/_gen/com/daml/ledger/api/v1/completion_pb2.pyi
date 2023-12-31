# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Completion(_message.Message):
    __slots__ = ["command_id", "status", "transaction_id", "application_id", "act_as", "submission_id", "deduplication_offset", "deduplication_duration"]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    command_id: str
    status: _status_pb2.Status
    transaction_id: str
    application_id: str
    act_as: _containers.RepeatedScalarFieldContainer[str]
    submission_id: str
    deduplication_offset: str
    deduplication_duration: _duration_pb2.Duration
    def __init__(self, command_id: _Optional[str] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., transaction_id: _Optional[str] = ..., application_id: _Optional[str] = ..., act_as: _Optional[_Iterable[str]] = ..., submission_id: _Optional[str] = ..., deduplication_offset: _Optional[str] = ..., deduplication_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
