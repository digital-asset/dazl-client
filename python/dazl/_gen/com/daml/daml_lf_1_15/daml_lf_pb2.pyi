# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.descriptor import EnumDescriptor
from google.protobuf.message import Message as _Message

from .daml_lf_1_pb2 import Package

__all__ = [
    "ArchivePayload",
    "Archive",
]

class HashFunction:
    DESCRIPTOR: _typing.ClassVar[EnumDescriptor] = ...
    SHA256: _typing.ClassVar[_typing.Literal[0]] = ...
SHA256 = _typing.Literal[0]


class ArchivePayload(_Message):
    minor: _builtins.str
    @property
    def daml_lf_1(self) -> Package: ...
    @_typing.overload
    def __init__(self, *, minor: _typing.Optional[_builtins.str] = ...): ...
    @_typing.overload
    def __init__(self, *, minor: _typing.Optional[_builtins.str] = ..., daml_lf_1: Package = ...): ...
    def HasField(self, field_name: _typing.Literal["minor", "Sum", "daml_lf_1"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _typing.Literal["minor", "Sum", "daml_lf_1"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.Literal["Sum"]) -> _typing.Literal[None, "daml_lf_1"]: ...

class Archive(_Message):
    hash_function: _typing.Literal[0]
    payload: _builtins.bytes
    hash: _builtins.str
    def __init__(self, *, hash_function: _typing.Optional[_typing.Literal['SHA256', 0]] = ..., payload: _typing.Optional[_builtins.bytes] = ..., hash: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _typing.Literal["hash_function", "payload", "hash"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _typing.Literal["hash_function", "payload", "hash"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
