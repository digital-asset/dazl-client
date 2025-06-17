# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_channel_service_pb2 import ConnectToSequencerChannelRequest, ConnectToSequencerChannelResponse, PingRequest, PingResponse

__all__ = [
    "SequencerChannelServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerChannelServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerChannelServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerChannelServiceAsyncStub: ...  # type: ignore
    def ConnectToSequencerChannel(self, __1: _typing.Iterable[ConnectToSequencerChannelRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[ConnectToSequencerChannelResponse], _grpc_aio.UnaryStreamCall[_typing.Any, ConnectToSequencerChannelResponse]]: ...
    def Ping(self, __1: PingRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[PingResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, PingResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerChannelServiceBlockingStub(SequencerChannelServiceStub):
    def ConnectToSequencerChannel(self, __1: _typing.Iterable[ConnectToSequencerChannelRequest], timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[ConnectToSequencerChannelResponse]: ...
    def Ping(self, __1: PingRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> PingResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerChannelServiceAsyncStub(SequencerChannelServiceStub):
    def ConnectToSequencerChannel(self, __1: _typing.Iterable[ConnectToSequencerChannelRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, ConnectToSequencerChannelResponse]: ...  # type: ignore
    def Ping(self, __1: PingRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, PingResponse]: ...  # type: ignore
