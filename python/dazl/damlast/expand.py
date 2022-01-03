# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from types import MappingProxyType
from typing import Collection, Mapping, Optional

from .builtins import builtins
from .daml_lf_1 import Block, Expr, Type, ValName
from .protocols import SymbolLookup
from .util import package_local_name
from .visitor import IdentityVisitor


class RewriteVisitor(IdentityVisitor):
    def __init__(
        self,
        lookup: "SymbolLookup",
        always_expand: bool = False,
        val_blacklist: "Optional[Collection[ValName]]" = None,
        expr_args: "Optional[Mapping[str, Expr]]" = None,
        type_args: "Optional[Mapping[str, Type]]" = None,
    ):
        self.lookup = lookup
        self.always_expand = always_expand
        self.val_blacklist = frozenset(val_blacklist) if val_blacklist is not None else ()
        self.expr_args = MappingProxyType(expr_args or {})  # type: Mapping[str, Expr]
        self.type_args = MappingProxyType(type_args or {})  # type: Mapping[str, Type]

    def with_expr_var(self, var: str, value: "Expr") -> "RewriteVisitor":
        return type(self)(
            self.lookup,
            self.always_expand,
            self.val_blacklist,
            {**self.expr_args, var: value},
            self.type_args,
        )

    def with_expr_vars(self, var_values: "Mapping[str, Expr]") -> "RewriteVisitor":
        return type(self)(
            self.lookup,
            self.always_expand,
            self.val_blacklist,
            {**self.expr_args, **var_values},
            self.type_args,
        )

    def with_type_vars(self, type_values: "Mapping[str, Type]") -> "RewriteVisitor":
        return type(self)(
            self.lookup,
            self.always_expand,
            self.val_blacklist,
            self.expr_args,
            {**self.type_args, **type_values},
        )

    def without_val(self, val: "ValName") -> "RewriteVisitor":
        return type(self)(
            self.lookup,
            self.always_expand,
            {*self.val_blacklist, val},
            self.expr_args,
            self.type_args,
        )

    def resolve_val(self, val: "ValName") -> "Optional[Expr]":
        return self.lookup.value(val).expr if val not in self.val_blacklist else None

    def resolve_type_arg(self, type_arg: str) -> "Optional[Type]":
        return self.type_args.get(type_arg)

    def visit_expr_var(self, var: str) -> "Expr":
        expr = self.expr_args.get(var)
        return expr if expr is not None else Expr(var=var)

    def visit_type_var(self, var: "Type.Var") -> "Type":
        base_type = self.resolve_type_arg(var.var)
        if var.args:
            raise ValueError("higher kinded types are not yet currently supported")
        return base_type if base_type is not None else Type(var=var)


