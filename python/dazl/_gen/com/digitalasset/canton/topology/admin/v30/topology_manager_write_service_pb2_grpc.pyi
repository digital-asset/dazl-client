# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .topology_manager_write_service_pb2 import AddTransactionsRequest, AddTransactionsResponse, AuthorizeRequest, AuthorizeResponse, GenerateTransactionsRequest, GenerateTransactionsResponse, ImportTopologySnapshotRequest, ImportTopologySnapshotResponse, SignTransactionsRequest, SignTransactionsResponse

__all__ = [
    "TopologyManagerWriteServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class TopologyManagerWriteServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _TopologyManagerWriteServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _TopologyManagerWriteServiceAsyncStub: ...  # type: ignore
    def Authorize(self, __1: AuthorizeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AuthorizeResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AuthorizeResponse]]: ...
    def AddTransactions(self, __1: AddTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AddTransactionsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AddTransactionsResponse]]: ...
    def ImportTopologySnapshot(self, __1: ImportTopologySnapshotRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ImportTopologySnapshotResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, ImportTopologySnapshotResponse]]: ...
    def SignTransactions(self, __1: SignTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SignTransactionsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SignTransactionsResponse]]: ...
    def GenerateTransactions(self, __1: GenerateTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GenerateTransactionsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GenerateTransactionsResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _TopologyManagerWriteServiceBlockingStub(TopologyManagerWriteServiceStub):
    def Authorize(self, __1: AuthorizeRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AuthorizeResponse: ...
    def AddTransactions(self, __1: AddTransactionsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AddTransactionsResponse: ...
    def ImportTopologySnapshot(self, __1: ImportTopologySnapshotRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ImportTopologySnapshotResponse: ...
    def SignTransactions(self, __1: SignTransactionsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SignTransactionsResponse: ...
    def GenerateTransactions(self, __1: GenerateTransactionsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GenerateTransactionsResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _TopologyManagerWriteServiceAsyncStub(TopologyManagerWriteServiceStub):
    def Authorize(self, __1: AuthorizeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AuthorizeResponse]: ...  # type: ignore
    def AddTransactions(self, __1: AddTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AddTransactionsResponse]: ...  # type: ignore
    def ImportTopologySnapshot(self, __1: ImportTopologySnapshotRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ImportTopologySnapshotResponse]: ...  # type: ignore
    def SignTransactions(self, __1: SignTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SignTransactionsResponse]: ...  # type: ignore
    def GenerateTransactions(self, __1: GenerateTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GenerateTransactionsResponse]: ...  # type: ignore
