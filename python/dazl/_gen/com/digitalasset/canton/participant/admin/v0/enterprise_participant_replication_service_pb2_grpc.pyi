# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .enterprise_participant_replication_service_pb2 import SetPassive

__all__ = [
    "EnterpriseParticipantReplicationServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class EnterpriseParticipantReplicationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _EnterpriseParticipantReplicationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _EnterpriseParticipantReplicationServiceAsyncStub: ...  # type: ignore
    def SetPassive(self, __1: SetPassive.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SetPassive.Response, _grpc_aio.UnaryUnaryCall[_typing.Any, SetPassive.Response]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _EnterpriseParticipantReplicationServiceBlockingStub(EnterpriseParticipantReplicationServiceStub):
    def SetPassive(self, __1: SetPassive.Request, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SetPassive.Response: ...

# noinspection PyPep8Naming,DuplicatedCode
class _EnterpriseParticipantReplicationServiceAsyncStub(EnterpriseParticipantReplicationServiceStub):
    def SetPassive(self, __1: SetPassive.Request, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SetPassive.Response]: ...  # type: ignore
