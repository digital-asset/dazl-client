# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from types import MappingProxyType
from typing import Collection, Mapping, Optional
import warnings

from .daml_lf_1 import Expr, Type, ValName

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    from ..model.types_store import PackageStore


warnings.warn(
    "dazl.damlast.eval_scope is deprecated; there is no replacement.",
    DeprecationWarning,
    stacklevel=2,
)


class EvaluationScope:
    def __init__(
        self,
        store: "PackageStore",
        bindings: "Mapping[str, Expr]",
        blocked_value_refs: "Collection[ValName]" = (),
        depth: int = 0,
    ):
        warnings.warn(
            "EvaluationScope is deprecated; there is no replacement.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.store = store
        self.depth = depth
        self._vars = MappingProxyType(dict(bindings))
        self._blocked_value_refs = frozenset(blocked_value_refs)

    def without(self, var_name: str) -> "EvaluationScope":
        """
        Return a child scope with the specified variable name _unbound_.

        :param var_name:
        :return:
        """
        new_bindings = dict(self._vars)
        del new_bindings[var_name]
        return EvaluationScope(self.store, new_bindings, self._blocked_value_refs, self.depth + 1)

    def without_value(self, value_ref) -> "EvaluationScope":
        """
        Return a child scope where the value corresponding to the specified value reference will
        NOT be returned. (This is used to handle breaking otherwise recursive calls.)

        :param value_ref: The value to withhold.
        """
        values = set(self._blocked_value_refs)
        values.discard(value_ref)

        return EvaluationScope(self.store, self._vars, frozenset(values), self.depth + 1)

    def child_scope(self, new_bindings: "Mapping[str, Expr]") -> "EvaluationScope":
        bindings = dict(self._vars)
        bindings.update(new_bindings)
        return EvaluationScope(self.store, bindings, self._blocked_value_refs, self.depth + 1)

    def get_bound(self, var_name) -> "Expr":
        return self._vars[var_name]

    def resolve_type(self, type_ref) -> "Type":
        pass

    def resolve_value(self, value_ref) -> "Optional[Expr]":
        if value_ref in self._blocked_value_refs:
            return None
        else:
            return self.store.resolve_value_reference(value_ref)
