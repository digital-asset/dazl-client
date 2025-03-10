# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OffsetCheckpoint(_message.Message):
    __slots__ = ("offset", "domain_times")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_TIMES_FIELD_NUMBER: _ClassVar[int]
    offset: int
    domain_times: _containers.RepeatedCompositeFieldContainer[DomainTime]
    def __init__(self, offset: _Optional[int] = ..., domain_times: _Optional[_Iterable[_Union[DomainTime, _Mapping]]] = ...) -> None: ...

class DomainTime(_message.Message):
    __slots__ = ("domain_id", "record_time")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    record_time: _timestamp_pb2.Timestamp
    def __init__(self, domain_id: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
