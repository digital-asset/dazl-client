# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from io import StringIO
from itertools import product
import json
from keyword import iskeyword
import os.path
from typing import Dict, TextIO

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse
from google.protobuf.descriptor_pb2 import DescriptorProto, EnumDescriptorProto, FileDescriptorProto

from ..syntax.python import ImportContext, SymbolTable, Usage, all_decl, py_message_package
from ._header import HEADER

__all__ = ["run_plugin", "typing_file"]


def run_plugin(request: "CodeGeneratorRequest") -> "CodeGeneratorResponse":
    """
    Generate .pyi (typing stubs files) for Protobuf objects.
    """
    # build a mapping of all types that we'll ever need to generate any of the requested files
    symbol_table = SymbolTable()
    for fd in request.proto_file:
        symbol_table.load_file(fd)

    return CodeGeneratorResponse(
        file=[
            typing_file(pf, ImportContext(symbol_table))
            for pf in request.proto_file
            if pf.name in request.file_to_generate
        ]
    )


def typing_file(fd: "FileDescriptorProto", ictx: "ImportContext") -> "CodeGeneratorResponse.File":
    name = os.path.splitext(fd.name)[0] + "_pb2.pyi"

    # first, generate all message and enum bodies
    with StringIO() as buf:
        for ed in fd.enum_type:
            write_enum(buf, ed, ictx)

        for md in fd.message_type:
            write_message(buf, md, ictx)

        body = buf.getvalue()

    # once we know all of the enums/messages that we want to write, put together the set of imports
    ictx.add_system_import("", "builtins as _builtins")
    ictx.add_system_import("", "sys")
    ictx.add_system_import("", "typing as _typing")

    imports = ictx.py_import_block(py_message_package(fd.name))
    imports += (
        "\nif sys.version_info >= (3, 8):\n"
        "    from typing import Literal as _L\n"
        "else:\n"
        "    from typing_extensions import Literal as _L\n"
    )

    all_str = all_decl(md.name for md in fd.message_type)

    return CodeGeneratorResponse.File(name=name, content=f"{HEADER}\n{imports}\n{all_str}\n{body}")


def write_enum(buf: "TextIO", d: "EnumDescriptorProto", ictx: "ImportContext") -> None:
    ictx.add_import("google.protobuf.descriptor", "EnumDescriptor")

    buf.write(f"class {d.name}:\n")
    buf.write(f"    DESCRIPTOR: _typing.ClassVar[EnumDescriptor] = ...\n")
    for v in d.value:
        buf.write(f"    {v.name}: _typing.ClassVar[_L[{v.number}]] = ...\n")
    for v in d.value:
        buf.write(f"{v.name} = _L[{v.number}]\n")
    buf.write("\n")


def write_message(buf: "TextIO", md: "DescriptorProto", ictx: "ImportContext") -> None:
    if md.options.map_entry:
        # map types are represented as auto-generated messages;
        # there is nothing to emit for these types
        return

    ictx.add_import("google.protobuf.message", "Message as _Message")

    buf.write("\n")
    buf.write(f"class {md.name}(_Message):\n")

    # Write any nested messages first.
    if md.nested_type:
        with StringIO() as child_buf:
            for ed in md.enum_type:
                write_enum(child_buf, ed, ictx)
            for nd in md.nested_type:
                write_message(child_buf, nd, ictx)

            for line in child_buf.getvalue().splitlines():
                buf.write(f"    {line}\n")

    # Write fields.
    for fld in md.field:
        if not iskeyword(fld.name):
            py_type = ictx.py_type(fld, Usage.GETTER)
            if py_type.settable:
                buf.write(f"    {fld.name}: {py_type.py_str}\n")
            else:
                buf.write(f"    @property\n")
                buf.write(f"    def {fld.name}(self) -> {py_type.py_str}: ...\n")

    # for each oneof group that we have, generate a list of field names that represent the possible
    # options; also include an empty string which indicates the constructor that leaves out this
    # argument altogether
    oneof_groups = {
        od.name: [
            "",
            *(fld.name for fld in md.field if fld.HasField("oneof_index") and fld.oneof_index == i),
        ]
        for i, od in enumerate(md.oneof_decl)
    }

    # The constructor cannot include any arguments that are Python keywords. Callers can use kwargs
    # to pass in that information, but unfortunately there does not appear to be a good way to
    # expose that information, even through pyi files.
    #
    # Consequently we only generate permutations of constructors for combinations where arguments
    # are not Python keywords.
    oneof_field_names_groups = list(
        product(*[[f for f in g if not iskeyword(f)] for g in oneof_groups.values()])
    )
    for oneof_field_names in oneof_field_names_groups:
        init_fields = [
            fld
            for fld in md.field
            if not iskeyword(fld.name)
            and (not fld.HasField("oneof_index") or oneof_field_names[fld.oneof_index] == fld.name)
        ]
        self_name = "self"
        while self_name in [f.name for f in init_fields]:
            self_name += "_"

        if len(oneof_field_names_groups) > 1:
            buf.write("    @_typing.overload\n")

        if init_fields:
            buf.write(f"    def __init__({self_name}, *")

            for fld in init_fields:
                py_type = ictx.py_type(fld, Usage.INIT)
                buf.write(f", {fld.name}: {py_type.py_str} = ...")
            buf.write("): ...\n")
        else:
            buf.write(f"    def __init__(self): ...\n")

    if md.field:
        # We're using a dictionary here as a cheap order-preserving set, since Python dictionaries
        # preserve insertion order (which is important to us here).
        field_names = {}  # type: Dict[str, None]
        for fld in md.field:
            if fld.HasField("oneof_index"):
                field_names[md.oneof_decl[fld.oneof_index].name] = None
            field_names[fld.name] = None
        field_names_str = ", ".join(json.dumps(fld) for fld in field_names)
        args = f"self, field_name: _L[{field_names_str}]"
        buf.write(f"    def HasField({args}) -> _builtins.bool: ...\n")
        buf.write(f"    def ClearField({args}) -> None: ...\n")
    else:
        args = f"self, field_name: _typing.NoReturn"
        buf.write(f"    def HasField({args}) -> _typing.NoReturn: ...\n")
        buf.write(f"    def ClearField({args}) -> _typing.NoReturn: ...\n")

    if oneof_groups:
        for oneof_group_name, oneof_group_fields in oneof_groups.items():
            if len(oneof_groups) > 1:
                buf.write("    @_typing.overload\n")
            args = f'self, oneof_group: _L["{oneof_group_name}"]'
            ret = f"_L[{', '.join(json.dumps(f) if f else 'None' for f in oneof_group_fields)}]"
            buf.write(f"    def WhichOneof({args}) -> {ret}: ...\n")
    else:
        args = "self, oneof_group: _typing.NoReturn"
        ret = "_typing.NoReturn"
        buf.write(f"    def WhichOneof({args}) -> {ret}: ...\n")
