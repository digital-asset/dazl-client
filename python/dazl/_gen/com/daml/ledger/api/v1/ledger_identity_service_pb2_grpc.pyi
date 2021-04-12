# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

from typing import (
    AsyncIterable as __AsyncStream,
    Awaitable as __Awaitable,
    Iterable as __Stream,
    Union as __Union,
    overload,
)

from grpc import Channel as __Channel
from grpc.aio import Channel as __AsyncChannel

from .ledger_identity_service_pb2 import GetLedgerIdentityRequest, GetLedgerIdentityResponse

__all__ = [
    "LedgerIdentityServiceStub",
]

class LedgerIdentityServiceStub:
    @classmethod
    @overload
    def __new__(cls, channel: __Channel) -> _LedgerIdentityServiceStub: ...
    @classmethod
    @overload
    def __new__(cls, channel: __AsyncChannel) -> _LedgerIdentityServiceStub_Async: ...
    def GetLedgerIdentity(self, __1: GetLedgerIdentityRequest) -> __Union[GetLedgerIdentityResponse, __Awaitable[GetLedgerIdentityResponse]]: ...

class _LedgerIdentityServiceStub(LedgerIdentityServiceStub):
    def GetLedgerIdentity(self, __1: GetLedgerIdentityRequest) -> GetLedgerIdentityResponse: ...

class _LedgerIdentityServiceStub_Async(LedgerIdentityServiceStub):
    def GetLedgerIdentity(self, __1: GetLedgerIdentityRequest) -> __Awaitable[GetLedgerIdentityResponse]: ...
