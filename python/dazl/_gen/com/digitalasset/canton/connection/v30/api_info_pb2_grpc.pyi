# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .api_info_pb2 import GetApiInfoRequest, GetApiInfoResponse

__all__ = [
    "ApiInfoServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class ApiInfoServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _ApiInfoServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _ApiInfoServiceAsyncStub: ...  # type: ignore
    def GetApiInfo(self, __1: GetApiInfoRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetApiInfoResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetApiInfoResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ApiInfoServiceBlockingStub(ApiInfoServiceStub):
    def GetApiInfo(self, __1: GetApiInfoRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetApiInfoResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ApiInfoServiceAsyncStub(ApiInfoServiceStub):
    def GetApiInfo(self, __1: GetApiInfoRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetApiInfoResponse]: ...  # type: ignore
