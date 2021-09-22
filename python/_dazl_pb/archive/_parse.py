# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import Counter
from dataclasses import replace
import types
from typing import Dict, Optional

from google.protobuf.descriptor_pb2 import (
    DescriptorProto,
    EnumDescriptorProto,
    FieldDescriptorProto,
    FileDescriptorProto,
)

from .. import types as t
from ._model import ArchiveDefinition, EnumDefinition, FieldDefinition, MessageDefinition

__all__ = ["parse_archive_descriptor"]


# Mapping of Daml-LF types to fields that are considered to be optional.
OPTIONAL_TYPE_FIELDS = types.MappingProxyType(
    {
        "DefException": ("location",),
        "DefDataType": ("name", "location"),
        "DefValue": ("location",),
        "DefTemplate": ("key", "location"),
        "DefTypeSyn": ("location",),
        "Expr": ("location",),
        # TemplateChoice.observers was added in Daml-LF 1.11; earlier package formats
        # will not have had this field defined
        "TemplateChoice": ("location", "observers"),
        "Package": ("metadata",),
    }
)

# Mapping of Daml-LF types to fields that should be ignored.
IGNORED_TYPE_FIELDS = types.MappingProxyType(
    {
        "Package": ("interned_strings", "interned_dotted_names", "interned_types"),
        "Type": ("interned",),
    }
)


def parse_archive_descriptor(fd: "FileDescriptorProto") -> "ArchiveDefinition":
    enum_defs = [parse_enum_descriptor(None, ed) for ed in fd.enum_type]
    maybe_message_defs = [parse_md_proto(None, md) for md in fd.message_type]

    return ArchiveDefinition(
        enums=tuple(enum_defs),
        messages=tuple(
            [
                *(mdef for mdef in maybe_message_defs if mdef is not None),
                # The Archive message as described in daml_lf_1.proto is intentionally opaque, with the
                # package field declared as bytes. When we're dealing with parsed packages, we actually want
                # the full package.
                MessageDefinition(
                    "Archive",
                    "lf",
                    fields=(
                        FieldDefinition("hash", t.Message("PackageRef"), value_number=4),
                        FieldDefinition("package", t.Message("Package"), value_number=3),
                    ),
                ),
            ]
        ),
    )


def parse_enum_descriptor(parent: "Optional[str]", ed: "EnumDescriptorProto") -> "EnumDefinition":
    name = ed.name if not parent else parent + "." + ed.name
    return EnumDefinition(name, classification(name), {v.name: v.number for v in ed.value})


def parse_fd_proto(
    md: "DescriptorProto", fd: "FieldDescriptorProto"
) -> "Optional[FieldDefinition]":
    """
    Create a :class:`FieldDefinition` from the fields of a :class:`FieldDescriptorProto`.

    Returns ``None`` for fields that are to be ignored.
    """
    # some fields are outright ignored
    if md.name == "Package":
        # the intern tables are handled specially
        if fd.name in ("interned_strings", "interned_dotted_names", "interned_types"):
            return None
    elif md.name == "Type":
        # interned types are handled as a special case directly in the parser
        if fd.name == "interned":
            return None

    oneof = md.oneof_decl[fd.oneof_index].name if fd.HasField("oneof_index") else None

    # specialized interned fields; the name of these fields alone implies the type of the field
    fld_name = without_suffix(fd.name, "_interned_str")
    if fld_name is not None:
        return FieldDefinition(name=fld_name, type=t.STRING, oneof=oneof, intern_number=fd.number)

    fld_name = without_suffix(fd.name, "_interned")
    if fld_name is not None:
        return FieldDefinition(name=fld_name, type=t.STRING, oneof=oneof, intern_number=fd.number)

    fld_name = without_suffix(fd.name, "_str")
    if fld_name is not None:
        return FieldDefinition(name=fld_name, type=t.STRING, oneof=oneof, value_number=fd.number)

    fld_name = without_suffix(fd.name, "_interned_dname")
    if fld_name is not None:
        return FieldDefinition(
            name=fld_name, type=t.DOTTED_NAME, oneof=oneof, intern_number=fd.number
        )

    fld_name = without_suffix(fd.name, "_dname")
    if fld_name is not None:
        return FieldDefinition(
            name=fld_name, type=t.DOTTED_NAME, oneof=oneof, value_number=fd.number
        )

    # now check for optional types
    tfn = lambda i: i
    if md.name == "DefException":
        if fd.name == "location":
            tfn = t.Optional
    # "DefDataType": ("name", "location"),
    # "DefValue": ("location",),
    # "DefTemplate": ("key", "location"),
    # "DefTypeSyn": ("location",),
    # "Expr": ("location",),
    # # TemplateChoice.observers was added in Daml-LF 1.11; earlier package formats
    # # will not have had this field defined
    # "TemplateChoice": ("location", "observers"),
    # "Package": ("metadata",),
    if fd.label == FieldDescriptorProto.LABEL_REPEATED:
        tfn = t.Seq

    if fd.type == FieldDescriptorProto.TYPE_STRING:
        field_type = tfn(t.STRING)
    elif fd.type == FieldDescriptorProto.TYPE_BYTES:
        field_type = tfn(t.BYTES)
    elif fd.type == FieldDescriptorProto.TYPE_BOOL:
        field_type = tfn(t.BOOL)
    elif fd.type == FieldDescriptorProto.TYPE_INT32:
        field_type = tfn(t.INT32)
    elif fd.type == FieldDescriptorProto.TYPE_INT64:
        field_type = tfn(t.INT64)
    elif fd.type == FieldDescriptorProto.TYPE_SINT32:
        field_type = tfn(t.SINT32)
    elif fd.type == FieldDescriptorProto.TYPE_SINT64:
        field_type = tfn(t.SINT64)
    elif fd.type == FieldDescriptorProto.TYPE_UINT32:
        field_type = tfn(t.UINT32)
    elif fd.type == FieldDescriptorProto.TYPE_UINT64:
        field_type = tfn(t.UINT64)
    elif fd.type == FieldDescriptorProto.TYPE_FLOAT:
        field_type = tfn(t.FLOAT)
    elif fd.type == FieldDescriptorProto.TYPE_DOUBLE:
        field_type = tfn(t.DOUBLE)
    elif fd.type == FieldDescriptorProto.TYPE_FIXED32:
        field_type = tfn(t.FIXED32)
    elif fd.type == FieldDescriptorProto.TYPE_FIXED64:
        field_type = tfn(t.FIXED64)
    elif fd.type == FieldDescriptorProto.TYPE_SFIXED32:
        field_type = tfn(t.SFIXED32)
    elif fd.type == FieldDescriptorProto.TYPE_SFIXED64:
        field_type = tfn(t.SFIXED64)
    elif fd.type == FieldDescriptorProto.TYPE_ENUM:
        if fd.type_name.startswith(".daml_lf_1."):
            field_type = tfn(t.Enum(fd.type_name[11:]))
        else:
            raise ValueError("unknown message that wasn't a Daml-LF type")
    elif fd.type == FieldDescriptorProto.TYPE_MESSAGE:
        if fd.type_name.startswith(".daml_lf_1."):
            field_type = tfn(t.Message(fd.type_name[11:]))
        else:
            raise ValueError("unknown message that wasn't a Daml-LF type")
    else:
        raise ValueError(f"unknown field type: {fd.type}")

    return FieldDefinition(fd.name, type=field_type, oneof=oneof, value_number=fd.number)


