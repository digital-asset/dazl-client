# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_version_service_pb2 import SequencerVersion

__all__ = [
    "SequencerVersionServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerVersionServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerVersionServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerVersionServiceAsyncStub: ...  # type: ignore
    def Handshake(self, __1: SequencerVersion.HandshakeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerVersion.HandshakeResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerVersion.HandshakeResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerVersionServiceBlockingStub(SequencerVersionServiceStub):
    def Handshake(self, __1: SequencerVersion.HandshakeRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerVersion.HandshakeResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerVersionServiceAsyncStub(SequencerVersionServiceStub):
    def Handshake(self, __1: SequencerVersion.HandshakeRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerVersion.HandshakeResponse]: ...  # type: ignore