class ExpandVisitor(RewriteVisitor):
    def visit_expr_val(self, val: "ValName") -> "Expr":
        builtin = builtins.resolve(val)
        if builtin is not None:
            return Expr(val=val)
        if (
            self.always_expand
            or val._name[0][0] == "$"
            or package_local_name(val) == "DA.Internal.Template:toParties"
        ):
            val_expr = self.resolve_val(val)
            if val_expr is not None:
                child = self.without_val(val)
                return child.visit_expr(val_expr)
            else:
                print(
                    f"Failed to resolve {package_local_name(val)} against blacklist {self.val_blacklist}"
                )

        return super(ExpandVisitor, self).visit_expr_val(val)

    def visit_expr_ty_app(self, ty_app: "Expr.TyApp") -> "Expr":
        if ty_app.expr.ty_abs is not None:
            # perform type substitutions on the body, and remove the outer layers
            fn_vars = {
                p.var: self.visit_type(body)
                for p, body in zip(ty_app.expr.ty_abs.param, ty_app.types)
            }
            unapplied_args = ty_app.types[len(ty_app.expr.ty_abs.param) :]
            remaining_fn_args = ty_app.expr.ty_abs.param[len(ty_app.types) :]
            scope = self.with_type_vars(fn_vars)
            eval_body = scope.visit_expr(ty_app.expr.ty_abs.body)

            if unapplied_args:
                # the arguments are overapplied on the body of the function; substitute the passed
                # parameters in the body of the function, and the remaining parameters are applied
                # to the result of evaluation of the body
                return Expr(ty_app=Expr.TyApp(expr=eval_body, types=unapplied_args))
            elif remaining_fn_args:
                # the arguments are underapplied on the body of the function; substitute what we
                # can and return a partially-applied function
                return Expr(ty_abs=Expr.TyAbs(body=eval_body, param=remaining_fn_args))
            else:
                return eval_body
        elif ty_app.expr.builtin is not None:
            # this is a type abstraction over a built-in function; this TyApp serves more as
            # adornment over the bulit-in function tha anything else
            return Expr(ty_app=ty_app)
        else:
            return super(ExpandVisitor, self).visit_expr_ty_app(ty_app)

    #    ty_app.types[0]
    #     # some ty_apps get automatically expanded to compact representations that avoid a lot of the
    #     # declared machinery
    #     if ty_app.expr.val is not None and ty_app.expr.val.full_name_unambiguous == 'DA.Internal.Prelude:concat':
    #         # return a simple function call that takes two lists and concatenates them
    #         var_type = list_type(list_type(ty_app.types[0]))
    #         abs_param = (VarWithType('xxs', var_type),)  # type: Sequence[VarWithType]
    #         return Expr(abs=Expr.Abs(param=abs_param, body=Expr(builtin=BuiltinFunction.CONCAT_LIST)))
    #     else:
    #         return super(ExpandVisitor, self).visit_expr_ty_app(ty_app)
    #     # ty_app.types
    #     # ty_app.expr

    # def visit_expr_ty_abs(self, ty_abs: 'Expr.TyAbs') -> 'Expr':
    #     self.with_type_vars(ty_abs.param[0].var)
    #     ty_abs.param[0].var
    #     ty_abs.body
    #
    # def visit_expr_case(self, case: 'Case') -> 'Expr':
    #     case.scrut

    def visit_expr_let(self, let: "Block") -> "Expr":
        new_body = let.body
        for binding in reversed(let.bindings):
            scope = self.with_expr_var(binding.binder.var, binding.bound)
            new_body = scope.visit_expr(new_body)
        return new_body

    def visit_type_forall(self, forall: "Type.Forall") -> "Type":
        new_vars = [tvwk for tvwk in forall.vars if tvwk.var not in self.type_args]
        new_body = self.visit_type(forall.body)
        return Type(forall=Type.Forall(vars=new_vars, body=new_body))


