# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .bft_ordering_service_pb2 import BftOrderingServiceReceiveRequest, BftOrderingServiceReceiveResponse, PingRequest, PingResponse

__all__ = [
    "BftOrderingServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class BftOrderingServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _BftOrderingServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _BftOrderingServiceAsyncStub: ...  # type: ignore
    def Ping(self, __1: PingRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[PingResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, PingResponse]]: ...
    def Receive(self, __1: _typing.Iterable[BftOrderingServiceReceiveRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[BftOrderingServiceReceiveResponse], _grpc_aio.UnaryStreamCall[_typing.Any, BftOrderingServiceReceiveResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _BftOrderingServiceBlockingStub(BftOrderingServiceStub):
    def Ping(self, __1: PingRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> PingResponse: ...
    def Receive(self, __1: _typing.Iterable[BftOrderingServiceReceiveRequest], timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[BftOrderingServiceReceiveResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _BftOrderingServiceAsyncStub(BftOrderingServiceStub):
    def Ping(self, __1: PingRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, PingResponse]: ...  # type: ignore
    def Receive(self, __1: _typing.Iterable[BftOrderingServiceReceiveRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, BftOrderingServiceReceiveResponse]: ...  # type: ignore
