# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase

from dazl.util.prim_types import PrimitiveTypeConverter


class TestCoerceBool(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.converter = PrimitiveTypeConverter()

    def test_true_lowercase_bool(self):
        actual = self.converter.to_boolean('true')
        self.assertTrue(actual)

    def test_true_titlecase_bool(self):
        actual = self.converter.to_boolean('True')
        self.assertTrue(actual)

    def test_true_lowercase_whitespace_bool(self):
        actual = self.converter.to_boolean('  true ')
        self.assertTrue(actual)

    def test_false_lowercase_bool(self):
        actual = self.converter.to_boolean('false')
        self.assertFalse(actual)

    def test_false_titlecase_bool(self):
        actual = self.converter.to_boolean('False')
        self.assertFalse(actual)

    def test_false_lowercase_whitespace_bool(self):
        actual = self.converter.to_boolean('  false ')
        self.assertFalse(actual)
