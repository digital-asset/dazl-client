# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains a utility visitor for evaluating an expression tree.
"""

from typing import Any, Callable

from ._rewriter import RewriteContext
from .expr_impl import CreateStatementExpr, ExerciseStatementExpr, UpdateBlockExpr, \
    ConstantExpr, GetContractIdExpr, GetContractDataExpr, \
    TemplateSelectExpr, TemplateFieldExpr, AppExpr
from ..model.writing import CreateCommand, ExerciseCommand


def generate_lambda(expr):
    """
    Produces a function that takes a parameter and produces a result. The specific signature of the
    function varies on the specific kind of node passed in.
    """
    return lambda_generator.rewrite(expr)


# Visitor that produces callbacks based on the passed-in expression tree.
lambda_generator = RewriteContext()


@lambda_generator.register(ConstantExpr, recurse=False)
def constant(expr: ConstantExpr) -> Callable[[Any], Any]:
    """
    Produce a function that takes an arbitrary object and produces a constant value. The
    incoming parameter is ignored.
    """
    return lambda a: expr.value


@lambda_generator.register(AppExpr, recurse=False)
def _app(expr: AppExpr):
    arg_fns = tuple(lambda_generator.rewrite(arg) for arg in expr.args)
    return lambda a: expr.func.impl(*(arg_fn(a) for arg_fn in arg_fns))


@lambda_generator.register(GetContractIdExpr, recurse=False)
def get_cid(expr: GetContractIdExpr):
    fn = lambda_generator.rewrite(expr.expression)
    return lambda a: fn(a)[0]


@lambda_generator.register(GetContractDataExpr, recurse=False)
def get_cdata(expr: GetContractDataExpr):
    fn = lambda_generator.rewrite(expr.expression)
    return lambda a: fn(a)[1]


@lambda_generator.register(TemplateFieldExpr, recurse=False)
def field(expr: TemplateFieldExpr):
    """ Return a callback that extracts a field value. """
    from operator import getitem

    def _resolve_value(obj):
        try:
            return getitem(obj, expr.field_name)
        except (KeyError, TypeError):
            # TODO: This implementation needs to be fixed
            return None

    fn = lambda_generator.rewrite(expr.expression)
    get_field = _resolve_value
    return _compose(fn, get_field)


@lambda_generator.register(TemplateSelectExpr, recurse=False)
def select(expr: TemplateSelectExpr):
    """ Return a callback that extracts `ContractData` from the incoming parameter. """
    if expr.alias is None:
        raise ValueError('trying to create a lambda with an unnamed `let`')
    return lambda entry: entry[expr.alias]


@lambda_generator.register(CreateStatementExpr, recurse=False)
def create(expr: CreateStatementExpr):
    return lambda entry: CreateCommand(
        template=expr.template,
        arguments={k: lambda_generator.rewrite(v)(entry) for k, v in expr.arguments.items()})


@lambda_generator.register(ExerciseStatementExpr, recurse=False)
def exercise(expr: ExerciseStatementExpr):
    def _create_command(entry):
        template_id = None

        # TODO: This awkwardness can be removed as soon as ContractIds gain type parameters
        if isinstance(expr.expression, GetContractIdExpr):
            template_id = expr.expression.expression.template.template_ref

        return ExerciseCommand(
            contract=lambda_generator.rewrite(expr.expression)(entry),
            choice=expr.choice_name,
            arguments={k: lambda_generator.rewrite(v)(entry) for k, v in expr.arguments.items()},
        )#template_id=template_id)

    return _create_command


@lambda_generator.register(UpdateBlockExpr, recurse=False)
def update_block(expr: UpdateBlockExpr):
    statement_fns = tuple(lambda_generator.rewrite(stmt) for stmt in expr.statements)
    return lambda a: [stmt(a) for stmt in statement_fns]


def _compose(*functions):
    """
    Return a function that takes a single argument that is the result of feeding the result of
    one object into the next function.
    """
    def _impl(obj):
        for func in functions:
            obj = func(obj)
        return obj
    return _impl

