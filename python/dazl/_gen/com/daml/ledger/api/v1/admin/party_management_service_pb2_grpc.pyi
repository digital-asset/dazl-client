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

from .party_management_service_pb2 import (
    AllocatePartyRequest,
    AllocatePartyResponse,
    GetParticipantIdRequest,
    GetParticipantIdResponse,
    GetPartiesRequest,
    GetPartiesResponse,
    ListKnownPartiesRequest,
    ListKnownPartiesResponse,
)

__all__ = [
    "PartyManagementServiceStub",
]

class PartyManagementServiceStub:
    @classmethod
    @overload
    def __new__(cls, channel: __Channel) -> _PartyManagementServiceStub: ...
    @classmethod
    @overload
    def __new__(cls, channel: __AsyncChannel) -> _PartyManagementServiceStub_Async: ...
    def GetParticipantId(self, __1: GetParticipantIdRequest) -> __Union[GetParticipantIdResponse, __Awaitable[GetParticipantIdResponse]]: ...
    def GetParties(self, __1: GetPartiesRequest) -> __Union[GetPartiesResponse, __Awaitable[GetPartiesResponse]]: ...
    def ListKnownParties(self, __1: ListKnownPartiesRequest) -> __Union[ListKnownPartiesResponse, __Awaitable[ListKnownPartiesResponse]]: ...
    def AllocateParty(self, __1: AllocatePartyRequest) -> __Union[AllocatePartyResponse, __Awaitable[AllocatePartyResponse]]: ...

class _PartyManagementServiceStub(PartyManagementServiceStub):
    def GetParticipantId(self, __1: GetParticipantIdRequest) -> GetParticipantIdResponse: ...
    def GetParties(self, __1: GetPartiesRequest) -> GetPartiesResponse: ...
    def ListKnownParties(self, __1: ListKnownPartiesRequest) -> ListKnownPartiesResponse: ...
    def AllocateParty(self, __1: AllocatePartyRequest) -> AllocatePartyResponse: ...

class _PartyManagementServiceStub_Async(PartyManagementServiceStub):
    def GetParticipantId(self, __1: GetParticipantIdRequest) -> __Awaitable[GetParticipantIdResponse]: ...
    def GetParties(self, __1: GetPartiesRequest) -> __Awaitable[GetPartiesResponse]: ...
    def ListKnownParties(self, __1: ListKnownPartiesRequest) -> __Awaitable[ListKnownPartiesResponse]: ...
    def AllocateParty(self, __1: AllocatePartyRequest) -> __Awaitable[AllocatePartyResponse]: ...
