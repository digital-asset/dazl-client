# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

import typing as _typing

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
    @_typing.overload
    def __new__(cls, channel: __Channel) -> _ConfigManagementServiceStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __AsyncChannel) -> _ConfigManagementServiceStub_Async: ...
    def GetTimeModel(self, __1: GetTimeModelRequest) -> _typing.Union[GetTimeModelResponse, _typing.Awaitable[GetTimeModelResponse]]: ...
    def SetTimeModel(self, __1: SetTimeModelRequest) -> _typing.Union[SetTimeModelResponse, _typing.Awaitable[SetTimeModelResponse]]: ...

class _ConfigManagementServiceStub(ConfigManagementServiceStub):
    def GetTimeModel(self, __1: GetTimeModelRequest) -> GetTimeModelResponse: ...
    def SetTimeModel(self, __1: SetTimeModelRequest) -> SetTimeModelResponse: ...

class _ConfigManagementServiceStub_Async(ConfigManagementServiceStub):
    def GetTimeModel(self, __1: GetTimeModelRequest) -> _typing.Awaitable[GetTimeModelResponse]: ...
    def SetTimeModel(self, __1: SetTimeModelRequest) -> SetTimeModelResponse: ...
