# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

import typing as _typing

from grpc import Channel as __Channel
from grpc.aio import Channel as __AsyncChannel

from .ledger_identity_service_pb2 import GetLedgerIdentityRequest, GetLedgerIdentityResponse

__all__ = [
    "LedgerIdentityServiceStub",
]

class LedgerIdentityServiceStub:
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __Channel) -> _LedgerIdentityServiceStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __AsyncChannel) -> _LedgerIdentityServiceStub_Async: ...
    def GetLedgerIdentity(self, __1: GetLedgerIdentityRequest) -> _typing.Union[GetLedgerIdentityResponse, _typing.Awaitable[GetLedgerIdentityResponse]]: ...

class _LedgerIdentityServiceStub(LedgerIdentityServiceStub):
    def GetLedgerIdentity(self, __1: GetLedgerIdentityRequest) -> GetLedgerIdentityResponse: ...

class _LedgerIdentityServiceStub_Async(LedgerIdentityServiceStub):
    def GetLedgerIdentity(self, __1: GetLedgerIdentityRequest) -> _typing.Awaitable[GetLedgerIdentityResponse]: ...
