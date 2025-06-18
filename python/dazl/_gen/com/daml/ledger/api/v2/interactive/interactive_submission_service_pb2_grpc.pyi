# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .interactive_submission_service_pb2 import ExecuteSubmissionRequest, ExecuteSubmissionResponse, GetPreferredPackageVersionRequest, GetPreferredPackageVersionResponse, PrepareSubmissionRequest, PrepareSubmissionResponse

__all__ = [
    "InteractiveSubmissionServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class InteractiveSubmissionServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _InteractiveSubmissionServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _InteractiveSubmissionServiceAsyncStub: ...  # type: ignore
    def PrepareSubmission(self, __1: PrepareSubmissionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[PrepareSubmissionResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, PrepareSubmissionResponse]]: ...
    def ExecuteSubmission(self, __1: ExecuteSubmissionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ExecuteSubmissionResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, ExecuteSubmissionResponse]]: ...
    def GetPreferredPackageVersion(self, __1: GetPreferredPackageVersionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetPreferredPackageVersionResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetPreferredPackageVersionResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _InteractiveSubmissionServiceBlockingStub(InteractiveSubmissionServiceStub):
    def PrepareSubmission(self, __1: PrepareSubmissionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> PrepareSubmissionResponse: ...
    def ExecuteSubmission(self, __1: ExecuteSubmissionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ExecuteSubmissionResponse: ...
    def GetPreferredPackageVersion(self, __1: GetPreferredPackageVersionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetPreferredPackageVersionResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _InteractiveSubmissionServiceAsyncStub(InteractiveSubmissionServiceStub):
    def PrepareSubmission(self, __1: PrepareSubmissionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, PrepareSubmissionResponse]: ...  # type: ignore
    def ExecuteSubmission(self, __1: ExecuteSubmissionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ExecuteSubmissionResponse]: ...  # type: ignore
    def GetPreferredPackageVersion(self, __1: GetPreferredPackageVersionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetPreferredPackageVersionResponse]: ...  # type: ignore
