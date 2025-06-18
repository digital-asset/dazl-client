# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_status_service_pb2 import SequencerStatusRequest, SequencerStatusResponse

__all__ = [
    "SequencerStatusServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerStatusServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerStatusServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerStatusServiceAsyncStub: ...  # type: ignore
    def SequencerStatus(self, __1: SequencerStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[SequencerStatusResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerStatusResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerStatusServiceBlockingStub(SequencerStatusServiceStub):
    def SequencerStatus(self, __1: SequencerStatusRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SequencerStatusResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerStatusServiceAsyncStub(SequencerStatusServiceStub):
    def SequencerStatus(self, __1: SequencerStatusRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SequencerStatusResponse]: ...  # type: ignore
