# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .version_service_pb2 import GetLedgerApiVersionRequest, GetLedgerApiVersionResponse

__all__ = [
    "VersionServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class VersionServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _VersionServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _VersionServiceAsyncStub: ...  # type: ignore
    def GetLedgerApiVersion(self, __1: GetLedgerApiVersionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetLedgerApiVersionResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetLedgerApiVersionResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _VersionServiceBlockingStub(VersionServiceStub):
    def GetLedgerApiVersion(self, __1: GetLedgerApiVersionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetLedgerApiVersionResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _VersionServiceAsyncStub(VersionServiceStub):
    def GetLedgerApiVersion(self, __1: GetLedgerApiVersionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetLedgerApiVersionResponse]: ...  # type: ignore