class SimplifyVisitor(RewriteVisitor):
    def visit_expr_app(self, app: "Expr.App"):
        # first, if this is a built-in function, immediately apply its simplification logic on its
        # evaluated arguments
        if app.fun.ty_app is not None and app.fun.ty_app.expr.val is not None:
            from .builtins import builtins

            builtin = builtins.resolve(app.fun.ty_app.expr.val)
            if builtin is not None:
                type_args = app.fun.ty_app.types
                new_args = [self.visit_expr(arg) for arg in app.args]
                result = builtin.simplify(type_args, new_args)
                if result is not None:
                    return result

        # evaluate the function body (which we'll again re-evaluate with the arguments in a moment)
        new_fun = self.visit_expr(app.fun)

        if new_fun.abs is not None:
            #     builtin = builtins.resolve(new_fun.abs.body.ty_app.expr.val)
            #     if builtin is not None:
            #         type_args = new_fun.ty_app.types
            #         new_args = [self.visit_expr(arg) for arg in app.args]
            #         return builtin.simplify(type_args, new_args)

            # if new_fun.abs.val is not None and new_fun.abs.val in builtins:
            #     new_args = [self.visit_expr(arg) for arg in app.args]
            #     builtin = builtins.resolve(new_fun.abs.val)
            #     return builtin.simplify(None, new_args)

            if new_fun.abs.body.var is not None:
                # the body is a single variable; if it matches the name of the argument, then this
                # is the identity function and we simply return the argument
                if len(new_fun.abs.param) == 1 and len(app.args) == 1:
                    if new_fun.abs.param[0].var == new_fun.abs.body.var:
                        return self.visit_expr(app.args[0])

            if new_fun.abs.body.prim_lit is not None or new_fun.abs.body.prim_con is not None:
                # The body is actually NOT a function of its parameters, so we can skip evaluation of
                # the relevant parameters. This happens often enough in typical DAML models that it
                # is very much worth shortcutting this case
                if len(new_fun.abs.param) == 1 and len(app.args) == 1:
                    # just return the literal value and that's it
                    return new_fun.abs.body

            new_args = [self.visit_expr(arg) for arg in app.args]
            fn_vars = {p.var: self.visit_expr(body) for p, body in zip(new_fun.abs.param, new_args)}
            unapplied_args = new_args[len(new_fun.abs.param) :]
            remaining_fn_args = new_fun.abs.param[len(new_args) :]
            scope = self.with_expr_vars(fn_vars)
            eval_body = scope.visit_expr(new_fun.abs.body)

            if unapplied_args:
                # the arguments are overapplied on the body of the function; substitute the passed
                # parameters in the body of the function, and the remaining parameters are applied
                # to the result of evaluation of the body
                return self.visit_expr(Expr(app=Expr.App(fun=eval_body, args=unapplied_args)))
            elif remaining_fn_args:
                # the arguments are underapplied on the body of the function; substitute what we
                # can and return a partially-applied function
                return Expr(abs=Expr.Abs(body=eval_body, param=remaining_fn_args))
            else:
                return eval_body
        # elif app.fun.builtin is not None or (app.fun.ty_app is not None and app.fun.ty_app.expr.builtin is not None):
        #     builtin = app.fun.builtin or app.fun.ty_app.expr.builtin
        #     if builtin == BuiltinFunction.FOLDR:
        #         # foldr(func, acc, xs)
        #
        else:
            return super(SimplifyVisitor, self).visit_expr_app(app)

    def visit_expr_cons(self, cons: "Expr.Cons"):
        new_fronts = [self.visit_expr(front) for front in cons.front]
        new_tail = self.visit_expr(cons.tail)
        if new_tail.cons:
            new_fronts.extend(new_tail.cons.front)
            return Expr(
                cons=Expr.Cons(
                    type=cons.type,
                    front=tuple(new_fronts),
                    tail=Expr(nil=Expr.Nil(type=new_tail.cons.type)),
                )
            )
        else:
            return Expr(cons=Expr.Cons(type=cons.type, front=tuple(new_fronts), tail=new_tail))

    def visit_expr_rec_proj(self, rec_proj: "Expr.RecProj"):
        new_record = self.visit_expr(rec_proj.record)
        if new_record.rec_con is not None:
            for fwt in new_record.rec_con.fields:
                if fwt.field == rec_proj.field:
                    return self.visit_expr(fwt.expr)
            raise RuntimeError("rec_proj over a rec_con that did not have the necessary field")
        else:
            return Expr(
                rec_proj=Expr.RecProj(tycon=rec_proj.tycon, field=rec_proj.field, record=new_record)
            )

    def visit_expr_struct_proj(self, struct_proj: "Expr.StructProj"):
        new_tuple = self.visit_expr(struct_proj.struct)
        if new_tuple.struct_con is not None:
            for fwt in new_tuple.struct_con.fields:
                if fwt.field == struct_proj.field:
                    return self.visit_expr(fwt.expr)
            raise RuntimeError("rec_proj over a rec_con that did not have the necessary field")
        else:
            return Expr(struct_proj=Expr.StructProj(field=struct_proj.field, struct=new_tuple))
