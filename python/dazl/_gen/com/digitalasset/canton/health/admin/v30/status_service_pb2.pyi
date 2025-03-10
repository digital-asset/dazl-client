# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class StatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ("not_initialized", "success")
    class Status(_message.Message):
        __slots__ = ("id", "uptime", "ports", "extra", "active", "topology_queues", "components")
        class PortsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: int
            def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        UPTIME_FIELD_NUMBER: _ClassVar[int]
        PORTS_FIELD_NUMBER: _ClassVar[int]
        EXTRA_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        TOPOLOGY_QUEUES_FIELD_NUMBER: _ClassVar[int]
        COMPONENTS_FIELD_NUMBER: _ClassVar[int]
        id: str
        uptime: _duration_pb2.Duration
        ports: _containers.ScalarMap[str, int]
        extra: bytes
        active: bool
        topology_queues: TopologyQueueStatus
        components: _containers.RepeatedCompositeFieldContainer[StatusResponse.ComponentStatus]
        def __init__(self, id: _Optional[str] = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ports: _Optional[_Mapping[str, int]] = ..., extra: _Optional[bytes] = ..., active: bool = ..., topology_queues: _Optional[_Union[TopologyQueueStatus, _Mapping]] = ..., components: _Optional[_Iterable[_Union[StatusResponse.ComponentStatus, _Mapping]]] = ...) -> None: ...
    class ComponentStatus(_message.Message):
        __slots__ = ("name", "ok", "degraded", "failed", "fatal")
        class StatusData(_message.Message):
            __slots__ = ("description",)
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            description: _wrappers_pb2.StringValue
            def __init__(self, description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        OK_FIELD_NUMBER: _ClassVar[int]
        DEGRADED_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        FATAL_FIELD_NUMBER: _ClassVar[int]
        name: str
        ok: StatusResponse.ComponentStatus.StatusData
        degraded: StatusResponse.ComponentStatus.StatusData
        failed: StatusResponse.ComponentStatus.StatusData
        fatal: StatusResponse.ComponentStatus.StatusData
        def __init__(self, name: _Optional[str] = ..., ok: _Optional[_Union[StatusResponse.ComponentStatus.StatusData, _Mapping]] = ..., degraded: _Optional[_Union[StatusResponse.ComponentStatus.StatusData, _Mapping]] = ..., failed: _Optional[_Union[StatusResponse.ComponentStatus.StatusData, _Mapping]] = ..., fatal: _Optional[_Union[StatusResponse.ComponentStatus.StatusData, _Mapping]] = ...) -> None: ...
    class NotInitialized(_message.Message):
        __slots__ = ("active", "waiting_for_external_input")
        class WaitingForExternalInput(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WAITING_FOR_EXTERNAL_INPUT_UNSPECIFIED: _ClassVar[StatusResponse.NotInitialized.WaitingForExternalInput]
            WAITING_FOR_EXTERNAL_INPUT_ID: _ClassVar[StatusResponse.NotInitialized.WaitingForExternalInput]
            WAITING_FOR_EXTERNAL_INPUT_NODE_TOPOLOGY: _ClassVar[StatusResponse.NotInitialized.WaitingForExternalInput]
            WAITING_FOR_EXTERNAL_INPUT_INITIALIZATION: _ClassVar[StatusResponse.NotInitialized.WaitingForExternalInput]
        WAITING_FOR_EXTERNAL_INPUT_UNSPECIFIED: StatusResponse.NotInitialized.WaitingForExternalInput
        WAITING_FOR_EXTERNAL_INPUT_ID: StatusResponse.NotInitialized.WaitingForExternalInput
        WAITING_FOR_EXTERNAL_INPUT_NODE_TOPOLOGY: StatusResponse.NotInitialized.WaitingForExternalInput
        WAITING_FOR_EXTERNAL_INPUT_INITIALIZATION: StatusResponse.NotInitialized.WaitingForExternalInput
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        WAITING_FOR_EXTERNAL_INPUT_FIELD_NUMBER: _ClassVar[int]
        active: bool
        waiting_for_external_input: StatusResponse.NotInitialized.WaitingForExternalInput
        def __init__(self, active: bool = ..., waiting_for_external_input: _Optional[_Union[StatusResponse.NotInitialized.WaitingForExternalInput, str]] = ...) -> None: ...
    NOT_INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    not_initialized: StatusResponse.NotInitialized
    success: StatusResponse.Status
    def __init__(self, not_initialized: _Optional[_Union[StatusResponse.NotInitialized, _Mapping]] = ..., success: _Optional[_Union[StatusResponse.Status, _Mapping]] = ...) -> None: ...

class HealthDumpRequest(_message.Message):
    __slots__ = ("chunk_size",)
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    chunk_size: _wrappers_pb2.UInt32Value
    def __init__(self, chunk_size: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class HealthDumpResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class ParticipantStatusInfo(_message.Message):
    __slots__ = ("connected_domains", "active")
    class ConnectedDomain(_message.Message):
        __slots__ = ("domain", "healthy")
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        HEALTHY_FIELD_NUMBER: _ClassVar[int]
        domain: str
        healthy: bool
        def __init__(self, domain: _Optional[str] = ..., healthy: bool = ...) -> None: ...
    CONNECTED_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    connected_domains: _containers.RepeatedCompositeFieldContainer[ParticipantStatusInfo.ConnectedDomain]
    active: bool
    def __init__(self, connected_domains: _Optional[_Iterable[_Union[ParticipantStatusInfo.ConnectedDomain, _Mapping]]] = ..., active: bool = ...) -> None: ...

class SequencerNodeStatus(_message.Message):
    __slots__ = ("connected_participant_uids", "sequencer", "domain_id", "admin")
    CONNECTED_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    connected_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    sequencer: SequencerHealthStatus
    domain_id: str
    admin: SequencerAdminStatus
    def __init__(self, connected_participant_uids: _Optional[_Iterable[str]] = ..., sequencer: _Optional[_Union[SequencerHealthStatus, _Mapping]] = ..., domain_id: _Optional[str] = ..., admin: _Optional[_Union[SequencerAdminStatus, _Mapping]] = ...) -> None: ...

class SequencerHealthStatus(_message.Message):
    __slots__ = ("active", "details")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    active: bool
    details: _wrappers_pb2.StringValue
    def __init__(self, active: bool = ..., details: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class SequencerAdminStatus(_message.Message):
    __slots__ = ("accepts_admin_changes",)
    ACCEPTS_ADMIN_CHANGES_FIELD_NUMBER: _ClassVar[int]
    accepts_admin_changes: bool
    def __init__(self, accepts_admin_changes: bool = ...) -> None: ...

class MediatorNodeStatus(_message.Message):
    __slots__ = ("domain_id",)
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    def __init__(self, domain_id: _Optional[str] = ...) -> None: ...

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
