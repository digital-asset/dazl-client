# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol


class Type(Protocol):
    @property
    def go_rep(self) -> str:
        ...

    @property
    def py_rep(self) -> str:
        ...


class PrimType:
    def __init__(self, t: str, *, go_rep: str = None, py_rep: str = None):
        self._t = t
        self.go_rep = go_rep if go_rep is not None else t
        self.py_rep = py_rep if py_rep is not None else t

    def __str__(self):
        return self._t


class EnumOrMessageType:
    def __init__(self, t: str, *, go_rep: str = None, py_rep: str = None):
        from ..syntax import go

        self._t = t
        self.go_rep = go_rep if go_rep is not None else go.public_name(t)
        self.py_rep = py_rep


Enum = EnumOrMessageType
Message = EnumOrMessageType


BOOL = PrimType("Bool", py_rep="bool", go_rep="bool")
INT32 = PrimType("Int32", py_rep="int", go_rep="int32")
SINT32 = PrimType("SInt32", py_rep="int", go_rep="int32")
UINT32 = PrimType("UInt32", py_rep="int", go_rep="uint32")
INT64 = PrimType("Int64", py_rep="int", go_rep="int64")
SINT64 = PrimType("SInt64", py_rep="int", go_rep="int64")
UINT64 = PrimType("UInt64", py_rep="int", go_rep="uint64")
FLOAT = PrimType("Float", py_rep="float", go_rep="float32")
FIXED32 = PrimType("Fixed32", py_rep="float", go_rep="float32")
SFIXED32 = PrimType("SFixed32", py_rep="float", go_rep="float32")
FIXED64 = PrimType("Fixed64", py_rep="float", go_rep="float64")
SFIXED64 = PrimType("SFixed64", py_rep="float", go_rep="float64")
DOUBLE = PrimType("Double", py_rep="float", go_rep="float64")
BYTES = PrimType("Bytes", py_rep="bytes", go_rep="[]byte")
STRING = PrimType("String", py_rep="str", go_rep="string")
DOTTED_NAME = PrimType("DottedName", py_rep="DottedName", go_rep="DottedName")


class Seq:
    def __init__(self, arg: "Type"):
        self.arg = arg

    @property
    def go_rep(self) -> str:
        return f"[]{self.arg.go_rep}"

    @property
    def py_rep(self) -> str:
        return f"_typing.Sequence[{self.arg.py_rep}]"


class Map:
    def __init__(self, key_arg: "Type", value_arg: "Type"):
        self.key_arg = key_arg
        self.value_arg = value_arg

    @property
    def go_rep(self) -> str:
        return f"map[{self.key_arg.go_rep}]{self.value_arg.go_rep}"

    @property
    def py_rep(self) -> str:
        return f"_typing.Mapping[{self.key_arg.py_rep}, {self.value_arg.py_rep}]"


class Optional:
    def __init__(self, arg: "Type"):
        self.arg = arg

    @property
    def go_rep(self) -> str:
        return f"*{self.arg.go_rep}"

    @property
    def py_rep(self) -> str:
        return f"_typing.Optional[{self.arg.py_rep}]"

    def __str__(self):
        return f"{self.arg}?"
