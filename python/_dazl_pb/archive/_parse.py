# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from collections import defaultdict
from dataclasses import dataclass
import types
from typing import Mapping, Optional, Sequence

from google.protobuf.descriptor_pb2 import (
    DescriptorProto,
    EnumDescriptorProto,
    FieldDescriptorProto,
    FileDescriptorProto,
)

from ._conventions import as_interned_field, strip_interning
from ._model import IDENTITY, OPTIONAL, REPEATED, ArchiveMeta, EnumMeta, MessageMeta

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
        "TemplateChoice": (
            "location",
            "observers",
        ),
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


def parse_archive_descriptor(fd: "FileDescriptorProto") -> "ArchiveMeta":
    archive = ArchiveMeta()

    for ed in fd.enum_type:
        archive.enums.append(parse_enum_descriptor(None, ed))
    for md in fd.message_type:
        if md.name != "InternedDottedName":
            archive.messages.append(parse_message_descriptor(None, md))

    # The Archive message as described in daml_lf_1.proto is intentionally opaque, with the
    # package field declared as bytes. When we're dealing with parsed packages, we actually want
    # the full package.
    archive_msg = MessageMeta("Archive")
    archive_msg.field("hash", "PackageRef")
    archive_msg.field("package", "Package")

    archive.messages.append(archive_msg)

    return archive


def parse_enum_descriptor(parent: "Optional[str]", ed: "EnumDescriptorProto") -> "EnumMeta":
    name = ed.name if not parent else parent + "." + ed.name
    return EnumMeta(name, {v.name: v.number for v in ed.value})


def parse_message_descriptor(parent: "Optional[str]", md: "DescriptorProto") -> "MessageMeta":
    mb = MessageMetaBuilder(parent, md)
    mb.add_inner_types()
    mb.add_fields()
    return mb.build()


@dataclass(frozen=True)
class MessageFields:
    sum_types: Mapping[str, Sequence[str]]
    field_rewrites: Mapping[str, str]
    field_types: Mapping[str, str]

    def get_field_info(self, fd: "FieldDescriptorProto") -> "FieldInfo":
        field_name = self.field_rewrites.get(fd.name, fd.name)
        field_type = self.field_types.get(field_name, py_data_type(fd))
        field_name, field_type = strip_interning(field_name, field_type)
        return FieldInfo(field_name, field_type)


@dataclass(frozen=True)
class FieldInfo:
    name: str
    type: str


class MessageMetaBuilder:
    def __init__(self, parent: "Optional[str]", md: "DescriptorProto"):
        self.md = md
        self._name = md.name if not parent else parent + "." + md.name
        self._meta = MessageMeta(self._name)

    def add_inner_types(self):
        for ed in self.md.enum_type:
            self._meta.enums.append(parse_enum_descriptor(self._name, ed))
        for nd in self.md.nested_type:
            self._meta.messages.append(parse_message_descriptor(self._name, nd))

    def add_fields(self) -> None:
        message_fields = self._analyze_oneofs()
        for fd in self.md.field:
            self._maybe_add_field(fd, message_fields)

    def _analyze_oneofs(self) -> "MessageFields":
        # find all of the oneof fields, and arrange the names of fields by their oneof name
        sum_types = defaultdict(list)
        for fd in self.md.field:
            if fd.HasField("oneof_index"):
                sum_types[self.md.oneof_decl[fd.oneof_index].name].append(fd.name)

        field_rewrites = {}
        field_types = {}

        # look for oneofs that exist solely because they are used to distinguish between
        # interned and non-interned fields; form our perspective, those are uninteresting
        for sum_type, fields in list(sum_types.items()):
            field_name, data_type = as_interned_field(fields)
            if field_name is not None and data_type is not None:
                for field in fields:
                    field_rewrites[field] = field_name
                del sum_types[sum_type]
                field_types[field_name] = data_type

        return MessageFields(sum_types, field_rewrites, field_types)

    def _maybe_add_field(self, fd: "FieldDescriptorProto", message_fields: "MessageFields") -> None:
        # the intern tables in the Package object are all omitted from our archive types
        if fd.name in IGNORED_TYPE_FIELDS.get(self._name, ()):
            return

        fi = message_fields.get_field_info(fd)

        if (
            fd.HasField("oneof_index")
            and self.md.oneof_decl[fd.oneof_index].name in message_fields.sum_types
        ):
            # this field represents a oneof (even when we ignore interned fields)
            self._meta.oneof(self.md.oneof_decl[fd.oneof_index].name).field(fi.name, fi.type)

        elif fi.name in OPTIONAL_TYPE_FIELDS.get(self._name, ()):
            self._meta.field(fi.name, fi.type, OPTIONAL)

        else:
            repeated = fi.type != "DottedName" and fd.label == FieldDescriptorProto.LABEL_REPEATED
            self._meta.field(fi.name, fi.type, REPEATED if repeated else IDENTITY)

    def build(self) -> MessageMeta:
        return self._meta


def py_data_type(fld: "FieldDescriptorProto") -> str:
    if fld.type_name.startswith(".daml_lf_1."):
        return fld.type_name[len(".daml_lf_1.") :]

    if fld.type == FieldDescriptorProto.TYPE_STRING:
        return "str"
    elif fld.type == FieldDescriptorProto.TYPE_BYTES:
        return "bytes"
    elif fld.type == FieldDescriptorProto.TYPE_BOOL:
        return "bool"
    elif fld.type in (
        FieldDescriptorProto.TYPE_INT32,
        FieldDescriptorProto.TYPE_INT64,
        FieldDescriptorProto.TYPE_SINT32,
        FieldDescriptorProto.TYPE_SINT64,
        FieldDescriptorProto.TYPE_UINT32,
        FieldDescriptorProto.TYPE_UINT64,
    ):
        return "int"
    elif fld.type in (
        FieldDescriptorProto.TYPE_FLOAT,
        FieldDescriptorProto.TYPE_DOUBLE,
        FieldDescriptorProto.TYPE_FIXED32,
        FieldDescriptorProto.TYPE_FIXED64,
        FieldDescriptorProto.TYPE_SFIXED32,
        FieldDescriptorProto.TYPE_SFIXED64,
    ):
        return "float"
    else:
        return "..."
