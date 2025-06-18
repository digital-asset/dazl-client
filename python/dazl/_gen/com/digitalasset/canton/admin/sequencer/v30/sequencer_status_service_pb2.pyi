# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...health.v30 import status_service_pb2 as _status_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencerStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SequencerStatusResponse(_message.Message):
    __slots__ = ("status", "not_initialized")
    class ConnectedParticipant(_message.Message):
        __slots__ = ("uid",)
        UID_FIELD_NUMBER: _ClassVar[int]
        uid: str
        def __init__(self, uid: _Optional[str] = ...) -> None: ...
    class ConnectedMediator(_message.Message):
        __slots__ = ("uid",)
        UID_FIELD_NUMBER: _ClassVar[int]
        uid: str
        def __init__(self, uid: _Optional[str] = ...) -> None: ...
    class SequencerStatusResponseStatus(_message.Message):
        __slots__ = ("common_status", "connected_participants", "connected_mediators", "sequencer", "synchronizer_id", "admin", "protocol_version")
        COMMON_STATUS_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_MEDIATORS_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        ADMIN_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        common_status: _status_service_pb2.Status
        connected_participants: _containers.RepeatedCompositeFieldContainer[SequencerStatusResponse.ConnectedParticipant]
        connected_mediators: _containers.RepeatedCompositeFieldContainer[SequencerStatusResponse.ConnectedMediator]
        sequencer: SequencerHealthStatus
        synchronizer_id: str
        admin: SequencerAdminStatus
        protocol_version: int
        def __init__(self, common_status: _Optional[_Union[_status_service_pb2.Status, _Mapping]] = ..., connected_participants: _Optional[_Iterable[_Union[SequencerStatusResponse.ConnectedParticipant, _Mapping]]] = ..., connected_mediators: _Optional[_Iterable[_Union[SequencerStatusResponse.ConnectedMediator, _Mapping]]] = ..., sequencer: _Optional[_Union[SequencerHealthStatus, _Mapping]] = ..., synchronizer_id: _Optional[str] = ..., admin: _Optional[_Union[SequencerAdminStatus, _Mapping]] = ..., protocol_version: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NOT_INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    status: SequencerStatusResponse.SequencerStatusResponseStatus
    not_initialized: _status_service_pb2.NotInitialized
    def __init__(self, status: _Optional[_Union[SequencerStatusResponse.SequencerStatusResponseStatus, _Mapping]] = ..., not_initialized: _Optional[_Union[_status_service_pb2.NotInitialized, _Mapping]] = ...) -> None: ...

class SequencerHealthStatus(_message.Message):
    __slots__ = ("active", "details")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    active: bool
    details: str
    def __init__(self, active: bool = ..., details: _Optional[str] = ...) -> None: ...

class SequencerAdminStatus(_message.Message):
    __slots__ = ("accepts_admin_changes",)
    ACCEPTS_ADMIN_CHANGES_FIELD_NUMBER: _ClassVar[int]
    accepts_admin_changes: bool
    def __init__(self, accepts_admin_changes: bool = ...) -> None: ...
