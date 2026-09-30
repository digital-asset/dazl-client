# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .jose_service_pb2 import GetJwksRequest, GetJwksResponse

__all__ = [
    "JoseServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class JoseServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _JoseServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _JoseServiceAsyncStub: ...  # type: ignore
    def GetJwks(self, __1: GetJwksRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetJwksResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, GetJwksResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _JoseServiceBlockingStub(JoseServiceStub):
    def GetJwks(self, __1: GetJwksRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetJwksResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _JoseServiceAsyncStub(JoseServiceStub):
    def GetJwks(self, __1: GetJwksRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetJwksResponse]: ...  # type: ignore
