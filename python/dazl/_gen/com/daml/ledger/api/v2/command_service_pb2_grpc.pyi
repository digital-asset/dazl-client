# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .command_service_pb2 import SubmitAndWaitForReassignmentRequest, SubmitAndWaitForReassignmentResponse, SubmitAndWaitForTransactionRequest, SubmitAndWaitForTransactionResponse, SubmitAndWaitForTransactionTreeResponse, SubmitAndWaitRequest, SubmitAndWaitResponse

__all__ = [
    "CommandServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class CommandServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _CommandServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _CommandServiceAsyncStub: ...  # type: ignore
    def SubmitAndWait(self, __1: SubmitAndWaitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SubmitAndWaitResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitAndWaitResponse]]: ...
    def SubmitAndWaitForTransaction(self, __1: SubmitAndWaitForTransactionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SubmitAndWaitForTransactionResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitAndWaitForTransactionResponse]]: ...
    def SubmitAndWaitForTransactionTree(self, __1: SubmitAndWaitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SubmitAndWaitForTransactionTreeResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitAndWaitForTransactionTreeResponse]]: ...
    def SubmitAndWaitForReassignment(self, __1: SubmitAndWaitForReassignmentRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SubmitAndWaitForReassignmentResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitAndWaitForReassignmentResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandServiceBlockingStub(CommandServiceStub):
    def SubmitAndWait(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SubmitAndWaitResponse: ...
    def SubmitAndWaitForTransaction(self, __1: SubmitAndWaitForTransactionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SubmitAndWaitForTransactionResponse: ...
    def SubmitAndWaitForTransactionTree(self, __1: SubmitAndWaitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SubmitAndWaitForTransactionTreeResponse: ...
    def SubmitAndWaitForReassignment(self, __1: SubmitAndWaitForReassignmentRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SubmitAndWaitForReassignmentResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandServiceAsyncStub(CommandServiceStub):
    def SubmitAndWait(self, __1: SubmitAndWaitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitAndWaitResponse]: ...  # type: ignore
    def SubmitAndWaitForTransaction(self, __1: SubmitAndWaitForTransactionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitAndWaitForTransactionResponse]: ...  # type: ignore
    def SubmitAndWaitForTransactionTree(self, __1: SubmitAndWaitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitAndWaitForTransactionTreeResponse]: ...  # type: ignore
    def SubmitAndWaitForReassignment(self, __1: SubmitAndWaitForReassignmentRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitAndWaitForReassignmentResponse]: ...  # type: ignore
