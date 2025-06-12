# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .participant_status_service_pb2 import ParticipantStatusRequest, ParticipantStatusResponse

__all__ = [
    "ParticipantStatusServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class ParticipantStatusServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _ParticipantStatusServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _ParticipantStatusServiceAsyncStub: ...  # type: ignore
    def ParticipantStatus(self, __1: ParticipantStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ParticipantStatusResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, ParticipantStatusResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantStatusServiceBlockingStub(ParticipantStatusServiceStub):
    def ParticipantStatus(self, __1: ParticipantStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ParticipantStatusResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _ParticipantStatusServiceAsyncStub(ParticipantStatusServiceStub):
    def ParticipantStatus(self, __1: ParticipantStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ParticipantStatusResponse]: ...  # type: ignore
