# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains builders for applications.
"""
import collections

from ._rewriter import RewriteContext
from .expr_impl import SuiteExpr, ProgramExpr, TemplateSelectExpr, Application


class ApplicationBuilder:
    """
    Builder for an application.
    """
    def __init__(self):
        self.suite_builders = collections.OrderedDict()

    def as_party(self, party_name):
        """
        Creates a builder for a `SuiteExpr` to be run under the context of the named party.
        """
        suite_builder = self.suite_builders.get(party_name)
        if suite_builder is None:
            suite_builder = SuiteBuilder(party_name)
            self.suite_builders[party_name] = suite_builder
        return suite_builder

    def build(self) -> Application:
        """
        Builds an application.
        """
        return Application([builder.build() for builder in self.suite_builders.values()])


class SuiteBuilder:
    """
    Builder for a suite of programs.
    """
    def __init__(self, party_name):
        self.party_name = party_name
        self.programs = []

    def add(self, program):
        """
        Registers a program to watch and respond to changes in state on the ledger.

        :param program:
            A `ProgramExpr` that defines a search condition and an operation to perform against
            all members of the set that match the search condition.
        :return:
            `self`; this class is intended to be used in a fluent style.
        """
        self.programs.append(generate_default_aliases(ProgramExpr.coerce(program)))
        return self

    def extend(self, programs):
        self.programs.extend(map(generate_default_aliases, programs))
        return self

    def build(self):
        """
        Build a `SuiteExpr` that are the instructions to perform on the ledger.
        """
        return SuiteExpr(party=self.party_name, programs=list(self.programs))


def merge_suites(*suites):
    """
    Merges multiple suites together.
    """
    suites = [suite for suite in suites if suite]
    if not suites:
        raise ValueError("at least one suite required here")

    # TODO: The parties must all be the same; verify this
    party = suites[0].party
    programs = []
    for suite in suites:
        programs.extend(suite.programs)
    return SuiteExpr(party=party, programs=programs)


def generate_default_aliases(expr):
    template_refs = set()

    context = RewriteContext()

    @context.register(TemplateSelectExpr)
    def capture_distinct_selects(select):
        template_refs.add(_named_template_ref(select))
        return select

    context.rewrite(expr)

    unnamed_refs = {tref.template_id for tref in template_refs if tref.alias is None}
    used_ref_names = {tref.alias for tref in template_refs if tref.alias is not None}

    rewritten_template_refs = {
        NamedTemplateRef(template_id=tref, alias=None):
        NamedTemplateRef(template_id=tref, alias=generate_alias_name(used_ref_names, tref.name, i))
        for i, tref in enumerate(unnamed_refs)}

    @context.register(TemplateSelectExpr)
    def rewrite_select(select: TemplateSelectExpr):
        rewrite = rewritten_template_refs[_named_template_ref(select)]
        return TemplateSelectExpr(template=rewrite.template_id, alias=rewrite.alias)

    return context.rewrite(expr)


def generate_alias_name(used_names, template_id: str, i: int):
    candidate = template_id.split('.')[-1][0].lower() + str(i)
    return candidate if candidate not in used_names else candidate + '0'


def _named_template_ref(expr: TemplateSelectExpr):
    return NamedTemplateRef(expr.template.template_ref, expr.alias)


NamedTemplateRef = collections.namedtuple('NamedTemplateRef', ['template_id', 'alias'])
