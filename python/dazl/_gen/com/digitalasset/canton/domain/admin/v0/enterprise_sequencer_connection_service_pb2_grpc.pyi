# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from google.protobuf.empty_pb2 import Empty
from grpc import aio as _grpc_aio

from .enterprise_sequencer_connection_service_pb2 import GetConnectionRequest, GetConnectionResponse, SetConnectionRequest

__all__ = [
    "EnterpriseSequencerConnectionServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class EnterpriseSequencerConnectionServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _EnterpriseSequencerConnectionServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _EnterpriseSequencerConnectionServiceAsyncStub: ...  # type: ignore
    def GetConnection(self, __1: GetConnectionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetConnectionResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetConnectionResponse]]: ...
    def SetConnection(self, __1: SetConnectionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[Empty, _grpc_aio.UnaryUnaryCall[_typing.Any, Empty]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _EnterpriseSequencerConnectionServiceBlockingStub(EnterpriseSequencerConnectionServiceStub):
    def GetConnection(self, __1: GetConnectionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetConnectionResponse: ...
    def SetConnection(self, __1: SetConnectionRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> Empty: ...

# noinspection PyPep8Naming,DuplicatedCode
class _EnterpriseSequencerConnectionServiceAsyncStub(EnterpriseSequencerConnectionServiceStub):
    def GetConnection(self, __1: GetConnectionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetConnectionResponse]: ...  # type: ignore
    def SetConnection(self, __1: SetConnectionRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, Empty]: ...  # type: ignore
