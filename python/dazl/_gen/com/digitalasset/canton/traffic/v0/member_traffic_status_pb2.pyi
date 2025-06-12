# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MemberTrafficStatus(_message.Message):
    __slots__ = ("member", "total_extra_traffic_limit", "total_extra_traffic_consumed", "top_up_events", "ts")
    class TopUpEvent(_message.Message):
        __slots__ = ("effective_at", "serial", "extra_traffic_limit")
        EFFECTIVE_AT_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        EXTRA_TRAFFIC_LIMIT_FIELD_NUMBER: _ClassVar[int]
        effective_at: _timestamp_pb2.Timestamp
        serial: int
        extra_traffic_limit: int
        def __init__(self, effective_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., serial: _Optional[int] = ..., extra_traffic_limit: _Optional[int] = ...) -> None: ...
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXTRA_TRAFFIC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXTRA_TRAFFIC_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    TOP_UP_EVENTS_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    member: str
    total_extra_traffic_limit: _wrappers_pb2.UInt64Value
    total_extra_traffic_consumed: int
    top_up_events: _containers.RepeatedCompositeFieldContainer[MemberTrafficStatus.TopUpEvent]
    ts: _timestamp_pb2.Timestamp
    def __init__(self, member: _Optional[str] = ..., total_extra_traffic_limit: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., total_extra_traffic_consumed: _Optional[int] = ..., top_up_events: _Optional[_Iterable[_Union[MemberTrafficStatus.TopUpEvent, _Mapping]]] = ..., ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
