# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from google.protobuf.empty_pb2 import Empty
from grpc import aio as _grpc_aio

from .sequencer_initialization_service_pb2 import InitRequest as V0InitRequest, InitResponse, TopologyBootstrapRequest
from ..v1.sequencer_initialization_service_pb2 import InitRequest as V1InitRequest
from ..v2.sequencer_initialization_service_pb2 import InitRequest as V2InitRequest

__all__ = [
    "SequencerInitializationServiceStub",
    "TopologyBootstrapServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerInitializationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerInitializationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerInitializationServiceAsyncStub: ...  # type: ignore
    def Init(self, __1: V0InitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[InitResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, InitResponse]]: ...
    def InitV1(self, __1: V1InitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[InitResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, InitResponse]]: ...
    def InitV2(self, __1: V2InitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[InitResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, InitResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerInitializationServiceBlockingStub(SequencerInitializationServiceStub):
    def Init(self, __1: V0InitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> InitResponse: ...
    def InitV1(self, __1: V1InitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> InitResponse: ...
    def InitV2(self, __1: V2InitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> InitResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerInitializationServiceAsyncStub(SequencerInitializationServiceStub):
    def Init(self, __1: V0InitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, InitResponse]: ...  # type: ignore
    def InitV1(self, __1: V1InitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, InitResponse]: ...  # type: ignore
    def InitV2(self, __1: V2InitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, InitResponse]: ...  # type: ignore

# noinspection PyPep8Naming,DuplicatedCode
class TopologyBootstrapServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _TopologyBootstrapServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _TopologyBootstrapServiceAsyncStub: ...  # type: ignore
    def Bootstrap(self, __1: TopologyBootstrapRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[Empty, _grpc_aio.UnaryUnaryCall[_typing.Any, Empty]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _TopologyBootstrapServiceBlockingStub(TopologyBootstrapServiceStub):
    def Bootstrap(self, __1: TopologyBootstrapRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> Empty: ...

# noinspection PyPep8Naming,DuplicatedCode
class _TopologyBootstrapServiceAsyncStub(TopologyBootstrapServiceStub):
    def Bootstrap(self, __1: TopologyBootstrapRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, Empty]: ...  # type: ignore
