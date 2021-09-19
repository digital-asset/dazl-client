# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message
from google.protobuf.wrappers_pb2 import UInt64Value

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "TraceContext",
]


class TraceContext(_Message):
    trace_id_high: _builtins.int
    trace_id: _builtins.int
    span_id: _builtins.int
    @property
    def parent_span_id(self) -> UInt64Value: ...
    sampled: _builtins.bool
    def __init__(self, *, trace_id_high: _typing.Optional[_builtins.int] = ..., trace_id: _typing.Optional[_builtins.int] = ..., span_id: _typing.Optional[_builtins.int] = ..., parent_span_id: _typing.Optional[UInt64Value] = ..., sampled: _typing.Optional[_builtins.bool] = ...): ...
    def HasField(self, field_name: _L["trace_id_high", "trace_id", "span_id", "parent_span_id", "sampled"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["trace_id_high", "trace_id", "span_id", "parent_span_id", "sampled"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
