# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from enum import Enum
from typing import Dict, List, Tuple, Union

from google.protobuf.descriptor_pb2 import (
    DescriptorProto,
    EnumDescriptorProto,
    FieldDescriptorProto,
    FileDescriptorProto,
)

from .pb import py_message_package, py_scalar_type
from .types import (
    ANY,
    BOTTOM,
    COMPOSITE_CONTAINER,
    ITERABLE,
    MAP_CONTAINER,
    MAPPING,
    OPTIONAL,
    SCALAR_CONTAINER,
    PyType,
)

__all__ = ["Usage", "SymbolTable"]


class Usage(Enum):
    GETTER = 1
    ARG = 2
    ARG_STREAM = 3
    RET = 4
    RET_STREAM = 5
    RET_ASYNC = 6
    RET_STREAM_ASYNC = 7
    INIT = 8


class SymbolTable:
    """
    A map of "absolute" Protobuf imports to their Python types, taking into account that
    messages within the same file can be referenced without being fully-qualified.
    """

    def __init__(self):
        self._packages = {}  # type: Dict[str, str]
        self._imports = {}  # type: Dict[str, str]
        self._map_types = {}  # type: Dict[str, Tuple[FieldDescriptorProto, FieldDescriptorProto]]
        self._enums = {}  # type: Dict[str, Dict[str, int]]

    def load_file(self, fd: "FileDescriptorProto") -> None:
        """
        Load a single file.
        """
        prefix = f".{fd.package}"
        for ed in fd.enum_type:
            self.load_enum(ed, fd.name, prefix)
        for md in fd.message_type:
            self.load_message(md, fd.name, prefix, "")

    def load_enum(self, d: "EnumDescriptorProto", file_name: str, proto_prefix: str) -> None:
        """
        Load information about the specified enum.

        :param d:
            The :class:`EnumDescriptorProto` to load.
        :param file_name:
            The name of the file that contains this message.
        :param proto_prefix:
            The Protobuf namespace that contains this enum.
        """
        proto_type_name = proto_prefix + "." + d.name
        package = py_message_package(file_name)

        self._packages[proto_type_name] = package
        self._imports[proto_type_name] = d.name
        self._enums[proto_type_name] = {v.name: v.number for v in d.value}

    def load_message(
        self, d: "DescriptorProto", file_name: str, proto_prefix: str, local_prefix: str
    ) -> None:
        """
        Load information about the specified message.

        :param d:
            The :class:`EnumDescriptorProto` to load.
        :param file_name:
            The name of the file that contains this message.
        :param proto_prefix:
            The Protobuf namespace that contains this enum.
        :param local_prefix:
            The prefix of this type and any nested types, as it would be expressed in Python.
        """
        proto_type_name = proto_prefix + "." + d.name
        py_type_name = local_prefix + "." + d.name if local_prefix else d.name
        package = py_message_package(file_name)

        if d.options.map_entry:
            self._map_types[proto_type_name] = (d.field[0], d.field[1])
            return

        self._packages[proto_type_name] = package
        self._imports[proto_type_name] = py_type_name
        for ed in d.enum_type:
            self.load_enum(ed, file_name, proto_type_name)
        for nd in d.nested_type:
            self.load_message(nd, file_name, proto_type_name, py_type_name)

    def py_type(self, fd: "FieldDescriptorProto", usage: "Usage") -> "PyType":
        map_type = self._map_types.get(fd.type_name)
        if map_type is not None:
            key_type = self._base_py_type(map_type[0], Usage.GETTER)
            value_type = self._base_py_type(map_type[1], Usage.GETTER)
            if usage == Usage.GETTER:
                return MAP_CONTAINER.apply(key_type, value_type)
            elif usage == Usage.INIT:
                return OPTIONAL.apply(MAPPING.apply(key_type, value_type))
            elif usage == Usage.ARG or usage == Usage.RET:
                return MAPPING.apply(key_type, value_type)
            else:
                raise ValueError("unexpected map type in a stream context")

        py_type = self._base_py_type(fd, usage)
        if usage == Usage.GETTER:
            if fd.label == FieldDescriptorProto.LABEL_REPEATED:
                if py_type.settable:
                    return SCALAR_CONTAINER.apply(py_type)
                else:
                    return COMPOSITE_CONTAINER.apply(py_type)
            else:
                return py_type
        elif usage == Usage.INIT:
            if fd.label == FieldDescriptorProto.LABEL_REPEATED:
                return OPTIONAL.apply(ITERABLE.apply(py_type))
            elif fd.HasField("oneof_index"):
                return py_type
            else:
                return OPTIONAL.apply(py_type)
        elif usage == Usage.ARG:
            return py_type
        elif usage == Usage.ARG_STREAM:
            return ITERABLE.apply(py_type)
        elif usage == Usage.RET:
            return py_type
        elif usage == Usage.RET_STREAM:
            return PyType(py_str="_grpc.CallIterator").apply(py_type)
        elif usage == Usage.RET_ASYNC:
            return PyType(py_str="_grpc_aio.UnaryUnaryCall").apply(ANY, py_type)
        elif usage == Usage.RET_STREAM_ASYNC:
            return PyType(py_str="_grpc_aio.UnaryStreamCall").apply(ANY, py_type)
        else:
            raise ValueError

    def _base_py_type(self, fd: "FieldDescriptorProto", usage: "Usage") -> "PyType":
        """
        Return a Python string that represents the type of the requested field, ignoring whether
        or not it is a repeated field.
        """
        builtin_type = py_scalar_type(fd.type)
        if builtin_type is not None:
            return builtin_type

        enum_definition = self._enums.get(fd.type_name)
        if enum_definition is not None:
            # for enum definitions, the allowed constructors are literals over all the numeric AND
            # string representations for those types
            literals = []  # type: List[Union[str, int]]
            for key, value in enum_definition.items():
                if usage == Usage.INIT:
                    # for __init__ parameters for messages, the string values of enum entries are
                    # allowed; they are NOT allowed as setters for properties
                    literals.append(key)
                literals.append(value)

            if literals:
                # the Pythonic representation of a list is exactly what we need here
                return PyType(py_str=f"_L{literals}")
            else:
                # there are no allowable values; use the bottom type
                return BOTTOM

        type_str = self._imports.get(fd.type_name)
        if type_str is not None:
            python_package = self._packages[fd.type_name]
            return PyType(py_str=type_str, imports={python_package: [type_str.partition(".")[0]]})

        raise ValueError(f"could not compute a Pythonic representation of {fd.type_name!r}")
