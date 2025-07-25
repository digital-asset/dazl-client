# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .mediator_scan_service_pb2 import VerdictsRequest, VerdictsResponse

__all__ = [
    "MediatorScanServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class MediatorScanServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _MediatorScanServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _MediatorScanServiceAsyncStub: ...  # type: ignore
    def Verdicts(self, __1: VerdictsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[VerdictsResponse], _grpc_aio.UnaryStreamCall[_typing.Any, VerdictsResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _MediatorScanServiceBlockingStub(MediatorScanServiceStub):
    def Verdicts(self, __1: VerdictsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[VerdictsResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _MediatorScanServiceAsyncStub(MediatorScanServiceStub):
    def Verdicts(self, __1: VerdictsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, VerdictsResponse]: ...  # type: ignore
