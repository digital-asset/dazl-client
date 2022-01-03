# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.internal.containers import RepeatedCompositeFieldContainer
from google.protobuf.message import Message as _Message

from .event_pb2 import CreatedEvent
from .transaction_filter_pb2 import TransactionFilter

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "GetActiveContractsRequest",
    "GetActiveContractsResponse",
]


class GetActiveContractsRequest(_Message):
    ledger_id: _builtins.str
    @property
    def filter(self) -> TransactionFilter: ...
    verbose: _builtins.bool
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ..., filter: _typing.Optional[TransactionFilter] = ..., verbose: _typing.Optional[_builtins.bool] = ...): ...
    def HasField(self, field_name: _L["ledger_id", "filter", "verbose"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["ledger_id", "filter", "verbose"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetActiveContractsResponse(_Message):
    offset: _builtins.str
    workflow_id: _builtins.str
    @property
    def active_contracts(self) -> RepeatedCompositeFieldContainer[CreatedEvent]: ...
    def __init__(self, *, offset: _typing.Optional[_builtins.str] = ..., workflow_id: _typing.Optional[_builtins.str] = ..., active_contracts: _typing.Optional[_typing.Iterable[CreatedEvent]] = ...): ...
    def HasField(self, field_name: _L["offset", "workflow_id", "active_contracts"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["offset", "workflow_id", "active_contracts"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
