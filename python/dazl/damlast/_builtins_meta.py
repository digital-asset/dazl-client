# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains supporting infrastructure for built-in method definitions for interpreting
Daml-LF files.
"""

from typing import Any, Optional, Sequence, Type as PyType, Union
import warnings

from .daml_lf_1 import BuiltinFunction, Expr, Type, ValName
from .util import package_local_name

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    from ..model.types import TypeReference


class _BuiltinMeta(type):
    def __new__(mcs, name, bases, dct):
        if name != "Builtin":
            proposed_name = dct.get("name", None)
            proposed_builtin = dct.get("builtin", None)
            if proposed_name is None:
                if proposed_builtin is None:
                    raise ValueError("Neither `name` nor `builtin` are specified")
            elif proposed_builtin is not None:
                raise ValueError("Only `name` or `builtin` can be specified, not both")
            dct["name"] = proposed_name
            dct["builtin"] = proposed_builtin
            args = dct.get("args")
            if args is None:
                raise ValueError(f"`args` must be specified for class {proposed_name}")
            if isinstance(args, Type):
                dct["args"] = (args,)
            elif not isinstance(args, tuple):
                dct["args"] = tuple(args)
        return super().__new__(mcs, name, bases, dct)


class Builtin(metaclass=_BuiltinMeta):
    name: Optional[str]
    builtin: Optional[BuiltinFunction]
    arg_types: Sequence[Type]

    def evaluate(self, type_args: "Sequence[Type]", args: "Sequence[Any]") -> "Any":
        raise NotImplementedError()

    def simplify(self, type_args: "Sequence[Type]", args: "Sequence[Expr]") -> "Optional[Expr]":
        raise NotImplementedError()


class BuiltinTable:
    def __init__(self):
        self.by_name = dict()  # type: [BuiltinFunction, PyType[Builtin]]
        self.by_builtin = dict()  # type: [str, PyType[Builtin]]

    def add(self, builtin: "PyType[Builtin]"):
        if builtin.builtin is not None:
            self.by_builtin[builtin.builtin] = builtin
        elif builtin.name is not None:
            self.by_name[builtin.name] = builtin
        else:
            raise ValueError(f"A builtin could not be registered! {builtin!r}")

    def resolve(
        self, ref: "Union[str, ValName, TypeReference, BuiltinFunction]"
    ) -> "Optional[Builtin]":
        """
        Return a :class:`Builtin` implementation for the name or reference if one is defined.
        """
        if isinstance(ref, BuiltinFunction):
            # All BuiltinFunctions MUST be defined
            return self.by_builtin[ref]
        elif isinstance(ref, (ValName, TypeReference)):
            return self.by_name.get(package_local_name(ref))
        elif isinstance(ref, str):
            return self.by_name.get(ref)
        else:
            raise TypeError(f"unexpected key type: {ref!r}")

    def __contains__(self, ref):
        if isinstance(ref, BuiltinFunction):
            return True
