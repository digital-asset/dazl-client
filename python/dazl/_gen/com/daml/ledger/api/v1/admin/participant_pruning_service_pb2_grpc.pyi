# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .participant_pruning_service_pb2 import PruneRequest, PruneResponse

__all__ = [
    "ParticipantPruningServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class ParticipantPruningServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _ParticipantPruningServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _ParticipantPruningServiceAsyncStub: ...  # type: ignore
    def Prune(self, __1: PruneRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[PruneResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, PruneResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantPruningServiceBlockingStub(ParticipantPruningServiceStub):
    def Prune(self, __1: PruneRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> PruneResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantPruningServiceAsyncStub(ParticipantPruningServiceStub):
    def Prune(self, __1: PruneRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, PruneResponse]: ...  # type: ignore
