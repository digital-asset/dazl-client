# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_connect_service_pb2 import SequencerConnect

__all__ = [
    "SequencerConnectServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerConnectServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerConnectServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerConnectServiceAsyncStub: ...  # type: ignore
    def Handshake(self, __1: SequencerConnect.HandshakeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.HandshakeResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.HandshakeResponse]]: ...
    def GetSynchronizerId(self, __1: SequencerConnect.GetSynchronizerIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.GetSynchronizerIdResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetSynchronizerIdResponse]]: ...
    def GetSynchronizerParameters(self, __1: SequencerConnect.GetSynchronizerParametersRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.GetSynchronizerParametersResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetSynchronizerParametersResponse]]: ...
    def VerifyActive(self, __1: SequencerConnect.VerifyActiveRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.VerifyActiveResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.VerifyActiveResponse]]: ...
    def RegisterOnboardingTopologyTransactions(self, __1: SequencerConnect.RegisterOnboardingTopologyTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.RegisterOnboardingTopologyTransactionsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.RegisterOnboardingTopologyTransactionsResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerConnectServiceBlockingStub(SequencerConnectServiceStub):
    def Handshake(self, __1: SequencerConnect.HandshakeRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.HandshakeResponse: ...
    def GetSynchronizerId(self, __1: SequencerConnect.GetSynchronizerIdRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.GetSynchronizerIdResponse: ...
    def GetSynchronizerParameters(self, __1: SequencerConnect.GetSynchronizerParametersRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.GetSynchronizerParametersResponse: ...
    def VerifyActive(self, __1: SequencerConnect.VerifyActiveRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.VerifyActiveResponse: ...
    def RegisterOnboardingTopologyTransactions(self, __1: SequencerConnect.RegisterOnboardingTopologyTransactionsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.RegisterOnboardingTopologyTransactionsResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerConnectServiceAsyncStub(SequencerConnectServiceStub):
    def Handshake(self, __1: SequencerConnect.HandshakeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.HandshakeResponse]: ...  # type: ignore
    def GetSynchronizerId(self, __1: SequencerConnect.GetSynchronizerIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetSynchronizerIdResponse]: ...  # type: ignore
    def GetSynchronizerParameters(self, __1: SequencerConnect.GetSynchronizerParametersRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetSynchronizerParametersResponse]: ...  # type: ignore
    def VerifyActive(self, __1: SequencerConnect.VerifyActiveRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.VerifyActiveResponse]: ...  # type: ignore
    def RegisterOnboardingTopologyTransactions(self, __1: SequencerConnect.RegisterOnboardingTopologyTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.RegisterOnboardingTopologyTransactionsResponse]: ...  # type: ignore
