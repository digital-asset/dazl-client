# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from dataclasses import dataclass
from datetime import datetime, date, timedelta, timezone
from decimal import Decimal
from typing import Any, Union

from ..damlast.builtins import builtins
from ..damlast import ExprVisitor, IdentityTypeVisitor
from ..damlast.daml_lf_1 import Block, BuiltinFunction, Case, Expr, PrimCon, PrimLit, Scenario, \
    Type, Update, ValName
from ..model.core import Party
from ..util.prim_types import frozendict


@dataclass(frozen=True)
class Constant:
    value: Any


class ExpressionEvaluator(ExprVisitor[Any], IdentityTypeVisitor):
    """
    Compute the result of an expression.
    """

    def visit_expr(self, expr: 'Union[Expr, Constant]'):
        if isinstance(expr, Constant):
            return expr.value
        else:
            return super(ExpressionEvaluator, self).visit_expr(expr)

    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def visit_constant(self, constant: Constant) -> 'Any':
        return constant.value

    def visit_expr_var(self, var: str) -> 'Any':
        pass

    def visit_expr_val(self, val: 'ValName') -> 'Any':
        pass

    def visit_expr_builtin(self, builtin: 'BuiltinFunction') -> 'Any':
        return builtins.resolve(builtin).evaluate()

    def visit_expr_prim_con(self, prim_con: 'PrimCon') -> 'Any':
        if PrimCon.CON_TRUE == prim_con:
            return True
        elif PrimCon.CON_FALSE == prim_con:
            return False
        elif PrimCon.CON_UNIT == prim_con:
            return {}
        else:
            raise ValueError(f'unknown PrimCon value: {prim_con}')

    def visit_expr_prim_lit(self, prim_lit: 'PrimLit') -> 'Any':
        if prim_lit.int64 is not None:
            return prim_lit.int64
        elif prim_lit.decimal is not None:
            return Decimal(prim_lit.decimal)
        elif prim_lit.text is not None:
            return prim_lit.text
        elif prim_lit.timestamp is not None:
            return datetime.fromtimestamp(prim_lit.timestamp / 1e9, timezone.utc)
        elif prim_lit.party is not None:
            return Party(prim_lit.party)
        elif prim_lit.date is not None:
            return date(1970, 1, 1) + timedelta(days=prim_lit.date)
        else:
            raise ValueError(f'unknown PrimLit value: {prim_lit}')

    def visit_expr_rec_con(self, rec_con: 'Expr.RecCon') -> 'Any':
        return frozendict({fwt.field: self.visit_expr(fwt.expr) for fwt in rec_con.fields})

    def visit_expr_rec_proj(self, rec_proj: 'Expr.RecProj') -> 'Any':
        record_expr = self.visit_expr(rec_proj.record)
        return record_expr[rec_proj.field]

    def visit_expr_variant_con(self, variant_con: 'Expr.VariantCon') -> 'Any':
        ctor = variant_con.variant_con
        value = self.visit_expr(variant_con.variant_arg)
        return frozendict({ctor: value})

    def visit_expr_tuple_con(self, tuple_con: 'Expr.TupleCon') -> 'Any':
        return frozendict({fwt.field: self.visit_expr(fwt.expr) for fwt in tuple_con.fields})

    def visit_expr_tuple_proj(self, tuple_proj: 'Expr.TupleProj') -> 'Any':
        tuple_expr = self.visit_expr(tuple_proj.tuple)
        return tuple_expr[tuple_proj.field]

    def visit_expr_app(self, app: 'Expr.App') -> 'Any':
        fun = self.visit_expr(app.fun)
        args = [self.visit_expr(arg) for arg in app.args]
        return fun.apply(*args)

    def visit_expr_ty_app(self, ty_app: 'Expr.TyApp') -> 'Any':
        pass

    def visit_expr_abs(self, abs_: 'Expr.Abs') -> 'Any':
        pass

    def visit_expr_ty_abs(self, ty_abs: 'Expr.TyAbs') -> 'Any':
        pass

    def visit_expr_case(self, case: 'Case') -> 'Any':
        pass

    def visit_expr_let(self, let: 'Block') -> 'Any':
        current_scope = self
        for binding in let.bindings:
            var = binding.binder.var
            value = current_scope.eval_Expr(binding.bound)
            current_scope = current_scope.child_evaluator(value_bindings={var: Constant(value)})
        return current_scope.eval_Expr(let.body)

    def visit_expr_nil(self, nil: 'Expr.Nil') -> 'Any':
        pass

    def visit_expr_cons(self, cons: 'Expr.Cons') -> 'Any':
        pass

    def visit_expr_update(self, update: 'Update') -> 'Any':
        raise RuntimeError('expressions cannot currently be evaluated in the Update monad')

    def visit_expr_scenario(self, scenario: 'Scenario') -> 'Any':
        raise RuntimeError('expressions cannot currently be evaluated in the Scenario monad')

    def visit_expr_rec_upd(self, rec_upd: 'Expr.RecUpd') -> 'Any':
        raise RuntimeError('expressions cannot currently be evaluated in the Update monad')

    def visit_expr_tuple_upd(self, tuple_upd: 'Expr.TupleUpd') -> 'Any':
        raise RuntimeError('expressions cannot currently be evaluated in the Update monad')

    def visit_expr_optional_none(self, optional_none: 'Expr.OptionalNone') -> 'Any':
        return None

    def visit_expr_optional_some(self, optional_some: 'Expr.OptionalSome') -> 'Any':
        return self.visit_expr(optional_some.body)

    def visit_type_var(self, var: 'Type.Var') -> 'Type':
        resolved_type = self.resolve_type(var.var)
        if resolved_type is not None:
            return self.visit_type(resolved_type)
        else:
            return Type(var=var)

