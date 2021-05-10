# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from io import StringIO
import itertools
from typing import Collection, Mapping, TextIO

import black
from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse
from google.protobuf.descriptor_pb2 import FileDescriptorProto

from ..archive import (
    OPTIONAL,
    REPEATED,
    EnumMeta,
    FieldMeta,
    MessageMeta,
    OneOfMeta,
    parse_archive_descriptor,
)

__all__ = ["run_plugin"]


def run_plugin(request: "CodeGeneratorRequest") -> "CodeGeneratorResponse":
    return CodeGeneratorResponse(file=[pf for fd in request.proto_file for pf in archive_files(fd)])


def archive_files(fd: "FileDescriptorProto") -> "Collection[CodeGeneratorResponse.File]":
    """
    Return the files that define a Daml-LF archive format in Python.

    :param fd:
    :return:
    """
    archive_meta = parse_archive_descriptor(fd)

    with StringIO() as buf:
        write_header(buf, True)
        for e in archive_meta.enums:
            write_enum(buf, e)
        for m in archive_meta.messages:
            write_message(buf, m, True)

        py_file = CodeGeneratorResponse.File(
            name="daml_lf_1.py",
            content=black.format_str(buf.getvalue(), mode=black.Mode()),
        )

    with StringIO() as buf:
        write_header(buf, False)
        for e in archive_meta.enums:
            write_enum(buf, e)
        for m in archive_meta.messages:
            write_message(buf, m, False)

        pyi_file = CodeGeneratorResponse.File(
            name="daml_lf_1.pyi",
            content=black.format_str(buf.getvalue(), mode=black.Mode(is_pyi=True)),
        )

    return [py_file, pyi_file]


def write_header(buf: "TextIO", write_impl: bool) -> None:
    buf.write("from enum import IntEnum as _IntEnum\n")
    buf.write("import builtins as _builtins\n")
    buf.write("import sys\n\n")

    if not write_impl:
        buf.write("import typing as _typing\n\n")
        buf.write("if sys.version_info >= (3, 8):\n")
        buf.write("    from typing import Literal as _L\n")
        buf.write("else:\n")
        buf.write("    from typing_extensions import Literal as _L\n")

        buf.write("_T = _typing.TypeVar('_T')\n\n")


def write_enum(buf: "TextIO", d: "EnumMeta") -> None:
    buf.write(f"class {d.py_short_name}(_IntEnum):\n")
    for name, value in d.fields.items():
        buf.write(f"    {name} = {value}\n")
    buf.write("\n")


