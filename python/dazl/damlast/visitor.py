# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from .daml_lf_1 import (
    Binding,
    Block,
    BuiltinFunction,
    Case,
    Expr,
    FieldWithExpr,
    FieldWithType,
    Module,
    Package,
    PrimCon,
    PrimLit,
    Scenario,
    Type,
    Update,
    ValName,
    VarWithType,
)

E = TypeVar("E", contravariant=True)
RP = TypeVar("RP", covariant=True)
RM = TypeVar("RM", covariant=True)
RE = TypeVar("RE", covariant=True)
RT = TypeVar("RT", covariant=True)


__all__ = [
    "ExprVisitor",
    "IdentityTypeVisitor",
    "IdentityVisitor",
    "ModuleVisitor",
    "PackageVisitor",
    "TypeVisitor",
]


class PackageVisitor(Generic[RP]):
    def visit_package(self, p: Package, /) -> RP:
        raise NotImplementedError


class ModuleVisitor(Generic[RM]):
    def visit_module(self, m: Module, /) -> RM:
        raise NotImplementedError


class ExprVisitor(Generic[RE]):
    def visit_expr(self, e: Expr, /) -> RE:
        return e.Sum_match(
            self.visit_expr_var,
            self.visit_expr_val,
            self.visit_expr_builtin,
            self.visit_expr_prim_con,
            self.visit_expr_prim_lit,
            self.visit_expr_rec_con,
            self.visit_expr_rec_proj,
            self.visit_expr_rec_upd,
            self.visit_expr_variant_con,
            self.visit_expr_enum_con,
            self.visit_expr_struct_con,
            self.visit_expr_struct_proj,
            self.visit_expr_struct_upd,
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
            self.visit_expr_optional_none,
            self.visit_expr_optional_some,
            self.visit_expr_to_any,
            self.visit_expr_from_any,
            self.visit_expr_type_rep,
            self.visit_expr_to_any_exception,
            self.visit_expr_from_any_exception,
            self.visit_expr_throw,
            self.visit_expr_to_interface,
            self.visit_expr_from_interface,
            self.visit_expr_call_interface,
            self.visit_expr_signatory_interface,
            self.visit_expr_observer_interface,
            self.visit_expr_view_interface,
            self.visit_expr_unsafe_from_interface,
            self.visit_expr_interface_template_type_rep,
            self.visit_expr_to_required_interface,
            self.visit_expr_from_required_interface,
            self.visit_expr_unsafe_from_required_interface,
            self.visit_expr_experimental,
        )

    def visit_expr_var(self, e: str, /) -> RE:
        raise NotImplementedError

    def visit_expr_val(self, e: ValName, /) -> RE:
        raise NotImplementedError

    def visit_expr_builtin(self, e: BuiltinFunction, /) -> RE:
        raise NotImplementedError

    def visit_expr_prim_con(self, e: PrimCon, /) -> RE:
        raise NotImplementedError

    def visit_expr_prim_lit(self, e: PrimLit, /) -> RE:
        raise NotImplementedError

    def visit_expr_rec_con(self, e: Expr.RecCon, /) -> RE:
        raise NotImplementedError

    def visit_expr_rec_proj(self, e: Expr.RecProj, /) -> RE:
        raise NotImplementedError

    def visit_expr_variant_con(self, e: Expr.VariantCon, /) -> RE:
        raise NotImplementedError

    def visit_expr_enum_con(self, e: Expr.EnumCon, /) -> RE:
        raise NotImplementedError

    def visit_expr_struct_con(self, e: Expr.StructCon, /) -> RE:
        raise NotImplementedError

    def visit_expr_struct_proj(self, e: Expr.StructProj, /) -> RE:
        raise NotImplementedError

    def visit_expr_app(self, e: Expr.App, /) -> RE:
        raise NotImplementedError

    def visit_expr_ty_app(self, e: Expr.TyApp, /) -> RE:
        raise NotImplementedError

    def visit_expr_abs(self, e: Expr.Abs, /) -> RE:
        raise NotImplementedError

    def visit_expr_ty_abs(self, e: Expr.TyAbs, /) -> RE:
        raise NotImplementedError

    def visit_expr_case(self, e: Case, /) -> RE:
        raise NotImplementedError

    def visit_expr_let(self, e: Block, /) -> RE:
        raise NotImplementedError

    def visit_expr_nil(self, e: Expr.Nil, /) -> RE:
        raise NotImplementedError

    def visit_expr_cons(self, e: Expr.Cons, /) -> RE:
        raise NotImplementedError

    def visit_expr_update(self, e: Update, /) -> RE:
        raise NotImplementedError

    def visit_expr_scenario(self, e: Scenario, /) -> RE:
        raise NotImplementedError

    def visit_expr_rec_upd(self, e: Expr.RecUpd, /) -> RE:
        raise NotImplementedError

    def visit_expr_struct_upd(self, e: Expr.StructUpd, /) -> RE:
        raise NotImplementedError

    def visit_expr_optional_none(self, e: Expr.OptionalNone, /) -> RE:
        raise NotImplementedError

    def visit_expr_optional_some(self, e: Expr.OptionalSome, /) -> RE:
        raise NotImplementedError

    def visit_expr_to_any(self, e: Expr.ToAny, /) -> RE:
        raise NotImplementedError

    def visit_expr_from_any(self, e: Expr.FromAny, /) -> RE:
        raise NotImplementedError

    def visit_expr_type_rep(self, e: Type, /) -> RE:
        raise NotImplementedError

    def visit_expr_throw(self, e: Expr.Throw, /) -> RE:
        raise NotImplementedError

    def visit_expr_to_any_exception(self, e: Expr.ToAnyException, /) -> RE:
        raise NotImplementedError

    def visit_expr_from_any_exception(self, e: Expr.FromAnyException, /) -> RE:
        raise NotImplementedError

    def visit_expr_to_interface(self, e: Expr.ToInterface, /) -> RE:
        raise NotImplementedError

    def visit_expr_from_interface(self, e: Expr.FromInterface, /) -> RE:
        raise NotImplementedError

    def visit_expr_call_interface(self, e: Expr.CallInterface, /) -> RE:
        raise NotImplementedError

    def visit_expr_signatory_interface(self, e: Expr.SignatoryInterface, /) -> RE:
        raise NotImplementedError

    def visit_expr_observer_interface(self, e: Expr.ObserverInterface, /) -> RE:
        raise NotImplementedError

    def visit_expr_view_interface(self, e: Expr.ViewInterface, /) -> RE:
        raise NotImplementedError

    def visit_expr_unsafe_from_interface(self, e: Expr.UnsafeFromInterface, /) -> RE:
        raise NotImplementedError

    def visit_expr_interface_template_type_rep(self, e: Expr.InterfaceTemplateTypeRep, /) -> RE:
        raise NotImplementedError

    def visit_expr_to_required_interface(self, e: Expr.ToRequiredInterface, /) -> RE:
        raise NotImplementedError

    def visit_expr_from_required_interface(self, e: Expr.FromRequiredInterface, /) -> RE:
        raise NotImplementedError

    def visit_expr_unsafe_from_required_interface(
        self, e: Expr.UnsafeFromRequiredInterface, /
    ) -> RE:
        raise NotImplementedError

    def visit_expr_experimental(self, e: Expr.Experimental, /) -> RE:
        raise NotImplementedError


