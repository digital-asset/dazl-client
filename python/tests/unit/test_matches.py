# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains tests for testing contract data against a match object.
"""

from __future__ import annotations

from dazl.query import is_match


def test_match_of_partial_keys():
    match = {"a": 2, "b": 3}
    value = {"c": 4, "a": 2, "b": 3}
    assert is_match(match, value)


def test_match_of_partial_top_level_keys():
    match = {"d": 3}
    value = {"a": {"b": 1, "c": 2}, "d": 3}
    assert is_match(match, value)


def test_match_of_partial_deep_nested_keys():
    match = {"a": {"b": 1}}
    value = {"a": {"b": 1, "c": 2}, "d": 3}
    assert is_match(match, value)


def test_non_match_of_partial_deep_nested_keys():
    match = {"a": {"b": 1}}
    value = {"a": {"b": 2, "c": 2}, "d": 3}
    assert not is_match(match, value)


def test_non_match_of_disjoint_keys():
    match = {"x": 1}
    value = {"a": {"b": 2, "c": 2}, "d": 3}
    assert not is_match(match, value)
