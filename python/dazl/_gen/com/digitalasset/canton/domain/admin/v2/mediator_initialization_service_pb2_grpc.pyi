# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .mediator_initialization_service_pb2 import InitializeMediatorRequest, InitializeMediatorResponse

__all__ = [
    "MediatorInitializationServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class MediatorInitializationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _MediatorInitializationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _MediatorInitializationServiceAsyncStub: ...  # type: ignore
    def Initialize(self, __1: InitializeMediatorRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[InitializeMediatorResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, InitializeMediatorResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _MediatorInitializationServiceBlockingStub(MediatorInitializationServiceStub):
    def Initialize(self, __1: InitializeMediatorRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> InitializeMediatorResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _MediatorInitializationServiceAsyncStub(MediatorInitializationServiceStub):
    def Initialize(self, __1: InitializeMediatorRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, InitializeMediatorResponse]: ...  # type: ignore
