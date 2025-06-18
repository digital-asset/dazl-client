# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TopologyQueueStatus(_message.Message):
    __slots__ = ("manager", "dispatcher", "clients")
    MANAGER_FIELD_NUMBER: _ClassVar[int]
    DISPATCHER_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    manager: int
    dispatcher: int
    clients: int
    def __init__(self, manager: _Optional[int] = ..., dispatcher: _Optional[int] = ..., clients: _Optional[int] = ...) -> None: ...

class ComponentStatus(_message.Message):
    __slots__ = ("name", "ok", "degraded", "failed", "fatal")
    class StatusData(_message.Message):
        __slots__ = ("description",)
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        description: str
        def __init__(self, description: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    OK_FIELD_NUMBER: _ClassVar[int]
    DEGRADED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    FATAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    ok: ComponentStatus.StatusData
    degraded: ComponentStatus.StatusData
    failed: ComponentStatus.StatusData
    fatal: ComponentStatus.StatusData
    def __init__(self, name: _Optional[str] = ..., ok: _Optional[_Union[ComponentStatus.StatusData, _Mapping]] = ..., degraded: _Optional[_Union[ComponentStatus.StatusData, _Mapping]] = ..., failed: _Optional[_Union[ComponentStatus.StatusData, _Mapping]] = ..., fatal: _Optional[_Union[ComponentStatus.StatusData, _Mapping]] = ...) -> None: ...

class NotInitialized(_message.Message):
    __slots__ = ("active", "waiting_for_external_input")
    class WaitingForExternalInput(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WAITING_FOR_EXTERNAL_INPUT_UNSPECIFIED: _ClassVar[NotInitialized.WaitingForExternalInput]
        WAITING_FOR_EXTERNAL_INPUT_ID: _ClassVar[NotInitialized.WaitingForExternalInput]
        WAITING_FOR_EXTERNAL_INPUT_NODE_TOPOLOGY: _ClassVar[NotInitialized.WaitingForExternalInput]
        WAITING_FOR_EXTERNAL_INPUT_INITIALIZATION: _ClassVar[NotInitialized.WaitingForExternalInput]
    WAITING_FOR_EXTERNAL_INPUT_UNSPECIFIED: NotInitialized.WaitingForExternalInput
    WAITING_FOR_EXTERNAL_INPUT_ID: NotInitialized.WaitingForExternalInput
    WAITING_FOR_EXTERNAL_INPUT_NODE_TOPOLOGY: NotInitialized.WaitingForExternalInput
    WAITING_FOR_EXTERNAL_INPUT_INITIALIZATION: NotInitialized.WaitingForExternalInput
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    WAITING_FOR_EXTERNAL_INPUT_FIELD_NUMBER: _ClassVar[int]
    active: bool
    waiting_for_external_input: NotInitialized.WaitingForExternalInput
    def __init__(self, active: bool = ..., waiting_for_external_input: _Optional[_Union[NotInitialized.WaitingForExternalInput, str]] = ...) -> None: ...

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
    topology_queues: TopologyQueueStatus
    components: _containers.RepeatedCompositeFieldContainer[ComponentStatus]
    version: str
    def __init__(self, uid: _Optional[str] = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ports: _Optional[_Mapping[str, int]] = ..., active: bool = ..., topology_queues: _Optional[_Union[TopologyQueueStatus, _Mapping]] = ..., components: _Optional[_Iterable[_Union[ComponentStatus, _Mapping]]] = ..., version: _Optional[str] = ...) -> None: ...

class HealthDumpRequest(_message.Message):
    __slots__ = ("chunk_size",)
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    chunk_size: int
    def __init__(self, chunk_size: _Optional[int] = ...) -> None: ...

class HealthDumpResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class SetLogLevelRequest(_message.Message):
    __slots__ = ("level",)
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: str
    def __init__(self, level: _Optional[str] = ...) -> None: ...

class SetLogLevelResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLastErrorsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLastErrorsResponse(_message.Message):
    __slots__ = ("errors",)
    class Error(_message.Message):
        __slots__ = ("trace_id", "message")
        TRACE_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        trace_id: str
        message: str
        def __init__(self, trace_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[GetLastErrorsResponse.Error]
    def __init__(self, errors: _Optional[_Iterable[_Union[GetLastErrorsResponse.Error, _Mapping]]] = ...) -> None: ...

class GetLastErrorTraceRequest(_message.Message):
    __slots__ = ("trace_id",)
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    def __init__(self, trace_id: _Optional[str] = ...) -> None: ...

class GetLastErrorTraceResponse(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, messages: _Optional[_Iterable[str]] = ...) -> None: ...
