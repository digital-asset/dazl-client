# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .participant_repair_service_pb2 import ExportAcsRequest, ExportAcsResponse, IgnoreEventsRequest, IgnoreEventsResponse, ImportAcsRequest, ImportAcsResponse, MigrateDomainRequest, MigrateDomainResponse, PurgeContractsRequest, PurgeContractsResponse, PurgeDeactivatedDomainRequest, PurgeDeactivatedDomainResponse, UnignoreEventsRequest, UnignoreEventsResponse

__all__ = [
    "ParticipantRepairServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class ParticipantRepairServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _ParticipantRepairServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _ParticipantRepairServiceAsyncStub: ...  # type: ignore
    def ExportAcs(self, __1: ExportAcsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[ExportAcsResponse], _grpc_aio.UnaryStreamCall[_typing.Any, ExportAcsResponse]]: ...
    def ImportAcs(self, __1: _typing.Iterable[ImportAcsRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ImportAcsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, ImportAcsResponse]]: ...
    def PurgeContracts(self, __1: PurgeContractsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[PurgeContractsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, PurgeContractsResponse]]: ...
    def MigrateDomain(self, __1: MigrateDomainRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[MigrateDomainResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, MigrateDomainResponse]]: ...
    def PurgeDeactivatedDomain(self, __1: PurgeDeactivatedDomainRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[PurgeDeactivatedDomainResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, PurgeDeactivatedDomainResponse]]: ...
    def IgnoreEvents(self, __1: IgnoreEventsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[IgnoreEventsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, IgnoreEventsResponse]]: ...
    def UnignoreEvents(self, __1: UnignoreEventsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[UnignoreEventsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, UnignoreEventsResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantRepairServiceBlockingStub(ParticipantRepairServiceStub):
    def ExportAcs(self, __1: ExportAcsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[ExportAcsResponse]: ...
    def ImportAcs(self, __1: _typing.Iterable[ImportAcsRequest], timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ImportAcsResponse: ...
    def PurgeContracts(self, __1: PurgeContractsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> PurgeContractsResponse: ...
    def MigrateDomain(self, __1: MigrateDomainRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> MigrateDomainResponse: ...
    def PurgeDeactivatedDomain(self, __1: PurgeDeactivatedDomainRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> PurgeDeactivatedDomainResponse: ...
    def IgnoreEvents(self, __1: IgnoreEventsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> IgnoreEventsResponse: ...
    def UnignoreEvents(self, __1: UnignoreEventsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> UnignoreEventsResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantRepairServiceAsyncStub(ParticipantRepairServiceStub):
    def ExportAcs(self, __1: ExportAcsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, ExportAcsResponse]: ...  # type: ignore
    def ImportAcs(self, __1: _typing.Iterable[ImportAcsRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ImportAcsResponse]: ...  # type: ignore
    def PurgeContracts(self, __1: PurgeContractsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, PurgeContractsResponse]: ...  # type: ignore
    def MigrateDomain(self, __1: MigrateDomainRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, MigrateDomainResponse]: ...  # type: ignore
    def PurgeDeactivatedDomain(self, __1: PurgeDeactivatedDomainRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, PurgeDeactivatedDomainResponse]: ...  # type: ignore
    def IgnoreEvents(self, __1: IgnoreEventsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, IgnoreEventsResponse]: ...  # type: ignore
    def UnignoreEvents(self, __1: UnignoreEventsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, UnignoreEventsResponse]: ...  # type: ignore
