# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .identity_provider_config_service_pb2 import CreateIdentityProviderConfigRequest, CreateIdentityProviderConfigResponse, DeleteIdentityProviderConfigRequest, DeleteIdentityProviderConfigResponse, GetIdentityProviderConfigRequest, GetIdentityProviderConfigResponse, ListIdentityProviderConfigsRequest, ListIdentityProviderConfigsResponse, UpdateIdentityProviderConfigRequest, UpdateIdentityProviderConfigResponse

__all__ = [
    "IdentityProviderConfigServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class IdentityProviderConfigServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _IdentityProviderConfigServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _IdentityProviderConfigServiceAsyncStub: ...  # type: ignore
    def CreateIdentityProviderConfig(self, __1: CreateIdentityProviderConfigRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[CreateIdentityProviderConfigResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, CreateIdentityProviderConfigResponse]]: ...
    def GetIdentityProviderConfig(self, __1: GetIdentityProviderConfigRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetIdentityProviderConfigResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetIdentityProviderConfigResponse]]: ...
    def UpdateIdentityProviderConfig(self, __1: UpdateIdentityProviderConfigRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[UpdateIdentityProviderConfigResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, UpdateIdentityProviderConfigResponse]]: ...
    def ListIdentityProviderConfigs(self, __1: ListIdentityProviderConfigsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ListIdentityProviderConfigsResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, ListIdentityProviderConfigsResponse]]: ...
    def DeleteIdentityProviderConfig(self, __1: DeleteIdentityProviderConfigRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[DeleteIdentityProviderConfigResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, DeleteIdentityProviderConfigResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _IdentityProviderConfigServiceBlockingStub(IdentityProviderConfigServiceStub):
    def CreateIdentityProviderConfig(self, __1: CreateIdentityProviderConfigRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> CreateIdentityProviderConfigResponse: ...
    def GetIdentityProviderConfig(self, __1: GetIdentityProviderConfigRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetIdentityProviderConfigResponse: ...
    def UpdateIdentityProviderConfig(self, __1: UpdateIdentityProviderConfigRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> UpdateIdentityProviderConfigResponse: ...
    def ListIdentityProviderConfigs(self, __1: ListIdentityProviderConfigsRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ListIdentityProviderConfigsResponse: ...
    def DeleteIdentityProviderConfig(self, __1: DeleteIdentityProviderConfigRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> DeleteIdentityProviderConfigResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _IdentityProviderConfigServiceAsyncStub(IdentityProviderConfigServiceStub):
    def CreateIdentityProviderConfig(self, __1: CreateIdentityProviderConfigRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, CreateIdentityProviderConfigResponse]: ...  # type: ignore
    def GetIdentityProviderConfig(self, __1: GetIdentityProviderConfigRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetIdentityProviderConfigResponse]: ...  # type: ignore
    def UpdateIdentityProviderConfig(self, __1: UpdateIdentityProviderConfigRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, UpdateIdentityProviderConfigResponse]: ...  # type: ignore
    def ListIdentityProviderConfigs(self, __1: ListIdentityProviderConfigsRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ListIdentityProviderConfigsResponse]: ...  # type: ignore
    def DeleteIdentityProviderConfig(self, __1: DeleteIdentityProviderConfigRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, DeleteIdentityProviderConfigResponse]: ...  # type: ignore
