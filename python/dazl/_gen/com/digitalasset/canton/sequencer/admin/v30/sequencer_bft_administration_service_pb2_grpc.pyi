# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_bft_administration_service_pb2 import AddPeerEndpointRequest, AddPeerEndpointResponse, GetOrderingTopologyRequest, GetOrderingTopologyResponse, GetPeerNetworkStatusRequest, GetPeerNetworkStatusResponse, RemovePeerEndpointRequest, RemovePeerEndpointResponse

__all__ = [
    "SequencerBftAdministrationServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerBftAdministrationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerBftAdministrationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerBftAdministrationServiceAsyncStub: ...  # type: ignore
    def AddPeerEndpoint(self, __1: AddPeerEndpointRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AddPeerEndpointResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AddPeerEndpointResponse]]: ...
    def RemovePeerEndpoint(self, __1: RemovePeerEndpointRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[RemovePeerEndpointResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, RemovePeerEndpointResponse]]: ...
    def GetPeerNetworkStatus(self, __1: GetPeerNetworkStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetPeerNetworkStatusResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetPeerNetworkStatusResponse]]: ...
    def GetOrderingTopology(self, __1: GetOrderingTopologyRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetOrderingTopologyResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetOrderingTopologyResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerBftAdministrationServiceBlockingStub(SequencerBftAdministrationServiceStub):
    def AddPeerEndpoint(self, __1: AddPeerEndpointRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AddPeerEndpointResponse: ...
    def RemovePeerEndpoint(self, __1: RemovePeerEndpointRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> RemovePeerEndpointResponse: ...
    def GetPeerNetworkStatus(self, __1: GetPeerNetworkStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetPeerNetworkStatusResponse: ...
    def GetOrderingTopology(self, __1: GetOrderingTopologyRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetOrderingTopologyResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerBftAdministrationServiceAsyncStub(SequencerBftAdministrationServiceStub):
    def AddPeerEndpoint(self, __1: AddPeerEndpointRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AddPeerEndpointResponse]: ...  # type: ignore
    def RemovePeerEndpoint(self, __1: RemovePeerEndpointRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, RemovePeerEndpointResponse]: ...  # type: ignore
    def GetPeerNetworkStatus(self, __1: GetPeerNetworkStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetPeerNetworkStatusResponse]: ...  # type: ignore
    def GetOrderingTopology(self, __1: GetOrderingTopologyRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetOrderingTopologyResponse]: ...  # type: ignore
