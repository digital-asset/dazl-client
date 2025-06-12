# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .domain_manager_status_service_pb2 import DomainManagerStatusRequest, DomainManagerStatusResponse

__all__ = [
    "DomainManagerStatusServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class DomainManagerStatusServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _DomainManagerStatusServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _DomainManagerStatusServiceAsyncStub: ...  # type: ignore
    def DomainManagerStatus(self, __1: DomainManagerStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[DomainManagerStatusResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, DomainManagerStatusResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainManagerStatusServiceBlockingStub(DomainManagerStatusServiceStub):
    def DomainManagerStatus(self, __1: DomainManagerStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> DomainManagerStatusResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainManagerStatusServiceAsyncStub(DomainManagerStatusServiceStub):
    def DomainManagerStatus(self, __1: DomainManagerStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, DomainManagerStatusResponse]: ...  # type: ignore
