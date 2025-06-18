# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import state_service_pb2 as _state_service_pb2
from . import trace_context_pb2 as _trace_context_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TopologyTransaction(_message.Message):
    __slots__ = ("update_id", "offset", "synchronizer_id", "record_time", "events", "trace_context")
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    offset: int
    synchronizer_id: str
    record_time: _timestamp_pb2.Timestamp
    events: _containers.RepeatedCompositeFieldContainer[TopologyEvent]
    trace_context: _trace_context_pb2.TraceContext
    def __init__(self, update_id: _Optional[str] = ..., offset: _Optional[int] = ..., synchronizer_id: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., events: _Optional[_Iterable[_Union[TopologyEvent, _Mapping]]] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ...) -> None: ...

class TopologyEvent(_message.Message):
    __slots__ = ("participant_authorization_changed", "participant_authorization_revoked", "participant_authorization_added")
    PARTICIPANT_AUTHORIZATION_CHANGED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_AUTHORIZATION_REVOKED_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_AUTHORIZATION_ADDED_FIELD_NUMBER: _ClassVar[int]
    participant_authorization_changed: ParticipantAuthorizationChanged
    participant_authorization_revoked: ParticipantAuthorizationRevoked
    participant_authorization_added: ParticipantAuthorizationAdded
    def __init__(self, participant_authorization_changed: _Optional[_Union[ParticipantAuthorizationChanged, _Mapping]] = ..., participant_authorization_revoked: _Optional[_Union[ParticipantAuthorizationRevoked, _Mapping]] = ..., participant_authorization_added: _Optional[_Union[ParticipantAuthorizationAdded, _Mapping]] = ...) -> None: ...

class ParticipantAuthorizationAdded(_message.Message):
    __slots__ = ("party_id", "participant_id", "participant_permission")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    participant_id: str
    participant_permission: _state_service_pb2.ParticipantPermission
    def __init__(self, party_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., participant_permission: _Optional[_Union[_state_service_pb2.ParticipantPermission, str]] = ...) -> None: ...

class ParticipantAuthorizationChanged(_message.Message):
    __slots__ = ("party_id", "participant_id", "participant_permission")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    participant_id: str
    participant_permission: _state_service_pb2.ParticipantPermission
    def __init__(self, party_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., participant_permission: _Optional[_Union[_state_service_pb2.ParticipantPermission, str]] = ...) -> None: ...

class ParticipantAuthorizationRevoked(_message.Message):
    __slots__ = ("party_id", "participant_id")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    participant_id: str
    def __init__(self, party_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...
