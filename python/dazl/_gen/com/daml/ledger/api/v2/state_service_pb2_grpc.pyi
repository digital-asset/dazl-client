# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .state_service_pb2 import GetActiveContractsRequest, GetActiveContractsResponse, GetConnectedSynchronizersRequest, GetConnectedSynchronizersResponse, GetLatestPrunedOffsetsRequest, GetLatestPrunedOffsetsResponse, GetLedgerEndRequest, GetLedgerEndResponse

__all__ = [
    "StateServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class StateServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _StateServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _StateServiceAsyncStub: ...  # type: ignore
    def GetActiveContracts(self, __1: GetActiveContractsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[GetActiveContractsResponse], _grpc_aio.UnaryStreamCall[_typing.Any, GetActiveContractsResponse]]: ...
    def GetConnectedSynchronizers(self, __1: GetConnectedSynchronizersRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetConnectedSynchronizersResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetConnectedSynchronizersResponse]]: ...
    def GetLedgerEnd(self, __1: GetLedgerEndRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetLedgerEndResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetLedgerEndResponse]]: ...
    def GetLatestPrunedOffsets(self, __1: GetLatestPrunedOffsetsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetLatestPrunedOffsetsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetLatestPrunedOffsetsResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _StateServiceBlockingStub(StateServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[GetActiveContractsResponse]: ...
    def GetConnectedSynchronizers(self, __1: GetConnectedSynchronizersRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetConnectedSynchronizersResponse: ...
    def GetLedgerEnd(self, __1: GetLedgerEndRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetLedgerEndResponse: ...
    def GetLatestPrunedOffsets(self, __1: GetLatestPrunedOffsetsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetLatestPrunedOffsetsResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _StateServiceAsyncStub(StateServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, GetActiveContractsResponse]: ...  # type: ignore
    def GetConnectedSynchronizers(self, __1: GetConnectedSynchronizersRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetConnectedSynchronizersResponse]: ...  # type: ignore
    def GetLedgerEnd(self, __1: GetLedgerEndRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetLedgerEndResponse]: ...  # type: ignore
    def GetLatestPrunedOffsets(self, __1: GetLatestPrunedOffsetsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetLatestPrunedOffsetsResponse]: ...  # type: ignore
