# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

from google.protobuf.internal.containers import RepeatedCompositeFieldContainer
from google.protobuf.message import Message as _Message

from .event_pb2 import CreatedEvent
from .trace_context_pb2 import TraceContext
from .transaction_filter_pb2 import TransactionFilter

__all__ = [
    "GetActiveContractsRequest",
    "GetActiveContractsResponse",
]


class GetActiveContractsRequest(_Message):
    ledger_id: str
    @property
    def filter(self) -> TransactionFilter: ...
    verbose: bool
    @property
    def trace_context(self) -> TraceContext: ...
    def __init__(self, *, ledger_id: _typing.Optional[str] = ..., filter: _typing.Optional[TransactionFilter] = ..., verbose: _typing.Optional[bool] = ..., trace_context: _typing.Optional[TraceContext] = ...): ...
    def HasField(self, field_name: _typing.Literal["ledger_id", "filter", "verbose", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["ledger_id", "filter", "verbose", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetActiveContractsResponse(_Message):
    offset: str
    workflow_id: str
    @property
    def active_contracts(self) -> RepeatedCompositeFieldContainer[CreatedEvent]: ...
    @property
    def trace_context(self) -> TraceContext: ...
    def __init__(self, *, offset: _typing.Optional[str] = ..., workflow_id: _typing.Optional[str] = ..., active_contracts: _typing.Optional[_typing.Iterable[CreatedEvent]] = ..., trace_context: _typing.Optional[TraceContext] = ...): ...
    def HasField(self, field_name: _typing.Literal["offset", "workflow_id", "active_contracts", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["offset", "workflow_id", "active_contracts", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
