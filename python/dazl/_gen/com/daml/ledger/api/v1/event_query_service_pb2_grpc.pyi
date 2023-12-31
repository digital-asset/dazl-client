# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .event_query_service_pb2 import GetEventsByContractIdRequest, GetEventsByContractIdResponse, GetEventsByContractKeyRequest, GetEventsByContractKeyResponse

__all__ = [
    "EventQueryServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class EventQueryServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _EventQueryServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _EventQueryServiceAsyncStub: ...  # type: ignore
    def GetEventsByContractId(self, __1: GetEventsByContractIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetEventsByContractIdResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetEventsByContractIdResponse]]: ...
    def GetEventsByContractKey(self, __1: GetEventsByContractKeyRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetEventsByContractKeyResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetEventsByContractKeyResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _EventQueryServiceBlockingStub(EventQueryServiceStub):
    def GetEventsByContractId(self, __1: GetEventsByContractIdRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetEventsByContractIdResponse: ...
    def GetEventsByContractKey(self, __1: GetEventsByContractKeyRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetEventsByContractKeyResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _EventQueryServiceAsyncStub(EventQueryServiceStub):
    def GetEventsByContractId(self, __1: GetEventsByContractIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetEventsByContractIdResponse]: ...  # type: ignore
    def GetEventsByContractKey(self, __1: GetEventsByContractKeyRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetEventsByContractKeyResponse]: ...  # type: ignore
