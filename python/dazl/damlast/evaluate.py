# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime, date, timedelta, timezone
from decimal import Decimal
from typing import Any, Mapping

from .. import LOG
from ..model.core import Party
from ..model.types_store import PackageStore
from ..util.prim_types import frozendict
from .daml_lf_1 import *


class Evaluator:

    def __init__(
            self,
            store: 'PackageStore',
            value_bindings: 'Mapping[str, Expr]',
            type_bindings: 'Mapping[str, Type]'):
        self.store = store
        self.value_bindings = frozendict(value_bindings)
        self.type_bindings = frozendict(type_bindings)

    def child_evaluator(
            self,
            value_bindings: 'Optional[Mapping[str, Expr]]' = None,
            type_bindings: 'Optional[Mapping[str, Type]]' = None) -> 'Evaluator':
        if value_bindings:
            new_value_bindings = dict()
            new_value_bindings.update(self.value_bindings)
            vars_to_delete = []
            for k, v in value_bindings.items():
                if not isinstance(k, str):
                    raise TypeError()
                if not isinstance(v, (Expr, Evaluator.Constant)):
                    raise TypeError('Only Expr and Evaluator.Constant are allowed here')
                if isinstance(v, Expr):
                    if v.var is not None and v.var == k:
                        vars_to_delete.append(v.var)
                if k in self.value_bindings:
                    LOG.warning('Variable %r is shadowing another variable with the same name in an outer scope! (original value: %r, new value: %r)', k, self.value_bindings[k], v)

            for k in vars_to_delete:
                del value_bindings[k]

            new_value_bindings.update(value_bindings)
        else:
            new_value_bindings = self.value_bindings

        if type_bindings:
            new_type_bindings = dict()
            new_type_bindings.update(self.type_bindings)
            new_type_bindings.update(type_bindings)
        else:
            new_type_bindings = self.type_bindings

        return Evaluator(self.store, new_value_bindings, new_type_bindings)

    class Constant:
        def __init__(self, value):
            if isinstance(value, Expr):
                raise TypeError('The Constant wrapper is only intended to be used with non-Expr')
            self.value = value

        def __repr__(self):
            return f'Constant({self.value!r})'

    def eval_Expr(self, expr: 'Expr') -> Any:
        if isinstance(expr, Evaluator.Constant):
            return expr.value
        result = expr.Sum_match(
            self.eval_var,
            self.eval_val,
            self.eval_builtin,
            self.eval_prim_con,
            self.eval_prim_lit,
            self.eval_rec_con,
            self.eval_rec_proj,
            self.eval_variant_con,
            self.eval_enum_con,
            self.eval_tuple_con,
            self.eval_tuple_proj,
            self.eval_app,
            self.eval_ty_app,
            self.eval_abs,
            self.eval_ty_abs,
            self.eval_case,
            self.eval_let,
            self.eval_nil,
            self.eval_cons,
            self.eval_update,
            self.eval_scenario,
            self.eval_rec_upd,
            self.eval_tuple_upd,
            self.eval_optional_none,
            self.eval_optional_some)
        if isinstance(result, Expr):
            LOG.warning('An Expr eval generated another Expr, which is probably incorrect.')
            LOG.warning('  Initial Expr: %r', expr)
            LOG.warning('  Result Expr: %r', result)
        return result

    def eval_var(self, var: str) -> Any:
        expr = self.value_bindings.get(var)
        if expr is None:
            LOG.warning('var %r could not be resolved to a value in the current scope!', var)
            return Expr(var=var)

        return self.eval_Expr(expr)

    def eval_val(self, val: 'ValName') -> 'Any':
        if val.full_name_unambiguous == 'DA.Internal.Prelude:concat':
            return PartialFunction(lambda a: PartialFunction(Evaluator.concat))
        value = self.store.resolve_value_reference(val)
        if value is None:
            LOG.warning('data type %s is undefined!', val)
            return Expr(val=val)

        return self.eval_Expr(value)

    @staticmethod
    def concat(xxs):
        result = []
        for xs in xxs:
            result.extend(xs)
        return result

    @staticmethod
    def eval_builtin(builtin: 'BuiltinFunction') -> 'Any':
        return BUILTINS.definition(builtin)

    @staticmethod
    def eval_prim_con(prim_con: 'PrimCon') -> 'Any':
        if PrimCon.CON_TRUE == prim_con:
            return True
        elif PrimCon.CON_FALSE == prim_con:
            return False
        elif PrimCon.CON_UNIT == prim_con:
            return {}
        else:
            raise ValueError(f'unknown PrimCon value: {prim_con}')

    @staticmethod
    def eval_prim_lit(prim_lit: 'PrimLit') -> 'Any':
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

    def eval_rec_con(self, rec_con: 'Expr.RecCon') -> 'Any':
        return frozendict({fwt.field: self.eval_Expr(fwt.expr) for fwt in rec_con.fields})

    def eval_rec_proj(self, rec_proj: 'Expr.RecProj') -> 'Any':
        record_expr = self.eval_Expr(rec_proj.record)
        return record_expr[rec_proj.field]

    def eval_variant_con(self, variant_con: 'Expr.VariantCon') -> 'Any':
        ctor = variant_con.variant_con
        value = self.eval_Expr(variant_con.variant_arg)
        return frozendict({ctor: value})

    def eval_enum_con(self, enum_con: 'Expr.EnumCon') -> 'Any':
        return enum_con.enum_con

    def eval_tuple_con(self, struct_con: 'Expr.StructCon') -> 'Any':
        return frozendict({fwt.field: self.eval_Expr(fwt.expr) for fwt in struct_con.fields})

    def eval_tuple_proj(self, struct_proj: 'Expr.StructProj') -> 'Any':
        tuple_expr = self.eval_Expr(struct_proj.tuple)
        return tuple_expr[struct_proj.field]

    def eval_app(self, app: 'Expr.App') -> 'Any':
        fun = self.eval_Expr(app.fun)
        if hasattr(fun, 'kind') and fun.kind != 'abs':
            raise ValueError('oh what the hell')

        args = [self.eval_Expr(arg) for arg in app.args]
        return fun.apply(*args)

    def eval_ty_app(self, ty_app: 'Expr.TyApp') -> 'Any':
        fun = self.eval_Expr(ty_app.expr)
        if hasattr(fun, 'kind') and fun.kind != 'ty_abs':
            raise ValueError('oh what the hell')
        # TODO: No actual Type visiting happens here; is this necessary for us?
        args = [arg for arg in ty_app.types]
        return fun.apply(*args)

    def eval_abs(self, abs_: 'Expr.Abs') -> 'Any':
        func_parameters = [p.var for p in abs_.param]

        pf = PartialFunction(
            PartialFunctionBody(self, func_parameters, abs_.body),
            arg_count=len(func_parameters))
        pf.kind = 'abs'
        return pf

    def eval_ty_abs(self, ty_abs: 'Expr.TyAbs') -> 'Any':
        ty_func_parameters = [t.var for t in ty_abs.param]

        # the body will return a Callable, but only when all variables are bound.
        # Delay evaluation of the expression until all variables' values are gathered
        def implementation(*args):
            evaluator = self.child_evaluator(type_bindings=dict(
                zip(ty_func_parameters, args)))
            return evaluator.eval_Expr(ty_abs.body)

        pf = PartialFunction(implementation, arg_count=len(ty_func_parameters))
        pf.kind = 'ty_abs'
        return pf

    def eval_case(self, case: 'Case') -> 'Any':
        scrut = self.eval_Expr(case.scrut)
        raise ValueError('not handling case yet')

    def eval_let(self, let: 'Block') -> 'Any':
        current_scope = self
        for binding in let.bindings:
            var = binding.binder.var
            value = current_scope.eval_Expr(binding.bound)
            current_scope = current_scope.child_evaluator(value_bindings={var: Evaluator.Constant(value)})
        return current_scope.eval_Expr(let.body)

    @staticmethod
    def eval_nil(nil: 'Expr.Nil') -> 'Any':
        return ()

    def eval_cons(self, cons: 'Expr.Cons') -> 'Any':
        result = []
        for f in cons.front:
            resolved_val = self.eval_Expr(f)
            try:
                result.append(resolved_val)
            except:
                LOG.exception()
                raise
        result.extend(self.eval_Expr(cons.tail))
        return tuple(result)

    def eval_update(self, update: 'Update') -> 'Any':
        raise ValueError('not handling updates yet')

    def eval_scenario(self, scenario: 'Scenario') -> 'Any':
        raise ValueError('not handling scenarios yet')

    def eval_rec_upd(self, rec_upd: 'Expr.RecUpd') -> 'Any':
        raise ValueError('not handling updates yet')

    def eval_tuple_upd(self, struct_upd: 'Expr.StructUpd') -> 'Any':
        raise ValueError('not handling updates yet')

    @staticmethod
    def eval_optional_none(optional_none: 'Expr.OptionalNone') -> 'Any':
        return None

    def eval_optional_some(self, optional_some: 'Expr.OptionalSome') -> 'Any':
        return self.eval_Expr(optional_some.body)


