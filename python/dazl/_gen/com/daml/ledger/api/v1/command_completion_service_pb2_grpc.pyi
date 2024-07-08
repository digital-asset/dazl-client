# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .command_completion_service_pb2 import CompletionEndRequest, CompletionEndResponse, CompletionStreamRequest, CompletionStreamResponse

__all__ = [
    "CommandCompletionServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class CommandCompletionServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _CommandCompletionServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _CommandCompletionServiceAsyncStub: ...  # type: ignore
    def CompletionStream(self, __1: CompletionStreamRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[_grpc.CallIterator[CompletionStreamResponse], _grpc_aio.UnaryStreamCall[_typing.Any, CompletionStreamResponse]]: ...
    def CompletionEnd(self, __1: CompletionEndRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[CompletionEndResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, CompletionEndResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandCompletionServiceBlockingStub(CommandCompletionServiceStub):
    def CompletionStream(self, __1: CompletionStreamRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[CompletionStreamResponse]: ...
    def CompletionEnd(self, __1: CompletionEndRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> CompletionEndResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _CommandCompletionServiceAsyncStub(CommandCompletionServiceStub):
    def CompletionStream(self, __1: CompletionStreamRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, CompletionStreamResponse]: ...  # type: ignore
    def CompletionEnd(self, __1: CompletionEndRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, CompletionEndResponse]: ...  # type: ignore
