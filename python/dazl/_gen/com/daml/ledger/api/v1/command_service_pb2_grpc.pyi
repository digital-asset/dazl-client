# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

import grpc as _grpc
from google.protobuf.empty_pb2 import Empty
from grpc import aio as _grpc_aio

from .command_service_pb2 import SubmitAndWaitForTransactionIdResponse, SubmitAndWaitForTransactionResponse, SubmitAndWaitForTransactionTreeResponse, SubmitAndWaitRequest

__all__ = [
    "CommandServiceStub",
]

_T = _typing.TypeVar('_T')


# noinspection PyAbstractClass
class _Async(_grpc_aio.UnaryUnaryCall, _typing.Awaitable[_T]):
    pass

# noinspection PyAbstractClass
class _AsyncStream(_grpc_aio.UnaryStreamCall, _typing.AsyncIterator[_T]):
    pass


# noinspection PyPep8Naming,DuplicatedCode
class CommandServiceStub:
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _CommandServiceBlockingStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _CommandServiceAsyncStub: ...
    def SubmitAndWait(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[Empty, _Async[Empty]]: ...
    def SubmitAndWaitForTransactionId(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SubmitAndWaitForTransactionIdResponse, _Async[SubmitAndWaitForTransactionIdResponse]]: ...
    def SubmitAndWaitForTransaction(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SubmitAndWaitForTransactionResponse, _Async[SubmitAndWaitForTransactionResponse]]: ...
    def SubmitAndWaitForTransactionTree(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SubmitAndWaitForTransactionTreeResponse, _Async[SubmitAndWaitForTransactionTreeResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandServiceBlockingStub(CommandServiceStub):
    def SubmitAndWait(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> Empty: ...
    def SubmitAndWaitForTransactionId(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SubmitAndWaitForTransactionIdResponse: ...
    def SubmitAndWaitForTransaction(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SubmitAndWaitForTransactionResponse: ...
    def SubmitAndWaitForTransactionTree(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SubmitAndWaitForTransactionTreeResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandServiceAsyncStub(CommandServiceStub):
    def SubmitAndWait(self, __1: SubmitAndWaitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _Async[Empty]: ...
    def SubmitAndWaitForTransactionId(self, __1: SubmitAndWaitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _Async[SubmitAndWaitForTransactionIdResponse]: ...
    def SubmitAndWaitForTransaction(self, __1: SubmitAndWaitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _Async[SubmitAndWaitForTransactionResponse]: ...
    def SubmitAndWaitForTransactionTree(self, __1: SubmitAndWaitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _Async[SubmitAndWaitForTransactionTreeResponse]: ...
