# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .command_completion_service_pb2 import CompletionEndRequest, CompletionEndResponse, CompletionStreamRequest, CompletionStreamResponse

__all__ = [
    "CommandCompletionServiceStub",
]

_T = _typing.TypeVar('_T')


# noinspection PyAbstractClass
class _Async(_grpc_aio.UnaryUnaryCall, _typing.Awaitable[_T]):
    pass

# noinspection PyAbstractClass
class _AsyncStream(_grpc_aio.UnaryStreamCall, _typing.AsyncIterator[_T]):
    pass


# noinspection PyPep8Naming,DuplicatedCode
class CommandCompletionServiceStub:
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _CommandCompletionServiceBlockingStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _CommandCompletionServiceAsyncStub: ...
    def CompletionStream(self, __1: CompletionStreamRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[CompletionStreamResponse], _AsyncStream[CompletionStreamResponse]]: ...
    def CompletionEnd(self, __1: CompletionEndRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[CompletionEndResponse, _Async[CompletionEndResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandCompletionServiceBlockingStub(CommandCompletionServiceStub):
    def CompletionStream(self, __1: CompletionStreamRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[CompletionStreamResponse]: ...
    def CompletionEnd(self, __1: CompletionEndRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> CompletionEndResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandCompletionServiceAsyncStub(CommandCompletionServiceStub):
    def CompletionStream(self, __1: CompletionStreamRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _AsyncStream[CompletionStreamResponse]: ...
    def CompletionEnd(self, __1: CompletionEndRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _Async[CompletionEndResponse]: ...
