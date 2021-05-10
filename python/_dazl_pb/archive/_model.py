# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains a lightweight object model for describing a Daml-LF archive format.
"""
from collections import Mapping
from io import StringIO
from typing import Dict, List, Optional, Union

from ._conventions import pyize_name

__all__ = [
    "ArchiveMeta",
    "MessageMeta",
    "EnumMeta",
    "FieldMeta",
    "OneOfMeta",
    "IDENTITY",
    "OPTIONAL",
    "REPEATED",
]

IDENTITY = "identity"
OPTIONAL = "optional"
REPEATED = "repeated"


class _ContainerMeta:
    def __init__(self):
        self.messages = list()  # type: List[MessageMeta]
        self.enums = list()  # type: List[EnumMeta]


class ArchiveMeta(_ContainerMeta):
    """
    Information about a Daml-LF Archive object model.
    """


class MessageMeta(_ContainerMeta):
    """
    Information about a Daml-LF message.
    """

    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.members = list()  # type: List[MemberMeta]

    @property
    def py_short_name(self):
        return self.name.rpartition(".")[2]

    def oneof(self, name: str) -> "OneOfMeta":
        """
        Get or create and return a :class:`OneOfMeta` of the specified name in this
        :class:`Message`.

        :param name: The name of the :class:`OneOfMeta` to return.
        :return: The existing or newly-created :class:`OneOfMeta`.
        """
        for member in self.members:
            if member.name == name:
                if isinstance(member, OneOfMeta):
                    return member
                else:
                    raise ValueError(
                        f"cannot replace an existing field {member.name} of "
                        f"type {member.data_type} with a oneof"
                    )

        oneof = OneOfMeta(name)
        self.members.append(oneof)
        return oneof

    def field(self, name: str, data_type: str, enclosing_type: str = IDENTITY) -> "FieldMeta":
        """
        Get or create and return a :class:`FieldMeta` of the specified name in this
        :class:`Message`.

        :param name:
        :param data_type:
        :param enclosing_type:
            Either "identity", "optional", or "repeated".
        :return:
        """
        for member in self.members:
            if member.name == name:
                if isinstance(member, FieldMeta):
                    if member.data_type == data_type:
                        return member
                    else:
                        raise ValueError(
                            f"cannot replace an existing field {member.name} of "
                            f"type {member.data_type} with field of type {data_type}"
                        )
                else:
                    raise ValueError(
                        f"cannot replace an existing field {member.name} that is a oneof"
                    )

        fm = FieldMeta(name, data_type, enclosing_type)
        self.members.append(fm)
        return fm


class EnumMeta:
    def __init__(self, name: str, fields: "Optional[Mapping[str, int]]" = None):
        self.name = name
        self.fields = dict()  # type: Dict[str, int]
        if fields is not None:
            self.fields.update(fields)

    @property
    def py_short_name(self):
        return self.name.rpartition(".")[2]


class FieldMeta:
    """
    :class:`FieldMeta` is a field in a :class:`MessageMeta` or a :class:`OneOfMeta`.
    """

    def __init__(self, name: str, data_type: str, enclosing_type: str = IDENTITY):
        self.name = name
        self.data_type = data_type
        self.enclosing_type = enclosing_type

    @property
    def py_name(self):
        return pyize_name(self.name)

    @property
    def py_slot_name(self):
        return self.py_name

    @property
    def py_init_type(self):
        if self.enclosing_type == IDENTITY:
            return self.data_type
        elif self.enclosing_type == REPEATED:
            return f"_typing.Iterable[{self.data_type}]"
        elif self.enclosing_type == OPTIONAL:
            return f"_typing.Optional[{self.data_type}]"
        else:
            raise ValueError("unknown enclosing type")

    @property
    def py_ret_type(self):
        if self.enclosing_type == IDENTITY:
            return self.data_type
        elif self.enclosing_type == REPEATED:
            return f"_typing.Tuple[{self.data_type}, ...]"
        elif self.enclosing_type == OPTIONAL:
            return f"_typing.Optional[{self.data_type}]"
        else:
            raise ValueError("unknown enclosing type")

    @property
    def py_type(self):
        return self.data_type


class OneOfMeta:
    def __init__(self, name: str):
        self.name = name
        self.cases = list()  # type: List[FieldMeta]

    @property
    def py_name(self):
        return pyize_name(self.name)

    @property
    def py_slot_name(self):
        return self.name

    @property
    def py_init_type(self):
        return self.py_type

    @property
    def py_ret_type(self):
        return self.py_type

    @property
    def py_type(self):
        with StringIO() as buf:
            buf.write("_typing.Union[\n")
            for c in self.cases:
                buf.write(f"_typing.Tuple[_L[{c.name!r}], {c.py_type}],\n")
            buf.write("]")

            return buf.getvalue()

    def field(self, name: str, data_type: str) -> "FieldMeta":
        """
        Get or create and return a :class:`FieldMeta` of the specified name in this
        :class:`Message`.

        :param name:
        :param data_type:
        :return:
        """
        for member in self.cases:
            if member.name == name:
                if member.data_type == data_type:
                    return member
                else:
                    raise ValueError(
                        f"cannot replace an existing field {member.name} of "
                        f"type {member.data_type} with field of type {data_type}"
                    )

        field_meta = FieldMeta(name, data_type)
        self.cases.append(field_meta)
        return field_meta


MemberMeta = Union[OneOfMeta, FieldMeta]
