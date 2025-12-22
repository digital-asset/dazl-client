# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .update_service_pb2 import GetUpdateByIdRequest, GetUpdateByOffsetRequest, GetUpdateResponse, GetUpdatesRequest, GetUpdatesResponse

__all__ = [
    "UpdateServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class UpdateServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _UpdateServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _UpdateServiceAsyncStub: ...  # type: ignore
    def GetUpdates(self, __1: GetUpdatesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[GetUpdatesResponse] | _grpc_aio.UnaryStreamCall[_typing.Any, GetUpdatesResponse]: ...
    def GetUpdateByOffset(self, __1: GetUpdateByOffsetRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetUpdateResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, GetUpdateResponse]: ...
    def GetUpdateById(self, __1: GetUpdateByIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetUpdateResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, GetUpdateResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _UpdateServiceBlockingStub(UpdateServiceStub):
    def GetUpdates(self, __1: GetUpdatesRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[GetUpdatesResponse]: ...
    def GetUpdateByOffset(self, __1: GetUpdateByOffsetRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetUpdateResponse: ...
    def GetUpdateById(self, __1: GetUpdateByIdRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetUpdateResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _UpdateServiceAsyncStub(UpdateServiceStub):
    def GetUpdates(self, __1: GetUpdatesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, GetUpdatesResponse]: ...  # type: ignore
    def GetUpdateByOffset(self, __1: GetUpdateByOffsetRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetUpdateResponse]: ...  # type: ignore
    def GetUpdateById(self, __1: GetUpdateByIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetUpdateResponse]: ...  # type: ignore
