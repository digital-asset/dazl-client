# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PingRequest(_message.Message):
    __slots__ = ("target_parties", "validators", "timeout", "levels", "synchronizer_id", "workflow_id", "id")
    TARGET_PARTIES_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    target_parties: _containers.RepeatedScalarFieldContainer[str]
    validators: _containers.RepeatedScalarFieldContainer[str]
    timeout: _duration_pb2.Duration
    levels: int
    synchronizer_id: str
    workflow_id: str
    id: str
    def __init__(self, target_parties: _Optional[_Iterable[str]] = ..., validators: _Optional[_Iterable[str]] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., levels: _Optional[int] = ..., synchronizer_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class PingSuccess(_message.Message):
    __slots__ = ("ping_time", "responder")
    PING_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONDER_FIELD_NUMBER: _ClassVar[int]
    ping_time: int
    responder: str
    def __init__(self, ping_time: _Optional[int] = ..., responder: _Optional[str] = ...) -> None: ...

class PingFailure(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ("success", "failure")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: PingSuccess
    failure: PingFailure
    def __init__(self, success: _Optional[_Union[PingSuccess, _Mapping]] = ..., failure: _Optional[_Union[PingFailure, _Mapping]] = ...) -> None: ...
