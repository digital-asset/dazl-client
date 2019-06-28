# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Optional

from ..damlast.visitor import ExprVisitor, IdentityTypeVisitor
from ..damlast.daml_lf_1 import Expr, Type, PrimType, FieldWithType, PrimCon, PrimLit, BuiltinFunction, ValName
from ..model.types_store import PackageStore
from ..util.typing import safe_cast


class TypeComputer(ExprVisitor[Type], IdentityTypeVisitor):
    """
    Evaluate the :class:`Type` of an :class:`Expr`.
    """
    def __init__(self, store: 'PackageStore'):
        self.store = safe_cast(PackageStore, store)

    def resolve_type(self, var: str) -> 'Optional[Type]':
        return None

    def visit_expr_var(self, var: str) -> 'Type':
        pass

    def visit_expr_val(self, val: 'ValName') -> 'Type':
        vref = self.store.resolve_value_reference(val)
        if vref is not None:
            return self.visit_expr(vref)
        else:
            raise RuntimeError(f'unknown val name: {val}')

    def visit_expr_builtin(self, builtin: 'BuiltinFunction') -> 'Type':
        pass

    def visit_expr_prim_con(self, prim_con: 'PrimCon') -> 'Type':
        if PrimCon.CON_TRUE == prim_con or PrimCon.CON_FALSE == prim_con:
            return Type(prim=Type.Prim(PrimType.BOOL, args=()))
        else:
            return Type(prim=Type.Prim(PrimType.UNIT, args=()))

    def visit_expr_prim_lit(self, prim_lit: 'PrimLit') -> 'Type':
        if prim_lit.int64 is not None:
            return Type(prim=Type.Prim(PrimType.INT64, args=()))
        elif prim_lit.date is not None:
            return Type(prim=Type.Prim(PrimType.DATE, args=()))
        elif prim_lit.timestamp is not None:
            return Type(prim=Type.Prim(PrimType.TIMESTAMP, args=()))
        elif prim_lit.decimal is not None:
            return Type(prim=Type.Prim(PrimType.DECIMAL, args=()))
        elif prim_lit.party is not None:
            return Type(prim=Type.Prim(PrimType.PARTY, args=()))
        elif prim_lit.text is not None:
            return Type(prim=Type.Prim(PrimType.TEXT, args=()))
        else:
            raise RuntimeError('unknown prim lit type')

    def visit_expr_rec_con(self, rec_con: 'Expr.RecCon') -> 'Type':
        return self.visit_type(Type(con=rec_con.tycon))

    def visit_expr_rec_proj(self, rec_proj: 'Expr.RecProj') -> 'Type':
        rec_type = self.visit_type_con(rec_proj.tycon)
        old_type = self.store.resolve_type_reference(rec_type.con.tycon)
        for n, v in old_type.as_args_list():
            if n == rec_proj.field:
                return get_new_type(v)

    def visit_expr_variant_con(self, variant_con: 'Expr.VariantCon') -> 'Type':
        return self.visit_type(Type(con=variant_con.tycon))

    def visit_expr_tuple_con(self, tuple_con: 'Expr.TupleCon') -> 'Type':
        return Type(tuple=Type.Tuple([FieldWithType(fwe.field, self.visit_expr(fwe.expr))
                                      for fwe in tuple_con.fields]))

    def visit_expr_tuple_proj(self, tuple_proj: 'Expr.TupleProj') -> 'Type':
        pass

    def visit_expr_app(self, app: 'Expr.App') -> 'Type':
        fun_type = self.visit_expr(app.fun)
        if fun_type.prim.prim == PrimType.ARROW:
            t = fun_type
            arg_count = len(app.args)
            while arg_count > 0:
                arg_count -= 1
                t = t.prim.args[1]
            return t
        else:
            raise ValueError(f'unexpected type of app body: {fun_type}')

    def visit_expr_ty_app(self, ty_app: 'Expr.TyApp') -> 'Type':
        core_type = self.visit_expr(ty_app.expr)
        if ty_app.types:
            def unexpected_type_error(*_, **__):
                raise RuntimeError('Unexpected tyapp')

            return core_type.Sum_match(
                lambda var: Type(var=Type.Var(var=var.var, args=var.args + ty_app.types)),
                lambda con: Type(con=Type.Con(tycon=con.tycon, args=con.args + ty_app.types)),
                lambda prim: Type(prim=Type.Prim(prim=prim.prim, args=prim.args + ty_app.types)),
                lambda forall: unexpected_type_error,
                lambda tuple: unexpected_type_error)
        return core_type

    def visit_expr_abs(self, abs_: 'Expr.Abs') -> 'Type':
        t = self.visit_expr(abs_.body)
        for param in reversed(abs_.param):
            t = arrow_type(param.type, t)
        return t

    def visit_expr_ty_abs(self, ty_abs: 'Expr.TyAbs') -> 'Type':
        return '...'
        #scope = self.with_type_var() ty_abs.param[0].var
        #return scope.visit_expr(ty_abs.body)

    def visit_expr_case(self, case: 'Case') -> 'Type':
        # TODO: Probably not right
        return self.visit_expr(case.alts[0].body)

    def visit_expr_let(self, let: 'Block') -> 'Type':
        return self.visit_expr(let.body)

    def visit_expr_nil(self, nil: 'Expr.Nil') -> 'Type':
        return Type(prim=Type.Prim(PrimType.LIST, [self.visit_type(nil.type)]))

    def visit_expr_cons(self, cons: 'Expr.Cons') -> 'Type':
        return Type(prim=Type.Prim(PrimType.LIST, [self.visit_type(cons.type)]))

    def visit_expr_update(self, update: 'Update') -> 'Type':
        raise Exception('Update not yet supported')

    def visit_expr_scenario(self, scenario: 'Scenario') -> 'Type':
        raise Exception('Scenario not yet supported')

    def visit_expr_rec_upd(self, rec_upd: 'Expr.RecUpd') -> 'Type':
        raise Exception('Update not yet supported')

    def visit_expr_tuple_upd(self, tuple_upd: 'Expr.TupleUpd') -> 'Type':
        raise Exception('Update not yet supported')

    def visit_expr_optional_none(self, optional_none: 'Expr.OptionalNone') -> 'Type':
        return Type(prim=Type.Prim(PrimType.OPTIONAL, [self.visit_type(optional_none.type)]))

    def visit_expr_optional_some(self, optional_some: 'Expr.OptionalSome') -> 'Type':
        return Type(prim=Type.Prim(PrimType.OPTIONAL, [self.visit_type(optional_some.type)]))

    def visit_type_var(self, var: 'Type.Var') -> 'Type':
        resolved_type = self.resolve_type(var.var)
        if resolved_type is not None:
            return self.visit_type(resolved_type)
        else:
            return Type(var=var)


def arrow_type(input: 'Type', output: 'Type') -> 'Type':
    return Type(prim=Type.Prim(PrimType.ARROW, (input, output)))
