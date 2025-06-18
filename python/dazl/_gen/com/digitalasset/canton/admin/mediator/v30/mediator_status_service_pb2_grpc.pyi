# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .mediator_status_service_pb2 import MediatorStatusRequest, MediatorStatusResponse

__all__ = [
    "MediatorStatusServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class MediatorStatusServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _MediatorStatusServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _MediatorStatusServiceAsyncStub: ...  # type: ignore
    def MediatorStatus(self, __1: MediatorStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[MediatorStatusResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, MediatorStatusResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _MediatorStatusServiceBlockingStub(MediatorStatusServiceStub):
    def MediatorStatus(self, __1: MediatorStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> MediatorStatusResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _MediatorStatusServiceAsyncStub(MediatorStatusServiceStub):
    def MediatorStatus(self, __1: MediatorStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, MediatorStatusResponse]: ...  # type: ignore
