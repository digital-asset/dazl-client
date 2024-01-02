# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FetchTimeRequest(_message.Message):
    __slots__ = ["domain_id", "freshness_bound"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    FRESHNESS_BOUND_FIELD_NUMBER: _ClassVar[int]
    domain_id: _wrappers_pb2.StringValue
    freshness_bound: _duration_pb2.Duration
    def __init__(self, domain_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., freshness_bound: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class FetchTimeResponse(_message.Message):
    __slots__ = ["timestamp"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AwaitTimeRequest(_message.Message):
    __slots__ = ["domain_id", "timestamp"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    domain_id: _wrappers_pb2.StringValue
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, domain_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
