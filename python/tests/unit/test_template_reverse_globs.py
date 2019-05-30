# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase

from dazl.model.reading import template_reverse_globs


class TestTemplateReverseGlobs(TestCase):
    def test_non_primary_simple_unknown_module(self):
        expected = ['*/MyTemplate', '*/*']
        actual = list(template_reverse_globs(False, '*', 'MyTemplate'))
        self.assertEqual(expected, actual)

    def test_primary_simple_unknown_module(self):
        expected = ['*/MyTemplate']
        actual = list(template_reverse_globs(True, '*', 'MyTemplate'))
        self.assertEqual(expected, actual)

    def test_non_primary_simple_known_module(self):
        expected = ['0000dead0000beef/MyTemplate', '0000dead0000beef/*', '*/MyTemplate', '*/*']
        actual = list(template_reverse_globs(False, '0000dead0000beef', 'MyTemplate'))
        self.assertEqual(expected, actual)

    def test_primary_simple_known_module(self):
        expected = ['0000dead0000beef/MyTemplate']
        actual = list(template_reverse_globs(True, '0000dead0000beef', 'MyTemplate'))
        self.assertEqual(expected, actual)
