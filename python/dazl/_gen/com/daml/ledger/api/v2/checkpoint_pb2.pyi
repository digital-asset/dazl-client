# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Checkpoint(_message.Message):
    __slots__ = ("record_time", "offset")
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    record_time: _timestamp_pb2.Timestamp
    offset: str
    def __init__(self, record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., offset: _Optional[str] = ...) -> None: ...
