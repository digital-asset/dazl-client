# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .config_management_service_pb2 import GetTimeModelRequest, GetTimeModelResponse, SetTimeModelRequest, SetTimeModelResponse

__all__ = [
    "ConfigManagementServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class ConfigManagementServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _ConfigManagementServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _ConfigManagementServiceAsyncStub: ...  # type: ignore
    def GetTimeModel(self, __1: GetTimeModelRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetTimeModelResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetTimeModelResponse]]: ...
    def SetTimeModel(self, __1: SetTimeModelRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SetTimeModelResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SetTimeModelResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ConfigManagementServiceBlockingStub(ConfigManagementServiceStub):
    def GetTimeModel(self, __1: GetTimeModelRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetTimeModelResponse: ...
    def SetTimeModel(self, __1: SetTimeModelRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SetTimeModelResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ConfigManagementServiceAsyncStub(ConfigManagementServiceStub):
    def GetTimeModel(self, __1: GetTimeModelRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetTimeModelResponse]: ...  # type: ignore
    def SetTimeModel(self, __1: SetTimeModelRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SetTimeModelResponse]: ...  # type: ignore
