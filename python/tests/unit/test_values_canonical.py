# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import date

from dazl.damlast import daml_types as daml
from dazl.prim import Party
from dazl.values import CanonicalMapper, Context


def test_values_canonical_bool():
    ctx = Context(CanonicalMapper())
    actual = ctx.convert(daml.Bool, False)
    assert not actual


def test_values_canonical_bool_false_string():
    ctx = Context(CanonicalMapper())
    actual = ctx.convert(daml.Bool, "false")
    assert not actual


def test_values_canonical_bool_random_string():
    ctx = Context(CanonicalMapper())
    try:
        ctx.convert(daml.Bool, "blahblahblah")
        assert False, "we were supposed to fail!"
    except ValueError:
        pass


def test_values_canonical_date():
    ctx = Context(CanonicalMapper())
    actual = ctx.convert(daml.Date, date(2020, 1, 1))
    assert date(2020, 1, 1) == actual


def test_values_canonical_date_str():
    ctx = Context(CanonicalMapper())
    actual = ctx.convert(daml.Date, "2020-01-01")
    assert date(2020, 1, 1) == actual


def test_values_canonical_str_that_looks_like_a_date():
    ctx = Context(CanonicalMapper())
    actual = ctx.convert(daml.Text, "2020-01-01")
    assert "2020-01-01" == actual


def test_values_optional_some_empty_string():
    ctx = Context(CanonicalMapper())
    actual = ctx.convert(daml.Optional(daml.Text), "")
    assert "" == actual


def test_values_optional_none():
    ctx = Context(CanonicalMapper())
    actual = ctx.convert(daml.Optional(daml.Text), None)
    assert None is actual


def test_values_party():
    ctx = Context(CanonicalMapper())
    actual = ctx.convert(daml.Party, "some-party")
    assert actual == Party("some-party")
