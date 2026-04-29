# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .contract_service_pb2 import GetContractRequest, GetContractResponse

__all__ = [
    "ContractServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class ContractServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _ContractServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _ContractServiceAsyncStub: ...  # type: ignore
    def GetContract(self, __1: GetContractRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetContractResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, GetContractResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ContractServiceBlockingStub(ContractServiceStub):
    def GetContract(self, __1: GetContractRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetContractResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ContractServiceAsyncStub(ContractServiceStub):
    def GetContract(self, __1: GetContractRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetContractResponse]: ...  # type: ignore
