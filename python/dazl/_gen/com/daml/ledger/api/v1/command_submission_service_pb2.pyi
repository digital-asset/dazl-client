# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

from google.protobuf.message import Message as _Message

from .commands_pb2 import Commands
from .trace_context_pb2 import TraceContext

__all__ = [
    "SubmitRequest",
]


class SubmitRequest(_Message):
    @property
    def commands(self) -> Commands: ...
    @property
    def trace_context(self) -> TraceContext: ...
    def __init__(self, *, commands: _typing.Optional[Commands] = ..., trace_context: _typing.Optional[TraceContext] = ...): ...
    def HasField(self, field_name: _typing.Literal["commands", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["commands", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
