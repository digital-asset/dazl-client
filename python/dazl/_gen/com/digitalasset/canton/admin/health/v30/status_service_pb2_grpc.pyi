# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .status_service_pb2 import HealthDumpRequest, HealthDumpResponse, SetLogLevelRequest, SetLogLevelResponse

__all__ = [
    "StatusServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class StatusServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _StatusServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _StatusServiceAsyncStub: ...  # type: ignore
    def HealthDump(self, __1: HealthDumpRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[HealthDumpResponse] | _grpc_aio.UnaryStreamCall[_typing.Any, HealthDumpResponse]: ...
    def SetLogLevel(self, __1: SetLogLevelRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SetLogLevelResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, SetLogLevelResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _StatusServiceBlockingStub(StatusServiceStub):
    def HealthDump(self, __1: HealthDumpRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[HealthDumpResponse]: ...
    def SetLogLevel(self, __1: SetLogLevelRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SetLogLevelResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _StatusServiceAsyncStub(StatusServiceStub):
    def HealthDump(self, __1: HealthDumpRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, HealthDumpResponse]: ...  # type: ignore
    def SetLogLevel(self, __1: SetLogLevelRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SetLogLevelResponse]: ...  # type: ignore
