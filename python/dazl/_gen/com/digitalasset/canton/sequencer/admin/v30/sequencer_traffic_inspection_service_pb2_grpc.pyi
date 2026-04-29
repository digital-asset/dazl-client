# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_traffic_inspection_service_pb2 import GetTrafficSummariesRequest, GetTrafficSummariesResponse

__all__ = [
    "SequencerTrafficInspectionServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerTrafficInspectionServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerTrafficInspectionServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerTrafficInspectionServiceAsyncStub: ...  # type: ignore
    def GetTrafficSummaries(self, __1: GetTrafficSummariesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetTrafficSummariesResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, GetTrafficSummariesResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerTrafficInspectionServiceBlockingStub(SequencerTrafficInspectionServiceStub):
    def GetTrafficSummaries(self, __1: GetTrafficSummariesRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetTrafficSummariesResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerTrafficInspectionServiceAsyncStub(SequencerTrafficInspectionServiceStub):
    def GetTrafficSummaries(self, __1: GetTrafficSummariesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetTrafficSummariesResponse]: ...  # type: ignore