class BuiltinImpl:
    def __init__(self):
        self._functions = {
            BuiltinFunction.APPEND_TEXT: PartialFunction(self.append_text),
            BuiltinFunction.TO_TEXT_INT64: PartialFunction(self.to_text_int64),
            BuiltinFunction.TO_TEXT_PARTY: PartialFunction(self.to_text_party),
            BuiltinFunction.FOLDL: PartialFunction(self.foldl),
            BuiltinFunction.FOLDR: PartialFunction(self.foldr),
        }

    def definition(self, builtin: 'BuiltinFunction') -> 'Callable[[...], Any]':
        return self._functions[builtin]

    def append_text(self, xs, ys) -> str:
        return xs + ys

    def to_text_int64(self, int64) -> str:
        return str(int64)

    def to_text_party(self, party) -> str:
        return party

    def foldl(self, func, acc, xs):
        from functools import reduce
        return reduce(func, acc, xs)

    def foldr(self, func, acc, xs):
        from functools import reduce
        return reduce(lambda x, y: func(y, x), xs[::-1], acc)


class PartialFunction:
    """
    Wrapper around a function that accumulates arguments and invokes the underlying function only
    once all arguments have been collected.
    """
    def __init__(self, fn, *args, arg_count: 'Optional[int]' = None):
        from inspect import signature, Parameter

        if arg_count is None:
            allowed_param_kinds = (Parameter.POSITIONAL_ONLY, Parameter.POSITIONAL_OR_KEYWORD)
            # try to compute argument count from the function
            parameters = signature(fn).parameters.values()
            if not all(p.kind in allowed_param_kinds for p in parameters):
                raise ValueError(f'the function {fn!r} cannot be used in a PartialFunction because '
                                 f'it takes an unknown number of parameters; specify arg_count '
                                 f'explicitly if you wish to use the function')
            arg_count = len(parameters)

        if arg_count == 0:
            raise ValueError('Non-zero number of arguments required for a PartialFunction')
        if len(args) >= arg_count:
            raise ValueError('YOU GOT MORE WORK TO DO BUDDY')

        self.fn = fn
        self.args = args
        self.arg_count = arg_count

    def apply(self, *args):
        """
        Apply the specified number of arguments to this function, possibly invoking the underlying
        function and returning its result.

        :param args:
            The arguments to apply to this function.
        :return:
            Either a new :class:`PartialFunction` instance with some values applied, or the result
            of invoking the underlying function with the accumulated values.
        """
        total_args = self.args + args
        total_arg_count = len(total_args)
        if total_arg_count < self.arg_count:
            pf = PartialFunction(self.fn, total_args, arg_count=self.arg_count)
            if hasattr(self, 'kind'):
                pf.kind = self.kind
            return pf
        elif total_arg_count == self.arg_count:
            return self.fn(*total_args)
        else:
            # fully apply this function; THEN expect the function to return a function, and apply
            # remaining arguments to THAT
            remaining_args = total_arg_count - self.arg_count

            result = self.fn(*total_args[:-remaining_args])
            return result(*total_args[remaining_args:])

    def __call__(self, *args):
        return self.apply(*args)

    def __repr__(self):
        return f'PartialFunction({self.fn!r}, args={self.args}, arg_count={self.arg_count})'


class PartialFunctionBody:
    def __init__(self, scope: Evaluator, func_parameters: Sequence[str], func_body_expr: 'Expr'):
        self.scope = scope
        self.func_parameters = tuple(func_parameters)
        self.func_body_expr = func_body_expr

    def __call__(self, *args):
        new_value_bindings = dict(zip(self.func_parameters, [Evaluator.Constant(arg) for arg in args]))
        evaluator = self.scope.child_evaluator(value_bindings=new_value_bindings)
        return evaluator.eval_Expr(self.func_body_expr)

    def __repr__(self):
        return f'PartialFunctionBody(func_parameters={self.func_parameters}, func_body={self.func_body_expr})'


BUILTINS = BuiltinImpl()
