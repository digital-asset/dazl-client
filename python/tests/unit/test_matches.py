# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains tests for testing contract data against a match object.
"""

from unittest import TestCase

from dazl.client._reader_match import is_match


class TestMatches(TestCase):
    def test_match_of_partial_keys(self):
        match = {"a": 2, "b": 3}
        value = {"c": 4, "a": 2, "b": 3}
        self.assertTrue(is_match(match, value))

    def test_match_of_partial_top_level_keys(self):
        match = {"d": 3}
        value = {"a": {"b": 1, "c": 2}, "d": 3}
        self.assertTrue(is_match(match, value))

    def test_match_of_partial_deep_nested_keys(self):
        match = {"a": {"b": 1}}
        value = {"a": {"b": 1, "c": 2}, "d": 3}
        self.assertTrue(is_match(match, value))
