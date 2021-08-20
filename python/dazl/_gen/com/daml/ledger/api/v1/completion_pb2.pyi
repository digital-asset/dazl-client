# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

from google.protobuf.message import Message as _Message
from google.rpc.status_pb2 import Status

from .trace_context_pb2 import TraceContext

__all__ = [
    "Completion",
]


class Completion(_Message):
    command_id: str
    @property
    def status(self) -> Status: ...
    transaction_id: str
    @property
    def trace_context(self) -> TraceContext: ...
    def __init__(self, *, command_id: _typing.Optional[str] = ..., status: _typing.Optional[Status] = ..., transaction_id: _typing.Optional[str] = ..., trace_context: _typing.Optional[TraceContext] = ...): ...
    def HasField(self, field_name: _typing.Literal["command_id", "status", "transaction_id", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["command_id", "status", "transaction_id", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
