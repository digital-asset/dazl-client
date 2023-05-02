# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message

from .commands_pb2 import Commands

__all__ = [
    "SubmitRequest",
]


class SubmitRequest(_Message):
    @property
    def commands(self) -> Commands: ...
    def __init__(self, *, commands: _typing.Optional[Commands] = ...): ...
    def HasField(self, field_name: _typing.Literal["commands"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _typing.Literal["commands"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
