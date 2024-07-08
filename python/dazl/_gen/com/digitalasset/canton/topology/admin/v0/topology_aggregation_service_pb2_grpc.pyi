# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .topology_aggregation_service_pb2 import ListKeyOwnersRequest, ListKeyOwnersResponse, ListPartiesRequest, ListPartiesResponse

__all__ = [
    "TopologyAggregationServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class TopologyAggregationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _TopologyAggregationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _TopologyAggregationServiceAsyncStub: ...  # type: ignore
    def ListParties(self, __1: ListPartiesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ListPartiesResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, ListPartiesResponse]]: ...
    def ListKeyOwners(self, __1: ListKeyOwnersRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ListKeyOwnersResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, ListKeyOwnersResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _TopologyAggregationServiceBlockingStub(TopologyAggregationServiceStub):
    def ListParties(self, __1: ListPartiesRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ListPartiesResponse: ...
    def ListKeyOwners(self, __1: ListKeyOwnersRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ListKeyOwnersResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _TopologyAggregationServiceAsyncStub(TopologyAggregationServiceStub):
    def ListParties(self, __1: ListPartiesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ListPartiesResponse]: ...  # type: ignore
    def ListKeyOwners(self, __1: ListKeyOwnersRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, ListKeyOwnersResponse]: ...  # type: ignore
