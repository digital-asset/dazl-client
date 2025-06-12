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

class SequencerStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SequencerStatusResponse(_message.Message):
    __slots__ = ("status", "unavailable", "failure")
    class SequencerStatusResponseStatus(_message.Message):
        __slots__ = ("common_status", "connected_participants_uid", "connected_mediators_uid", "sequencer", "domain_id", "admin", "protocol_version")
        COMMON_STATUS_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_PARTICIPANTS_UID_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_MEDIATORS_UID_FIELD_NUMBER: _ClassVar[int]
        SEQUENCER_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        ADMIN_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        common_status: _status_service_pb2_1.Status
        connected_participants_uid: _containers.RepeatedScalarFieldContainer[str]
        connected_mediators_uid: _containers.RepeatedScalarFieldContainer[str]
        sequencer: _status_service_pb2.SequencerHealthStatus
        domain_id: str
        admin: _status_service_pb2.SequencerAdminStatus
        protocol_version: int
        def __init__(self, common_status: _Optional[_Union[_status_service_pb2_1.Status, _Mapping]] = ..., connected_participants_uid: _Optional[_Iterable[str]] = ..., connected_mediators_uid: _Optional[_Iterable[str]] = ..., sequencer: _Optional[_Union[_status_service_pb2.SequencerHealthStatus, _Mapping]] = ..., domain_id: _Optional[str] = ..., admin: _Optional[_Union[_status_service_pb2.SequencerAdminStatus, _Mapping]] = ..., protocol_version: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    status: SequencerStatusResponse.SequencerStatusResponseStatus
    unavailable: _status_service_pb2.NodeStatus.NotInitialized
    failure: _status_service_pb2_1.Failure
    def __init__(self, status: _Optional[_Union[SequencerStatusResponse.SequencerStatusResponseStatus, _Mapping]] = ..., unavailable: _Optional[_Union[_status_service_pb2.NodeStatus.NotInitialized, _Mapping]] = ..., failure: _Optional[_Union[_status_service_pb2_1.Failure, _Mapping]] = ...) -> None: ...
