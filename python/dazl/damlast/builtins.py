# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Define a few DAML values and functions that have been inlined in Python for efficiency and
simplicity.
"""

from typing import Any, Optional, Sequence

from ._builtins_meta import BuiltinTable, Builtin
from .daml_lf_1 import BuiltinFunction, Expr, PrimLit, Type
from .util import list_type, var, STRING

builtins = BuiltinTable()


@builtins.add
class Concat(Builtin):
    name = 'DA.Internal.Prelude:concat'
    args = list_type(list_type(var('x'))),

    def evaluate(self, _: 'Sequence[Type]', args: 'Sequence[Any]') -> 'Any':
        xxs = args[0]

        result = []
        for xs in xxs:
            result.extend(xs)
        return result

    def simplify(self, _: 'Sequence[Type]', args: 'Sequence[Expr]') -> 'Optional[Expr]':
        xxs = args[0]

        # if there is a single-element list as an arg to concat, simply remove the function call
        # and fully unwrap
        if xxs.cons is not None and xxs.cons.tail.nil is not None and len(xxs.cons.front) == 1:
            return xxs.cons.front[0]
        if xxs.nil is not None:
            return Expr(nil=Expr.Nil(xxs.nil.type.prim.args[0]))


@builtins.add
class Show(Builtin):
    name = 'GHC.Show:show'
    args = (STRING, STRING)

    def evaluate(self, _: 'Sequence[Type]', args: 'Sequence[Any]') -> 'Any':
        return str(args[1])

    def simplify(self, _: 'Sequence[Type]', args: 'Sequence[Expr]') -> 'Optional[Expr]':
        return None


@builtins.add
class AppendText(Builtin):
    builtin = BuiltinFunction.APPEND_TEXT
    args = (STRING, STRING)

    def evaluate(self, _: 'Sequence[Type]', args: 'Sequence[Any]') -> 'Any':
        return args[0] + args[1]

    def simplify(self, _: 'Sequence[Type]', args: 'Sequence[Expr]') -> 'Expr':
        if args[0].prim_lit is not None and args[1].prim_lit is not None:
            return Expr(prim_lit=PrimLit(text=args[0].prim_lit.text + args[1].prim_lit.text))



