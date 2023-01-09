# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.damlast.lookup import parse_type_con_name
from dazl.query import EMPTY, Filter, parse_query
import pytest

SuperCoolTmpl = parse_type_con_name("SuperCool:Tmpl")
ReallyCoolTmpl = parse_type_con_name("ReallyCool:Tmpl")


@pytest.mark.parametrize("server_side_filters", [False, True])
def test_empty_query(server_side_filters):
    actual = parse_query(server_side_filters=server_side_filters)
    assert actual is None


@pytest.mark.parametrize("server_side_filters", [False, True])
def test_single_template(server_side_filters):
    expected = {SuperCoolTmpl: EMPTY}
    actual = parse_query("SuperCool:Tmpl", server_side_filters=server_side_filters)

    assert expected == actual


@pytest.mark.parametrize(
    "queries",
    [
        ["SuperCool:Tmpl", "ReallyCool:Tmpl"],
        [["SuperCool:Tmpl", "ReallyCool:Tmpl"]],
        [{"SuperCool:Tmpl", "ReallyCool:Tmpl"}],
        [{"SuperCool:Tmpl": {}, "ReallyCool:Tmpl": {}}],
        [{"SuperCool:Tmpl": None, "ReallyCool:Tmpl": None}],
        [{"SuperCool:Tmpl": None}, {"ReallyCool:Tmpl": None}],
    ],
)
@pytest.mark.parametrize("server_side_filters", [False, True])
def test_two_templates(queries, server_side_filters):
    expected = {SuperCoolTmpl: EMPTY, ReallyCoolTmpl: EMPTY}
    actual = parse_query(*queries, server_side_filters=server_side_filters)

    assert expected == actual


def test_two_templates_as_dict_with_one_match_server_side_filters():
    expected = {SuperCoolTmpl: Filter(server_side={"field": 42}), ReallyCoolTmpl: EMPTY}
    actual = parse_query(
        {"SuperCool:Tmpl": {"field": 42}, "ReallyCool:Tmpl": None}, server_side_filters=True
    )

    assert expected == actual


def test_two_templates_as_dict_with_one_match_no_server_side_filters():
    """
    Assert that client-side filtering works; the gRPC Ledger API does not support any server-side
    filtering of contracts beyond template names, so filtering must be done on the client in this
    case.
    """
    actual = parse_query(
        {"SuperCool:Tmpl": {"field": 42}, "ReallyCool:Tmpl": None}, server_side_filters=False
    )

    assert actual is not None
    assert actual[SuperCoolTmpl].server_side is None

    # A contract with a "field" value of 42 should match the client-side filter
    assert actual[SuperCoolTmpl].client_side({"field": 42})

    # A contract with a "field" value of 43 should NOT match the client-side filter
    assert not actual[SuperCoolTmpl].client_side({"field": 43})

    assert actual[ReallyCoolTmpl] == EMPTY
