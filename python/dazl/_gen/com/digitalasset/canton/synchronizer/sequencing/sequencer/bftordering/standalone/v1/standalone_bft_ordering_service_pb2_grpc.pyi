# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .standalone_bft_ordering_service_pb2 import ReadOrderedRequest, ReadOrderedResponse, SendRequest, SendResponse

__all__ = [
    "StandaloneBftOrderingServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class StandaloneBftOrderingServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _StandaloneBftOrderingServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _StandaloneBftOrderingServiceAsyncStub: ...  # type: ignore
    def Send(self, __1: SendRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SendResponse | _grpc_aio.UnaryUnaryCall[_typing.Any, SendResponse]: ...
    def ReadOrdered(self, __1: ReadOrderedRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[ReadOrderedResponse] | _grpc_aio.UnaryStreamCall[_typing.Any, ReadOrderedResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _StandaloneBftOrderingServiceBlockingStub(StandaloneBftOrderingServiceStub):
    def Send(self, __1: SendRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> SendResponse: ...
    def ReadOrdered(self, __1: ReadOrderedRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, str | bytes], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc.CallIterator[ReadOrderedResponse]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _StandaloneBftOrderingServiceAsyncStub(StandaloneBftOrderingServiceStub):
    def Send(self, __1: SendRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, SendResponse]: ...  # type: ignore
    def ReadOrdered(self, __1: ReadOrderedRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryStreamCall[_typing.Any, ReadOrderedResponse]: ...  # type: ignore
