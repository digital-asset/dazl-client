# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .version_service_pb2 import GetLedgerApiVersionRequest, GetLedgerApiVersionResponse

__all__ = [
    "VersionServiceStub",
]

_T = _typing.TypeVar('_T')


# noinspection PyAbstractClass
class _Async(_grpc_aio.UnaryUnaryCall, _typing.Awaitable[_T]):
    pass

# noinspection PyAbstractClass
class _AsyncStream(_grpc_aio.UnaryStreamCall, _typing.AsyncIterator[_T]):
    pass


# noinspection PyPep8Naming,DuplicatedCode
class VersionServiceStub:
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _VersionServiceBlockingStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _VersionServiceAsyncStub: ...
    def GetLedgerApiVersion(self, __1: GetLedgerApiVersionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetLedgerApiVersionResponse, _Async[GetLedgerApiVersionResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _VersionServiceBlockingStub(VersionServiceStub):
    def GetLedgerApiVersion(self, __1: GetLedgerApiVersionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetLedgerApiVersionResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _VersionServiceAsyncStub(VersionServiceStub):
    def GetLedgerApiVersion(self, __1: GetLedgerApiVersionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _Async[GetLedgerApiVersionResponse]: ...