def parse_md_proto(parent: "Optional[str]", md: "DescriptorProto") -> "Optional[MessageDefinition]":
    if md.name == "InternedDottedName":
        return None

    name = md.name if not parent else parent + "." + md.name
    enums = [parse_enum_descriptor(name, ed) for ed in md.enum_type]
    messages = [parse_md_proto(name, nd) for nd in md.nested_type if nd is not None]

    accs = {}  # type: Dict[str, FieldDefinition]
    for fd in md.field:
        fi = parse_fd_proto(md, fd)
        if fi is not None:
            accs[fi.name] = fi.merge(accs.get(fi.name))

    # any oneofs that have only one case are not really oneofs; wipe the oneof field
    oneof_counts = Counter(fi.oneof for fi in accs.values() if fi.oneof is not None)
    oneof_names = {oneof for oneof, count in oneof_counts.items() if count == 1}
    fields = [replace(fi, oneof=None) if fi.name in oneof_names else fi for fi in accs.values()]

    return MessageDefinition(
        name=name,
        classification=classification(name),
        enums=enums,
        messages=messages,
        fields=fields,
    )


def without_suffix(value: str, suffix: str) -> "Optional[str]":
    return value[: -len(suffix)] if value.endswith(suffix) else None


def classification(name: str) -> str:
    """
    Return the classification for a message of the specified name (see the comments on
    :class:`MessageMeta`)
    """
    if name == "Archive":
        return "lf"
    if (
        name
        in (
            "Package",
            "PackageRef",
            "DottedName",
            "ModuleRef",
            "TypeConName",
            "TypeSynName",
            "ValName",
            "DefTemplate",
            "TemplateChoice",
            "DefException",
            "DefDataType",
            "DefTypeSyn",
            "DefValue",
            "FeatureFlags",
            "Module",
            "PackageMetadata",
        )
        or name.startswith("DefTemplate")
        or name.startswith("DefDataType")
        or name.startswith("DefValue.")
    ):
        return "lfpkg"
    elif (
        name
        in (
            "Expr",
            "Update",
            "Scenario",
            "BuiltinFunction",
            "FieldWithExpr",
            "Binding",
            "PrimLit",
            "Case",
            "CaseAlt",
            "Block",
            "Pure",
            "KeyExpr",
            "PrimCon",
        )
        or name.startswith("Expr.")
        or name.startswith("Case")
        or name.startswith("CaseAlt.")
        or name.startswith("Update.")
        or name.startswith("Scenario.")
        or name.startswith("KeyExpr.")
        or name.startswith("PrimLit.")
    ):
        return "lfexpr"
    elif (
        name in ("Type", "PrimType", "FieldWithType", "VarWithType", "TypeVarWithKind", "Kind")
        or name.startswith("Type.")
        or name.startswith("Kind.")
    ):
        return "lftype"
    elif name in ("Location", "Location.Range"):
        return "lfloc"
    elif name == "Unit":
        return "builtin"
    else:
        raise ValueError(f"unknown classification: {name}")
