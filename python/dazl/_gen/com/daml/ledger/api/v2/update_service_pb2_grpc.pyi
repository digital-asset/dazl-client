# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .update_service_pb2 import GetTransactionByEventIdRequest, GetTransactionByIdRequest, GetTransactionResponse, GetTransactionTreeResponse, GetUpdateTreesResponse, GetUpdatesRequest, GetUpdatesResponse

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
    def GetUpdates(self, __1: GetUpdatesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[GetUpdatesResponse], _grpc_aio.UnaryStreamCall[_typing.Any, GetUpdatesResponse]]: ...
    def GetUpdateTrees(self, __1: GetUpdatesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[GetUpdateTreesResponse], _grpc_aio.UnaryStreamCall[_typing.Any, GetUpdateTreesResponse]]: ...
    def GetTransactionTreeByEventId(self, __1: GetTransactionByEventIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetTransactionTreeResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetTransactionTreeResponse]]: ...
    def GetTransactionTreeById(self, __1: GetTransactionByIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetTransactionTreeResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetTransactionTreeResponse]]: ...
    def GetTransactionByEventId(self, __1: GetTransactionByEventIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetTransactionResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetTransactionResponse]]: ...
    def GetTransactionById(self, __1: GetTransactionByIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetTransactionResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetTransactionResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _UpdateServiceBlockingStub(UpdateServiceStub):
    def GetUpdates(self, __1: GetUpdatesRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[GetUpdatesResponse]: ...
    def GetUpdateTrees(self, __1: GetUpdatesRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[GetUpdateTreesResponse]: ...
    def GetTransactionTreeByEventId(self, __1: GetTransactionByEventIdRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetTransactionTreeResponse: ...
    def GetTransactionTreeById(self, __1: GetTransactionByIdRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetTransactionTreeResponse: ...
    def GetTransactionByEventId(self, __1: GetTransactionByEventIdRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetTransactionResponse: ...
    def GetTransactionById(self, __1: GetTransactionByIdRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetTransactionResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _UpdateServiceAsyncStub(UpdateServiceStub):
    def GetUpdates(self, __1: GetUpdatesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, GetUpdatesResponse]: ...  # type: ignore
    def GetUpdateTrees(self, __1: GetUpdatesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, GetUpdateTreesResponse]: ...  # type: ignore
    def GetTransactionTreeByEventId(self, __1: GetTransactionByEventIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetTransactionTreeResponse]: ...  # type: ignore
    def GetTransactionTreeById(self, __1: GetTransactionByIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetTransactionTreeResponse]: ...  # type: ignore
    def GetTransactionByEventId(self, __1: GetTransactionByEventIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetTransactionResponse]: ...  # type: ignore
    def GetTransactionById(self, __1: GetTransactionByIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetTransactionResponse]: ...  # type: ignore
