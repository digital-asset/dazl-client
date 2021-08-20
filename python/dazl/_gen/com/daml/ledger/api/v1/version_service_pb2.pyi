# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

from google.protobuf.message import Message as _Message

__all__ = [
    "GetLedgerApiVersionRequest",
    "GetLedgerApiVersionResponse",
]


class GetLedgerApiVersionRequest(_Message):
    ledger_id: str
    def __init__(self, *, ledger_id: _typing.Optional[str] = ...): ...
    def HasField(self, field_name: _typing.Literal["ledger_id"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["ledger_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetLedgerApiVersionResponse(_Message):
    version: str
    def __init__(self, *, version: _typing.Optional[str] = ...): ...
    def HasField(self, field_name: _typing.Literal["version"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["version"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