class TypeVisitor(Generic[RT]):
    def visit_type(self, t: Type, /) -> RT:
        return t.Sum_match(
            self.visit_type_var,
            self.visit_type_con,
            self.visit_type_prim,
            self.visit_type_forall,
            self.visit_type_struct,
            self.visit_type_nat,
            self.visit_type_syn,
        )

    def visit_type_var(self, t: Type.Var, /) -> RT:
        raise NotImplementedError

    def visit_type_con(self, t: Type.Con, /) -> RT:
        raise NotImplementedError

    def visit_type_prim(self, t: Type.Prim, /) -> RT:
        raise NotImplementedError

    def visit_type_forall(self, t: Type.Forall, /) -> RT:
        raise NotImplementedError

    def visit_type_struct(self, t: Type.Struct, /) -> RT:
        raise NotImplementedError

    def visit_type_nat(self, nat: int) -> RT:
        raise NotImplementedError

    def visit_type_syn(self, t: Type.Syn) -> RT:
        raise NotImplementedError


class IdentityTypeVisitor(TypeVisitor[Type]):
    def resolve_type(self, var: str, /) -> Optional[Type]:
        """
        Return a :class:`Type` for the specified variable, or ``None`` if there is no mapping for
        that type variable.
        """
        raise NotImplementedError

    def visit_type_var(self, t: Type.Var, /) -> Type:
        resolved_type = self.resolve_type(t.var)
        if resolved_type is not None:
            base_type = self.visit_type(resolved_type)
        else:
            base_type = Type(var=t)

        if t.args:
            new_args = tuple(self.visit_type(arg) for arg in t.args)
            return Type(var=Type.Var(var=t.var, args=new_args))
        else:
            return base_type

    def visit_type_con(self, t: Type.Con, /) -> Type:
        new_args = tuple(self.visit_type(arg) for arg in t.args)
        return Type(con=Type.Con(tycon=t.tycon, args=new_args))

    def visit_type_prim(self, t: Type.Prim, /) -> Type:
        new_args = tuple(self.visit_type(arg) for arg in t.args)
        return Type(prim=Type.Prim(prim=t.prim, args=new_args))

    def visit_type_forall(self, t: Type.Forall, /) -> Type:
        new_body = self.visit_type(t.body)
        return Type(forall=Type.Forall(t.vars, new_body))

    def visit_type_struct(self, t: Type.Struct, /) -> Type:
        new_fields = tuple(
            FieldWithType(field=fwt.field, type=self.visit_type(fwt.type)) for fwt in t.fields
        )
        return Type(struct=Type.Struct(fields=new_fields))

    def visit_type_nat(self, nat: int, /) -> Type:
        return Type(nat=nat)


