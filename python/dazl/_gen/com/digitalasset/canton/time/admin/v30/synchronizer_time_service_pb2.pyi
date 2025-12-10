# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ....topology.admin.v30 import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FetchTimeRequest(_message.Message):
    __slots__ = ("synchronizer", "freshness_bound")
    SYNCHRONIZER_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_BOUND_FIELD_NUMBER: _ClassVar[int]
    synchronizer: _common_pb2.Synchronizer
    freshness_bound: _duration_pb2.Duration
    def __init__(self, synchronizer: _Optional[_Union[_common_pb2.Synchronizer, _Mapping]] = ..., freshness_bound: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class FetchTimeResponse(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AwaitTimeRequest(_message.Message):
    __slots__ = ("synchronizer", "timestamp")
    SYNCHRONIZER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    synchronizer: _common_pb2.Synchronizer
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, synchronizer: _Optional[_Union[_common_pb2.Synchronizer, _Mapping]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AwaitTimeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
