# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Generic, TypeVar
from .daml_lf_1 import Expr, Type, ValName, BuiltinFunction, PrimCon, PrimLit, Case, Block, Update, \
    Scenario, Package, Module, FieldWithType, FieldWithExpr, VarWithType, Binding

E = TypeVar('E', contravariant=True)
RP = TypeVar('RP', covariant=True)
RM = TypeVar('RM', covariant=True)
RE = TypeVar('RE', covariant=True)
RT = TypeVar('RT', covariant=True)
_tuple = tuple


class PackageVisitor(Generic[RP]):
    def visit_package(self, package: 'Package') -> 'RP':
        raise NotImplementedError


class ModuleVisitor(Generic[RM]):
    def visit_module(self, module: 'Module') -> 'RM':
        raise NotImplementedError


class ExprVisitor(Generic[RE]):

    def visit_expr(self, expr: 'Expr') -> 'RE':
        return expr.Sum_match(
            self.visit_expr_var,
            self.visit_expr_val,
            self.visit_expr_builtin,
            self.visit_expr_prim_con,
            self.visit_expr_prim_lit,
            self.visit_expr_rec_con,
            self.visit_expr_rec_proj,
            self.visit_expr_variant_con,
            self.visit_expr_enum_con,
            self.visit_expr_tuple_con,
            self.visit_expr_tuple_proj,
            self.visit_expr_app,
            self.visit_expr_ty_app,
            self.visit_expr_abs,
            self.visit_expr_ty_abs,
            self.visit_expr_case,
            self.visit_expr_let,
            self.visit_expr_nil,
            self.visit_expr_cons,
            self.visit_expr_update,
            self.visit_expr_scenario,
            self.visit_expr_rec_upd,
            self.visit_expr_tuple_upd,
            self.visit_expr_optional_none,
            self.visit_expr_optional_some)

    def visit_expr_var(self, var: str) -> 'RE':
        raise NotImplementedError

    def visit_expr_val(self, val: 'ValName') -> 'RE':
        raise NotImplementedError

    def visit_expr_builtin(self, builtin: 'BuiltinFunction') -> 'RE':
        raise NotImplementedError

    def visit_expr_prim_con(self, prim_con: 'PrimCon') -> 'RE':
        raise NotImplementedError

    def visit_expr_prim_lit(self, prim_lit: 'PrimLit') -> 'RE':
        raise NotImplementedError

    def visit_expr_rec_con(self, rec_con: 'Expr.RecCon') -> 'RE':
        raise NotImplementedError

    def visit_expr_rec_proj(self, rec_proj: 'Expr.RecProj') -> 'RE':
        raise NotImplementedError

    def visit_expr_variant_con(self, variant_con: 'Expr.VariantCon') -> 'RE':
        raise NotImplementedError

    def visit_expr_enum_con(self, tuple_con: 'Expr.EnumCon') -> 'RE':
        raise NotImplementedError

    def visit_expr_tuple_con(self, tuple_con: 'Expr.TupleCon') -> 'RE':
        raise NotImplementedError

    def visit_expr_tuple_proj(self, tuple_proj: 'Expr.TupleProj') -> 'RE':
        raise NotImplementedError

    def visit_expr_app(self, app: 'Expr.App') -> 'RE':
        raise NotImplementedError

    def visit_expr_ty_app(self, ty_app: 'Expr.TyApp') -> 'RE':
        raise NotImplementedError

    def visit_expr_abs(self, abs_: 'Expr.Abs') -> 'RE':
        raise NotImplementedError

    def visit_expr_ty_abs(self, ty_abs: 'Expr.TyAbs') -> 'RE':
        raise NotImplementedError

    def visit_expr_case(self, case: 'Case') -> 'RE':
        raise NotImplementedError

    def visit_expr_let(self, let: 'Block') -> 'RE':
        raise NotImplementedError

    def visit_expr_nil(self, nil: 'Expr.Nil') -> 'RE':
        raise NotImplementedError

    def visit_expr_cons(self, cons: 'Expr.Cons') -> 'RE':
        raise NotImplementedError

    def visit_expr_update(self, update: 'Update') -> 'RE':
        raise NotImplementedError

    def visit_expr_scenario(self, scenario: 'Scenario') -> 'RE':
        raise NotImplementedError

    def visit_expr_rec_upd(self, rec_upd: 'Expr.RecUpd') -> 'RE':
        raise NotImplementedError

    def visit_expr_tuple_upd(self, tuple_upd: 'Expr.TupleUpd') -> 'RE':
        raise NotImplementedError

    def visit_expr_optional_none(self, optional_none: 'Expr.OptionalNone') -> 'RE':
        raise NotImplementedError

    def visit_expr_optional_some(self, optional_some: 'Expr.OptionalSome') -> 'RE':
        raise NotImplementedError


