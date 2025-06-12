# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .domain_status_service_pb2 import DomainStatusRequest, DomainStatusResponse

__all__ = [
    "DomainStatusServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class DomainStatusServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _DomainStatusServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _DomainStatusServiceAsyncStub: ...  # type: ignore
    def DomainStatus(self, __1: DomainStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[DomainStatusResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, DomainStatusResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainStatusServiceBlockingStub(DomainStatusServiceStub):
    def DomainStatus(self, __1: DomainStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> DomainStatusResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainStatusServiceAsyncStub(DomainStatusServiceStub):
    def DomainStatus(self, __1: DomainStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, DomainStatusResponse]: ...  # type: ignore
