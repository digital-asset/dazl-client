# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.prim import to_bool


def test_true_lowercase_bool():
    actual = to_bool("true")

    assert actual


def test_true_titlecase_bool():
    actual = to_bool("True")

    assert actual


def test_true_lowercase_whitespace_bool():
    actual = to_bool("  true ")

    assert actual


def test_false_lowercase_bool():
    actual = to_bool("false")

    assert not actual


def test_false_titlecase_bool():
    actual = to_bool("False")

    assert not actual


def test_false_lowercase_whitespace_bool():
    actual = to_bool("  false ")

    assert not actual
