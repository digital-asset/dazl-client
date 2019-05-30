# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains the definitions and implementations for expression types supported by the
query API.
"""

from typing import List, Optional, Set, Collection, Any

from .expr_base import Expr, exprify_args, exprify_value, TRIGGER_ANY_TIME, TRIGGER_ON_INIT
from ..model.types import Type, UnresolvedTypeReference


class UpdateStatementExpr(Expr):
    """ A statement in an update block. """

    def __getattr__(self, choice_name):
        """
        Generate a callable for the specified choice name. When the callable is invoked with
        arguments, an `ExerciseStatementExpr` is created that captures those args.
        """
        return _ExerciseStatementExprFactory(self, choice_name)

    @classmethod
    def coerce(cls, obj):
        if isinstance(obj, UpdateStatementExpr):
            return obj
        raise TypeError("Couldn't convert to a UpdateStatementExpr: {!r}".format(obj))


class TemplateExpr(Expr):
    """
    An :class:`Expr` wrapper around a :class:`TemplateRef`.

    In the context of an update block, this is coerced to a `create` statement.
    In the context of a `from` expression, this is coerced to a `TemplateSelectExpr` with a default
    label.
    """
    template_ref: Type

    def __init__(self, template_ref=None):
        self.template_ref = template_ref if isinstance(template_ref, Type) \
            else UnresolvedTypeReference(template_ref)

    @classmethod
    def coerce(cls, obj) -> 'TemplateExpr':
        """
        Attempt to coerce the specified type to a `TemplateExpr`.
        """
        if isinstance(obj, TemplateExpr):
            return obj
        if isinstance(obj, (Type, str)):
            return TemplateExpr(template_ref=obj)
        raise TypeError(f"Couldn't convert to a TemplateExpr: {obj!r}")

    def __getitem__(self, field_name: str) -> 'TemplateFieldExpr':
        """
        Return an expression that represents a field access of this template.
        """
        return TemplateFieldExpr(
            self, self._validate_field_name(field_name))

    def __getattr__(self, choice_name) -> '_TemplateChoiceFactory':
        return _TemplateChoiceFactory(self.template_ref, choice_name)

    def __call__(self, **kwargs):
        return CreateStatementExpr(template=self.template_ref, arguments=exprify_args(kwargs))

    def __repr__(self):
        return '<TemplateExpr({!r})>'.format(self.template_ref)

    def _validate_field_name(self, field_name):
        """
        Return the desired field name, or throw an error if the field name is unknown.

        The default implementation merely returns the exact field name passed in.
        """
        return field_name


class _TemplateChoiceFactory:
    __slots__ = ('template_ref', 'choice_name',)

    def __init__(self, template_ref, choice_name):
        self.template_ref = template_ref
        self.choice_name = choice_name

    def __call__(self, **kwargs) -> 'ExerciseStatementExpr':
        return ExerciseStatementExpr(
            expression=GetContractIdExpr(expression=TemplateSelectExpr(template=self.template_ref, alias=None)),
            choice_name=self.choice_name,
            arguments=exprify_args(kwargs))

    def __repr__(self):
        return f'<_TemplateChoiceFactory({self.choice_name!r})>'


class ConstantExpr(Expr):
    """ An expression that evaluates to a constant. """
    value: object

    @classmethod
    def coerce(cls, obj):
        if isinstance(obj, Expr):
            # TODO:
            return obj
        else:
            return ConstantExpr(value=obj)


class TemplateSelectExpr(Expr):
    """ A selection on a template. """
    template: TemplateExpr
    alias: str

    def __init__(self, template=None, alias=None):
        self.template = TemplateExpr.coerce(template)
        self.alias = alias

    @classmethod
    def coerce(cls, obj):
        """
        Attempt to coerce the specified type to a `TemplateSelectExpr`.
        """
        if isinstance(obj, TemplateSelectExpr):
            return obj
        if isinstance(obj, TemplateExpr):
            return TemplateSelectExpr(TemplateExpr.coerce(obj.template_ref), alias=None)
        elif isinstance(obj, str):
            return TemplateSelectExpr(TemplateExpr.coerce(obj), alias=None)
        raise TypeError("Couldn't convert to a {!r}: {!r}".format(cls.__name__, obj))

    def __repr__(self):
        return "<TemplateSelectExpr(template={!r}, alias={!r})>".format(self.template, self.alias)


class AppExpr(Expr):
    """
    An application of a function on one or arguments.
    """
    func: Any
    args: Collection[Expr]

    def __call__(self, *args, **kwargs):
        raise Exception(f'now where did THIS come from? args:{args} kwargs:{kwargs}')


class TemplateFieldExpr(Expr):
    """ An access of a field on a template. """
    expression: Expr
    field_name: str

    def __init__(self, expression=None, field_name=None):
        # coercion rules here are a little cumbersome:
        #  * str, TemplateRef, TemplateExpr and TemplateSelectExpr all expand to
        #    a cdata() reference on the appropriate contract fetch
        #  * all other expressions are assumed to be usable in this context
        # TODO: Formalize this here
        if isinstance(expression, (str, Type, TemplateExpr, TemplateSelectExpr)):
            expression = GetContractDataExpr(expression=TemplateSelectExpr.coerce(expression))
        elif not isinstance(expression, Expr):
            raise TypeError('Could not convert to an appropriate expression of a field access: {!r}'.format(expression))

        self.expression = expression
        self.field_name = field_name

    def __getitem__(self, sub_field_name):
        return TemplateFieldExpr(self, sub_field_name)

    @classmethod
    def coerce(cls, obj):
        if isinstance(obj, TemplateFieldExpr):
            return obj
        raise TypeError("Couldn't convert to a TemplateFieldExpr: {!r}".format(obj))


class TemplateSelectsExpr(Expr):
    """
    A set of template selections that define a cartesian join across all template options,
    paired with a predicate that establishes membership.
    """

    select: Set[TemplateSelectExpr]
    predicate: Optional[Expr]

    @classmethod
    def coerce(cls, obj):
        if isinstance(obj, TemplateSelectsExpr):
            return TemplateSelectsExpr(select=[TemplateSelectExpr.coerce(s) for s in obj.select], predicate=obj.predicate)
        elif isinstance(obj, TemplateSelectExpr):
            return TemplateSelectsExpr(select=[obj], predicate=None)
        elif isinstance(obj, TemplateExpr):
            return TemplateSelectsExpr(select=[TemplateSelectExpr(obj.template_ref, alias=None)])
        raise TypeError("Couldn't convert to a TemplateSelectsExpr: {!r}".format(obj))


class CreateStatementExpr(UpdateStatementExpr):
    """ A create statement. """
    template: Type
    arguments: dict


class ExerciseStatementExpr(UpdateStatementExpr):
    """ An exercise choice statement. """
    expression: Expr
    choice_name: str
    arguments: dict


class GetContractIdExpr(Expr):
    """
    Retrieve the contract ID for the specified expression. Automatically inserted at naked
    table references.
    """
    expression: TemplateSelectExpr

    @classmethod
    def coerce(cls, obj):
        if isinstance(obj, (Type, TemplateExpr, TemplateSelectExpr)):
            return GetContractIdExpr(expression=TemplateSelectExpr.coerce(obj))
        return super().coerce(obj)


class GetContractDataExpr(Expr):
    """
    Retrieve the contract data for the specified expression. Automatically inserted at field
    access sites.
    """
    expression: TemplateSelectExpr

    @classmethod
    def coerce(cls, obj):
        if isinstance(obj, (Type, TemplateExpr, TemplateSelectExpr)):
            return GetContractDataExpr(expression=TemplateSelectExpr.coerce(obj))


class _ExerciseStatementExprFactory:
    """
    A partially-applied choice exercise, containing everything except the actual arguments to
    parameters.
    """
    __slots__ = ('expression', 'choice_name')

    def __init__(self, expression, choice_name):
        self.expression = exprify_value(expression)
        self.choice_name = choice_name

    def __call__(self, **kwargs):
        return ExerciseStatementExpr(
            expression=self.expression,
            choice_name=self.choice_name,
            arguments=exprify_args(kwargs))

    def __repr__(self):
        return '<_ExerciseStatementExprFactory(expression={!r}, choice_name={!r})>'.format(
            self.expression, self.choice_name)


class UpdateBlockExpr(Expr):
    """ A block of updates. """
    statements: List[UpdateStatementExpr]

    def __init__(self, statements=None):
        self.statements = [UpdateStatementExpr.coerce(stmt) for stmt in _listify(statements)]

    @classmethod
    def coerce(cls, obj):
        """
        Attempt to coerce the specified type to a `UpdateBlockExpr`.
        """
        if obj is None:
            raise ValueError("can't be none")
        if isinstance(obj, UpdateBlockExpr):
            return obj
        if isinstance(obj, UpdateStatementExpr):
            return UpdateBlockExpr([obj])
        elif isinstance(obj, list):
            return UpdateBlockExpr(obj)
        raise TypeError("Couldn't convert to a UpdateBlockExpr: {!r}".format(obj))


class ProgramExpr(Expr):
    """
    A program, which is the combination of template selection with a block of updates and a trigger
    condition.
    """
    select: TemplateSelectsExpr
    update: UpdateBlockExpr
    trigger: str
    name: str

    def __init__(self, select=None, update=None, trigger=None, name=None):
        self.update = UpdateBlockExpr.coerce(update)
        self.trigger = trigger or TRIGGER_ANY_TIME
        self.name = name if name is not None else "p{}".format(id(self))

        if self.trigger == TRIGGER_ON_INIT and select is None:
            self.select = None
        elif select is not None:
            self.select = TemplateSelectsExpr.coerce(select)
        else:
            raise ValueError('a selection is required on ANY_TIME triggers')

    @staticmethod
    def coerce(obj):
        if isinstance(obj, ProgramExpr):
            return obj
        elif isinstance(obj, ExerciseStatementExpr):
            # only certain kinds of exercise statements can be easily converted to a Program
            # exercise 'choice_name' on cid(a) -> from a do update [ exercise 'choice_name' on cid(a) ]
            if isinstance(obj.expression, GetContractIdExpr) and \
               isinstance(obj.expression.expression, TemplateSelectExpr):
                return ProgramExpr(select=TemplateSelectsExpr.coerce(obj.expression.expression), update=UpdateBlockExpr.coerce(obj))
        raise TypeError("Couldn't convert to a ProgramExpr: {!r}".format(obj))


class SuiteExpr(Expr):
    """ A suite of initialization routines and programs. """
    party: str
    programs: List[ProgramExpr]


class Application(Expr):
    """
    An application, including the parties that are running programs on the ledger
    and required initialization steps.
    """
    suites: List[SuiteExpr]

    def as_string(self, color=False):
        """
        Print the `Application` expression tree.
        """
        from .visitor_pretty import pretty_print
        return pretty_print(self)

    def __str__(self):
        """
        Print the `Application` expression tree.
        """
        return self.as_string()


def and_(*predicates):
    """
    Convenience method for creating an AND expression over multiple expressions.
    """
    from .builtins import BUILTIN_AND
    return AppExpr(BUILTIN_AND, predicates)


def _listify(obj):
    """
    Wrap the object in a list if it is not already a list. `None` is converted into an empty list.
    """
    if obj is None:
        return []
    if isinstance(obj, str):
        return [obj]
    elif isinstance(obj, (list, tuple)):
        return obj
    else:
        return [obj]

