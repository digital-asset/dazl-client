# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message


__all__ = [
    "ResetRequest",
]


class ResetRequest(_Message):
    ledger_id: _builtins.str
    def __init__(self, *, ledger_id: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _typing.Literal["ledger_id"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _typing.Literal["ledger_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