class TypeVisitor(Generic[RT]):

    def visit_type(self, type: 'Type') -> 'RT':
        return type.Sum_match(
            self.visit_type_var,
            self.visit_type_con,
            self.visit_type_prim,
            self.visit_type_forall,
            self.visit_type_tuple)

    def visit_type_var(self, var: 'Type.Var') -> 'RT':
        raise NotImplementedError

    def visit_type_con(self, con: 'Type.Con') -> 'RT':
        raise NotImplementedError

    def visit_type_prim(self, prim: 'Type.Prim') -> 'RT':
        raise NotImplementedError

    def visit_type_forall(self, forall: 'Type.Forall') -> 'RT':
        raise NotImplementedError

    def visit_type_tuple(self, tuple: 'Type.Tuple') -> 'RT':
        raise NotImplementedError


class IdentityTypeVisitor(TypeVisitor[Type]):

    def resolve_type(self, var: 'str') -> 'Optional[Type]':
        """
        Return a :class:`Type` for the specified variable, or ``None`` if there is no mapping for
        that type variable.
        """
        raise NotImplementedError

    def visit_type_var(self, var: 'Type.Var') -> 'Type':
        resolved_type = self.resolve_type(var.var)
        if resolved_type is not None:
            base_type = self.visit_type(resolved_type)
        else:
            base_type = Type(var=var)

        if var.args:
            new_args = tuple(self.visit_type(arg) for arg in var.args)
            return Type(var=Type.Var(var=var.var, args=new_args))
        else:
            return base_type

    def visit_type_con(self, con: 'Type.Con') -> 'Type':
        new_args = tuple(self.visit_type(arg) for arg in con.args)
        return Type(con=Type.Con(tycon=con.tycon, args=new_args))

    def visit_type_prim(self, prim: 'Type.Prim') -> 'Type':
        new_args = tuple(self.visit_type(arg) for arg in prim.args)
        return Type(prim=Type.Prim(prim=prim.prim, args=new_args))

    def visit_type_forall(self, forall: 'Type.Forall') -> 'Type':
        new_body = self.visit_type(forall.body)
        return Type(forall=Type.Forall(forall.vars, new_body))

    def visit_type_tuple(self, tuple: 'Type.Tuple') -> 'Type':
        new_fields = _tuple([FieldWithType(field=fwt.field, type=self.visit_type(fwt.type))
                             for fwt in tuple.fields])
        return Type(tuple=Type.Tuple(fields=new_fields))


