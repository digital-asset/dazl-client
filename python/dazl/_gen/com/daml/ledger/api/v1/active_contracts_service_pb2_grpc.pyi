# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .active_contracts_service_pb2 import GetActiveContractsRequest, GetActiveContractsResponse

__all__ = [
    "ActiveContractsServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class ActiveContractsServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _ActiveContractsServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _ActiveContractsServiceAsyncStub: ...  # type: ignore
    def GetActiveContracts(self, __1: GetActiveContractsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[GetActiveContractsResponse], _grpc_aio.UnaryStreamCall[_typing.Any, GetActiveContractsResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ActiveContractsServiceBlockingStub(ActiveContractsServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[GetActiveContractsResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ActiveContractsServiceAsyncStub(ActiveContractsServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, GetActiveContractsResponse]: ...  # type: ignore
