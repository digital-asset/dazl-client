# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Utility methods operating on a full expression tree.
"""

from collections import defaultdict
from typing import Set, Dict

from ._rewriter import RewriteContext
from ..model.types import Type


def get_distinct_templates(expr) -> Dict[str, Set[Type]]:
    """
    Return the distinct :class:`TemplateRef` that occur in the expression tree and their
    associated aliases.

    :return:
        A dict whose keys are template ID strings and values are lists of strings
        that are their corresponding aliases in the expression tree.
    """
    from .expr_impl import TemplateSelectExpr

    template_refs = defaultdict(set)

    context = RewriteContext()

    @context.register(TemplateSelectExpr)
    def _capture_select(expr_):
        template_refs[expr_.template.template_ref.name].add(expr_.alias)
        return expr_

    context.rewrite(expr)

    return {key: sorted(value) for key, value in template_refs.items()}


def get_distinct_aliases(expr) -> Set[str]:
    from .expr_impl import TemplateSelectExpr

    aliases = set()

    context = RewriteContext()

    @context.register(TemplateSelectExpr)
    def _capture_select(expr_: TemplateSelectExpr):
        aliases.add(expr_.alias)
        return expr_

    context.rewrite(expr)

    return aliases
