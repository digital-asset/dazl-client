# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_authentication_service_pb2 import SequencerAuthentication

__all__ = [
    "SequencerAuthenticationServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerAuthenticationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerAuthenticationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerAuthenticationServiceAsyncStub: ...  # type: ignore
    def Challenge(self, __1: SequencerAuthentication.ChallengeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerAuthentication.ChallengeResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerAuthentication.ChallengeResponse]]: ...
    def Authenticate(self, __1: SequencerAuthentication.AuthenticateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerAuthentication.AuthenticateResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerAuthentication.AuthenticateResponse]]: ...
    def Logout(self, __1: SequencerAuthentication.LogoutRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerAuthentication.LogoutResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerAuthentication.LogoutResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerAuthenticationServiceBlockingStub(SequencerAuthenticationServiceStub):
    def Challenge(self, __1: SequencerAuthentication.ChallengeRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerAuthentication.ChallengeResponse: ...
    def Authenticate(self, __1: SequencerAuthentication.AuthenticateRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerAuthentication.AuthenticateResponse: ...
    def Logout(self, __1: SequencerAuthentication.LogoutRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerAuthentication.LogoutResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerAuthenticationServiceAsyncStub(SequencerAuthenticationServiceStub):
    def Challenge(self, __1: SequencerAuthentication.ChallengeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerAuthentication.ChallengeResponse]: ...  # type: ignore
    def Authenticate(self, __1: SequencerAuthentication.AuthenticateRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerAuthentication.AuthenticateResponse]: ...  # type: ignore
    def Logout(self, __1: SequencerAuthentication.LogoutRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerAuthentication.LogoutResponse]: ...  # type: ignore
