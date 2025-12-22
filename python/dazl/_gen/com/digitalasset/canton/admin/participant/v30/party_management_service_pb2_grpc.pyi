# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .party_management_service_pb2 import AddPartyAsyncRequest, AddPartyAsyncResponse, ClearPartyOnboardingFlagRequest, ClearPartyOnboardingFlagResponse, ExportPartyAcsRequest, ExportPartyAcsResponse, GetAddPartyStatusRequest, GetAddPartyStatusResponse, GetHighestOffsetByTimestampRequest, GetHighestOffsetByTimestampResponse, ImportPartyAcsRequest, ImportPartyAcsResponse

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
    def AddPartyAsync(self, __1: AddPartyAsyncRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AddPartyAsyncResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, AddPartyAsyncResponse]: ...
    def GetAddPartyStatus(self, __1: GetAddPartyStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetAddPartyStatusResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, GetAddPartyStatusResponse]: ...
    def ExportPartyAcs(self, __1: ExportPartyAcsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[ExportPartyAcsResponse] | _grpc_aio.UnaryStreamCall[_typing.Any, ExportPartyAcsResponse]: ...
    def ImportPartyAcs(self, __1: _typing.Iterable[ImportPartyAcsRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ImportPartyAcsResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, ImportPartyAcsResponse]: ...
    def GetHighestOffsetByTimestamp(self, __1: GetHighestOffsetByTimestampRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetHighestOffsetByTimestampResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, GetHighestOffsetByTimestampResponse]: ...
    def ClearPartyOnboardingFlag(self, __1: ClearPartyOnboardingFlagRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ClearPartyOnboardingFlagResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, ClearPartyOnboardingFlagResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyManagementServiceBlockingStub(PartyManagementServiceStub):
    def AddPartyAsync(self, __1: AddPartyAsyncRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AddPartyAsyncResponse: ...
    def GetAddPartyStatus(self, __1: GetAddPartyStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetAddPartyStatusResponse: ...
    def ExportPartyAcs(self, __1: ExportPartyAcsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[ExportPartyAcsResponse]: ...
    def ImportPartyAcs(self, __1: _typing.Iterable[ImportPartyAcsRequest], timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ImportPartyAcsResponse: ...
    def GetHighestOffsetByTimestamp(self, __1: GetHighestOffsetByTimestampRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetHighestOffsetByTimestampResponse: ...
    def ClearPartyOnboardingFlag(self, __1: ClearPartyOnboardingFlagRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ClearPartyOnboardingFlagResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyManagementServiceAsyncStub(PartyManagementServiceStub):
    def AddPartyAsync(self, __1: AddPartyAsyncRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AddPartyAsyncResponse]: ...  # type: ignore
    def GetAddPartyStatus(self, __1: GetAddPartyStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetAddPartyStatusResponse]: ...  # type: ignore
    def ExportPartyAcs(self, __1: ExportPartyAcsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, ExportPartyAcsResponse]: ...  # type: ignore
    def ImportPartyAcs(self, __1: _typing.Iterable[ImportPartyAcsRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ImportPartyAcsResponse]: ...  # type: ignore
    def GetHighestOffsetByTimestamp(self, __1: GetHighestOffsetByTimestampRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetHighestOffsetByTimestampResponse]: ...  # type: ignore
    def ClearPartyOnboardingFlag(self, __1: ClearPartyOnboardingFlagRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ClearPartyOnboardingFlagResponse]: ...  # type: ignore
