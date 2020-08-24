# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.util.prim_types import PrimitiveTypeConverter


def test_true_lowercase_bool():
    sut = PrimitiveTypeConverter()
    actual = sut.to_boolean('true')

    assert actual


def test_true_titlecase_bool():
    sut = PrimitiveTypeConverter()
    actual = sut.to_boolean('True')

    assert actual


def test_true_lowercase_whitespace_bool():
    sut = PrimitiveTypeConverter()
    actual = sut.to_boolean('  true ')

    assert actual


def test_false_lowercase_bool():
    sut = PrimitiveTypeConverter()
    actual = sut.to_boolean('false')

    assert not actual


def test_false_titlecase_bool():
    sut = PrimitiveTypeConverter()
    actual = sut.to_boolean('False')

    assert not actual


def test_false_lowercase_whitespace_bool():
    sut = PrimitiveTypeConverter()
    actual = sut.to_boolean('  false ')

    assert not actual
