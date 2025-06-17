# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FetchTimeRequest(_message.Message):
    __slots__ = ("synchronizer_id", "freshness_bound")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_BOUND_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    freshness_bound: _duration_pb2.Duration
    def __init__(self, synchronizer_id: _Optional[str] = ..., freshness_bound: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class FetchTimeResponse(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AwaitTimeRequest(_message.Message):
    __slots__ = ("synchronizer_id", "timestamp")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, synchronizer_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AwaitTimeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
