# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import pytest

from dazl.damlast.lookup import matching_normalizations, normalize
from dazl.model.lookup import template_reverse_globs


def test_non_primary_simple_unknown_module():
    expected = ["*:MyModule:MyTemplate", "*:*"]
    actual = matching_normalizations("*:MyModule:MyTemplate")
    assert actual == expected


def test_non_primary_simple_unknown_module_deprecated():
    with pytest.warns(DeprecationWarning):
        expected = ["*:MyModule:MyTemplate", "*:*"]
        actual = list(template_reverse_globs(False, "*", "MyModule:MyTemplate"))
        assert actual == expected


def test_normalize_unknown_package_with_explicit_star():
    expected = "*:MyModule:MyTemplate"
    actual = normalize("*:MyModule:MyTemplate")
    assert actual == expected


def test_normalize_unknown_package_without_explicit_star():
    expected = "*:MyModule:MyTemplate"
    actual = normalize("MyModule:MyTemplate")
    assert actual == expected


def test_primary_simple_unknown_module_deprecated():
    with pytest.warns(DeprecationWarning):
        expected = ["*:MyModule:MyTemplate"]
        actual = list(template_reverse_globs(True, "*", "MyModule:MyTemplate"))
        assert actual == expected


def test_non_primary_simple_unknown_module_rejects_deprecated_style():
    with pytest.raises(ValueError):
        # Period forms for template names are explicitly not allowed in the new API
        matching_normalizations("*:MyModule.MyTemplate")


def test_non_primary_simple_unknown_module_deprecated_style():
    with pytest.warns(DeprecationWarning):
        expected = ["*:MyModule:MyTemplate", "*:MyModule.MyTemplate", "*:*"]
        actual = list(template_reverse_globs(False, "*", "MyModule.MyTemplate"))
        assert actual == expected


def test_primary_simple_unknown_module_deprecated_style():
    with pytest.warns(DeprecationWarning):
        expected = ["*:MyModule:MyTemplate"]
        actual = list(template_reverse_globs(True, "*", "MyModule.MyTemplate"))
        assert actual == expected


def test_non_primary_simple_known_module():
    expected = [
        "0000dead0000beef:MyModule:MyTemplate",
        "0000dead0000beef:*",
        "*:MyModule:MyTemplate",
        "*:*",
    ]
    actual = matching_normalizations("0000dead0000beef:MyModule:MyTemplate")
    assert actual == expected


def test_non_primary_simple_known_module_deprecated():
    with pytest.warns(DeprecationWarning):
        expected = [
            "0000dead0000beef:MyModule:MyTemplate",
            "0000dead0000beef:*",
            "*:MyModule:MyTemplate",
            "*:*",
        ]
        actual = list(template_reverse_globs(False, "0000dead0000beef", "MyModule:MyTemplate"))
        assert actual == expected


def test_primary_simple_known_module():
    expected = "0000dead0000beef:MyModule:MyTemplate"
    actual = normalize("0000dead0000beef:MyModule:MyTemplate")
    assert actual == expected


def test_primary_simple_known_module_deprecated():
    with pytest.warns(DeprecationWarning):
        expected = ["0000dead0000beef:MyModule:MyTemplate"]
        actual = list(template_reverse_globs(True, "0000dead0000beef", "MyModule:MyTemplate"))
        assert actual == expected


def test_star_normalize():
    expected = "*:*"
    actual = normalize("*")
    assert actual == expected


def test_star_matching_normalizations():
    expected = ["*:*"]
    actual = matching_normalizations("*")
    assert actual == expected


def test_star_star_normalize():
    expected = "*:*"
    actual = normalize("*:*")
    assert actual == expected


def test_star_star_matching_normalizations():
    expected = ["*:*"]
    actual = matching_normalizations("*:*")
    assert actual == expected


def test_star_deprecated_primary_only():
    with pytest.warns(DeprecationWarning):
        expected = ["*:*"]
        actual = list(template_reverse_globs(True, "*", "*"))
        assert actual == expected


def test_star_deprecated_all():
    with pytest.warns(DeprecationWarning):
        expected = ["*:*"]
        actual = list(template_reverse_globs(False, "*", "*"))
        assert actual == expected
