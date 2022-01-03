# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.duration_pb2 import Duration
from google.protobuf.internal.containers import RepeatedScalarFieldContainer
from google.protobuf.message import Message as _Message
from google.rpc.status_pb2 import Status

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "Completion",
]


class Completion(_Message):
    command_id: _builtins.str
    @property
    def status(self) -> Status: ...
    transaction_id: _builtins.str
    application_id: _builtins.str
    @property
    def act_as(self) -> RepeatedScalarFieldContainer[_builtins.str]: ...
    submission_id: _builtins.str
    deduplication_offset: _builtins.str
    @property
    def deduplication_duration(self) -> Duration: ...
    @_typing.overload
    def __init__(self, *, command_id: _typing.Optional[_builtins.str] = ..., status: _typing.Optional[Status] = ..., transaction_id: _typing.Optional[_builtins.str] = ..., application_id: _typing.Optional[_builtins.str] = ..., act_as: _typing.Optional[_typing.Iterable[_builtins.str]] = ..., submission_id: _typing.Optional[_builtins.str] = ...): ...
    @_typing.overload
    def __init__(self, *, command_id: _typing.Optional[_builtins.str] = ..., status: _typing.Optional[Status] = ..., transaction_id: _typing.Optional[_builtins.str] = ..., application_id: _typing.Optional[_builtins.str] = ..., act_as: _typing.Optional[_typing.Iterable[_builtins.str]] = ..., submission_id: _typing.Optional[_builtins.str] = ..., deduplication_offset: _builtins.str = ...): ...
    @_typing.overload
    def __init__(self, *, command_id: _typing.Optional[_builtins.str] = ..., status: _typing.Optional[Status] = ..., transaction_id: _typing.Optional[_builtins.str] = ..., application_id: _typing.Optional[_builtins.str] = ..., act_as: _typing.Optional[_typing.Iterable[_builtins.str]] = ..., submission_id: _typing.Optional[_builtins.str] = ..., deduplication_duration: Duration = ...): ...
    def HasField(self, field_name: _L["command_id", "status", "transaction_id", "application_id", "act_as", "submission_id", "deduplication_period", "deduplication_offset", "deduplication_duration"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["command_id", "status", "transaction_id", "application_id", "act_as", "submission_id", "deduplication_period", "deduplication_offset", "deduplication_duration"]) -> None: ...
    def WhichOneof(self, oneof_group: _L["deduplication_period"]) -> _L[None, "deduplication_offset", "deduplication_duration"]: ...
