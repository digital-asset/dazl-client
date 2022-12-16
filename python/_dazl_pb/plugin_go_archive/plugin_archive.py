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

    # create three Go modules: lf, lfexpr, and lftype
    # lf depends on nothing
    # lftype depends on lf
    # lfexpr depends on lf and lftype

    go_files = []
    for go_module in ('lf', 'lf/impl'):
        with StringIO() as buf:
            write_header(buf, go_module)
            for e in archive_meta.enums:
                write_enum(buf, e, go_module)
            for m in archive_meta.messages:
                write_message(buf, m, go_module)

            go_files.append(CodeGeneratorResponse.File(
                name=f"{go_module}/{go_module.rpartition('/')[2]}.go",
                content=buf.getvalue(),
            ))

    return go_files


def write_header(buf: "TextIO", go_module: str) -> None:
    buf.write(f"package {go_module.rpartition('/')[2]}\n\n")
    if go_module != 'lf':
        buf.write("import (\n")
        buf.write('\t"github.com/digital-asset/dazl-client/v8/go/pkg/lf"\n')
        buf.write(")\n\n")



def write_enum(buf: "TextIO", d: "EnumMeta", go_module: str) -> None:
    if go_module == "lf":
        buf.write(f"type {d.go_public_name} int\n")
        for name, value in d.fields.items():
            buf.write(f"const {d.go_public_name}{name} {d.go_public_name} = {value}\n")
        buf.write("\n")


def write_message(buf: "TextIO", md: "MessageMeta", go_module: str) -> None:
    """
    Write a Python class to the buffer that is a more Pythonic and simplified representation of a
    Daml-LF message than the Protobuf-generated files.
    """
    if go_module == "lf":
        if md.name == "PackageRef":
            buf.write("type PackageRef string\n\n")
        else:
            _write_interface(buf, md)
            for nd in md.messages:
                _write_interface(buf, nd)
    elif go_module == "lf/impl":
            _write_struct(buf, md)
            for nd in md.messages:
                _write_struct(buf, nd)


def _write_interface(buf: TextIO, md: MessageMeta) -> None:
    buf.write(f"type {md.go_public_name} interface {{\n")
    for m in md.members:
        if isinstance(m, OneOfMeta):
            enum_type_name = md.go_public_name + m.go_public_name
            buf.write(f"\t{m.go_public_name}() {enum_type_name}\n")
            for c in m.cases:
                    buf.write(f"\t{c.go_public_name}() {c.go_type}\n")
        else:
            buf.write(f"\t{m.go_public_name}() {m.go_type}\n")

    buf.write("}\n\n")

    for m in md.members:
        if isinstance(m, OneOfMeta):
            enum_type_name = md.go_public_name + m.go_public_name
            buf.write(f'type {enum_type_name} string\n')
            for c in m.cases:
                buf.write(f'const {enum_type_name}{c.go_public_name} = "{c.name}"\n')


def _write_struct(buf: TextIO, md: MessageMeta) -> None:
        buf.write(f"type {md.go_private_name} struct {{\n")
        for m in md.members:
            buf.write(f"\t{m.go_private_name} lf.{m.go_type}\n")
        buf.write("}\n\n")

        for m in md.members:
            buf.write(f"func (o *{md.go_private_name}) {m.go_public_name}() lf.{m.go_type} {{\n")
            buf.write(f"\treturn o.{m.go_private_name}\n")
            buf.write("}\n\n")
