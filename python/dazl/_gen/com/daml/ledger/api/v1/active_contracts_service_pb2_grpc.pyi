# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

from typing import AsyncIterable as __AsyncStream, Iterable as __Stream, Union as __Union, overload

from grpc import Channel as __Channel
from grpc.aio import Channel as __AsyncChannel

from .active_contracts_service_pb2 import GetActiveContractsRequest, GetActiveContractsResponse

__all__ = [
    "ActiveContractsServiceStub",
]

class ActiveContractsServiceStub:
    @classmethod
    @overload
    def __new__(cls, channel: __Channel) -> _ActiveContractsServiceStub: ...
    @classmethod
    @overload
    def __new__(cls, channel: __AsyncChannel) -> _ActiveContractsServiceStub_Async: ...
    def GetActiveContracts(self, __1: GetActiveContractsRequest) -> __Union[__Stream[GetActiveContractsResponse], __AsyncStream[GetActiveContractsResponse]]: ...

class _ActiveContractsServiceStub(ActiveContractsServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest) -> __Stream[GetActiveContractsResponse]: ...

class _ActiveContractsServiceStub_Async(ActiveContractsServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest) -> __AsyncStream[GetActiveContractsResponse]: ...
