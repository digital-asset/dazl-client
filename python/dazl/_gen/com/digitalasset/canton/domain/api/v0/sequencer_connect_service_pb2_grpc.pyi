# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_connect_service_pb2 import SequencerConnect
from .service_agreement_pb2 import GetServiceAgreementRequest, GetServiceAgreementResponse
from ....protocol.v0.sequencing_pb2 import Handshake

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
    def Handshake(self, __1: Handshake.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[Handshake.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, Handshake.Response]]: ...
    def GetDomainId(self, __1: SequencerConnect.GetDomainId.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.GetDomainId.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetDomainId.Response]]: ...
    def GetDomainParameters(self, __1: SequencerConnect.GetDomainParameters.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.GetDomainParameters.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetDomainParameters.Response]]: ...
    def VerifyActive(self, __1: SequencerConnect.VerifyActive.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerConnect.VerifyActive.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.VerifyActive.Response]]: ...
    def GetServiceAgreement(self, __1: GetServiceAgreementRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetServiceAgreementResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetServiceAgreementResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerConnectServiceBlockingStub(SequencerConnectServiceStub):
    def Handshake(self, __1: Handshake.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> Handshake.Response: ...
    def GetDomainId(self, __1: SequencerConnect.GetDomainId.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.GetDomainId.Response: ...
    def GetDomainParameters(self, __1: SequencerConnect.GetDomainParameters.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.GetDomainParameters.Response: ...
    def VerifyActive(self, __1: SequencerConnect.VerifyActive.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerConnect.VerifyActive.Response: ...
    def GetServiceAgreement(self, __1: GetServiceAgreementRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetServiceAgreementResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerConnectServiceAsyncStub(SequencerConnectServiceStub):
    def Handshake(self, __1: Handshake.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, Handshake.Response]: ...  # type: ignore
    def GetDomainId(self, __1: SequencerConnect.GetDomainId.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetDomainId.Response]: ...  # type: ignore
    def GetDomainParameters(self, __1: SequencerConnect.GetDomainParameters.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.GetDomainParameters.Response]: ...  # type: ignore
    def VerifyActive(self, __1: SequencerConnect.VerifyActive.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerConnect.VerifyActive.Response]: ...  # type: ignore
    def GetServiceAgreement(self, __1: GetServiceAgreementRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetServiceAgreementResponse]: ...  # type: ignore
