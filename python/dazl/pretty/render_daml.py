# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from io import StringIO
from typing import Optional, Sequence, Union

from ._render_base import PrettyPrintBase
from .util import maybe_parentheses
from ..damlast.daml_lf_1 import DefDataType, DefTemplate, Expr, Module, PrimCon, PrimType, \
    Type as NewType
from ..model.types import Type as OldType, ScalarType, ContractIdType, ListType, OptionalType, \
    MapType, RecordType, TypeApp, TypeVariable, TypeReference, UpdateType, VariantType, \
    type_dispatch_table, SCALAR_TYPE_UNIT, SCALAR_TYPE_BOOL, SCALAR_TYPE_CHAR, \
    SCALAR_TYPE_INTEGER, SCALAR_TYPE_DECIMAL, SCALAR_TYPE_TEXT, SCALAR_TYPE_PARTY, \
    SCALAR_TYPE_RELTIME, SCALAR_TYPE_DATE, SCALAR_TYPE_TIME, ForAllType


_OldTypePrim = Union[ScalarType, ContractIdType, ListType, OptionalType, MapType, UpdateType,
                     NewType.Prim]


class DamlPrettyPrinter(PrettyPrintBase):

    syntax = 'daml'

    def lexer(self):
        try:
            from .pygments_daml_lexer import DAMLLexer
        except ImportError:
            return None

        return DAMLLexer()

    def visit_module_ref_start(self, module_ref: 'ModuleRef'):
        module_name = '.'.join(module_ref.module_name)
        return f'module {module_name} where\n'

    def visit_def_data_type(self, def_data_type: 'DefDataType') -> str:
        return self.visit_def_template(None, def_data_type)

    def visit_def_template(
            self, template: 'Optional[DefTemplate]', def_data_type: 'DefDataType') -> str:
        """
        Render a template (or a simple data type).

        :param template:
            The :class:`DefTemplate` to render. If not supplied, only the :class:`DefDataType` is
            rendered.
        :param def_data_type:
            The :class:`DefDataType` to render.
        :return:
            String rendering of the template and/or data type.
        """
        local_name = '.'.join(def_data_type.name.segments)

        from ..damlast.expand import ExpandVisitor, SimplifyVisitor
        ex = ExpandVisitor(self.store)
        sp = SimplifyVisitor(self.store)

        def render(expr: Expr) -> str:
            #return self.visit_expr(expr)
            e1 = ex.visit_expr(expr)
            e2 = sp.visit_expr(e1)
            return self.visit_expr(e2)

        with StringIO() as buf:
            if def_data_type.record is not None:
                type_args = ''.join(f' {p.var}' for p in def_data_type.params)
                if template is not None:
                    buf.write('template ' + local_name)
                else:
                    buf.write(f'data {local_name}{type_args} = {local_name}')
                buf.write('\n  with\n')
                for field in def_data_type.record.fields:
                    buf.write(f'    {field.field}: {self.visit_type(field.type)}\n')
                if template is not None:
                    buf.write('  where\n')
                    buf.write(f'    signatory {render(template.signatories)}\n')
                    buf.write(f'    observer {render(template.observers)}\n')
                    buf.write(f'    ensure {render(template.precond)}\n')
                    buf.write(f'    agreement {render(template.agreement)}\n')
                    # buf.write('    controller')
            elif def_data_type.variant is not None:
                buf.write('data ' + local_name + ' = ')

            if template is None:
                if def_data_type.serializable:
                    buf.write('\n  deriving (Eq, Show)')

            return buf.getvalue()

    # region visit_expr_* methods

    def visit_expr_prim_con_inline_unit(self):
        return '()'

    def visit_expr_rec_con_decl(self, rec_con: 'Expr.RecCon', context: 'CodeContext'):
        return self._visit_expr_decl(
            context, self.visit_expr_rec_con_inline(rec_con, line_endings=True))

    def visit_expr_rec_con_inline(self, rec_con: 'Expr.RecCon', line_endings: bool = False):
        ctor_expr = f'{self.visit_type_con(rec_con.tycon)} with'
        field_exprs = [f'{fwt.field}={self.visit_expr(fwt.expr)}' for fwt in rec_con.fields]
        if line_endings:
            return f'{ctor_expr} {"; ".join(field_exprs)}'
        else:
            return ctor_expr + '\n  '.join(field_exprs)

    def visit_expr_rec_proj(self, rec_proj: 'Expr.RecProj'):
        rec_text = maybe_parentheses(self.visit_expr(rec_proj.record))
        return f'{rec_text}.{rec_proj.field}'

    def visit_expr_variant_con(self, variant_con: 'Expr.VariantCon') -> str:
        arg_text = self.visit_expr(variant_con.variant_arg)
        return f'{variant_con.variant_con} {maybe_parentheses(arg_text)}'

    def visit_expr_tuple_proj(self, tuple_proj: 'Expr.TupleProj'):
        tuple_text = maybe_parentheses(self.visit_expr(tuple_proj.tuple))
        return f'{tuple_text}.{tuple_proj.field}'

    def visit_expr_app_inline(self, app: 'Expr.App'):
        components = [app.fun, *app.args]
        return ' '.join(maybe_parentheses(self.visit_expr(e)) for e in components)

    def visit_expr_abs_decl(self, abs_: 'Expr.Abs', context: 'CodeContext'):
        local_name = '.'.join(context.decl_name)
        field_def = f'{local_name} :: {self.visit_type(context.decl_type)}'
        all_params = [t.var for t in context.type_abs] if context.type_abs is not None else []
        all_params.extend(p.var for p in abs_.param)

        param_text = ''.join(' ' + p for p in all_params)
        body_text = self.visit_expr(abs_.body)
        field_decl = f'{local_name}{param_text} = {body_text}'
        return f'{field_def}\n{field_decl}'

    def visit_expr_abs_inline(self, abs_: 'Expr.Abs'):
        param_text = ' '.join(p.var for p in abs_.param)
        body_expr = self.visit_expr(abs_.body)
        return f'(\\{param_text} -> {body_expr})'

    def visit_expr_case(self, case: 'Case'):
        scrut_text = maybe_parentheses(self.visit_expr(case.scrut))
        patterns = ['  ' + self.visit_expr_casealt(alt) for alt in case.alts]
        lines = [f'case {scrut_text} of']
        lines.extend(patterns)
        return '\n'.join(lines)

    def visit_expr_let(self, let: 'Block') -> str:
        binding_lines = [f'{binding.binder.var} = {self.visit_expr(binding.bound)}'
                         for binding in let.bindings]
        with StringIO() as buf:
            buf.write('let ')
            delim = ''
            for line in binding_lines:
                buf.write(delim)
                buf.write(line)
                buf.write('\n')
                delim = '    '
            buf.write('in ')
            expr_text = self.visit_expr(let.body)
            buf.write(expr_text)
            return buf.getvalue()

    def visit_expr_nil_inline(self, nil: 'Expr.Nil') -> str:
        return 'nil'

    def visit_expr_cons(self, cons: 'Expr.Cons') -> str:
        front_texts = [self.visit_expr(front) for front in cons.front]
        if cons.tail.nil:
            return '[' + ', '.join(maybe_parentheses(t, ',') for t in front_texts) + ']'

        tail_text = self.visit_expr(cons.tail)
        if len(front_texts) > 1:
            return '[' + ', '.join(maybe_parentheses(t, ',') for t in front_texts) + '] ++ ' + \
                   maybe_parentheses(tail_text)
        else:
            return f'{front_texts[0]} `Cons` {tail_text}'

    def visit_expr_update(self, update: 'Update'):
        return 'do ... return'

    def visit_expr_scenario(self, scenario: 'Scenario'):
        return 'test ... return'

    def visit_expr_none(self, none: 'Expr.None_') -> str:
        return f'None'

    def visit_expr_some(self, some: 'Expr.Some') -> str:
        expr_text = self.visit_expr(some.body)
        return f'Some {maybe_parentheses(expr_text)}'

    # endregion

    # region visit_type_* methods

    def visit_type(self, type: 'Union[str, NewType, OldType]', parenthesize: bool = False) -> str:
        if isinstance(type, str):
            type_str = type
        elif isinstance(type, NewType):
            type_str = type.Sum_match(
                var=self.visit_type_var,
                con=self.visit_type_con,
                prim=self.visit_type_prim,
                forall=self.visit_type_forall,
                tuple=self.visit_type_tuple)
        elif isinstance(type, UpdateType):
            type_str = self.visit_type_prim(type)
        elif isinstance(type, ForAllType):
            type_str = self.visit_type_forall(type)
        elif isinstance(type, OldType):
            type_str = type_dispatch_table(
                on_type_var=self.visit_type_var,
                on_type_ref=self.visit_type_con,
                on_scalar=self.visit_type_prim,
                on_contract_id=self.visit_type_prim,
                on_list=self.visit_type_prim,
                on_optional=self.visit_type_prim,
                on_map=self.visit_type_prim,
                on_record=self.visit_type_con,
                on_variant=self.visit_type_con,
                on_type_app=self._visit_type_app,
                on_unsupported=repr)(type)
        else:
            raise TypeError(f'A DAML Type is required here (got {type!r} instead')

        return maybe_parentheses(type_str) if parenthesize else type_str

    def visit_type_var(self, var: 'Union[str, TypeVariable, NewType.Var]'):
        if isinstance(var, NewType.Var):
            return self._visit_type_app((var.var, *var.args))
        elif isinstance(var, TypeVariable):
            return var.name
        elif isinstance(var, str):
            return var
        else:
            raise TypeError(f'A DAML Type variable is required here (got {var!r} instead')

    def visit_type_con(self, con: 'Union[TypeReference, RecordType, VariantType, NewType.Con]') -> str:
        if isinstance(con, TypeReference):
            return con.full_name_unambiguous
        elif isinstance(con, (RecordType, VariantType)):
            if con.name is None:
                raise ValueError('A named Record or Variant type is required here')
            return con.name.full_name_unambiguous
        elif isinstance(con, NewType.Con):
            return self._visit_type_app((con.tycon.full_name_unambiguous, *con.args))
        else:
            raise TypeError(f'A DAML Type constructor is required here (got {con!r} instead')

    def visit_type_prim(self, prim: '_OldTypePrim') -> str:
        prim_type = prim.prim if isinstance(prim, NewType.Prim) else None

        if PrimType.UNIT == prim_type or SCALAR_TYPE_UNIT == prim:
            return 'Unit'
        elif PrimType.BOOL == prim_type or SCALAR_TYPE_BOOL == prim:
            return 'Bool'
        elif PrimType.INT64 == prim_type or SCALAR_TYPE_INTEGER == prim:
            return 'Int'
        elif PrimType.DECIMAL == prim_type or SCALAR_TYPE_DECIMAL == prim:
            return 'Decimal'
        elif PrimType.CHAR == prim_type or SCALAR_TYPE_CHAR == prim:
            return 'Char'
        elif PrimType.TEXT == prim_type or SCALAR_TYPE_TEXT == prim:
            return 'Text'
        elif PrimType.TIMESTAMP == prim_type or SCALAR_TYPE_TIME == prim:
            return 'Time'
        elif PrimType.RELTIME == prim_type or SCALAR_TYPE_RELTIME == prim:
            return 'RelTime'
        elif PrimType.PARTY == prim_type or SCALAR_TYPE_PARTY == prim:
            return 'Party'

        elif PrimType.LIST == prim_type:
            if len(prim.args) == 0:
                return 'List'
            else:
                return f'[{self.visit_type(prim.args[0])}]'
        elif isinstance(prim, ListType):
            return f'[{self.visit_type(prim.type_parameter)}]'

        elif PrimType.UPDATE == prim_type:
            return self._visit_type_app(('Update', *prim.args))
        elif isinstance(prim, UpdateType):
            return self._visit_type_app(('Update', prim.type_parameter))

        elif PrimType.SCENARIO == prim_type:
            return self._visit_type_app(('Scenario', *prim.args))

        elif PrimType.DATE == prim_type or SCALAR_TYPE_DATE == prim:
            return 'Date'

        elif PrimType.CONTRACT_ID == prim_type:
            return self._visit_type_app(('ContractId', *prim.args))
        elif isinstance(prim, ContractIdType):
            return self._visit_type_app(('ContractId', prim.type_parameter))

        elif PrimType.OPTIONAL == prim_type:
            return self._visit_type_app(('Optional', *prim.args))
        elif isinstance(prim, OptionalType):
            return self._visit_type_app(('Optional', prim.type_parameter))

        elif PrimType.ARROW == prim_type:
            arrow_operator = ' -> '
            return arrow_operator.join(
                maybe_parentheses(self.visit_type(a), arrow_operator) for a in prim.args)

        elif PrimType.MAP == prim_type:
            return self._visit_type_app(('Map', *prim.args))
        elif PrimType.MAP_GENERIC == prim_type:
            return self._visit_type_app(('Map', *prim.args))
        elif isinstance(prim, MapType):
            return self._visit_type_app(('Map', prim.key_type, prim.value_type))

        else:
            raise TypeError(f'A DAML Type primitive is required here (got {prim!r} instead')

    def visit_type_forall(self, forall: 'Union[ForAllType, NewType.Forall]') -> str:
        if isinstance(forall, NewType.Forall):
            return f'forall {" ".join(self.visit_type_var(v.var) for v in forall.vars)}. {self.visit_type(forall.body)}'
        elif isinstance(forall, ForAllType):
            return f'forall {" ".join(self.visit_type_var(v.var) for v in forall.type_vars)}. ' \
                f'{self.visit_type(forall.body_type)}'
        else:
            raise TypeError(f'A DAML forall Type is required here (got {forall!r} instead')

    # noinspection PyShadowingBuiltins
    def visit_type_tuple(self, tuple: 'NewType.Tuple') -> str:
        return '(' + ','.join(self.visit_type(t.type) for t in tuple.fields) + ')'

    def _visit_type_app(self, types: 'Union[TypeApp, Sequence[Union[str, NewType, OldType]]]'):
        if isinstance(types, TypeApp):
            types = (types.body, *types.arguments)

        return ' '.join(self.visit_type(c, True) for c in types)

    # endregion


DEFAULT_PRINTER = DamlPrettyPrinter()
