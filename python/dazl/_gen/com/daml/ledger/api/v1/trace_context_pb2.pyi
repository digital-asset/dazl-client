# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

from google.protobuf.message import Message as _Message
from google.protobuf.wrappers_pb2 import UInt64Value

__all__ = [
    "TraceContext",
]


class TraceContext(_Message):
    trace_id_high: int
    trace_id: int
    span_id: int
    @property
    def parent_span_id(self) -> UInt64Value: ...
    sampled: bool
    def __init__(self, *, trace_id_high: _typing.Optional[int] = ..., trace_id: _typing.Optional[int] = ..., span_id: _typing.Optional[int] = ..., parent_span_id: _typing.Optional[UInt64Value] = ..., sampled: _typing.Optional[bool] = ...): ...
    def HasField(self, field_name: _typing.Literal["trace_id_high", "trace_id", "span_id", "parent_span_id", "sampled"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["trace_id_high", "trace_id", "span_id", "parent_span_id", "sampled"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
