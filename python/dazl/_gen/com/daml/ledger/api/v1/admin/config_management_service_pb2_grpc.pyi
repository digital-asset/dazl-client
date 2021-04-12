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

from .config_management_service_pb2 import (
    GetTimeModelRequest,
    GetTimeModelResponse,
    SetTimeModelRequest,
    SetTimeModelResponse,
)

__all__ = [
    "ConfigManagementServiceStub",
]

class ConfigManagementServiceStub:
    @classmethod
    @overload
    def __new__(cls, channel: __Channel) -> _ConfigManagementServiceStub: ...
    @classmethod
    @overload
    def __new__(cls, channel: __AsyncChannel) -> _ConfigManagementServiceStub_Async: ...
    def GetTimeModel(self, __1: GetTimeModelRequest) -> __Union[GetTimeModelResponse, __Awaitable[GetTimeModelResponse]]: ...
    def SetTimeModel(self, __1: SetTimeModelRequest) -> __Union[SetTimeModelResponse, __Awaitable[SetTimeModelResponse]]: ...

class _ConfigManagementServiceStub(ConfigManagementServiceStub):
    def GetTimeModel(self, __1: GetTimeModelRequest) -> GetTimeModelResponse: ...
    def SetTimeModel(self, __1: SetTimeModelRequest) -> SetTimeModelResponse: ...

class _ConfigManagementServiceStub_Async(ConfigManagementServiceStub):
    def GetTimeModel(self, __1: GetTimeModelRequest) -> __Awaitable[GetTimeModelResponse]: ...
    def SetTimeModel(self, __1: SetTimeModelRequest) -> SetTimeModelResponse: ...
