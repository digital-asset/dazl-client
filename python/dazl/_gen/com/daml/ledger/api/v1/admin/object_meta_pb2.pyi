# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.internal.containers import MessageMap
from google.protobuf.message import Message as _Message

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "ObjectMeta",
]


class ObjectMeta(_Message):
    resource_version: _builtins.str
    @property
    def annotations(self) -> MessageMap[_builtins.str, _builtins.str]: ...
    def __init__(self, *, resource_version: _typing.Optional[_builtins.str] = ..., annotations: _typing.Optional[_typing.Mapping[_builtins.str, _builtins.str]] = ...): ...
    def HasField(self, field_name: _L["resource_version", "annotations"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["resource_version", "annotations"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
