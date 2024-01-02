# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TopologyQueueStatus(_message.Message):
    __slots__ = ["manager", "dispatcher", "clients"]
    MANAGER_FIELD_NUMBER: _ClassVar[int]
    DISPATCHER_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    manager: int
    dispatcher: int
    clients: int
    def __init__(self, manager: _Optional[int] = ..., dispatcher: _Optional[int] = ..., clients: _Optional[int] = ...) -> None: ...

class NodeStatus(_message.Message):
    __slots__ = ["not_initialized", "success"]
    class Status(_message.Message):
        __slots__ = ["id", "uptime", "ports", "extra", "active", "topology_queues", "components"]
        class PortsEntry(_message.Message):
            __slots__ = ["key", "value"]
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
        components: _containers.RepeatedCompositeFieldContainer[NodeStatus.ComponentStatus]
        def __init__(self, id: _Optional[str] = ..., uptime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ports: _Optional[_Mapping[str, int]] = ..., extra: _Optional[bytes] = ..., active: bool = ..., topology_queues: _Optional[_Union[TopologyQueueStatus, _Mapping]] = ..., components: _Optional[_Iterable[_Union[NodeStatus.ComponentStatus, _Mapping]]] = ...) -> None: ...
    class ComponentStatus(_message.Message):
        __slots__ = ["name", "ok", "degraded", "failed"]
        class StatusData(_message.Message):
            __slots__ = ["description"]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            description: _wrappers_pb2.StringValue
            def __init__(self, description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        OK_FIELD_NUMBER: _ClassVar[int]
        DEGRADED_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        name: str
        ok: NodeStatus.ComponentStatus.StatusData
        degraded: NodeStatus.ComponentStatus.StatusData
        failed: NodeStatus.ComponentStatus.StatusData
        def __init__(self, name: _Optional[str] = ..., ok: _Optional[_Union[NodeStatus.ComponentStatus.StatusData, _Mapping]] = ..., degraded: _Optional[_Union[NodeStatus.ComponentStatus.StatusData, _Mapping]] = ..., failed: _Optional[_Union[NodeStatus.ComponentStatus.StatusData, _Mapping]] = ...) -> None: ...
    class NotInitialized(_message.Message):
        __slots__ = ["active"]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        active: bool
        def __init__(self, active: bool = ...) -> None: ...
    NOT_INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    not_initialized: NodeStatus.NotInitialized
    success: NodeStatus.Status
    def __init__(self, not_initialized: _Optional[_Union[NodeStatus.NotInitialized, _Mapping]] = ..., success: _Optional[_Union[NodeStatus.Status, _Mapping]] = ...) -> None: ...

class HealthDumpRequest(_message.Message):
    __slots__ = ["chunkSize"]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    chunkSize: _wrappers_pb2.UInt32Value
    def __init__(self, chunkSize: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class HealthDumpChunk(_message.Message):
    __slots__ = ["chunk"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class DomainStatusInfo(_message.Message):
    __slots__ = ["connected_participants", "sequencer"]
    CONNECTED_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    connected_participants: _containers.RepeatedScalarFieldContainer[str]
    sequencer: SequencerHealthStatus
    def __init__(self, connected_participants: _Optional[_Iterable[str]] = ..., sequencer: _Optional[_Union[SequencerHealthStatus, _Mapping]] = ...) -> None: ...

class ParticipantStatusInfo(_message.Message):
    __slots__ = ["connected_domains", "active"]
    class ConnectedDomain(_message.Message):
        __slots__ = ["domain", "healthy"]
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
    __slots__ = ["connected_participants", "sequencer", "domain_id"]
    CONNECTED_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    connected_participants: _containers.RepeatedScalarFieldContainer[str]
    sequencer: SequencerHealthStatus
    domain_id: str
    def __init__(self, connected_participants: _Optional[_Iterable[str]] = ..., sequencer: _Optional[_Union[SequencerHealthStatus, _Mapping]] = ..., domain_id: _Optional[str] = ...) -> None: ...

class SequencerHealthStatus(_message.Message):
    __slots__ = ["active", "details"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    active: bool
    details: _wrappers_pb2.StringValue
    def __init__(self, active: bool = ..., details: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class MediatorNodeStatus(_message.Message):
    __slots__ = ["domain_id"]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    def __init__(self, domain_id: _Optional[str] = ...) -> None: ...
