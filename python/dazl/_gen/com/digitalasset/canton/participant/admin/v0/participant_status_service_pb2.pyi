# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....health.admin.v0 import status_service_pb2 as _status_service_pb2
from ....health.admin.v1 import status_service_pb2 as _status_service_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParticipantStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConnectedDomain(_message.Message):
    __slots__ = ("domain_id", "healthy")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    healthy: bool
    def __init__(self, domain_id: _Optional[str] = ..., healthy: bool = ...) -> None: ...

class ParticipantStatusResponse(_message.Message):
    __slots__ = ("status", "unavailable", "failure")
    class ParticipantStatusResponseStatus(_message.Message):
        __slots__ = ("common_status", "connected_domains", "active", "supported_protocol_versions")
        COMMON_STATUS_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_PROTOCOL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        common_status: _status_service_pb2_1.Status
        connected_domains: _containers.RepeatedCompositeFieldContainer[ConnectedDomain]
        active: bool
        supported_protocol_versions: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, common_status: _Optional[_Union[_status_service_pb2_1.Status, _Mapping]] = ..., connected_domains: _Optional[_Iterable[_Union[ConnectedDomain, _Mapping]]] = ..., active: bool = ..., supported_protocol_versions: _Optional[_Iterable[int]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    status: ParticipantStatusResponse.ParticipantStatusResponseStatus
    unavailable: _status_service_pb2.NodeStatus.NotInitialized
    failure: _status_service_pb2_1.Failure
    def __init__(self, status: _Optional[_Union[ParticipantStatusResponse.ParticipantStatusResponseStatus, _Mapping]] = ..., unavailable: _Optional[_Union[_status_service_pb2.NodeStatus.NotInitialized, _Mapping]] = ..., failure: _Optional[_Union[_status_service_pb2_1.Failure, _Mapping]] = ...) -> None: ...
