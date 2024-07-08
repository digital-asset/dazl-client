# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .participant_repair_service_pb2 import AcsSnapshotChunk, DownloadRequest, MigrateDomainRequest, MigrateDomainResponse, PurgeContractsRequest, PurgeContractsResponse, UploadRequest, UploadResponse

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
    def Download(self, __1: DownloadRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[AcsSnapshotChunk], _grpc_aio.UnaryStreamCall[_typing.Any, AcsSnapshotChunk]]: ...
    def Upload(self, __1: _typing.Iterable[UploadRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[UploadResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, UploadResponse]]: ...
    def PurgeContracts(self, __1: PurgeContractsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[PurgeContractsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, PurgeContractsResponse]]: ...
    def MigrateDomain(self, __1: MigrateDomainRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[MigrateDomainResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, MigrateDomainResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantRepairServiceBlockingStub(ParticipantRepairServiceStub):
    def Download(self, __1: DownloadRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[AcsSnapshotChunk]: ...
    def Upload(self, __1: _typing.Iterable[UploadRequest], timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> UploadResponse: ...
    def PurgeContracts(self, __1: PurgeContractsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> PurgeContractsResponse: ...
    def MigrateDomain(self, __1: MigrateDomainRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> MigrateDomainResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantRepairServiceAsyncStub(ParticipantRepairServiceStub):
    def Download(self, __1: DownloadRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, AcsSnapshotChunk]: ...  # type: ignore
    def Upload(self, __1: _typing.Iterable[UploadRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, UploadResponse]: ...  # type: ignore
    def PurgeContracts(self, __1: PurgeContractsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, PurgeContractsResponse]: ...  # type: ignore
    def MigrateDomain(self, __1: MigrateDomainRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, MigrateDomainResponse]: ...  # type: ignore
