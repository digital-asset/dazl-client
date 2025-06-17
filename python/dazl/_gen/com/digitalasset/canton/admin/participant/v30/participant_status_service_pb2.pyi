# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...health.v30 import status_service_pb2 as _status_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParticipantStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConnectedSynchronizer(_message.Message):
    __slots__ = ("synchronizer_id", "health")
    class Health(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEALTH_UNSPECIFIED: _ClassVar[ConnectedSynchronizer.Health]
        HEALTH_HEALTHY: _ClassVar[ConnectedSynchronizer.Health]
        HEALTH_UNHEALTHY: _ClassVar[ConnectedSynchronizer.Health]
    HEALTH_UNSPECIFIED: ConnectedSynchronizer.Health
    HEALTH_HEALTHY: ConnectedSynchronizer.Health
    HEALTH_UNHEALTHY: ConnectedSynchronizer.Health
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    health: ConnectedSynchronizer.Health
    def __init__(self, synchronizer_id: _Optional[str] = ..., health: _Optional[_Union[ConnectedSynchronizer.Health, str]] = ...) -> None: ...

class ParticipantStatusResponse(_message.Message):
    __slots__ = ("status", "not_initialized")
    class ParticipantStatusResponseStatus(_message.Message):
        __slots__ = ("common_status", "connected_synchronizers", "active", "supported_protocol_versions")
        COMMON_STATUS_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_SYNCHRONIZERS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_PROTOCOL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        common_status: _status_service_pb2.Status
        connected_synchronizers: _containers.RepeatedCompositeFieldContainer[ConnectedSynchronizer]
        active: bool
        supported_protocol_versions: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, common_status: _Optional[_Union[_status_service_pb2.Status, _Mapping]] = ..., connected_synchronizers: _Optional[_Iterable[_Union[ConnectedSynchronizer, _Mapping]]] = ..., active: bool = ..., supported_protocol_versions: _Optional[_Iterable[int]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NOT_INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    status: ParticipantStatusResponse.ParticipantStatusResponseStatus
    not_initialized: _status_service_pb2.NotInitialized
    def __init__(self, status: _Optional[_Union[ParticipantStatusResponse.ParticipantStatusResponseStatus, _Mapping]] = ..., not_initialized: _Optional[_Union[_status_service_pb2.NotInitialized, _Mapping]] = ...) -> None: ...
