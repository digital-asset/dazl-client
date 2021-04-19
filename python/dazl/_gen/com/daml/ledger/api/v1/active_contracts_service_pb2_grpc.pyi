# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

from typing import (
    AsyncIterable as __AsyncStream,
    AsyncIterator as __AsyncIterator,
    Iterable as __Stream,
    Iterator as __Iterator,
    Union as __Union,
    overload,
)

from grpc import Channel as __Channel, UnaryStreamMultiCallable as __UnaryStreamCall
from grpc.aio import Channel as __AsyncChannel, UnaryStreamCall as __AsyncUnaryStreamCall

from .active_contracts_service_pb2 import GetActiveContractsRequest, GetActiveContractsResponse

__all__ = [
    "ActiveContractsServiceStub",
]

class ActiveContractsServiceStub:
    @classmethod
    @overload
    def __new__(cls, channel: __Channel) -> __ActiveContractsServiceStub: ...
    @classmethod
    @overload
    def __new__(cls, channel: __AsyncChannel) -> __ActiveContractsServiceStub_Async: ...
    def GetActiveContracts(self, __1: GetActiveContractsRequest) -> __Union[__ActiveContractsServiceStub_GetActiveContracts_Response, __ActiveContractsServiceStub_GetActiveContracts_AsyncResponse]: ...

class __ActiveContractsServiceStub(ActiveContractsServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest) -> __ActiveContractsServiceStub_GetActiveContracts_Response: ...

class __ActiveContractsServiceStub_GetActiveContracts_Response(__UnaryStreamCall):
    def __iter__(self) -> __Iterator[GetActiveContractsResponse]: ...

class __ActiveContractsServiceStub_Async(ActiveContractsServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest) -> __ActiveContractsServiceStub_GetActiveContracts_AsyncResponse: ...

class __ActiveContractsServiceStub_GetActiveContracts_AsyncResponse(__AsyncUnaryStreamCall):
    def __aiter__(self) -> __AsyncIterator[GetActiveContractsResponse]: ...
