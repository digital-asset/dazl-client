# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_service_pb2 import AcknowledgeSignedRequest, AcknowledgeSignedResponse, DownloadTopologyStateForInitRequest, DownloadTopologyStateForInitResponse, GetTrafficStateForMemberRequest, GetTrafficStateForMemberResponse, SendAsyncVersionedRequest, SendAsyncVersionedResponse, SubscriptionRequest, VersionedSubscriptionResponse

__all__ = [
    "SequencerServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerServiceAsyncStub: ...  # type: ignore
    def SendAsyncVersioned(self, __1: SendAsyncVersionedRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SendAsyncVersionedResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SendAsyncVersionedResponse]]: ...
    def SubscribeVersioned(self, __1: SubscriptionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[VersionedSubscriptionResponse], _grpc_aio.UnaryStreamCall[_typing.Any, VersionedSubscriptionResponse]]: ...
    def AcknowledgeSigned(self, __1: AcknowledgeSignedRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[AcknowledgeSignedResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, AcknowledgeSignedResponse]]: ...
    def DownloadTopologyStateForInit(self, __1: DownloadTopologyStateForInitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[DownloadTopologyStateForInitResponse], _grpc_aio.UnaryStreamCall[_typing.Any, DownloadTopologyStateForInitResponse]]: ...
    def GetTrafficStateForMember(self, __1: GetTrafficStateForMemberRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetTrafficStateForMemberResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetTrafficStateForMemberResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerServiceBlockingStub(SequencerServiceStub):
    def SendAsyncVersioned(self, __1: SendAsyncVersionedRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SendAsyncVersionedResponse: ...
    def SubscribeVersioned(self, __1: SubscriptionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[VersionedSubscriptionResponse]: ...
    def AcknowledgeSigned(self, __1: AcknowledgeSignedRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AcknowledgeSignedResponse: ...
    def DownloadTopologyStateForInit(self, __1: DownloadTopologyStateForInitRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[DownloadTopologyStateForInitResponse]: ...
    def GetTrafficStateForMember(self, __1: GetTrafficStateForMemberRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetTrafficStateForMemberResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerServiceAsyncStub(SequencerServiceStub):
    def SendAsyncVersioned(self, __1: SendAsyncVersionedRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SendAsyncVersionedResponse]: ...  # type: ignore
    def SubscribeVersioned(self, __1: SubscriptionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, VersionedSubscriptionResponse]: ...  # type: ignore
    def AcknowledgeSigned(self, __1: AcknowledgeSignedRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AcknowledgeSignedResponse]: ...  # type: ignore
    def DownloadTopologyStateForInit(self, __1: DownloadTopologyStateForInitRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, DownloadTopologyStateForInitResponse]: ...  # type: ignore
    def GetTrafficStateForMember(self, __1: GetTrafficStateForMemberRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetTrafficStateForMemberResponse]: ...  # type: ignore
