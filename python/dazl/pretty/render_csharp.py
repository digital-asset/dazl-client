# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Mapping, Optional, Sequence, Union

from dazl.model.definition import DamlTemplate
from ._render_base import PrettyPrintBase, decode_special_chars, CodeContext, register_pretty_printer
from ..damlast.daml_lf_1 import Module, Expr, Type, PrimType, DefDataType, PrimCon, PrimLit, \
    ValName, BuiltinFunction, Block, Case, Update, Scenario
from ..damlast.util import pack_arrow_type, unpack_arrow_type


class CSharpPrettyPrint(PrettyPrintBase):

    syntax = 'csharp'

    def lexer(self):
        try:
            from pygments.lexers.dotnet import CSharpLexer
        except ImportError:
            return None
        return CSharpLexer()

    def visit_module(self, module: 'Module') -> str:
        prefix = f'namespace {".".join(module.name.segments[:-1])} {{\n' + \
                 f'public static class {module.name.segments[-1]} {{\n'

        lines = []
        for value in module.values:
            proposed_name = '.'.join(value.name_with_type.name)
            final_name = decode_special_chars(proposed_name)
            if final_name != proposed_name:
                final_name = f'{proposed_name} ({final_name})'

            lines.append('/*')
            lines.append(' NAME: ' + final_name)
            lines.append(' TYPE: ' + repr(value.name_with_type.type))
            lines.append(' EXPR: ' + repr(value.expr))
            lines.append('*/')
            child = self.with_decl(value.name_with_type.name, value.name_with_type.type)
            expr_text = child.visit_expr(value.expr)
            if expr_text is None:
                type_text = self.visit_type(value.name_with_type.type)
                expr_text = f'// {value.expr!r}\npublic extern {type_text} {".".join(value.name_with_type.name)};'
            lines.extend(expr_text.splitlines())
            lines.append('')

        for data_type in module.data_types:
            def_data_text = self.visit_def_data_type(data_type)
            lines.extend(def_data_text.splitlines())
            lines.append('')

        return prefix + '\n'.join('    ' + line.replace('$', '_') if line else '' for line in lines) + '}}\n\n'

    def visit_def_data_type(self, def_data_type: 'DefDataType') -> 'str':
        lines = []
        type_params = [v.var for v in def_data_type.params]
        type_param_text = ('<' + ', '.join(type_params) + '>') if type_params else ''
        if def_data_type.serializable:
            lines.append('[Serializable]')
        if def_data_type.record is not None:
            fields = {f.field: self.visit_type(f.type) for f in def_data_type.record.fields}
            lines.append('public sealed class ' + '.'.join(def_data_type.name.segments) + type_param_text + ' {')
            for name, type_str in fields.items():
                lines.append(f'    public {type_str} {name} {{ get; }} = {name};')
            lines.append('}')
        elif def_data_type.variant is not None:
            fields = {f.field: self.visit_type(f.type) for f in def_data_type.variant.fields}
            lines.append('public sealed class ' + '.'.join(def_data_type.name.segments) + type_param_text + ' {')
            for name, type_str in fields.items():
                lines.append(f'    public {type_str} {name} {{ get; }} = {name};')
            lines.append('}')
        else:
            lines.append('public sealed class ' + '.'.join(def_data_type.name.segments) + '{}')
        return '\n'.join(lines) + '\n'

    def visit_daml_template(self, template: 'DamlTemplate'):

        pass

    def visit_expr_abs_decl_eq(self, expr: 'Expr.Abs'):
        return f"""
        /**
         * Originally defined at ...
         */
        public static boolean operator ==() {{
        }}"""


    def visit_expr_var(self, var: str) -> 'str':
        return self._render_rhs(var, None)

    def visit_expr_val(self, val: 'ValName') -> 'str':
        if self.context.decl_name is not None:
            lines = []
            if self.context.type_abs is not None:
                lines.append(f'// WARNING: Not sure how to render these: {self.context.type_abs}')
            lines.append(f'public static {self.visit_type(self.context.decl_type)} '
                         f'{".".join(self.context.decl_name)} = {val.full_name}')
            return '\n'.join(lines)
        else:
            return self._render_rhs(val.full_name, None)

    def visit_expr_builtin(self, builtin: 'BuiltinFunction') -> 'str':
        return self._render_rhs(f'BuiltIns.{builtin.name}', None)

    def visit_expr_prim_con(self, prim_con: 'PrimCon') -> 'str':
        if PrimCon.CON_TRUE == prim_con:
            text = 'true'
        elif PrimCon.CON_FALSE == prim_con:
            text = 'false'
        elif PrimCon.CON_UNIT == prim_con:
            text = 'Unit'
        else:
            text = repr(prim_con)
        return self._render_rhs(text, None)

    def visit_expr_prim_lit(self, prim_lit: 'PrimLit') -> 'str':
        if prim_lit.int64 is not None:
            text = str(prim_lit.int64)
        elif prim_lit.party is not None:
            text = f'Party("{prim_lit.party}")'
        elif prim_lit.text is not None:
            import json
            text = json.dumps(prim_lit.text)
        elif prim_lit.date is not None:
            from datetime import date, timedelta
            d = date(1970, 1, 1) + timedelta(days=prim_lit.date)
            text = f'Date({d.year}, {d.month}, {d.day})'
        elif prim_lit.timestamp is not None:
            text = f'ConstructDateTime({prim_lit.timestamp})'
        else:
            text = repr(prim_lit)

        return self._render_rhs(text, None)

    def _render_rhs(self, ctor: str, args: Optional[Sequence[str]]):
        if self.context.decl_name is not None:
            lines = []
            if self.context.type_abs is not None:
                lines.append(f'// WARNING: Not sure how to render these: {self.context.type_abs}')

            decl_line = f'public static {self.visit_type(self.context.decl_type)} ' \
                f'{".".join(self.context.decl_name)} = {ctor}'
            if args is not None:
                decl_line += '('
                delim = ''
                for arg in args:
                    decl_line += delim
                    delim = ','
                    decl_line += '\n    '
                    decl_line += arg
                decl_line += ')'
            decl_line += ';'
            return decl_line
        else:
            decl_line = ctor
            if args is not None:
                delim = '('
                for arg in args:
                    decl_line += delim
                    delim = ', '
                    decl_line += arg
                decl_line += ')'

        return decl_line if self.context.in_expression else f'return {decl_line};'

    def visit_expr_rec_con(self, rec_con: 'Expr.RecCon') -> 'str':
        scope = self.with_expression()
        args = [f'{field.field}: {scope.visit_expr(field.expr)}' for field in rec_con.fields]
        return self._render_rhs('new ' + self.visit_type_con(rec_con.tycon), args)

    def visit_expr_rec_proj(self, rec_proj: 'Expr.RecProj') -> 'str':
        scope = self.with_expression()
        return self._render_rhs(f'{scope.visit_expr(rec_proj.record)}.{rec_proj.field}', None)

    def visit_expr_variant_con(self, variant_con: 'Expr.VariantCon') -> 'str':
        scope = self.with_expression()
        args = [f'{variant_con.variant_con}: {scope.visit_expr(variant_con.variant_arg)}']
        return self._render_rhs(self.visit_type_con(variant_con.tycon), args)

    def visit_expr_tuple_con(self, tuple_con: 'Expr.TupleCon') -> 'str':
        scope = self.with_expression()
        args = [f'{field}: {scope.visit_expr(field.expr)}' for field in tuple_con.fields]
        return self._render_rhs('', args)

    def visit_expr_tuple_proj(self, tuple_proj: 'Expr.TupleProj') -> 'str':
        scope = self.with_expression()
        return self._render_rhs(f'{scope.visit_expr(tuple_proj.tuple)}.{tuple_proj.field}', None)

    def visit_expr_app(self, app: 'Expr.App') -> 'str':
        scope = self.with_expression()
        ctor_name = scope.visit_expr(app.fun)
        if self.context.decl_name is not None:
            lines = []
            if self.context.type_abs is not None:
                lines.append(f'// WARNING: Not sure how to render these: {self.context.type_abs}')

            if self.context.type_app:
                type_app_str = '<' + ', '.join(self.visit_type(t) for t in self.context.type_app) + '>'
            else:
                type_app_str = ''
            decl_line = f'public static {self.visit_type(self.context.decl_type)} ' \
                f'{".".join(self.context.decl_name)} = {ctor_name}{type_app_str}('
            delim = ''
            for arg in app.args:
                decl_line += delim
                delim = ','
                decl_line += '\n    '
                decl_line += scope.visit_expr(arg)
            decl_line += ');'

            return decl_line
        else:
            decl_line = ctor_name
            if ' ' in decl_line:
                decl_line = '(' + decl_line + ')'
            delim = '('
            for arg in app.args:
                decl_line += delim
                delim = ', '
                decl_line += scope.visit_expr(arg)
            decl_line += ')'

            return decl_line if self.context.in_expression else f'return {decl_line};'

    def visit_expr_abs_decl(self, abs_: 'Expr.Abs', context: 'CodeContext') -> 'str':
        fn_types = unpack_arrow_type(context.decl_type)

        if context.type_abs is not None:
            generic_args = '<' + (', '.join(self.visit_type_var(tvwk.var) for tvwk in context.type_abs)) + '>'
        else:
            generic_args = ''

        length_of_abstraction = len(abs_.param)
        length_of_proposed_signature = len(fn_types) - 1

        fn_args = {}  # type: Mapping[str, Type]
        ret_type = None  # type: Type
        if length_of_abstraction <= length_of_proposed_signature:
            # TODO: vwt.type and type should always agree with each other; might be nice if we validated that
            #  here instead of just assuming
            fn_args = {vwt.var: self.visit_type(type) for vwt, type in zip(abs_.param, fn_types)}
            ret_type = pack_arrow_type(fn_types[len(abs_.param):])
        elif length_of_abstraction > length_of_proposed_signature:
            # we're passing additional parameters to function returned from the original expression
            fn_args = {vwt.var: self.visit_type(type) for vwt, type in zip(abs_.param, fn_types)}
            return '???'

        fn_args_text = ', '.join(f'{arg_type_text} {arg_name}' for arg_name, arg_type_text in fn_args.items())

        child = self.with_statement_block()
        return_type_text = self.visit_type(ret_type)
        l1 = f'public static {return_type_text} {".".join(context.decl_name)}{generic_args}({fn_args_text}) {{'
        l2 = child.visit_expr(abs_.body) or '...'
        l3 = '}'
        return '\n'.join([l1, *('    ' + text for text in l2.splitlines()), l3])

    def visit_expr_abs_inline(self, abs_: 'Expr.Abs') -> 'str':
        type_params = []
        for param in abs_.param:
            type_expr = self.visit_type(param.type) + ' '
            if type_expr == 'var ':
                type_expr = ''
            type_params.append(type_expr + param.var)
        body_expr = self.visit_expr(abs_.body)
        expr_text = f'({", ".join(type_params)}) => {body_expr}'
        return expr_text if self.context.in_expression else f'return {expr_text};'

    def visit_expr_ty_abs(self, ty_abs: 'Expr.TyAbs') -> 'str':
        return self.with_type_abs(ty_abs.param).visit_expr(ty_abs.body)

    def visit_expr_case(self, case: 'Case') -> 'str':
        pass

    def visit_expr_let(self, let: 'Block') -> 'str':
        lines = []
        scope = self.with_expression()
        for binding in let.bindings:
            type_str = scope.visit_type(binding.binder.type)
            expr_str = scope.visit_expr(binding.bound)
            lines.append(f'{type_str} {binding.binder.var} = {expr_str};')
        lines.append('return ' + scope.visit_expr(let.body) + ';')
        return '\n'.join(lines)

    def visit_expr_nil(self, nil: 'Expr.Nil') -> 'str':
        return self._render_rhs(f'ImmutableList<{self.visit_type(nil.type)}>.Empty', None)

    def visit_expr_cons(self, cons: 'Expr.Cons') -> 'str':
        scope = self.with_expression()
        front_args = ', '.join(scope.visit_expr(f) for f in cons.front)
        tail_arg = scope.visit_expr(cons.tail)
        expr_text = f'ImmutableList.Create<{scope.visit_type(cons.type)}>({front_args}).AddRange({tail_arg})'
        return self._render_rhs(expr_text, None)

    def visit_expr_update(self, update: 'Update') -> 'str':
        pass

    def visit_expr_scenario(self, scenario: 'Scenario') -> 'str':
        pass

    def visit_expr_rec_upd(self, rec_upd: 'Expr.RecUpd') -> 'str':
        pass

    def visit_expr_tuple_upd(self, tuple_upd: 'Expr.TupleUpd') -> 'str':
        pass

    def visit_expr_optional_none(self, optional_none: 'Expr.OptionalNone') -> 'str':
        expr_text = f'ImmutableList<{self.visit_type(optional_none.type)}>.Empty'
        return expr_text if self.context.in_expression else f'return {expr_text};'

    def visit_expr_optional_some(self, optional_some: 'Expr.OptionalSome') -> 'str':
        return self.visit_expr(optional_some.body)

    def visit_type_var(self, var: 'Union[str, Type.Var]') -> 'str':
        rendered_var = super(CSharpPrettyPrint, self).visit_type_var(var)
        return rendered_var[0].upper() + rendered_var[1:]

    def visit_type_con(self, con: 'Type.Con') -> 'str':
        type_args = [self.visit_type(arg) for arg in con.args]
        if type_args:
            return f'{con.tycon.full_name}<{", ".join(type_args)}>'
        else:
            return con.tycon.full_name

    def visit_type_prim(self, prim: 'Type.Prim') -> 'str':
        if PrimType.UNIT == prim.prim:
            return 'Unit'
        elif PrimType.BOOL == prim.prim:
            return 'boolean'
        elif PrimType.INT64 == prim.prim:
            return 'int'
        elif PrimType.DECIMAL == prim.prim:
            return 'Decimal'
        elif PrimType.CHAR == prim.prim:
            return 'string'
        elif PrimType.TEXT == prim.prim:
            return 'string'
        elif PrimType.TIMESTAMP == prim.prim:
            return 'DateTime'
        elif PrimType.RELTIME == prim.prim:
            return 'timedelta'
        elif PrimType.PARTY == prim.prim:
            return 'Party'
        elif PrimType.LIST == prim.prim:
            if len(prim.args) == 0:
                return 'List<>'
            else:
                return f'List<{self.visit_type(prim.args[0])}>'
        elif PrimType.UPDATE == prim.prim:
            if len(prim.args) == 0:
                return 'Update<>'
            else:
                return f'Update<{self.visit_type(prim.args[0])}>'
        elif PrimType.SCENARIO == prim.prim:
            if len(prim.args) == 0:
                return 'Scenario'
            else:
                return f'Scenario<{self.visit_type(prim.args[0])}>'
        elif PrimType.DATE == prim.prim:
            return 'Date'
        elif PrimType.CONTRACT_ID == prim.prim:
            return f'ContractId<{self.visit_type(prim.args[0])}>'
        elif PrimType.OPTIONAL == prim.prim:
            if len(prim.args) == 0:
                return 'Optional<>'
            else:
                return f'Optional<{self.visit_type(prim.args[0])}>'
        elif PrimType.ARROW == prim.prim:
            type_strings = [self.visit_type(a) for a in prim.args]
            return f'Func<{", ".join(type_strings)}>'
        elif PrimType.MAP == prim.prim:
            return f'Dictionary<{self.visit_type(prim.args[0])},  {self.visit_type(prim.args[1])}>'
        else:
            raise ValueError(f'unknown Type.Prim: {prim!r}')

    def visit_type_forall(self, forall: 'Type.Forall') -> 'str':
        return self.visit_type(forall.body)

    def visit_type_tuple(self, tuple: 'Type.Tuple') -> 'str':
        args = ', '.join(f'{self.visit_type(fwt.type)} {fwt.field}' for fwt in tuple.fields)
        return f'({args})'

    def _visit_type_default(self):
        return 'var'
