# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v0 import status_service_pb2 as _status_service_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Failure(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    def __init__(self, error_message: _Optional[str] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("uid", "uptime", "ports", "active", "topology_queues", "components", "version")
    class PortsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    UID_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_QUEUES_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    uid: str
    uptime: _duration_pb2.Duration
    ports: _containers.ScalarMap[str, int]
    active: bool
    topology_queues: _status_service_pb2.TopologyQueueStatus
    components: _containers.RepeatedCompositeFieldContainer[_status_service_pb2.NodeStatus.ComponentStatus]
    version: str
    def __init__(self, uid: _Optional[str] = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ports: _Optional[_Mapping[str, int]] = ..., active: bool = ..., topology_queues: _Optional[_Union[_status_service_pb2.TopologyQueueStatus, _Mapping]] = ..., components: _Optional[_Iterable[_Union[_status_service_pb2.NodeStatus.ComponentStatus, _Mapping]]] = ..., version: _Optional[str] = ...) -> None: ...
