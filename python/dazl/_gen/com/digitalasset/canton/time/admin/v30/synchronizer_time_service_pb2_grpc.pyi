# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .synchronizer_time_service_pb2 import AwaitTimeRequest, AwaitTimeResponse, FetchTimeRequest, FetchTimeResponse

__all__ = [
    "SynchronizerTimeServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SynchronizerTimeServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SynchronizerTimeServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SynchronizerTimeServiceAsyncStub: ...  # type: ignore
    def FetchTime(self, __1: FetchTimeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[FetchTimeResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, FetchTimeResponse]]: ...
    def AwaitTime(self, __1: AwaitTimeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AwaitTimeResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AwaitTimeResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SynchronizerTimeServiceBlockingStub(SynchronizerTimeServiceStub):
    def FetchTime(self, __1: FetchTimeRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> FetchTimeResponse: ...
    def AwaitTime(self, __1: AwaitTimeRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AwaitTimeResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SynchronizerTimeServiceAsyncStub(SynchronizerTimeServiceStub):
    def FetchTime(self, __1: FetchTimeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, FetchTimeResponse]: ...  # type: ignore
    def AwaitTime(self, __1: AwaitTimeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AwaitTimeResponse]: ...  # type: ignore
