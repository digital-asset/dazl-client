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
    def GetDomainId(self, __1: SequencerConnect.GetDomainIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.GetDomainIdResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetDomainIdResponse]]: ...
    def GetDomainParameters(self, __1: SequencerConnect.GetDomainParametersRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.GetDomainParametersResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetDomainParametersResponse]]: ...
    def VerifyActive(self, __1: SequencerConnect.VerifyActiveRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.VerifyActiveResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.VerifyActiveResponse]]: ...
    def RegisterOnboardingTopologyTransactions(self, __1: SequencerConnect.RegisterOnboardingTopologyTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.RegisterOnboardingTopologyTransactionsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.RegisterOnboardingTopologyTransactionsResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerConnectServiceBlockingStub(SequencerConnectServiceStub):
    def Handshake(self, __1: SequencerConnect.HandshakeRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.HandshakeResponse: ...
    def GetDomainId(self, __1: SequencerConnect.GetDomainIdRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.GetDomainIdResponse: ...
    def GetDomainParameters(self, __1: SequencerConnect.GetDomainParametersRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.GetDomainParametersResponse: ...
    def VerifyActive(self, __1: SequencerConnect.VerifyActiveRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.VerifyActiveResponse: ...
    def RegisterOnboardingTopologyTransactions(self, __1: SequencerConnect.RegisterOnboardingTopologyTransactionsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.RegisterOnboardingTopologyTransactionsResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerConnectServiceAsyncStub(SequencerConnectServiceStub):
    def Handshake(self, __1: SequencerConnect.HandshakeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.HandshakeResponse]: ...  # type: ignore
    def GetDomainId(self, __1: SequencerConnect.GetDomainIdRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetDomainIdResponse]: ...  # type: ignore
    def GetDomainParameters(self, __1: SequencerConnect.GetDomainParametersRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetDomainParametersResponse]: ...  # type: ignore
    def VerifyActive(self, __1: SequencerConnect.VerifyActiveRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.VerifyActiveResponse]: ...  # type: ignore
    def RegisterOnboardingTopologyTransactions(self, __1: SequencerConnect.RegisterOnboardingTopologyTransactionsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.RegisterOnboardingTopologyTransactionsResponse]: ...  # type: ignore
