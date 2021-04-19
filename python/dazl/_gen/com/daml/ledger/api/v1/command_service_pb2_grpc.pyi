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

from google.protobuf.empty_pb2 import Empty
from grpc import Channel as __Channel
from grpc.aio import Channel as __AsyncChannel

from .command_service_pb2 import (
    SubmitAndWaitForTransactionIdResponse,
    SubmitAndWaitForTransactionResponse,
    SubmitAndWaitForTransactionTreeResponse,
    SubmitAndWaitRequest,
)

__all__ = [
    "CommandServiceStub",
]

class CommandServiceStub:
    @classmethod
    @overload
    def __new__(cls, channel: __Channel) -> _CommandSubmissionServiceStub: ...
    @classmethod
    @overload
    def __new__(cls, channel: __AsyncChannel) -> _CommandSubmissionServiceStub_Async: ...
    def SubmitAndWait(self, __1: SubmitAndWaitRequest) -> __Union[Empty, __Awaitable[Empty]]: ...
    def SubmitAndWaitForTransactionId(self, __1: SubmitAndWaitRequest) -> __Union[SubmitAndWaitForTransactionIdResponse, __Awaitable[SubmitAndWaitForTransactionIdResponse]]: ...
    def SubmitAndWaitForTransaction(self, __1: SubmitAndWaitRequest) -> __Union[SubmitAndWaitForTransactionResponse, __Awaitable[SubmitAndWaitForTransactionResponse]]: ...
    def SubmitAndWaitForTransactionTree(self, __1: SubmitAndWaitRequest) -> __Union[SubmitAndWaitForTransactionTreeResponse, __Awaitable[SubmitAndWaitForTransactionTreeResponse]]: ...

class _CommandSubmissionServiceStub(CommandServiceStub):
    def SubmitAndWait(self, __1: SubmitAndWaitRequest) -> Empty: ...
    def SubmitAndWaitForTransactionId(self, __1: SubmitAndWaitRequest) -> SubmitAndWaitForTransactionIdResponse: ...
    def SubmitAndWaitForTransaction(self, __1: SubmitAndWaitRequest) -> SubmitAndWaitForTransactionResponse: ...
    def SubmitAndWaitForTransactionTree(self, __1: SubmitAndWaitRequest) -> SubmitAndWaitForTransactionTreeResponse: ...

class _CommandSubmissionServiceStub_Async(CommandServiceStub):
    def SubmitAndWait(self, __1: SubmitAndWaitRequest) -> __Awaitable[Empty]: ...
    def SubmitAndWaitForTransactionId(self, __1: SubmitAndWaitRequest) -> __Awaitable[SubmitAndWaitForTransactionIdResponse]: ...
    def SubmitAndWaitForTransaction(self, __1: SubmitAndWaitRequest) -> __Awaitable[SubmitAndWaitForTransactionResponse]: ...
    def SubmitAndWaitForTransactionTree(self, __1: SubmitAndWaitRequest) -> __Awaitable[SubmitAndWaitForTransactionTreeResponse]: ...