class IdentityVisitor(ExprVisitor[Expr], IdentityTypeVisitor):
    """
    Implementation of :class:`ExprVisitor` that returns the same object for every case.
    """

    def visit_expr(self, e: Expr) -> Expr:
        return super(IdentityVisitor, self).visit_expr(e)

    def visit_expr_var(self, e: str, /) -> Expr:
        return Expr(var=e)

    def visit_expr_val(self, e: ValName, /) -> Expr:
        return Expr(val=e)

    def visit_expr_builtin(self, e: BuiltinFunction, /) -> Expr:
        return Expr(builtin=e)

    def visit_expr_prim_con(self, e: PrimCon, /) -> Expr:
        return Expr(prim_con=e)

    def visit_expr_prim_lit(self, e: PrimLit, /) -> Expr:
        return Expr(prim_lit=e)

    def visit_expr_rec_con(self, e: Expr.RecCon, /) -> Expr:
        new_fields = tuple(FieldWithExpr(fwt.field, self.visit_expr(fwt.expr)) for fwt in e.fields)
        new_tycon = self.visit_type_con(e.tycon).con
        return Expr(rec_con=Expr.RecCon(tycon=new_tycon, fields=new_fields))

    def visit_expr_rec_proj(self, e: Expr.RecProj, /) -> Expr:
        new_tycon = self.visit_type_con(e.tycon).con
        new_record = self.visit_expr(e.record)
        return Expr(rec_proj=Expr.RecProj(tycon=new_tycon, field=e.field, record=new_record))

    def visit_expr_variant_con(self, e: Expr.VariantCon, /) -> Expr:
        new_type_con = self.visit_type_con(e.tycon).con
        new_variant_arg = self.visit_expr(e.variant_arg)
        return Expr(
            variant_con=Expr.VariantCon(
                tycon=new_type_con, variant_con=e.variant_con, variant_arg=new_variant_arg
            )
        )

    def visit_expr_enum_con(self, e: Expr.EnumCon, /) -> Expr:
        return Expr(enum_con=Expr.EnumCon(tycon=e.tycon, enum_con=e.enum_con))

    def visit_expr_struct_con(self, e: Expr.StructCon, /) -> Expr:
        new_fields = tuple(FieldWithExpr(fwt.field, self.visit_expr(fwt.expr)) for fwt in e.fields)
        return Expr(struct_con=Expr.StructCon(fields=new_fields))

    def visit_expr_struct_proj(self, e: Expr.StructProj, /) -> Expr:
        new_struct = self.visit_expr(e.struct)
        return Expr(struct_proj=Expr.StructProj(field=e.field, struct=new_struct))

    def visit_expr_app(self, e: Expr.App, /) -> Expr:
        new_fun = self.visit_expr(e.fun)
        new_args = tuple([self.visit_expr(arg) for arg in e.args])
        return Expr(app=Expr.App(new_fun, new_args))

    def visit_expr_ty_app(self, e: Expr.TyApp, /) -> Expr:
        new_expr = self.visit_expr(e.expr)
        new_types = tuple(self.visit_type(t) for t in e.types)
        return Expr(ty_app=Expr.TyApp(new_expr, new_types))

    def visit_expr_abs(self, e: Expr.Abs, /) -> Expr:
        new_body = self.visit_expr(e.body)
        return Expr(abs=Expr.Abs(param=e.param, body=new_body))

    def visit_expr_ty_abs(self, e: Expr.TyAbs, /) -> Expr:
        new_body = self.visit_expr(e.body)
        return Expr(ty_abs=Expr.TyAbs(param=e.param, body=new_body))

    def visit_expr_case(self, e: Case, /) -> Expr:
        new_scrut = self.visit_expr(e.scrut)
        # TODO: Real implementation
        new_alts = [alt for alt in e.alts]
        return Expr(case=Case(scrut=new_scrut, alts=new_alts))

    def visit_expr_let(self, e: Block, /) -> Expr:
        new_bindings = [
            Binding(
                VarWithType(binding.binder.var, self.visit_type(binding.binder.type)),
                self.visit_expr(binding.bound),
            )
            for binding in e.bindings
        ]
        new_body = self.visit_expr(e.body)
        return Expr(let=Block(bindings=new_bindings, body=new_body))

    def visit_expr_nil(self, e: Expr.Nil, /) -> Expr:
        return Expr(nil=Expr.Nil(self.visit_type(e.type)))

    def visit_expr_cons(self, e: Expr.Cons, /) -> Expr:
        new_type = self.visit_type(e.type)
        new_front = tuple(self.visit_expr(front) for front in e.front)
        new_tail = self.visit_expr(e.tail)
        return Expr(cons=Expr.Cons(type=new_type, front=new_front, tail=new_tail))

    def visit_expr_update(self, e: Update, /) -> Expr:
        return Expr(update=e)

    def visit_expr_scenario(self, e: Scenario, /) -> Expr:
        return Expr(scenario=e)

    def visit_expr_rec_upd(self, e: Expr.RecUpd, /) -> Expr:
        return Expr(rec_upd=e)

    def visit_expr_struct_upd(self, e: Expr.StructUpd, /) -> Expr:
        return Expr(struct_upd=e)

    def visit_expr_optional_none(self, e: Expr.OptionalNone, /) -> Expr:
        new_type = self.visit_type(e.type)
        return Expr(optional_none=Expr.OptionalNone(type=new_type))

    def visit_expr_optional_some(self, e: Expr.OptionalSome, /) -> Expr:
        new_type = self.visit_type(e.type)
        new_body = self.visit_expr(e.body)
        return Expr(optional_some=Expr.OptionalSome(type=new_type, body=new_body))

    def visit_expr_to_any(self, e: Expr.ToAny, /) -> Expr:
        return Expr(to_any=Expr.ToAny(type=self.visit_type(e.type), expr=self.visit_expr(e.expr)))

    def visit_expr_from_any(self, e: Expr.FromAny, /) -> Expr:
        return Expr(
            from_any=Expr.FromAny(type=self.visit_type(e.type), expr=self.visit_expr(e.expr))
        )
