# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "LedgerOffset",
]


class LedgerOffset(_Message):
    absolute: _builtins.str
    @property
    def boundary(self) -> _L[0, 1]: ...
    @_typing.overload
    def __init__(self): ...
    @_typing.overload
    def __init__(self, *, absolute: _builtins.str = ...): ...
    @_typing.overload
    def __init__(self, *, boundary: _L['LEDGER_BEGIN', 0, 'LEDGER_END', 1] = ...): ...
    def HasField(self, field_name: _L["value", "absolute", "boundary"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["value", "absolute", "boundary"]) -> None: ...
    def WhichOneof(self, oneof_group: _L["value"]) -> _L[None, "absolute", "boundary"]: ...
