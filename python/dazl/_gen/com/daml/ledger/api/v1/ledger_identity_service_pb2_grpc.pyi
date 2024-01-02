# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .ledger_identity_service_pb2 import GetLedgerIdentityRequest, GetLedgerIdentityResponse

__all__ = [
    "LedgerIdentityServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class LedgerIdentityServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _LedgerIdentityServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _LedgerIdentityServiceAsyncStub: ...  # type: ignore
    def GetLedgerIdentity(self, __1: GetLedgerIdentityRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetLedgerIdentityResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetLedgerIdentityResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _LedgerIdentityServiceBlockingStub(LedgerIdentityServiceStub):
    def GetLedgerIdentity(self, __1: GetLedgerIdentityRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetLedgerIdentityResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _LedgerIdentityServiceAsyncStub(LedgerIdentityServiceStub):
    def GetLedgerIdentity(self, __1: GetLedgerIdentityRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetLedgerIdentityResponse]: ...  # type: ignore
