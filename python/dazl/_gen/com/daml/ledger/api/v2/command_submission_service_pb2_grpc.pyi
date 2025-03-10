# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .command_submission_service_pb2 import SubmitReassignmentRequest, SubmitReassignmentResponse, SubmitRequest, SubmitResponse

__all__ = [
    "CommandSubmissionServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class CommandSubmissionServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _CommandSubmissionServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _CommandSubmissionServiceAsyncStub: ...  # type: ignore
    def Submit(self, __1: SubmitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SubmitResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitResponse]]: ...
    def SubmitReassignment(self, __1: SubmitReassignmentRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SubmitReassignmentResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitReassignmentResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandSubmissionServiceBlockingStub(CommandSubmissionServiceStub):
    def Submit(self, __1: SubmitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SubmitResponse: ...
    def SubmitReassignment(self, __1: SubmitReassignmentRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SubmitReassignmentResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandSubmissionServiceAsyncStub(CommandSubmissionServiceStub):
    def Submit(self, __1: SubmitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitResponse]: ...  # type: ignore
    def SubmitReassignment(self, __1: SubmitReassignmentRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SubmitReassignmentResponse]: ...  # type: ignore
