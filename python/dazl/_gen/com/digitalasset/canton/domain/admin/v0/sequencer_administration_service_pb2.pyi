# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....traffic.v0 import member_traffic_status_pb2 as _member_traffic_status_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerMemberStatus(_message.Message):
    __slots__ = ["member", "registered_at", "last_acknowledged", "enabled"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    member: str
    registered_at: _timestamp_pb2.Timestamp
    last_acknowledged: _timestamp_pb2.Timestamp
    enabled: bool
    def __init__(self, member: _Optional[str] = ..., registered_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_acknowledged: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., enabled: bool = ...) -> None: ...

class SequencerPruningStatus(_message.Message):
    __slots__ = ["now", "earliest_event_timestamp", "members"]
    NOW_FIELD_NUMBER: _ClassVar[int]
    EARLIEST_EVENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    now: _timestamp_pb2.Timestamp
    earliest_event_timestamp: _timestamp_pb2.Timestamp
    members: _containers.RepeatedCompositeFieldContainer[SequencerMemberStatus]
    def __init__(self, now: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., earliest_event_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., members: _Optional[_Iterable[_Union[SequencerMemberStatus, _Mapping]]] = ...) -> None: ...

class TrafficControlStateRequest(_message.Message):
    __slots__ = ["members"]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, members: _Optional[_Iterable[str]] = ...) -> None: ...

class TrafficControlStateResponse(_message.Message):
    __slots__ = ["traffic_states"]
    TRAFFIC_STATES_FIELD_NUMBER: _ClassVar[int]
    traffic_states: _containers.RepeatedCompositeFieldContainer[_member_traffic_status_pb2.MemberTrafficStatus]
    def __init__(self, traffic_states: _Optional[_Iterable[_Union[_member_traffic_status_pb2.MemberTrafficStatus, _Mapping]]] = ...) -> None: ...
