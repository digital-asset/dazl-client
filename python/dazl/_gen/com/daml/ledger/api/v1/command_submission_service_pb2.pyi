# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message

from .commands_pb2 import Commands

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "SubmitRequest",
]


class SubmitRequest(_Message):
    @property
    def commands(self) -> Commands: ...
    def __init__(self, *, commands: _typing.Optional[Commands] = ...): ...
    def HasField(self, field_name: _L["commands"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["commands"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
