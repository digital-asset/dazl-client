# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddPeerEndpointRequest(_message.Message):
    __slots__ = ("endpoint",)
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: PeerEndpoint
    def __init__(self, endpoint: _Optional[_Union[PeerEndpoint, _Mapping]] = ...) -> None: ...

class RemovePeerEndpointRequest(_message.Message):
    __slots__ = ("endpoint_id",)
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint_id: PeerEndpointId
    def __init__(self, endpoint_id: _Optional[_Union[PeerEndpointId, _Mapping]] = ...) -> None: ...

class PeerEndpoint(_message.Message):
    __slots__ = ("address", "port", "plain_text", "tls")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PLAIN_TEXT_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    plain_text: PlainTextPeerEndpoint
    tls: TlsPeerEndpoint
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ..., plain_text: _Optional[_Union[PlainTextPeerEndpoint, _Mapping]] = ..., tls: _Optional[_Union[TlsPeerEndpoint, _Mapping]] = ...) -> None: ...

class PeerEndpointId(_message.Message):
    __slots__ = ("address", "port", "tls")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    tls: bool
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ..., tls: bool = ...) -> None: ...

class PlainTextPeerEndpoint(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TlsPeerEndpoint(_message.Message):
    __slots__ = ("custom_server_trust_certificate", "client_certificate")
    CUSTOM_SERVER_TRUST_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    custom_server_trust_certificate: bytes
    client_certificate: TlsClientCertificate
    def __init__(self, custom_server_trust_certificate: _Optional[bytes] = ..., client_certificate: _Optional[_Union[TlsClientCertificate, _Mapping]] = ...) -> None: ...

class TlsClientCertificate(_message.Message):
    __slots__ = ("certificate_chain", "private_key_file")
    CERTIFICATE_CHAIN_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FILE_FIELD_NUMBER: _ClassVar[int]
    certificate_chain: bytes
    private_key_file: str
    def __init__(self, certificate_chain: _Optional[bytes] = ..., private_key_file: _Optional[str] = ...) -> None: ...

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

class PeerEndpointHealthStatus(_message.Message):
    __slots__ = ("unknown_endpoint", "unauthenticated", "authenticated")
    class UnknownEndpoint(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Unauthenticated(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Authenticated(_message.Message):
        __slots__ = ("sequencer_id",)
        SEQUENCER_ID_FIELD_NUMBER: _ClassVar[int]
        sequencer_id: str
        def __init__(self, sequencer_id: _Optional[str] = ...) -> None: ...
    UNKNOWN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    UNAUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    unknown_endpoint: PeerEndpointHealthStatus.UnknownEndpoint
    unauthenticated: PeerEndpointHealthStatus.Unauthenticated
    authenticated: PeerEndpointHealthStatus.Authenticated
    def __init__(self, unknown_endpoint: _Optional[_Union[PeerEndpointHealthStatus.UnknownEndpoint, _Mapping]] = ..., unauthenticated: _Optional[_Union[PeerEndpointHealthStatus.Unauthenticated, _Mapping]] = ..., authenticated: _Optional[_Union[PeerEndpointHealthStatus.Authenticated, _Mapping]] = ...) -> None: ...

class PeerEndpointHealth(_message.Message):
    __slots__ = ("status", "description")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    status: PeerEndpointHealthStatus
    description: str
    def __init__(self, status: _Optional[_Union[PeerEndpointHealthStatus, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class PeerEndpointStatus(_message.Message):
    __slots__ = ("endpoint_id", "health")
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    endpoint_id: PeerEndpointId
    health: PeerEndpointHealth
    def __init__(self, endpoint_id: _Optional[_Union[PeerEndpointId, _Mapping]] = ..., health: _Optional[_Union[PeerEndpointHealth, _Mapping]] = ...) -> None: ...

class GetPeerNetworkStatusRequest(_message.Message):
    __slots__ = ("endpoint_ids",)
    ENDPOINT_IDS_FIELD_NUMBER: _ClassVar[int]
    endpoint_ids: _containers.RepeatedCompositeFieldContainer[PeerEndpointId]
    def __init__(self, endpoint_ids: _Optional[_Iterable[_Union[PeerEndpointId, _Mapping]]] = ...) -> None: ...

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
