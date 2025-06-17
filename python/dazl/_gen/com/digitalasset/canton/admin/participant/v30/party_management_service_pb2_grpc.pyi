# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .party_management_service_pb2 import AddPartyAsyncRequest, AddPartyAsyncResponse, ExportAcsAtTimestampRequest, ExportAcsAtTimestampResponse, ExportAcsRequest, ExportAcsResponse, GetAddPartyStatusRequest, GetAddPartyStatusResponse

__all__ = [
    "PartyManagementServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class PartyManagementServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _PartyManagementServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _PartyManagementServiceAsyncStub: ...  # type: ignore
    def AddPartyAsync(self, __1: AddPartyAsyncRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AddPartyAsyncResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AddPartyAsyncResponse]]: ...
    def GetAddPartyStatus(self, __1: GetAddPartyStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetAddPartyStatusResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetAddPartyStatusResponse]]: ...
    def ExportAcs(self, __1: ExportAcsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[ExportAcsResponse], _grpc_aio.UnaryStreamCall[_typing.Any, ExportAcsResponse]]: ...
    def ExportAcsAtTimestamp(self, __1: ExportAcsAtTimestampRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[ExportAcsAtTimestampResponse], _grpc_aio.UnaryStreamCall[_typing.Any, ExportAcsAtTimestampResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyManagementServiceBlockingStub(PartyManagementServiceStub):
    def AddPartyAsync(self, __1: AddPartyAsyncRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AddPartyAsyncResponse: ...
    def GetAddPartyStatus(self, __1: GetAddPartyStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetAddPartyStatusResponse: ...
    def ExportAcs(self, __1: ExportAcsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[ExportAcsResponse]: ...
    def ExportAcsAtTimestamp(self, __1: ExportAcsAtTimestampRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[ExportAcsAtTimestampResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyManagementServiceAsyncStub(PartyManagementServiceStub):
    def AddPartyAsync(self, __1: AddPartyAsyncRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AddPartyAsyncResponse]: ...  # type: ignore
    def GetAddPartyStatus(self, __1: GetAddPartyStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetAddPartyStatusResponse]: ...  # type: ignore
    def ExportAcs(self, __1: ExportAcsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, ExportAcsResponse]: ...  # type: ignore
    def ExportAcsAtTimestamp(self, __1: ExportAcsAtTimestampRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, ExportAcsAtTimestampResponse]: ...  # type: ignore
