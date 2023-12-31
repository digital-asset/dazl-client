# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

# noinspection PyProtectedMember
from dazl.client.events import _template_reverse_globs as template_reverse_globs


def test_non_primary_simple_unknown_module():
    expected = ["*:MyModule:MyTemplate", "*:*"]
    actual = list(template_reverse_globs(False, "*", "MyModule:MyTemplate"))
    assert expected == actual


def test_primary_simple_unknown_module():
    expected = ["*:MyModule:MyTemplate"]
    actual = list(template_reverse_globs(True, "*", "MyModule:MyTemplate"))
    assert expected == actual


def test_non_primary_simple_unknown_module_deprecated_style():
    expected = ["*:MyModule:MyTemplate", "*:MyModule.MyTemplate", "*:*"]
    actual = list(template_reverse_globs(False, "*", "MyModule.MyTemplate"))
    assert expected == actual


def test_primary_simple_unknown_module_deprecated_style():
    expected = ["*:MyModule:MyTemplate"]
    actual = list(template_reverse_globs(True, "*", "MyModule.MyTemplate"))
    assert expected == actual


def test_non_primary_simple_known_module():
    expected = [
        "0000dead0000beef:MyModule:MyTemplate",
        "0000dead0000beef:*",
        "*:MyModule:MyTemplate",
        "*:*",
    ]
    actual = list(template_reverse_globs(False, "0000dead0000beef", "MyModule:MyTemplate"))
    assert expected == actual


def test_primary_simple_known_module():
    expected = ["0000dead0000beef:MyModule:MyTemplate"]
    actual = list(template_reverse_globs(True, "0000dead0000beef", "MyModule:MyTemplate"))
    assert expected == actual
