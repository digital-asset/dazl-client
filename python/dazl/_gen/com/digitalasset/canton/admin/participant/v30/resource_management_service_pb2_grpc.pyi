# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .resource_management_service_pb2 import GetResourceLimitsRequest, GetResourceLimitsResponse, SetResourceLimitsRequest, SetResourceLimitsResponse

__all__ = [
    "ResourceManagementServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class ResourceManagementServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _ResourceManagementServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _ResourceManagementServiceAsyncStub: ...  # type: ignore
    def SetResourceLimits(self, __1: SetResourceLimitsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SetResourceLimitsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SetResourceLimitsResponse]]: ...
    def GetResourceLimits(self, __1: GetResourceLimitsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetResourceLimitsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetResourceLimitsResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ResourceManagementServiceBlockingStub(ResourceManagementServiceStub):
    def SetResourceLimits(self, __1: SetResourceLimitsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SetResourceLimitsResponse: ...
    def GetResourceLimits(self, __1: GetResourceLimitsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetResourceLimitsResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ResourceManagementServiceAsyncStub(ResourceManagementServiceStub):
    def SetResourceLimits(self, __1: SetResourceLimitsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SetResourceLimitsResponse]: ...  # type: ignore
    def GetResourceLimits(self, __1: GetResourceLimitsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetResourceLimitsResponse]: ...  # type: ignore
