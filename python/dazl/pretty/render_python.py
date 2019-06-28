# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from io import StringIO
from typing import Mapping, Optional, Sequence, Union

from ._render_base import PrettyPrintBase, pretty_print_syntax
from .util import maybe_parentheses, indent
from .. import LOG
from ..damlast.daml_lf_1 import DefDataType, DefTemplate, Expr, Type, Case, Block, \
    Update, Scenario, PrimType
from ..damlast.util import def_value, list_type, PARTY_TYPE
from ..model.types import ModuleRef, Type as OldType, TypeReference
from ..model.types_store import PackageStore


def values_by_module(store: 'PackageStore') \
        -> 'Mapping[ModuleRef, Mapping[Sequence[str], Union[Expr, OldType]]]':
    from collections import defaultdict
    d = defaultdict(defaultdict)
    for vn, vv in store._value_types.items():
        d[vn.module][vn.name] = vv
    for vn, vv in store._data_types.items():
        d[vn.module][vn.name] = vv
    return d


@pretty_print_syntax('python')
class PythonPrettyPrint(PrettyPrintBase):
    """
    Renderer for :class:`Expr` and :class:`Type` hierarchies that output text that look like
    Python code.
    """

    syntax = 'python'

    def lexer(self):
        try:
            from pygments.lexers.python import PythonLexer
        except ImportError:
            return None
        return PythonLexer()

    def visit_module_ref_start(self, module_ref: 'ModuleRef') -> str:
        return f'@module\nclass {module_ref.module_name[-1]}:\n' if module_ref.module_name else ''

    # def visit_def_value(self, def_value: 'DefValue', as_instance_method: bool = False):
    #     def_value.name_with_type

    def visit_empty_block_body(self):
        return 'pass'

    def visit_def_template(
            self,
            template: 'Optional[DefTemplate]',
            def_data_type: 'Optional[DefDataType]' = None) -> str:
        template_full_name = TypeReference(self.context.current_module, def_data_type.name.segments).full_name
        template_name = def_data_type.name.segments[-1]
        slot_names = tuple(fwt.field for fwt in def_data_type.record.fields) if def_data_type.record else ()
        signatories_def = def_value('signatories', list_type(PARTY_TYPE), template.signatories) if template is not None else None

        if template is not None:
            lines = []
            lines.append(f'class {template_name}(metaclass=TemplateMeta, template_name={template_full_name!r}):')
            lines.append('    """')
            lines.append('    Example usage:')
            lines.append(f'        create({template_full_name},')
            lines.append(f'               {python_example_object(self.store, def_data_type)})')
            for choice in template.choices:
                lines.append(f'        exercise(cid, {choice.name!r}, {python_example_object(self.store, choice.arg_binder.type)})')
            lines.append('    """')
            lines.append(indent(self._visit_def_type_body(slot_names), 4))
            for choice in template.choices:
                ct = choice.arg_binder.type
                if ct.prim is not None and ct.prim.prim == PrimType.UNIT:
                    choice_slot_names = ()
                else:
                    tt = self.store.resolve_type_reference(ct.con.tycon)
                    choice_slot_names = tuple(name for name, _ in tt.named_args) if tt is not None else ()
                lines.append(f'    class {choice.name}(metaclass=ChoiceMeta, template_name={template_full_name!r}, choice_name={choice.name!r}):')
                lines.append(indent(self._visit_def_type_body(choice_slot_names), 8))
            return '\n'.join(lines)
        else:
            return ''

    def _visit_def_type_body(self, slot_names: 'Sequence[str]') -> str:
        lines = [f'__slots__ = {slot_names!r}\n']
        if slot_names:
            lines.append(f'def __init__(self, {", ".join(slot_names)}):')
            lines.extend(f'    self.{slot_name} = {slot_name}' for slot_name in slot_names)
            lines.append('')
            lines.append(f'def _asdict(self) -> dict:')
            lines.append(f'    return {{')
            lines.extend(f'        {slot_name!r}: self.{slot_name},' for slot_name in slot_names)
            lines.append(f'        }}')
        else:
            lines.append('def _asdict(self) -> dict:')
            lines.append('    return {}')
        return '\n'.join(lines) + '\n'

    def visit_expr_prim_con_inline_unit(self):
        return '{}'

    def visit_expr_rec_con_inline(self, rec_con: 'Expr.RecCon'):
        with StringIO() as buf:
            buf.write('record(')
            delim = ''
            for fwe in rec_con.fields:
                buf.write(delim)
                buf.write(fwe.field)
                buf.write('=')
                expr = self.visit_expr(fwe.expr)
                if ' ' in expr:
                    buf.write('(')
                buf.write(expr)
                if ' ' in expr:
                    buf.write(')')
                delim = ', '
            buf.write(')')

            # if self.decl_name is not None:
            #     buf.write('  # type: ')
            #     buf.write(self.visit_type_con(rec_con.tycon))
            return buf.getvalue()

    def visit_expr_rec_proj(self, rec_proj: 'Expr.RecProj') -> str:
        record_text = self.visit_expr(rec_proj.record)
        if ' ' in record_text:
            return f'({record_text})[{rec_proj.field!r}]'
        else:
            return f'{record_text}[{rec_proj.field!r}]'

    def visit_expr_variant_con(self, variant_con: 'Expr.VariantCon') -> str:
        with StringIO() as buf:
            try:
                scope = self
                if self.context.decl_name is not None:
                    buf.write('.'.join(self.context.decl_name))
                    buf.write(' = ')
                else:
                    buf.write('return ')
                buf.write('variant(')
                buf.write(variant_con.variant_con)
                buf.write('=')
                expr = scope.visit_expr(variant_con.variant_arg)
                if ' ' in expr:
                    buf.write('(')
                buf.write(expr)
                if ' ' in expr:
                    buf.write(')')
                buf.write(')')

                if self.context.decl_name is not None:
                    buf.write('  # type: ')
                    buf.write(self.visit_type_con(variant_con.tycon))
                return buf.getvalue()
            except:
                LOG.exception('why why why')
                exit(-1)

    def visit_expr_tuple_con(self, tuple_con: 'Expr.TupleCon') -> str:
        if tuple_con.fields:
            with StringIO() as buf:
                delim = 'tuple('
                for fwe in tuple_con.fields:
                    buf.write(delim)
                    buf.write(fwe.field)
                    buf.write('=')
                    expr = self.visit_expr(fwe.expr)
                    if ' ' in expr:
                        buf.write('(')
                    buf.write(expr)
                    if ' ' in expr:
                        buf.write(')')
                    delim = ', '
                buf.write(')')
                return buf.getvalue()
        else:
            return 'tuple()'

    def visit_expr_tuple_proj(self, tuple_proj: 'Expr.TupleProj') -> str:
        record_text = self.visit_expr(tuple_proj.tuple)
        if ' ' in record_text:
            return f'({record_text})[{tuple_proj.field!r}]'
        else:
            return f'{record_text}[{tuple_proj.field!r}]'

    def visit_expr_app_inline(self, app: 'Expr.App'):
        fun_text = maybe_parentheses(self.visit_expr(app.fun))
        args_text = ', '.join(self.visit_expr(arg) for arg in app.args)
        return f'{fun_text}({args_text})'

    def visit_expr_ty_app(self, ty_app: 'Expr.TyApp') -> str:
        fun_text = self.visit_expr(ty_app.expr)
        return fun_text
        args_text = ', '.join(self.visit_type(arg) for arg in ty_app.types)
        return f'ty_apply({fun_text})<{args_text}>'

    def visit_expr_abs_decl(self, abs_: 'Expr.Abs', context: 'CodeContext'):
        body = self.visit_expr(abs_.body)
        try:
            body_type = self.type_computer.visit_expr(abs_.body)
            body_type_expr = ' -> \'' + self.visit_type(body_type) + '\''
        except:
            # LOG.exception("Couldn't compute a type!")
            body_type_expr = ''
        safe_decl_name = '.'.join(context.decl_name).replace('$', '_')
        args = ', '.join(f'{p.var}: \'{self.visit_type(p.type)}\'' for p in abs_.param)
        decl_line = f'@staticmethod\ndef {safe_decl_name}({args}){body_type_expr}:\n'
        return decl_line + ''.join(('    ' + line) for line in body.splitlines(keepends=True))

    def visit_expr_abs_inline(self, abs_: 'Expr.Abs'):
        body = self.visit_expr(abs_.body)
        args = ', '.join(f'{p.var}' for p in abs_.param)
        if args:
            args = ' ' + args
        return f'lambda{args}: {body}'

    def visit_expr_ty_abs(self, ty_abs: 'Expr.TyAbs') -> str:
        args = ', '.join(p.var for p in ty_abs.param)
        if args:
            args = ' ' + args
        body = self.visit_expr(ty_abs.body)
        return body

        return f'ty_lambda{args}: {body}'

    def visit_expr_case(self, case: 'Case') -> str:
        scrut = self.visit_expr(case.scrut)
        line = f'    scrut = {scrut}\n'
        # for alt in case.alts:
        #     alt.Sum_match()
        #     alt.body
        line += '    ...'
        return line

    def visit_expr_let(self, let: 'Block') -> str:
        if self.context.in_expression:
            assignments = ', '.join(f'{b.binder.var} := {self.visit_expr(b.bound)}' for b in let.bindings)
            return f'({assignments}, {self.visit_expr(let.body)})[-1]'
        else:
            with StringIO() as buf:
                for b in let.bindings:
                    buf.write(f'{b.binder.var} = {self.visit_expr(b.bound)}\n')
                buf.write(f'return {self.visit_expr(let.body)}')
                return buf.getvalue()

    def visit_expr_nil_inline(self, nil: 'Expr.Nil') -> str:
        return '()'

    def visit_expr_cons(self, cons: 'Expr.Cons') -> str:
        with StringIO() as buf:
            delim = ''
            buf.write('[')
            for f in cons.front:
                buf.write(delim)
                expr = self.visit_expr(f)
                if ' ' in expr:
                    buf.write('(')
                buf.write(expr)
                if ' ' in expr:
                    buf.write(')')
                delim = ', '

            buf.write(delim)
            expr = self.visit_expr(cons.tail)
            buf.write('*')
            if ' ' in expr:
                buf.write('(')
            buf.write(expr)
            if ' ' in expr:
                buf.write(')')
            buf.write(']')
            return buf.getvalue()

    def visit_expr_update(self, update: 'Update') -> str:
        raise Exception

    def visit_expr_scenario(self, scenario: 'Scenario') -> str:
        raise Exception

    def visit_expr_rec_upd(self, rec_upd: 'Expr.RecUpd') -> str:
        raise Exception

    def visit_expr_tuple_upd(self, tuple_upd: 'Expr.TupleUpd') -> str:
        raise Exception

    def visit_expr_optional_none(self, optional_none: 'Expr.OptionalNone') -> str:
        expr = 'None'
        if self.context.in_expression:
            return expr
        else:
            try:
                type_str = self.visit_type(optional_none.type)
                type_str = f'  # type: Optional[{type_str}]'
            except:
                type_str = None

            return f'return {expr}{type_str}'

    def visit_expr_optional_some(self, optional_some: 'Expr.OptionalSome') -> str:
        expr = self.visit_expr(optional_some.body)
        if self.in_lambda_body:
            return expr
        else:
            try:
                type_str = self.visit_type(optional_some.type)
                type_str = f'  # type: Optional[{type_str}]'
            except:
                type_str = None

            return f'return {expr}{type_str}'

    def visit_type_var(self, var: 'Type.Var') -> str:
        return var.var

    def visit_type_con(self, con: 'Type.Con') -> str:
        if con.args:
            return f'{con.tycon.full_name}[{", ".join([self.visit_type(a) for a in con.args])}]'
        else:
            return con.tycon.full_name

    def visit_type_prim(self, prim: 'Type.Prim') -> str:
        if PrimType.UNIT == prim.prim:
            return 'Unit'
        elif PrimType.BOOL == prim.prim:
            return 'bool'
        elif PrimType.INT64 == prim.prim:
            return 'int'
        elif PrimType.DECIMAL == prim.prim:
            return 'Decimal'
        elif PrimType.CHAR == prim.prim:
            return 'str'
        elif PrimType.TEXT == prim.prim:
            return 'str'
        elif PrimType.TIMESTAMP == prim.prim:
            return 'datetime'
        elif PrimType.RELTIME == prim.prim:
            return 'timedelta'
        elif PrimType.PARTY == prim.prim:
            return 'Party'
        elif PrimType.LIST == prim.prim:
            if len(prim.args) == 0:
                return 'List'
            else:
                return f'List[{prim.args[0]}]'
        elif PrimType.UPDATE == prim.prim:
            if len(prim.args) == 0:
                return 'Update'
            else:
                return f'Update[{self.visit_type(prim.args[0])}]'
        elif PrimType.SCENARIO == prim.prim:
            if len(prim.args) == 0:
                return 'Scenario'
            else:
                return f'Scenario[{self.visit_type(prim.args[0])}]'
        elif PrimType.DATE == prim.prim:
            return 'Date'
        elif PrimType.CONTRACT_ID == prim.prim:
            return f'ContractId[{self.visit_type(prim.args[0])}]'
        elif PrimType.OPTIONAL == prim.prim:
            if len(prim.args) == 0:
                return 'Optional'
            else:
                return f'Optional[{self.visit_type(prim.args[0])}]'
        elif PrimType.ARROW == prim.prim:
            type_strings = [self.visit_type(a) for a in prim.args]
            return f'Callable[[{", ".join(type_strings[:-1])}], {type_strings[-1]}]'
        elif PrimType.MAP == prim.prim:
            return f'Map[{self.visit_type(prim.args[0])},  {self.visit_type(prim.args[1])}]'
        else:
            raise ValueError(f'unknown Type.Prim: {prim!r}')

    def visit_type_forall(self, forall: 'Type.Forall') -> str:
        # Python does not have a way of modelling existential quantification, so simply throw this
        # information away
        return self.visit_type(forall.body)

    def visit_type_tuple(self, tuple: 'Type.Tuple') -> str:
        return '?'


def python_example_object(*_, **__):
    return '...'
