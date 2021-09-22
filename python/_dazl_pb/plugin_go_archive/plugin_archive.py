# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import Sequence, defaultdict
from io import StringIO
from typing import Collection, DefaultDict, List, TextIO, Union

from google.protobuf.compiler.plugin_pb2 import CodeGeneratorRequest, CodeGeneratorResponse
from google.protobuf.descriptor_pb2 import FileDescriptorProto

from ..archive import EnumDefinition, MessageDefinition, parse_archive_descriptor
from ..syntax import go
from .. import types as t

__all__ = ["run_plugin"]

from ..archive._model import FieldDefinition, OneofDefinition


def run_plugin(request: "CodeGeneratorRequest") -> "CodeGeneratorResponse":
    return CodeGeneratorResponse(file=[pf for fd in request.proto_file for pf in archive_files(fd)])


def archive_files(fd: "FileDescriptorProto") -> "Collection[CodeGeneratorResponse.File]":
    """
    Return the files that define a Daml-LF archive format in Python.

    :param fd:
    :return:
    """
    archive_meta = parse_archive_descriptor(fd)

    # organize our data by classification; each classification goes into its own file
    by_classification = defaultdict(
        list
    )  # type: DefaultDict[str, List[Union[EnumDefinition, MessageDefinition]]]
    for e in archive_meta.enums:
        by_classification[e.classification].append(e)
    for m in archive_meta.messages:
        by_classification[m.classification].append(m)

    return [
        file
        for classification, types in by_classification.items()
        for file in archive_files_for_classification(classification, types)
    ]


def archive_files_for_classification(
    classification: str, types: "Sequence[Union[EnumDefinition, MessageDefinition]]"
) -> "Sequence[CodeGeneratorResponse.File]":
    with StringIO() as buf:
        write_header(buf)
        for typ in types:
            if isinstance(typ, EnumDefinition):
                write_enum(buf, typ)
            elif isinstance(typ, MessageDefinition):
                write_message(buf, typ)

        go_file = CodeGeneratorResponse.File(
            name=f"{classification}/{classification}.go",
            content=buf.getvalue(),
        )

    return [go_file]


def write_header(buf: "TextIO") -> None:
    buf.write("package damlast\n\n")


def write_enum(buf: "TextIO", enum_def: "EnumDefinition") -> None:
    type_name = go.public_name(enum_def.name)
    buf.write(f"type {type_name} int32\n\n")
    buf.write("const (\n")
    for name, value in enum_def.values.items():
        buf.write(f"\t{name} {type_name} = {value}\n")
    buf.write(")\n")