class IdentityVisitor(ExprVisitor[Expr], IdentityTypeVisitor):
    """
    Implementation of :class:`ExprVisitor` that returns the same object for every case.
    """

    def visit_expr(self, expr: 'Expr') -> 'Expr':
        return super(IdentityVisitor, self).visit_expr(expr)

    def visit_expr_var(self, var: str) -> 'Expr':
        return Expr(var=var)

    def visit_expr_val(self, val: 'ValName') -> 'Expr':
        return Expr(val=val)

    def visit_expr_builtin(self, builtin: 'BuiltinFunction') -> 'Expr':
        return Expr(builtin=builtin)

    def visit_expr_prim_con(self, prim_con: 'PrimCon') -> 'Expr':
        return Expr(prim_con=prim_con)

    def visit_expr_prim_lit(self, prim_lit: 'PrimLit') -> 'Expr':
        return Expr(prim_lit=prim_lit)

    def visit_expr_rec_con(self, rec_con: 'Expr.RecCon') -> 'Expr':
        new_fields = tuple([FieldWithExpr(fwt.field, self.visit_expr(fwt.expr))
                            for fwt in rec_con.fields])
        new_tycon = self.visit_type_con(rec_con.tycon).con
        return Expr(rec_con=Expr.RecCon(tycon=new_tycon, fields=new_fields))

    def visit_expr_rec_proj(self, rec_proj: 'Expr.RecProj') -> 'Expr':
        new_tycon = self.visit_type_con(rec_proj.tycon).con
        new_record = self.visit_expr(rec_proj.record)
        return Expr(rec_proj=Expr.RecProj(tycon=new_tycon, field=rec_proj.field, record=new_record))

    def visit_expr_variant_con(self, variant_con: 'Expr.VariantCon') -> 'Expr':
        new_type_con = self.visit_type_con(variant_con.tycon).con
        new_variant_arg = self.visit_expr(variant_con.variant_arg)
        return Expr(variant_con=Expr.VariantCon(
            tycon=new_type_con, variant_con=variant_con.variant_con, variant_arg=new_variant_arg))

    def visit_expr_enum_con(self, enum_con: 'Expr.EnumCon') -> 'Expr':
        new_type_con = self.visit_type_con(enum_con.tycon).con
        return Expr(enum_con=Expr.EnumCon(tycon=new_type_con, enum_con=enum_con.enum_con))

    def visit_expr_tuple_con(self, tuple_con: 'Expr.TupleCon') -> 'Expr':
        new_fields = tuple([FieldWithExpr(fwt.field, self.visit_expr(fwt.expr))
                            for fwt in tuple_con.fields])
        return Expr(tuple_con=Expr.TupleCon(fields=new_fields))

    def visit_expr_tuple_proj(self, tuple_proj: 'Expr.TupleProj') -> 'Expr':
        new_tuple = self.visit_expr(tuple_proj.tuple)
        return Expr(tuple_proj=Expr.TupleProj(field=tuple_proj.field, tuple=new_tuple))

    def visit_expr_app(self, app: 'Expr.App') -> 'Expr':
        new_fun = self.visit_expr(app.fun)
        new_args = tuple([self.visit_expr(arg) for arg in app.args])
        return Expr(app=Expr.App(new_fun, new_args))

    def visit_expr_ty_app(self, ty_app: 'Expr.TyApp') -> 'Expr':
        new_expr = self.visit_expr(ty_app.expr)
        new_types = tuple([self.visit_type(t) for t in ty_app.types])
        return Expr(ty_app=Expr.TyApp(new_expr, new_types))

    def visit_expr_abs(self, abs_: 'Expr.Abs') -> 'Expr':
        new_body = self.visit_expr(abs_.body)
        return Expr(abs=Expr.Abs(param=abs_.param, body=new_body))

    def visit_expr_ty_abs(self, ty_abs: 'Expr.TyAbs') -> 'Expr':
        new_body = self.visit_expr(ty_abs.body)
        return Expr(ty_abs=Expr.TyAbs(param=ty_abs.param, body=new_body))

    def visit_expr_case(self, case: 'Case') -> 'Expr':
        new_scrut = self.visit_expr(case.scrut)
        # TODO: Real implementation
        new_alts = [alt for alt in case.alts]
        return Expr(case=Case(scrut=new_scrut, alts=new_alts))

    def visit_expr_let(self, let: 'Block') -> 'Expr':
        new_bindings = [Binding(VarWithType(binding.binder.var, self.visit_type(binding.binder.type)),
                                self.visit_expr(binding.bound)) for binding in let.bindings]
        new_body = self.visit_expr(let.body)
        return Expr(let=Block(bindings=new_bindings, body=new_body))

    def visit_expr_nil(self, nil: 'Expr.Nil') -> 'Expr':
        return Expr(nil=Expr.Nil(self.visit_type(nil.type)))

    def visit_expr_cons(self, cons: 'Expr.Cons') -> 'Expr':
        new_type = self.visit_type(cons.type)
        new_front = tuple(self.visit_expr(front) for front in cons.front)
        new_tail = self.visit_expr(cons.tail)
        return Expr(cons=Expr.Cons(type=new_type, front=new_front, tail=new_tail))

    def visit_expr_update(self, update: 'Update') -> 'Expr':
        return Expr(update=update)

    def visit_expr_scenario(self, scenario: 'Scenario') -> 'Expr':
        return Expr(scenario=scenario)

    def visit_expr_rec_upd(self, rec_upd: 'Expr.RecUpd') -> 'Expr':
        return Expr(rec_upd=rec_upd)

    def visit_expr_tuple_upd(self, tuple_upd: 'Expr.TupleUpd') -> 'Expr':
        return Expr(tuple_upd=tuple_upd)

    def visit_expr_optional_none(self, optional_none: 'Expr.OptionalNone') -> 'Expr':
        new_type = self.visit_type(optional_none.type)
        return Expr(optional_none=Expr.OptionalNone(type=new_type))

    def visit_expr_optional_some(self, optional_some: 'Expr.OptionalSome') -> 'Expr':
        new_type = self.visit_type(optional_some.type)
        new_body = self.visit_expr(optional_some.body)
        return Expr(optional_some=Expr.OptionalSome(type=new_type, body=new_body))
