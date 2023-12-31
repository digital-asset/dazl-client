# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .service_agreement_pb2 import GetServiceAgreementRequest, GetServiceAgreementResponse

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
    def GetServiceAgreement(self, __1: GetServiceAgreementRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetServiceAgreementResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetServiceAgreementResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainServiceBlockingStub(DomainServiceStub):
    def GetServiceAgreement(self, __1: GetServiceAgreementRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetServiceAgreementResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _DomainServiceAsyncStub(DomainServiceStub):
    def GetServiceAgreement(self, __1: GetServiceAgreementRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetServiceAgreementResponse]: ...  # type: ignore