def write_message(buf: "TextIO", msg_def: "MessageDefinition") -> None:
    """
    Write a Go class to the buffer that is a more idiosyncratic Go and simplified
    representation of a Daml-LF message than the Protobuf-generated files.
    """

    # outside of the lfexpr classification, write ``[]byte`` instead of ``Expr``;
    # we intentionally do not eagerly parse ``Expr`` objects because they tend to be quite large,
    # and dazl doesn't actually use the results of these expressions for any purpose currently

    type_name = go.public_name(msg_def.name)

    buf.write(f"// classification: {msg_def.classification}\n")
    if type_name == "PackageRef":
        buf.write("type PackageRef string\n\n")
        return

    buf.write("\n")
    buf.write(f"type {type_name} struct {{\n")
    for mdef in msg_def.members:
        priv_name = go.private_name(mdef.name)
        if isinstance(mdef, OneofDefinition):
            buf.write(f"\t_{priv_name} case{type_name}{go.public_name(mdef.name)}\n")
            buf.write(f"\t{priv_name} interface{{}}\n")
        elif isinstance(mdef, FieldDefinition):
            buf.write(f"\t{priv_name} {mdef.type.go_rep}\n")
    buf.write("}\n")

    # parser
    buf.write(f"func (p Parser) Read{type_name}(r io.Reader) (v {type_name}, err error) {{\n")
    buf.write("\tvar n int64\n")
    buf.write("\tfor {\n")
    buf.write("\t\tn, err = _pb.ReadVarInt(r)\n")
    buf.write("\t\tif err == io.EOF {\n")
    buf.write("\t\t\terr = nil; return\n")
    buf.write("\t\t} else if err != nil {\n")
    buf.write("\t\t\treturn\n")
    buf.write("\t\t}\n")
    buf.write("\t\tswitch n >> 3 {\n")
    for fld_def in msg_def.fields:
        if fld_def.value_number is not None:
            buf.write(f"\t\tcase {fld_def.value_number}: // {fld_def.name}\n")
            if fld_def.oneof is not None:
                priv_name = go.private_name(fld_def.oneof)
                buf.write(f'\t\t\tv._{priv_name} = "{fld_def.name}"\n')
                buf.write(f"\t\t\tv.{priv_name}, err = p.Read{fld_def.type.go_rep}(r)\n")
            elif isinstance(fld_def.type, t.Seq):
                priv_name = go.private_name(fld_def.name)
                buf.write(f"\t\t\tvar obj {fld_def.type.arg.go_rep}\n")
                buf.write(f"\t\t\tobj, err = p.Read{fld_def.type.arg.go_rep}(r)\n")
                buf.write(f"\t\t\tif err == nil {{\n")
                buf.write(f"\t\t\t\tv.{priv_name} = append(v.{priv_name}, obj)\n")
                buf.write(f"\t\t\t}}\n")

            else:
                priv_name = go.private_name(fld_def.name)
                buf.write(f"\t\t\tv.{priv_name}, err = p.Read{fld_def.type.go_rep}(r)\n")

    buf.write("\t\t}\n")
    buf.write("\t}\n")
    buf.write("}\n")

    # # type constructor
    # oneof_members = [m for m in md.members if isinstance(m, OneofDefinition)]
    # if oneof_members:
    #     for oneof_combo in itertools.product(*[m.cases for m in oneof_members]):
    #         fields = [c.go_field_name + " " + c.go_type for c in oneof_combo]
    #
    #         buf.write(f"func New{md.name}{''.join(c.go_name for c in oneof_combo)}({', '.join(fields)}) {md.go_name} {{\n")
    #         buf.write(f"\treturn {md.go_name}{{\n")
    #         for c in oneof_combo:
    #             buf.write(f"\t\t{c.parent_oneof.go_field_name}N: {c.go_case_const_name},\n")
    #             buf.write(f"\t\t{c.parent_oneof.go_field_name}V: {c.go_field_name},\n")
    #         buf.write("\t}\n")
    #         buf.write("}\n")
    # else:
    #     buf.write(f"func New{md.go_name}(")
    #     for m in md.members:
    #         buf.write(f"{m.go_field_name} {m.go_type}, ")
    #     buf.write(f") {md.go_name} {{\n")
    #     buf.write(f"\treturn {md.go_name}{{\n")
    #     for m in md.members:
    #         buf.write(f"\t\t{m.go_field_name}: {m.go_field_name},\n")
    #     buf.write(f"\t}}\n")
    #     buf.write("}\n")
    #
    # for m in md.members:
    #     if isinstance(m, OneofDefinition):
    #         case_type = m.go_case_type
    #         buf.write(f"type {case_type} string\n")
    #         buf.write("const (\n")
    #         for c in m.cases:
    #             buf.write(f"\t{c.go_case_const_name} {case_type} = \"{c.name}\"\n")
    #         buf.write(")\n")
    #
    #     if isinstance(m, OneOfMeta):
    #         buf.write(f"func (x {md.go_name}) {m.go_name}() {m.go_ret_type} {{\n")
    #         buf.write(f"\treturn x.{m.go_field_name}N, x.{m.go_field_name}V\n")
    #         buf.write("}\n")
    #         for c in m.cases:
    #             buf.write(f"func (x {md.go_name}) {c.go_name}() *{c.go_type} {{\n")
    #             buf.write(f"\tif x.{c.parent_oneof.go_field_name}N == {c.go_case_const_name} {{\n")
    #             buf.write(f"\t\t_v := x.{c.parent_oneof.go_field_name}V.({c.go_type})\n")
    #             buf.write("\t\treturn &_v\n")
    #             buf.write("\t}\n")
    #             buf.write("\treturn nil\n")
    #             buf.write("}\n")
    #     else:
    #         buf.write(f"func (x {md.go_name}) {m.go_name}() {m.go_ret_type} {{ return x.{m.go_field_name} }}\n")

    for enum_def in msg_def.enums:
        write_enum(buf, enum_def)
    for nested_def in msg_def.messages:
        write_message(buf, nested_def)
