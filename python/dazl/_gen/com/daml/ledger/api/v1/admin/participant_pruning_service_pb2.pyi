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
    "PruneRequest",
    "PruneResponse",
]


class PruneRequest(_Message):
    prune_up_to: _builtins.str
    submission_id: _builtins.str
    prune_all_divulged_contracts: _builtins.bool
    def __init__(self, *, prune_up_to: _typing.Optional[_builtins.str] = ..., submission_id: _typing.Optional[_builtins.str] = ..., prune_all_divulged_contracts: _typing.Optional[_builtins.bool] = ...): ...
    def HasField(self, field_name: _L["prune_up_to", "submission_id", "prune_all_divulged_contracts"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["prune_up_to", "submission_id", "prune_all_divulged_contracts"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class PruneResponse(_Message):
    def __init__(self): ...
    def HasField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def ClearField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
