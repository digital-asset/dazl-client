# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import inspect
from typing import List, Union

from .expr_base import Expr, TRIGGER_ON_INIT, TRIGGER_ANY_TIME
from .expr_impl import TemplateExpr, TemplateSelectsExpr, TemplateSelectExpr, \
    UpdateBlockExpr, UpdateStatementExpr, ProgramExpr


UpdateType = Union[UpdateBlockExpr, UpdateStatementExpr, List[Union[UpdateBlockExpr, UpdateStatementExpr]]]


def from_(*templates: Union[TemplateExpr, TemplateSelectExpr], name=None) -> 'ProgramExprBuilder':
    """
    Builder method for a `ProgramExpr` that runs on a set of templates at any time.
    """
    if name is None:
        frameinfo: inspect.FrameInfo = inspect.stack()[1]
        name = frameinfo.function
    return ProgramExprBuilder(name=name, trigger=TRIGGER_ANY_TIME, templates=templates)


def init(name: str=None) -> 'InitProgramExprBuilder':
    """
    Builder method for a `ProgramExpr` that runs only when an initial condition has been met.
    """
    if name is None:
        frameinfo: inspect.FrameInfo = inspect.stack()[1]
        name = frameinfo.function
    return InitProgramExprBuilder(name)


class InitProgramExprBuilder(object):
    """
    Builder class for a `ProgramExpr`, starting from the assumption that the trigger condition is
    `TRIGGER_ON_INIT`.
    """
    def __init__(self, name: str=None):
        if name is None:
            frameinfo: inspect.FrameInfo = inspect.stack()[1]
            name = frameinfo.function
        self.name = name

    def from_(self, *templates: Union[TemplateExpr, TemplateSelectExpr]) -> 'ProgramExprBuilder':
        """
        Specify that the initial condition is, in part, based on ledger state of a select set of
        templates.
        """
        return ProgramExprBuilder(name=self.name, trigger=TRIGGER_ON_INIT, templates=templates)

    def update(self, expression: Union['UpdateBlockExpr', 'UpdateStatementExpr']) -> 'ProgramExpr':
        """
        Specify the update block to invoke when the ledger is initialized and otherwise has no
        pre-existing state.
        """
        return ProgramExpr(name=self.name, select=None, update=expression, trigger=TRIGGER_ON_INIT)


class ProgramExprBuilder(object):
    def __init__(self, name, trigger, templates, predicate=None):
        self.name = name
        self.trigger = trigger
        self.templates = templates
        self.predicate = predicate

    def where(self, *predicates: 'Expr') -> 'ProgramExprBuilder':
        from . import and_
        return ProgramExprBuilder(
            name=self.name,
            trigger=self.trigger,
            templates=self.templates,
            predicate=and_(*predicates))

    def update(self, expression: UpdateType) -> ProgramExpr:
        """
        Return the :class:`ProgramExpr` with the specified parameters.
        """
        if isinstance(expression, UpdateStatementExpr):
            expression = UpdateBlockExpr((expression,))
        return ProgramExpr(
            name=self.name,
            select=TemplateSelectsExpr(self.templates, self.predicate),
            update=expression,
            trigger=self.trigger)
