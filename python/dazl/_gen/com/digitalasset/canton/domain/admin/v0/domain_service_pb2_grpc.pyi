# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from google.protobuf.empty_pb2 import Empty
from grpc import aio as _grpc_aio

from .domain_service_pb2 import GetDomainParameters, ServiceAgreementAcceptances
from ....protocol.v0.sequencing_pb2 import StaticDomainParameters

__all__ = [
    "DomainServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class DomainServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _DomainServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _DomainServiceAsyncStub: ...  # type: ignore
    def ListServiceAgreementAcceptances(self, __1: Empty, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ServiceAgreementAcceptances, _grpc_aio.UnaryUnaryCall[_typing.Any, ServiceAgreementAcceptances]]: ...
    def GetDomainParametersVersioned(self, __1: GetDomainParameters.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetDomainParameters.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, GetDomainParameters.Response]]: ...
    def GetDomainParameters(self, __1: Empty, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[StaticDomainParameters, _grpc_aio.UnaryUnaryCall[_typing.Any, StaticDomainParameters]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainServiceBlockingStub(DomainServiceStub):
    def ListServiceAgreementAcceptances(self, __1: Empty, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ServiceAgreementAcceptances: ...
    def GetDomainParametersVersioned(self, __1: GetDomainParameters.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetDomainParameters.Response: ...
    def GetDomainParameters(self, __1: Empty, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> StaticDomainParameters: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainServiceAsyncStub(DomainServiceStub):
    def ListServiceAgreementAcceptances(self, __1: Empty, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ServiceAgreementAcceptances]: ...  # type: ignore
    def GetDomainParametersVersioned(self, __1: GetDomainParameters.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetDomainParameters.Response]: ...  # type: ignore
    def GetDomainParameters(self, __1: Empty, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, StaticDomainParameters]: ...  # type: ignore
