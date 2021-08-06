# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

import typing as _typing

from google.protobuf.empty_pb2 import Empty
from grpc import Channel as __Channel
from grpc.aio import Channel as __AsyncChannel

from .command_submission_service_pb2 import SubmitRequest

__all__ = [
    "CommandSubmissionServiceStub",
]

class CommandSubmissionServiceStub:
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __Channel) -> _CommandSubmissionServiceStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __AsyncChannel) -> _CommandSubmissionServiceStub_Async: ...
    def Submit(self, __1: SubmitRequest) -> _typing.Union[Empty, _typing.Awaitable[Empty]]: ...

class _CommandSubmissionServiceStub(CommandSubmissionServiceStub):
    def Submit(self, __1: SubmitRequest) -> Empty: ...

class _CommandSubmissionServiceStub_Async(CommandSubmissionServiceStub):
    def Submit(self, __1: SubmitRequest) -> _typing.Awaitable[Empty]: ...
