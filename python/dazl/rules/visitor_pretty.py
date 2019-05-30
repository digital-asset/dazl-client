# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains a utility visitor for pretty-printing an expression tree.
"""

from io import StringIO
from typing import TextIO, NamedTuple, Union, Iterable, Optional

from ._rewriter import RewriteContext
from .expr_base import Expr, TRIGGER_ON_INIT
from .expr_impl import SuiteExpr, ProgramExpr, TemplateSelectsExpr, TemplateSelectExpr, \
    GetContractIdExpr, GetContractDataExpr, ConstantExpr, \
    TemplateFieldExpr, UpdateBlockExpr, CreateStatementExpr, ExerciseStatementExpr, Application, \
    AppExpr

from ..util.tools import boundary_iter

_PP = RewriteContext()


def pretty_print(expr: Expr) -> str:
    """
    Return a pretty-printed representation of an :class:`Expr`, optionally ANSI color-coded.
    """
    with StringIO() as buf:
        _PP.rewrite(expr, context=_PrettyPrintContext(buf, 0))
        return buf.getvalue()


class _PrettyPrintContext(NamedTuple):
    buf: TextIO
    indent: int

    def write(self, value: Union[None, str, Expr], **kwargs) -> None:
        if isinstance(value, str):
            self.buf.write(value)
        elif isinstance(value, Expr):
            _PP.rewrite(value, context=self, **kwargs)
        elif value is not None:
            raise ValueError(f'Only strings and Expr instances can be pretty printed (got {value})')

    def write_line(self, value: Union[None, str, Expr] = None) -> None:
        self.write(value)
        self.buf.write('\n')

    def write_keyword(self, text: str) -> None:
        self.buf.write(self.fmt.keyword(text))

    def write_keyword_line(self, text: str) -> None:
        self.buf.write(self.fmt.keyword(text))
        self.buf.write('\n')


####################################################################################################
# WRITER METHODS

@_PP.register(Application, recurse=False)
def _write_application(expr: Application, context: _PrettyPrintContext):
    for suite in expr.suites:
        context.write_line(suite)


@_PP.register(SuiteExpr, recurse=False)
def _write_suite(expr: SuiteExpr, context: _PrettyPrintContext):
    context.write_line(context.fmt.comments(f'-- rules for party {expr.party} --'))
    for program in expr.programs:
        context.write_line(program)


@_PP.register(ProgramExpr, recurse=False)
def _write_rule(expr: ProgramExpr, context: _PrettyPrintContext):
    context.write_keyword('rule ')
    context.write_line(f'{expr.name}')
    context.write(expr.select)
    if expr.trigger == TRIGGER_ON_INIT:
        context.write_keyword_line('    initially')
    else:
        context.write_keyword_line('    continually')
    context.write_keyword_line('    do')
    context.write(expr.update)


@_PP.register(TemplateSelectsExpr, recurse=False)
def _write_selects(expr: TemplateSelectsExpr, context: _PrettyPrintContext):
    context.write_keyword_line('  with')
    for tmpl in expr.select:
        context.write('    ')
        context.write(tmpl, include_type_info=True)
        context.write_line()

    context.write_keyword_line('  where')

    if expr.predicate is not None:
        context.write_keyword('    predicate ')
        context.write_line(expr.predicate)


@_PP.register(TemplateSelectExpr, recurse=False)
def _write_select(expr: TemplateSelectExpr, context: _PrettyPrintContext,
                  include_type_info: bool=False):
    if expr.alias is not None:
        context.write(expr.alias)
    else:
        context.write('_<' + expr.template.template_ref.name + '>')

    if include_type_info:
        context.write(' : ')
        context.write(expr.template.template_ref.name)


@_PP.register(AppExpr, recurse=False)
def _write_app(expr: AppExpr, context: _PrettyPrintContext):
    if expr.func.infix:
        _write_infix_operator(expr.func.name, expr.args, context)
    else:
        context.write(expr.func.name)
        for arg in expr.args:
            context.write(' ')
            context.write(arg)


@_PP.register(GetContractIdExpr, recurse=False)
def _write_cid(expr: GetContractIdExpr, context: _PrettyPrintContext):
    context.write('(')
    context.write_keyword('cid ')
    context.write(expr.expression)
    context.write(')')


@_PP.register(GetContractDataExpr, recurse=False)
def _write_cdata(expr: GetContractDataExpr, context: _PrettyPrintContext):
    context.write('(')
    context.write_keyword('cdata ')
    context.write(expr.expression)
    context.write(')')


@_PP.register(ConstantExpr, recurse=False)
def _write_constant(expr: ConstantExpr, context: _PrettyPrintContext):
    context.write(repr(expr.value))


@_PP.register(TemplateFieldExpr, recurse=False)
def _write_field(expr: TemplateFieldExpr, context: _PrettyPrintContext):
    context.write(expr.expression)
    context.write('.')
    context.write(expr.field_name)


@_PP.register(UpdateBlockExpr, recurse=False)
def _write_update(expr: UpdateBlockExpr, context: _PrettyPrintContext):
    if expr.statements:
        for stmt in expr.statements:
            context.write('      ')
            context.write_line(stmt)
    else:
        context.write_line('()')


@_PP.register(CreateStatementExpr, recurse=False)
def _write_create(expr: CreateStatementExpr, context: _PrettyPrintContext):
    context.write_keyword('create ')
    context.write(expr.template.name)
    _write_arguments(expr.arguments, context)


@_PP.register(ExerciseStatementExpr, recurse=False)
def _write_exercise(expr: ExerciseStatementExpr, context: _PrettyPrintContext):
    context.write_keyword('exercise ')
    context.write(expr.expression)
    context.write(' ')
    context.write(expr.choice_name)
    _write_arguments(expr.arguments, context)


####################################################################################################
# HELPER METHODS

def _write_infix_operator(infix_op: str,
                          expressions: Iterable[Expr],
                          context: _PrettyPrintContext) -> None:
    for is_last, child in boundary_iter(expressions):
        context.write(child)
        if not is_last:
            context.write(f' {infix_op} ')


def _write_arguments(arguments: Optional[dict], context: _PrettyPrintContext) -> None:
    if not arguments:
        return

    context.write_keyword(' with ')
    context.write('{')

    for is_last, (name, value) in boundary_iter(arguments.items()):
        context.write(name)
        context.write('=')
        if isinstance(value, Expr):
            context.write(value)
        else:
            context.write(repr(value))

        if not is_last:
            context.write(', ')

    context.write('}')
