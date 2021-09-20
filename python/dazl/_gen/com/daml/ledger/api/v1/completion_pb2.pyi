# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message
from google.rpc.status_pb2 import Status

from .trace_context_pb2 import TraceContext

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
    @property
    def trace_context(self) -> TraceContext: ...
    def __init__(self, *, command_id: _typing.Optional[_builtins.str] = ..., status: _typing.Optional[Status] = ..., transaction_id: _typing.Optional[_builtins.str] = ..., trace_context: _typing.Optional[TraceContext] = ...): ...
    def HasField(self, field_name: _L["command_id", "status", "transaction_id", "trace_context"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["command_id", "status", "transaction_id", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