def write_message(buf: "TextIO", md: "MessageMeta", write_impl: bool) -> None:
    """
    Write a Python class to the buffer that is a more Pythonic and simplified representation of a
    Daml-LF message than the Protobuf-generated files.
    """
    if md.name == "PackageRef":
        if write_impl:
            buf.write("def PackageRef(s):\n    return s\n\n")
        else:
            buf.write("PackageRef = _typing.NewType('PackageRef', str)\n\n")
        return

    buf.write("# noinspection PyShadowingBuiltins,SpellCheckingInspection\n")
    # if write_impl:
    #    buf.write(f"class _{md.name.replace('.', '_')}:\n")
    # else:
    buf.write(f"class {md.py_short_name}:\n")

    oneof_members = [m for m in md.members if isinstance(m, OneOfMeta)]
    simple_members = [
        m for m in md.members if isinstance(m, FieldMeta) and m.enclosing_type != OPTIONAL
    ]
    optional_members = [
        m for m in md.members if isinstance(m, FieldMeta) and m.enclosing_type == OPTIONAL
    ]
    fields_as_tuple = "(" + ", ".join("self." + m.py_name for m in md.members) + ")"
    other_fields_as_tuple = "(" + ", ".join("__other." + m.py_name for m in md.members) + ")"

    # in the typings file, write "inner" types sensibly
    # if not write_impl:
    if md.enums or md.members:
        with StringIO() as child_buf:
            for ed in md.enums:
                write_enum(child_buf, ed)
            for nd in md.messages:
                write_message(child_buf, nd, write_impl)

            for line in child_buf.getvalue().splitlines():
                buf.write("    " + line + "\n")

    buf.write(f"    __match_args__ = {tuple(m.py_slot_name for m in simple_members)}\n\n")

    if write_impl:
        # slots
        buf.write(f"    __slots__ = {tuple(m.py_slot_name for m in md.members)}\n")
    else:
        for m in md.members:
            buf.write(f"    @property\n")
            buf.write(f"    def {m.py_name}(self) -> {m.py_ret_type}: ...\n\n")

            if isinstance(m, OneOfMeta):
                for c in m.cases:
                    buf.write(f"    @property\n")
                    buf.write(
                        f"    def {c.py_name}(self) -> _typing.Optional[{c.py_ret_type}]: ...\n\n"
                    )

    # init
    if write_impl:
        buf.write("    def __init__(self")
        for m in simple_members:
            buf.write(", ")
            buf.write(m.py_name)
        if oneof_members:
            buf.write(", *")
            for m in oneof_members:
                for c in m.cases:
                    buf.write(", ")
                    buf.write(c.py_name)
                    buf.write("=None")
        for m in optional_members:
            buf.write(", ")
            buf.write(m.py_name)
            buf.write("=None")
        buf.write("):\n")
        if md.members:
            for m in simple_members + optional_members:
                if m.enclosing_type == REPEATED:
                    buf.write(
                        f"        object.__setattr__(self, {m.py_name!r}, _builtins.tuple({m.py_slot_name}))\n"
                    )
                else:
                    buf.write(
                        f"        object.__setattr__(self, {m.py_name!r}, {m.py_slot_name})\n"
                    )

            for m in oneof_members:
                buf.write(f"        {m.py_name} = []\n")
                for c in m.cases:
                    buf.write(f"        if {c.py_name} is not None:\n")
                    buf.write(
                        f"            object.__setattr__(self, {m.py_slot_name!r}, ({c.py_name!r}, {c.py_name}))\n"
                    )
                    buf.write(f"            {m.py_name}.append({c.py_name!r})\n")
                buf.write(f"        if len({m.py_name}) == 0:\n")
                buf.write(f"            raise ValueError('one of must be specified')\n")
                buf.write(f"        elif len({m.py_name}) > 1:\n")
                buf.write(f"            raise ValueError('cannot specify at the same time')\n")
        else:
            buf.write("        pass\n")
        buf.write("\n")

    elif oneof_members:
        ctor_prefix = "    @_typing.overload\n" "    def __init__(self\n"

        # the number of constructors is the cartesian product of all oneof groups
        for oneof_combo in itertools.product(*[m.cases for m in oneof_members]):
            buf.write(ctor_prefix)
            for m in simple_members:
                buf.write(", ")
                buf.write(m.py_name)
                buf.write(": ")
                buf.write(m.py_init_type)
            buf.write(", *")
            for m in oneof_combo:
                buf.write(", ")
                buf.write(m.py_name)
                buf.write(": ")
                buf.write(m.py_init_type)
                buf.write(" = ...")
            for m in optional_members:
                buf.write(", ")
                buf.write(m.py_name)
                buf.write(": ")
                buf.write(m.py_init_type)
                buf.write(" = ...")
            buf.write("): ...\n")
    else:
        # write a simple typing-only init declaration with no overloads
        buf.write("    def __init__(self")
        for m in md.members:
            buf.write(f", {m.py_name}: {m.py_init_type}")
        buf.write("): ...\n")

    for oneof in oneof_members:
        write_oneof_match_impl(buf, oneof, write_impl)

    # other special functions
    if write_impl:
        # If we declared sum type fields as properties in a more sane way, PyCharm annoyingly
        # insists on evaluating and displaying all of them in the debugger. For the 'oneof' fields,
        # this is more than a little annoying. So instead, implement the convenience 'oneof'
        # properties as __getattr__ to hide them from PyCharm.
        if any(isinstance(m, OneOfMeta) for m in md.members):
            buf.write("    def __getattr__(self, name):\n")
            for m in md.members:
                if isinstance(m, OneOfMeta):
                    buf.write(f"        if self.{m.py_slot_name}[0] == name:\n")
                    buf.write(f"            return self.{m.py_slot_name}[1]\n")
                    buf.write("        raise AttributeError\n\n")

        buf.write("    def __setattr__(self, name, value):\n")
        buf.write("        raise AttributeError\n\n")

        buf.write("    def __hash__(self):\n")
        buf.write(f"        return hash({fields_as_tuple})\n\n")

        buf.write("    def __eq__(self, __other):\n")
        if md.members:
            buf.write("        return ")
            buf.write(" and ".join(f"self.{m.py_name} == __other.{m.py_name}" for m in md.members))
            buf.write("\n\n")
        else:
            buf.write("        return self is __other\n\n")

        buf.write("    def __ne__(self, __other):\n")
        if md.members:
            buf.write("        return ")
            buf.write(" or ".join(f"self.{m.py_name} != __other.{m.py_name}" for m in md.members))
            buf.write("\n\n")
        else:
            buf.write("        return self is not __other\n\n")

        buf.write("    def __lt__(self, __other):\n")
        if md.members:
            buf.write(f"        return {fields_as_tuple} < {other_fields_as_tuple}\n")
        else:
            buf.write("        return False\n")

        buf.write("    def __le__(self, __other):\n")
        if md.members:
            buf.write(f"        return {fields_as_tuple} <= {other_fields_as_tuple}\n")
        else:
            buf.write("        return self is __other\n")

        buf.write("    def __gt__(self, __other):\n")
        if md.members:
            buf.write(f"        return {fields_as_tuple} > {other_fields_as_tuple}\n")
        else:
            buf.write("        return False\n")

        buf.write("    def __ge__(self, __other):\n")
        if md.members:
            buf.write(f"        return {fields_as_tuple} >= {other_fields_as_tuple}\n")
        else:
            buf.write("        return self is __other\n")

        buf.write("    def __repr__(self):\n")
        buf.write(f"        return f'{md.name}(")
        for m in md.members:
            if isinstance(m, OneOfMeta):
                buf.write("{self.")
                buf.write(m.py_slot_name)
                buf.write("[0]}={self.")
                buf.write(m.py_slot_name)
                buf.write("[1]!r}")
                buf.write(", ")
            else:
                buf.write(m.py_slot_name)
                buf.write("={self.")
                buf.write(m.py_slot_name)
                buf.write("!r}")
                buf.write(", ")
        buf.write(")'\n")

    buf.write("\n")


def write_oneof_match_impl(buf: "TextIO", oneof: "OneOfMeta", write_impl: bool):
    buf.write(f"    def {oneof.py_name}_match(self")
    for c in oneof.cases:
        buf.write(", ")
        buf.write(c.py_name)
        if not write_impl:
            buf.write(": _typing.Callable[[")
            buf.write(c.py_ret_type)
            buf.write("], _T]")

    if write_impl:
        buf.write("):\n")
        if_expr = "if"
        for c in oneof.cases:
            buf.write(f"        {if_expr} self.{oneof.py_name}[0] == {c.name!r}:")
            buf.write(f"            return {c.py_name}(self.{oneof.py_name}[1])\n")
            if_expr = "elif"
        buf.write("        else:\n")
        buf.write("            raise Exception('invalid case')\n")
    else:
        buf.write(") -> _T: ...\n")


def slots(m: Mapping[str, str]):
    d = {}
    for key in m:
        d[key.partition(".")[0]] = ""
    return tuple(d)
