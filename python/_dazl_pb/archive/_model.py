# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains a lightweight object model for describing a Daml-LF archive format.
"""

from collections import Mapping
from dataclasses import dataclass, field
import itertools
import operator
import types
from typing import Optional, Sequence

from .. import types as t

__all__ = [
    "ArchiveDefinition",
    "EnumDefinition",
    "MessageDefinition",
    "FieldDefinition",
    "MemberDefinition",
]

oneof_fn = operator.attrgetter("oneof")


@dataclass(frozen=True)
class ArchiveDefinition:
    enums: "Sequence[EnumDefinition]" = ()
    messages: "Sequence[MessageDefinition]" = ()


@dataclass(frozen=True)
class TypeDefinition:
    name: str
    classification: str


@dataclass(frozen=True)
class EnumDefinition(TypeDefinition):
    values: "Mapping[str, int]" = types.MappingProxyType({})


@dataclass(frozen=True)
class MessageDefinition(TypeDefinition):
    enums: "Sequence[EnumDefinition]" = ()
    messages: "Sequence[MessageDefinition]" = ()
    fields: "Sequence[FieldDefinition]" = ()
    members: "Sequence[MemberDefinition]" = field(init=False)

    def __post_init__(self):
        normal_fields = [fd for fd in self.fields if fd.oneof is None]
        oneof_fields = [
            OneofDefinition(oneof, tuple(cases))
            for oneof, cases in itertools.groupby(
                sorted((fd for fd in self.fields if fd.oneof is not None), key=oneof_fn),
                key=oneof_fn,
            )
        ]
        object.__setattr__(
            self,
            "members",
            tuple(normal_fields + oneof_fields),
        )


@dataclass(frozen=True)
class MemberDefinition:
    name: str


@dataclass(frozen=True)
class FieldDefinition(MemberDefinition):
    name: str
    type: "t.Type"
    oneof: "Optional[str]" = None
    value_number: "Optional[int]" = None
    intern_number: "Optional[int]" = None

    def merge(self, __other: "Optional[FieldDefinition]") -> "FieldDefinition":
        """
        Return a new :class:`FieldDefinition` that is the value of this object merged with the other
        object.
        """
        if __other is None:
            return self
        elif self.name != __other.name:
            raise ValueError(
                f"cannot merge a FieldDefinition named {self.name} with one named {__other.name}"
            )
        elif self.type != __other.type:
            raise ValueError(
                f"cannot merge a FieldDefinition(name={self.name}, type={self.type}) because of an incompatible type {__other.type}"
            )
        else:
            return FieldDefinition(
                name=self.name,
                type=self.type,
                oneof=self.oneof or __other.oneof,
                value_number=self.value_number or __other.value_number,
                intern_number=self.intern_number or __other.intern_number,
            )


@dataclass(frozen=True)
class OneofDefinition(MemberDefinition):
    cases: "Sequence[FieldDefinition]"


####################################################################################################

# IDENTITY = "identity"
# OPTIONAL = "optional"
# REPEATED = "repeated"
#
#
# class _ContainerMeta:
#     def __init__(self):
#         self.messages = list()  # type: List[MessageMeta]
#         self.enums = list()  # type: List[EnumMeta]
#
#
# class ArchiveMeta(_ContainerMeta):
#     """
#     Information about a Daml-LF Archive object model.
#     """
#
#
# class MessageMeta(_ContainerMeta):
#     """
#     Information about a Daml-LF message.
#
#     :ivar classification:
#         The grouping under which this Message belongs. This construct is not native to the Daml-LF
#         archive format, and instead inferred by the parser.
#
#         This exists to support lazy-loading of ``Expr`` sub-trees, which can be quite large and
#         expensive to parse, even though they don't have any current usage in dazl. It also provides
#         a package organization structure in Go, as Go doesn't have a notion of nested types.
#
#         Messages and enums in classifications are not permitted to circularly depend on each other.
#     """
#
#     def __init__(self, name: str):
#         super().__init__()
#         self.name = name
#         self.members = list()  # type: List[MemberMeta]
#         self.classification = classification(self.name)
#         self._heading = "expr" if (
#                 name.startswith("Expr") or name == "Update"
#         ) else "package"
#
#     @property
#     def go_name(self) -> str:
#         return self.name.replace('.', '_')
#
#     @property
#     def py_short_name(self) -> str:
#         return self.name.rpartition(".")[2]
#
#     def oneof(self, name: str) -> "OneOfMeta":
#         """
#         Get or create and return a :class:`OneOfMeta` of the specified name in this
#         :class:`Message`.
#
#         :param name: The name of the :class:`OneOfMeta` to return.
#         :return: The existing or newly-created :class:`OneOfMeta`.
#         """
#         for member in self.members:
#             if member.name == name:
#                 if isinstance(member, OneOfMeta):
#                     return member
#                 else:
#                     raise ValueError(
#                         f"cannot replace an existing field {member.name} of "
#                         f"type {member.data_type} with a oneof"
#                     )
#
#         oneof = OneOfMeta(self, name)
#         self.members.append(oneof)
#         return oneof
#
#     def field(self, name: str, data_type: str, enclosing_type: str = IDENTITY) -> "FieldMeta":
#         """
#         Get or create and return a :class:`FieldMeta` of the specified name in this
#         :class:`Message`.
#
#         :param name:
#         :param data_type:
#         :param enclosing_type:
#             Either "identity", "optional", or "repeated".
#         :return:
#         """
#         for member in self.members:
#             if member.name == name:
#                 if isinstance(member, FieldMeta):
#                     if member.data_type == data_type:
#                         return member
#                     else:
#                         raise ValueError(
#                             f"cannot replace an existing field {member.name} of "
#                             f"type {member.data_type} with field of type {data_type}"
#                         )
#                 else:
#                     raise ValueError(
#                         f"cannot replace an existing field {member.name} that is a oneof"
#                     )
#
#         fm = FieldMeta(self, None, name, data_type, enclosing_type)
#         self.members.append(fm)
#         return fm
#
#     @property
#     def fields(self) -> "Collection[FieldMeta]":
#         """
#         The _actual_ fields of the message. This includes the non-oneof members, and each possible
#         field of a oneof.
#         """
#         fields = []  # type: List[FieldMeta]
#         for member in self.members:
#             if isinstance(member, FieldMeta):
#                 fields.append(member)
#             elif isinstance(member, OneOfMeta):
#                 fields.extend(member.cases)
#         fields.sort(key=lambda f: f.proto_index)
#         return fields
#
#
# class EnumMeta:
#     def __init__(self, name: str, fields: "Optional[Mapping[str, int]]" = None):
#         self.name = name
#         self.classification = classification(name)
#         self.fields = dict()  # type: Dict[str, int]
#         if fields is not None:
#             self.fields.update(fields)
#
#     @property
#     def go_name(self) -> str:
#         return self.name.replace('.', '_')
#
#     @property
#     def py_short_name(self) -> str:
#         return self.name.rpartition(".")[2]
#
#
# class FieldMetaBase:
#     def __init__(self, parent: MessageMeta, name: str):
#         self.parent = parent
#         self.name = name
#
#     @property
#     def go_name(self) -> str:
#         return goize_name_public(self.name)
#
#     @property
#     def go_field_name(self) -> str:
#         return goize_name_private(self.name)
#
#     @property
#     def py_name(self) -> str:
#         return pyize_name(self.name)
#
#     @property
#     def py_slot_name(self):
#         return self.name
#
#
# class FieldMeta(FieldMetaBase):
#     """
#     :class:`FieldMeta` is a field in a :class:`MessageMeta` or a :class:`OneOfMeta`.
#     """
#
#     def __init__(self, parent: MessageMeta, parent_oneof: "Optional[OneOfMeta]", name: str, data_type: str, enclosing_type: str = IDENTITY):
#         super().__init__(parent, name)
#         self.parent_oneof = parent_oneof
#         self.data_type = data_type
#         self.enclosing_type = enclosing_type
#
#     @property
#     def go_type(self) -> str:
#         gt = self.data_type.replace('.', '_')
#         if gt == "str":
#             return "string"
#         return gt
#
#     @property
#     def go_ret_type(self) -> str:
#         return self.go_type
#
#     @property
#     def go_case_const_name(self) -> "Optional[str]":
#         """
#         Name of a ``const`` field that names this case in a ``oneof`` expression, or ``None`` if
#         this field is not a member of a ``oneof``
#         """
#         if self.parent_oneof is not None:
#             return f"{self.parent.go_name}{self.parent_oneof.go_name}{self.go_name}"
#         else:
#             return None
#
#     @property
#     def py_init_type(self):
#         if self.enclosing_type == IDENTITY:
#             return self.data_type
#         elif self.enclosing_type == REPEATED:
#             return f"_typing.Iterable[{self.data_type}]"
#         elif self.enclosing_type == OPTIONAL:
#             return f"_typing.Optional[{self.data_type}]"
#         else:
#             raise ValueError("unknown enclosing type")
#
#     @property
#     def py_ret_type(self):
#         if self.enclosing_type == IDENTITY:
#             return self.data_type
#         elif self.enclosing_type == REPEATED:
#             return f"_typing.Tuple[{self.data_type}, ...]"
#         elif self.enclosing_type == OPTIONAL:
#             return f"_typing.Optional[{self.data_type}]"
#         else:
#             raise ValueError("unknown enclosing type")
#
#     @property
#     def py_type(self):
#         return self.data_type
#
#
# class OneOfMeta(FieldMetaBase):
#     def __init__(self, parent: MessageMeta, name: str):
#         super().__init__(parent, name)
#         self.parent_field = parent
#         self.cases = list()  # type: List[FieldMeta]
#
#     @property
#     def go_type(self) -> str:
#         return "interface{}"
#
#     @property
#     def go_case_type(self) -> str:
#         return f"case{self.parent.go_name}{self.name}"
#
#     @property
#     def go_ret_type(self) -> str:
#         return f"({self.go_case_type}, {self.go_type})"
#
#     @property
#     def py_init_type(self):
#         return self.py_type
#
#     @property
#     def py_ret_type(self):
#         return self.py_type
#
#     @property
#     def py_type(self):
#         with StringIO() as buf:
#             buf.write("_typing.Union[\n")
#             for c in self.cases:
#                 buf.write(f"_typing.Tuple[_L[{c.name!r}], {c.py_type}],\n")
#             buf.write("]")
#
#             return buf.getvalue()
#
#     def field(self, name: str, data_type: str) -> "FieldMeta":
#         """
#         Get or create and return a :class:`FieldMeta` of the specified name in this
#         :class:`Message`.
#
#         :param name:
#         :param data_type:
#         :return:
#         """
#         for member in self.cases:
#             if member.name == name:
#                 if member.data_type == data_type:
#                     return member
#                 else:
#                     raise ValueError(
#                         f"cannot replace an existing field {member.name} of "
#                         f"type {member.data_type} with field of type {data_type}"
#                     )
#
#         field_meta = FieldMeta(self.parent, self, name, data_type)
#         self.cases.append(field_meta)
#         return field_meta
#
#
# MemberMeta = Union[OneOfMeta, FieldMeta]
