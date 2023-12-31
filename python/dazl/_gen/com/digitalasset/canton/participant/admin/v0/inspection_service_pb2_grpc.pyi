# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .inspection_service_pb2 import LookupContractDomain, LookupOffsetByIndex, LookupOffsetByTime, LookupTransactionDomain

__all__ = [
    "InspectionServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class InspectionServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _InspectionServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _InspectionServiceAsyncStub: ...  # type: ignore
    def LookupContractDomain(self, __1: LookupContractDomain.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[LookupContractDomain.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, LookupContractDomain.Response]]: ...
    def LookupTransactionDomain(self, __1: LookupTransactionDomain.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[LookupTransactionDomain.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, LookupTransactionDomain.Response]]: ...
    def LookupOffsetByTime(self, __1: LookupOffsetByTime.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[LookupOffsetByTime.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, LookupOffsetByTime.Response]]: ...
    def LookupOffsetByIndex(self, __1: LookupOffsetByIndex.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[LookupOffsetByIndex.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, LookupOffsetByIndex.Response]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _InspectionServiceBlockingStub(InspectionServiceStub):
    def LookupContractDomain(self, __1: LookupContractDomain.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> LookupContractDomain.Response: ...
    def LookupTransactionDomain(self, __1: LookupTransactionDomain.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> LookupTransactionDomain.Response: ...
    def LookupOffsetByTime(self, __1: LookupOffsetByTime.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> LookupOffsetByTime.Response: ...
    def LookupOffsetByIndex(self, __1: LookupOffsetByIndex.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> LookupOffsetByIndex.Response: ...

# noinspection PyPep8Naming,DuplicatedCode
class _InspectionServiceAsyncStub(InspectionServiceStub):
    def LookupContractDomain(self, __1: LookupContractDomain.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, LookupContractDomain.Response]: ...  # type: ignore
    def LookupTransactionDomain(self, __1: LookupTransactionDomain.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, LookupTransactionDomain.Response]: ...  # type: ignore
    def LookupOffsetByTime(self, __1: LookupOffsetByTime.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, LookupOffsetByTime.Response]: ...  # type: ignore
    def LookupOffsetByIndex(self, __1: LookupOffsetByIndex.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, LookupOffsetByIndex.Response]: ...  # type: ignore
