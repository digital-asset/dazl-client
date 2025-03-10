# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_administration_service_pb2 import DisableMemberRequest, DisableMemberResponse, OnboardingStateRequest, OnboardingStateResponse, PruningStatusRequest, PruningStatusResponse, SetTrafficPurchasedRequest, SetTrafficPurchasedResponse, SnapshotRequest, SnapshotResponse, TrafficControlStateRequest, TrafficControlStateResponse

__all__ = [
    "SequencerAdministrationServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerAdministrationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerAdministrationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerAdministrationServiceAsyncStub: ...  # type: ignore
    def PruningStatus(self, __1: PruningStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[PruningStatusResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, PruningStatusResponse]]: ...
    def TrafficControlState(self, __1: TrafficControlStateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[TrafficControlStateResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, TrafficControlStateResponse]]: ...
    def SetTrafficPurchased(self, __1: SetTrafficPurchasedRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SetTrafficPurchasedResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SetTrafficPurchasedResponse]]: ...
    def Snapshot(self, __1: SnapshotRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SnapshotResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SnapshotResponse]]: ...
    def OnboardingState(self, __1: OnboardingStateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[OnboardingStateResponse], _grpc_aio.UnaryStreamCall[_typing.Any, OnboardingStateResponse]]: ...
    def DisableMember(self, __1: DisableMemberRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[DisableMemberResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, DisableMemberResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerAdministrationServiceBlockingStub(SequencerAdministrationServiceStub):
    def PruningStatus(self, __1: PruningStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> PruningStatusResponse: ...
    def TrafficControlState(self, __1: TrafficControlStateRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> TrafficControlStateResponse: ...
    def SetTrafficPurchased(self, __1: SetTrafficPurchasedRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SetTrafficPurchasedResponse: ...
    def Snapshot(self, __1: SnapshotRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SnapshotResponse: ...
    def OnboardingState(self, __1: OnboardingStateRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[OnboardingStateResponse]: ...
    def DisableMember(self, __1: DisableMemberRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> DisableMemberResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerAdministrationServiceAsyncStub(SequencerAdministrationServiceStub):
    def PruningStatus(self, __1: PruningStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, PruningStatusResponse]: ...  # type: ignore
    def TrafficControlState(self, __1: TrafficControlStateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, TrafficControlStateResponse]: ...  # type: ignore
    def SetTrafficPurchased(self, __1: SetTrafficPurchasedRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SetTrafficPurchasedResponse]: ...  # type: ignore
    def Snapshot(self, __1: SnapshotRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SnapshotResponse]: ...  # type: ignore
    def OnboardingState(self, __1: OnboardingStateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, OnboardingStateResponse]: ...  # type: ignore
    def DisableMember(self, __1: DisableMemberRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, DisableMemberResponse]: ...  # type: ignore
