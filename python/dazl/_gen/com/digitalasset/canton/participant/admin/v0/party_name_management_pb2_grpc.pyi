# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .party_name_management_pb2 import SetPartyDisplayNameRequest, SetPartyDisplayNameResponse

__all__ = [
    "PartyNameManagementServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class PartyNameManagementServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _PartyNameManagementServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _PartyNameManagementServiceAsyncStub: ...  # type: ignore
    def setPartyDisplayName(self, __1: SetPartyDisplayNameRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SetPartyDisplayNameResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SetPartyDisplayNameResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyNameManagementServiceBlockingStub(PartyNameManagementServiceStub):
    def setPartyDisplayName(self, __1: SetPartyDisplayNameRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SetPartyDisplayNameResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyNameManagementServiceAsyncStub(PartyNameManagementServiceStub):
    def setPartyDisplayName(self, __1: SetPartyDisplayNameRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SetPartyDisplayNameResponse]: ...  # type: ignore
