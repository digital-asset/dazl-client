# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .command_inspection_service_pb2 import GetCommandStatusRequest, GetCommandStatusResponse

__all__ = [
    "CommandInspectionServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class CommandInspectionServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _CommandInspectionServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _CommandInspectionServiceAsyncStub: ...  # type: ignore
    def GetCommandStatus(self, __1: GetCommandStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetCommandStatusResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetCommandStatusResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandInspectionServiceBlockingStub(CommandInspectionServiceStub):
    def GetCommandStatus(self, __1: GetCommandStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetCommandStatusResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandInspectionServiceAsyncStub(CommandInspectionServiceStub):
    def GetCommandStatus(self, __1: GetCommandStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetCommandStatusResponse]: ...  # type: ignore
