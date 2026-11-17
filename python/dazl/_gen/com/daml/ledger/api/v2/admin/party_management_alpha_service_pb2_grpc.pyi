# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .party_management_alpha_service_pb2 import AuthorizePartyUpdateRequest, AuthorizePartyUpdateResponse, GeneratePartyTopologyUpdateRequest, GeneratePartyTopologyUpdateResponse, GetAddPartyStatusRequest, GetAddPartyStatusResponse

__all__ = [
    "PartyManagementAlphaServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class PartyManagementAlphaServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _PartyManagementAlphaServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _PartyManagementAlphaServiceAsyncStub: ...  # type: ignore
    def GeneratePartyTopologyUpdate(self, __1: GeneratePartyTopologyUpdateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GeneratePartyTopologyUpdateResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, GeneratePartyTopologyUpdateResponse]: ...
    def AuthorizePartyUpdate(self, __1: AuthorizePartyUpdateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AuthorizePartyUpdateResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, AuthorizePartyUpdateResponse]: ...
    def GetAddPartyStatus(self, __1: GetAddPartyStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetAddPartyStatusResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, GetAddPartyStatusResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyManagementAlphaServiceBlockingStub(PartyManagementAlphaServiceStub):
    def GeneratePartyTopologyUpdate(self, __1: GeneratePartyTopologyUpdateRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GeneratePartyTopologyUpdateResponse: ...
    def AuthorizePartyUpdate(self, __1: AuthorizePartyUpdateRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> AuthorizePartyUpdateResponse: ...
    def GetAddPartyStatus(self, __1: GetAddPartyStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetAddPartyStatusResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PartyManagementAlphaServiceAsyncStub(PartyManagementAlphaServiceStub):
    def GeneratePartyTopologyUpdate(self, __1: GeneratePartyTopologyUpdateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GeneratePartyTopologyUpdateResponse]: ...  # type: ignore
    def AuthorizePartyUpdate(self, __1: AuthorizePartyUpdateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, AuthorizePartyUpdateResponse]: ...  # type: ignore
    def GetAddPartyStatus(self, __1: GetAddPartyStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetAddPartyStatusResponse]: ...  # type: ignore
