# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import defaultdict
from io import StringIO
import re
from typing import Collection, DefaultDict, Dict, Iterable, Mapping, Sequence, Set, Union

from google.protobuf.descriptor_pb2 import FieldDescriptorProto

from .symbols import SymbolTable, Usage
from .types import PyType

__all__ = ["ImportContext", "rewrite_file_content"]


FROM = re.compile(r"from ([\w.]+) import (\w+) as (\w+)")


class ImportContext:
    def __init__(self, parent: "SymbolTable"):
        self._imports = defaultdict(set)  # type: DefaultDict[str, Set[str]]
        self._system_imports = defaultdict(set)  # type: DefaultDict[str, Set[str]]
        self._parent = parent

    def add_system_import(self, __from: str, __import: str) -> None:
        self._system_imports[__from].add(__import)

    def add_import(self, __from: str, __import: str) -> None:
        """
        Add an import to this context.

        :param __from:
            The Python module to import _from_.
        :param __import:
            The Python module to import.
        """
        self._imports[__from].add(__import)

    def py_type(self, fd: "Union[FieldDescriptorProto, str]", usage: "Usage") -> "PyType":
        if isinstance(fd, str):
            fd = FieldDescriptorProto(type=FieldDescriptorProto.TYPE_MESSAGE, type_name=fd)

        pt = self._parent.py_type(fd, usage)
        for k, v in pt.imports.items():
            self._imports[k].update(v)
        return pt

    def required_imports(self) -> "Mapping[str, Sequence[str]]":
        return {__from: sorted(__import) for __from, __import in self._imports.items()}

    def py_import_block(self, relative_to: str) -> str:
        absolute_imports = {}  # type: Dict[str, Collection[str]]
        relative_imports = {}  # type: Dict[str, Collection[str]]

        for __from, __imports in sorted(self.required_imports().items()):
            if __from == relative_to:
                # we don't need to include imports to our own file
                continue

            elif __from.startswith("com.daml."):
                # rewrite our own imports as relative imports
                relative_imports[relative_package(relative_to, __from)] = __imports

            else:
                absolute_imports[__from] = __imports

        import_groups = [
            self._system_imports,
            absolute_imports,
            relative_imports,
        ]  # type: Iterable[Mapping[str, Collection[str]]]

        return "\n".join(
            render_import_group(import_group) for import_group in import_groups if import_group
        )


def relative_package(__current_package: str, __target_package: str) -> str:
    """
    Return a replacement string for the target package that can be used to import that target
    package, but in a way that is interpreted relative to the current package.

    :param __current_package:
    :param __target_package:
    :return:

    >>> relative_package("com.daml.ledger.api.v1.commands_pb2", "com.daml.ledger.api.v1.value_pb2")
    '.value_pb2'
    >>> relative_package("com.abc.def", "com.abc.xyz.ghi.jkl")
    '.xyz.ghi.jkl'
    >>> relative_package("com.abc.xyz.ghi.jkl", "com.abc.def")
    '...def'
    """
    cur_elems = __current_package.split(".")
    target_elems = __target_package.split(".")

    i = 0
    for i, (cur, target) in enumerate(zip(cur_elems, target_elems)):
        if cur != target:
            break

    # i is now the first index where the lists don't match
    return "." * (len(cur_elems) - i) + ".".join(target_elems[i:])


def render_import_group(import_group: "Mapping[str, Collection[str]]") -> str:
    with StringIO() as buf:
        for f, i in import_group.items():
            import_expr = ", ".join(sorted(i))
            if f:
                buf.write(f"from {f} import {import_expr}\n")
            else:
                buf.write(f"import {import_expr}\n")

        return buf.getvalue()


def rewrite_file_content(name: str, content: str) -> str:
    """
    Rewrite the content of generated Python field to use relative imports instead of absolute
    imports, with an assumed root module as implied by the name of the file.

    :param name: The name of the ``.proto`` file.
    :param content: The original content from the Protobuf compiler.
    :return: The contents of the file, with imports modified.
    """
    current_module = name.rpartition("/")[0].replace("/", ".")
    with StringIO() as out_buf, StringIO(content) as in_buf:
        for line in in_buf.readlines():
            out_buf.write(rewrite_import(current_module, line))
        return out_buf.getvalue()


def rewrite_import(parent_module: str, line: str) -> str:
    result = FROM.match(line)
    if result:
        module_name = result.group(1)
        identifier_name = result.group(2)
        local_name = result.group(3)
        if module_name.startswith("google."):
            # don't rewrite Google imports; simply do nothing
            return line
        if module_name == parent_module:
            return f"from . import {identifier_name} as {local_name}\n"

    return line
