# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OffsetCheckpoint(_message.Message):
    __slots__ = ("offset", "synchronizer_times")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_TIMES_FIELD_NUMBER: _ClassVar[int]
    offset: int
    synchronizer_times: _containers.RepeatedCompositeFieldContainer[SynchronizerTime]
    def __init__(self, offset: _Optional[int] = ..., synchronizer_times: _Optional[_Iterable[_Union[SynchronizerTime, _Mapping]]] = ...) -> None: ...

class SynchronizerTime(_message.Message):
    __slots__ = ("synchronizer_id", "record_time")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    record_time: _timestamp_pb2.Timestamp
    def __init__(self, synchronizer_id: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
