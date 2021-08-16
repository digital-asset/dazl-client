# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

import typing as _typing

from grpc import Channel as __Channel, UnaryStreamMultiCallable as __UnaryStreamCall
from grpc.aio import Channel as __AsyncChannel, UnaryStreamCall as __AsyncUnaryStreamCall

from .active_contracts_service_pb2 import GetActiveContractsRequest, GetActiveContractsResponse

__all__ = [
    "ActiveContractsServiceStub",
]

class ActiveContractsServiceStub:
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __Channel) -> __ActiveContractsServiceStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __AsyncChannel) -> __ActiveContractsServiceStub_Async: ...
    def GetActiveContracts(self, __1: GetActiveContractsRequest) -> _typing.Union[__ActiveContractsServiceStub_GetActiveContracts_Response, __ActiveContractsServiceStub_GetActiveContracts_AsyncResponse]: ...

class __ActiveContractsServiceStub(ActiveContractsServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest) -> __ActiveContractsServiceStub_GetActiveContracts_Response: ...

class __ActiveContractsServiceStub_GetActiveContracts_Response(__UnaryStreamCall):
    def __iter__(self) -> _typing.Iterator[GetActiveContractsResponse]: ...

class __ActiveContractsServiceStub_Async(ActiveContractsServiceStub):
    def GetActiveContracts(self, __1: GetActiveContractsRequest) -> __ActiveContractsServiceStub_GetActiveContracts_AsyncResponse: ...

class __ActiveContractsServiceStub_GetActiveContracts_AsyncResponse(__AsyncUnaryStreamCall):
    def __aiter__(self) -> _typing.AsyncIterator[GetActiveContractsResponse]: ...
