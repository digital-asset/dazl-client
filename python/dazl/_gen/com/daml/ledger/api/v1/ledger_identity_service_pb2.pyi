# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

from google.protobuf.message import Message as _Message

from .trace_context_pb2 import TraceContext

__all__ = [
    "GetLedgerIdentityRequest",
    "GetLedgerIdentityResponse",
]


class GetLedgerIdentityRequest(_Message):
    @property
    def trace_context(self) -> TraceContext: ...
    def __init__(self, *, trace_context: _typing.Optional[TraceContext] = ...): ...
    def HasField(self, field_name: _typing.Literal["trace_context"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetLedgerIdentityResponse(_Message):
    ledger_id: str
    def __init__(self, *, ledger_id: _typing.Optional[str] = ...): ...
    def HasField(self, field_name: _typing.Literal["ledger_id"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["ledger_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
