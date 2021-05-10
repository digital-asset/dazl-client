# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Collection, Mapping, Optional

from ...collections import merge

__all__ = [
    "PyType",
    "ANY",
    "OPTIONAL",
    "ITERABLE",
    "MAPPING",
    "BOOL",
    "FLOAT",
    "INT",
    "BYTES",
    "STRING",
    "ENUM_DESCRIPTOR",
    "SCALAR_CONTAINER",
    "COMPOSITE_CONTAINER",
    "MAP_CONTAINER",
    "BOTTOM",
]


class PyType:
    """
    Contains information about a resolved type in an import context.
    """

    def __init__(
        self,
        *,
        package: "Optional[str]" = None,
        py_str: str,
        imports: "Optional[Mapping[str, Collection[str]]]" = None,
    ):
        self.py_str = py_str
        self._imports = merge(imports, {package: [py_str]} if package else None)

    def apply(self, *args: "PyType") -> "PyType":
        """
        Produce a new type that is the application of this generic type with the specified type
        parameter.

        :param args: The type argument(s) to apply.
        """
        if not args:
            return self

        return PyType(
            py_str=f"{self.py_str}[" + ", ".join(arg.py_str for arg in args) + f"]",
            imports=merge(self.imports, *(arg.imports for arg in args)),
        )

    @property
    def settable(self) -> bool:
        return self.py_str == self.py_str.lower() or self.py_str.startswith("_typing.Literal[")

    @property
    def imports(self) -> "Mapping[str, Collection[str]]":
        """
        The imports that are needed in order to have well-formed Python code that utilizes the
        string representation of the type as represented by this object.
        """
        return self._imports


ANY = PyType(py_str="_typing.Any")
OPTIONAL = PyType(py_str="_typing.Optional")
ITERABLE = PyType(py_str="_typing.Iterable")
MAPPING = PyType(py_str="_typing.Mapping")
BOOL = PyType(py_str="_builtins.bool")
FLOAT = PyType(py_str="_builtins.float")
INT = PyType(py_str="_builtins.int")
BYTES = PyType(py_str="_builtins.bytes")
STRING = PyType(py_str="_builtins.str")
ENUM_DESCRIPTOR = PyType(package="google.protobuf.descriptor", py_str="EnumDescriptor")
SCALAR_CONTAINER = PyType(
    package="google.protobuf.internal.containers", py_str="RepeatedScalarFieldContainer"
)
COMPOSITE_CONTAINER = PyType(
    package="google.protobuf.internal.containers", py_str="RepeatedCompositeFieldContainer"
)
MAP_CONTAINER = PyType(package="google.protobuf.internal.containers", py_str="MessageMap")
BOTTOM = PyType(py_str="_typing.NoReturn")
