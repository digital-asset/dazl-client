# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from google.protobuf.empty_pb2 import Empty
from grpc import aio as _grpc_aio

from .domain_initialization_service_pb2 import DomainInitRequest

__all__ = [
    "DomainInitializationServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class DomainInitializationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _DomainInitializationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _DomainInitializationServiceAsyncStub: ...  # type: ignore
    def Init(self, __1: DomainInitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[Empty, _grpc_aio.UnaryUnaryCall[_typing.Any, Empty]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainInitializationServiceBlockingStub(DomainInitializationServiceStub):
    def Init(self, __1: DomainInitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> Empty: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainInitializationServiceAsyncStub(DomainInitializationServiceStub):
    def Init(self, __1: DomainInitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, Empty]: ...  # type: ignore
