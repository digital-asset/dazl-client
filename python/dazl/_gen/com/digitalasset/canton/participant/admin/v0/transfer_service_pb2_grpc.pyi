# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .transfer_service_pb2 import AdminTransferInRequest, AdminTransferInResponse, AdminTransferOutRequest, AdminTransferOutResponse, AdminTransferSearchQuery, AdminTransferSearchResponse

__all__ = [
    "TransferServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class TransferServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _TransferServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _TransferServiceAsyncStub: ...  # type: ignore
    def TransferOut(self, __1: AdminTransferOutRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AdminTransferOutResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AdminTransferOutResponse]]: ...
    def TransferIn(self, __1: AdminTransferInRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AdminTransferInResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AdminTransferInResponse]]: ...
    def TransferSearch(self, __1: AdminTransferSearchQuery, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AdminTransferSearchResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AdminTransferSearchResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _TransferServiceBlockingStub(TransferServiceStub):
    def TransferOut(self, __1: AdminTransferOutRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AdminTransferOutResponse: ...
    def TransferIn(self, __1: AdminTransferInRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AdminTransferInResponse: ...
    def TransferSearch(self, __1: AdminTransferSearchQuery, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AdminTransferSearchResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _TransferServiceAsyncStub(TransferServiceStub):
    def TransferOut(self, __1: AdminTransferOutRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AdminTransferOutResponse]: ...  # type: ignore
    def TransferIn(self, __1: AdminTransferInRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AdminTransferInResponse]: ...  # type: ignore
    def TransferSearch(self, __1: AdminTransferSearchQuery, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AdminTransferSearchResponse]: ...  # type: ignore
