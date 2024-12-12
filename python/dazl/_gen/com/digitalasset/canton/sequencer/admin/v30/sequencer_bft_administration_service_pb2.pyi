# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PeerEndpointHealthStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PEER_ENDPOINT_HEALTH_STATUS_UNSPECIFIED: _ClassVar[PeerEndpointHealthStatus]
    PEER_ENDPOINT_HEALTH_STATUS_UNKNOWN_ENDPOINT: _ClassVar[PeerEndpointHealthStatus]
    PEER_ENDPOINT_HEALTH_STATUS_UNAUTHENTICATED: _ClassVar[PeerEndpointHealthStatus]
    PEER_ENDPOINT_HEALTH_STATUS_AUTHENTICATED: _ClassVar[PeerEndpointHealthStatus]
PEER_ENDPOINT_HEALTH_STATUS_UNSPECIFIED: PeerEndpointHealthStatus
PEER_ENDPOINT_HEALTH_STATUS_UNKNOWN_ENDPOINT: PeerEndpointHealthStatus
PEER_ENDPOINT_HEALTH_STATUS_UNAUTHENTICATED: PeerEndpointHealthStatus
PEER_ENDPOINT_HEALTH_STATUS_AUTHENTICATED: PeerEndpointHealthStatus

class AddPeerEndpointRequest(_message.Message):
    __slots__ = ("endpoint",)
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: PeerEndpoint
    def __init__(self, endpoint: _Optional[_Union[PeerEndpoint, _Mapping]] = ...) -> None: ...

class RemovePeerEndpointRequest(_message.Message):
    __slots__ = ("endpoint",)
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: PeerEndpoint
    def __init__(self, endpoint: _Optional[_Union[PeerEndpoint, _Mapping]] = ...) -> None: ...

class PeerEndpoint(_message.Message):
    __slots__ = ("host", "port")
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class AddPeerEndpointResponse(_message.Message):
    __slots__ = ("added",)
    ADDED_FIELD_NUMBER: _ClassVar[int]
    added: bool
    def __init__(self, added: bool = ...) -> None: ...

class RemovePeerEndpointResponse(_message.Message):
    __slots__ = ("removed",)
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    removed: bool
    def __init__(self, removed: bool = ...) -> None: ...

class PeerEndpointHealth(_message.Message):
    __slots__ = ("status", "description")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    status: PeerEndpointHealthStatus
    description: _wrappers_pb2.StringValue
    def __init__(self, status: _Optional[_Union[PeerEndpointHealthStatus, str]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class PeerEndpointStatus(_message.Message):
    __slots__ = ("endpoint", "health")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    endpoint: PeerEndpoint
    health: PeerEndpointHealth
    def __init__(self, endpoint: _Optional[_Union[PeerEndpoint, _Mapping]] = ..., health: _Optional[_Union[PeerEndpointHealth, _Mapping]] = ...) -> None: ...

class GetPeerNetworkStatusRequest(_message.Message):
    __slots__ = ("endpoints",)
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[PeerEndpoint]
    def __init__(self, endpoints: _Optional[_Iterable[_Union[PeerEndpoint, _Mapping]]] = ...) -> None: ...

class GetPeerNetworkStatusResponse(_message.Message):
    __slots__ = ("statuses",)
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedCompositeFieldContainer[PeerEndpointStatus]
    def __init__(self, statuses: _Optional[_Iterable[_Union[PeerEndpointStatus, _Mapping]]] = ...) -> None: ...

class GetOrderingTopologyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOrderingTopologyResponse(_message.Message):
    __slots__ = ("current_epoch", "sequencer_ids")
    CURRENT_EPOCH_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_IDS_FIELD_NUMBER: _ClassVar[int]
    current_epoch: int
    sequencer_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, current_epoch: _Optional[int] = ..., sequencer_ids: _Optional[_Iterable[str]] = ...) -> None: ...
