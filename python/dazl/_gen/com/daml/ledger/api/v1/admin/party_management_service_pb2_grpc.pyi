# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

import typing as _typing

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
    @_typing.overload
    def __new__(cls, channel: __Channel) -> _PartyManagementServiceStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __AsyncChannel) -> _PartyManagementServiceStub_Async: ...
    def GetParticipantId(self, __1: GetParticipantIdRequest) -> _typing.Union[GetParticipantIdResponse, _typing.Awaitable[GetParticipantIdResponse]]: ...
    def GetParties(self, __1: GetPartiesRequest) -> _typing.Union[GetPartiesResponse, _typing.Awaitable[GetPartiesResponse]]: ...
    def ListKnownParties(self, __1: ListKnownPartiesRequest) -> _typing.Union[ListKnownPartiesResponse, _typing.Awaitable[ListKnownPartiesResponse]]: ...
    def AllocateParty(self, __1: AllocatePartyRequest) -> _typing.Union[AllocatePartyResponse, _typing.Awaitable[AllocatePartyResponse]]: ...

class _PartyManagementServiceStub(PartyManagementServiceStub):
    def GetParticipantId(self, __1: GetParticipantIdRequest) -> GetParticipantIdResponse: ...
    def GetParties(self, __1: GetPartiesRequest) -> GetPartiesResponse: ...
    def ListKnownParties(self, __1: ListKnownPartiesRequest) -> ListKnownPartiesResponse: ...
    def AllocateParty(self, __1: AllocatePartyRequest) -> AllocatePartyResponse: ...

class _PartyManagementServiceStub_Async(PartyManagementServiceStub):
    def GetParticipantId(self, __1: GetParticipantIdRequest) -> _typing.Awaitable[GetParticipantIdResponse]: ...
    def GetParties(self, __1: GetPartiesRequest) -> _typing.Awaitable[GetPartiesResponse]: ...
    def ListKnownParties(self, __1: ListKnownPartiesRequest) -> _typing.Awaitable[ListKnownPartiesResponse]: ...
    def AllocateParty(self, __1: AllocatePartyRequest) -> _typing.Awaitable[AllocatePartyResponse]: ...
