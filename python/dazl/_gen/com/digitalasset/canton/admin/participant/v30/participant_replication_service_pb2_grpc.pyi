# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .participant_replication_service_pb2 import SetPassiveRequest, SetPassiveResponse

__all__ = [
    "ParticipantReplicationServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class ParticipantReplicationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _ParticipantReplicationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _ParticipantReplicationServiceAsyncStub: ...  # type: ignore
    def SetPassive(self, __1: SetPassiveRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SetPassiveResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, SetPassiveResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantReplicationServiceBlockingStub(ParticipantReplicationServiceStub):
    def SetPassive(self, __1: SetPassiveRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SetPassiveResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantReplicationServiceAsyncStub(ParticipantReplicationServiceStub):
    def SetPassive(self, __1: SetPassiveRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SetPassiveResponse]: ...  # type: ignore
