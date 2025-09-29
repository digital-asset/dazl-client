# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from dazl.damlast.lookup import matching_normalizations, normalize
import pytest


def test_non_primary_simple_unknown_module() -> None:
    expected = ["*:MyModule:MyTemplate", "*:*"]
    actual = matching_normalizations("*:MyModule:MyTemplate")
    assert actual == expected


def test_normalize_unknown_package_with_explicit_star() -> None:
    expected = "*:MyModule:MyTemplate"
    actual = normalize("*:MyModule:MyTemplate")
    assert actual == expected


def test_normalize_unknown_package_without_explicit_star() -> None:
    expected = "*:MyModule:MyTemplate"
    actual = normalize("MyModule:MyTemplate")
    assert actual == expected


def test_non_primary_simple_unknown_module_rejects_deprecated_style() -> None:
    with pytest.raises(ValueError):
        # Period forms for template names are explicitly not allowed in the new API
        matching_normalizations("*:MyModule.MyTemplate")


def test_non_primary_simple_known_module() -> None:
    expected = [
        "0000dead0000beef:MyModule:MyTemplate",
        "0000dead0000beef:*",
        "*:MyModule:MyTemplate",
        "*:*",
    ]
    actual = matching_normalizations("0000dead0000beef:MyModule:MyTemplate")
    assert actual == expected


def test_primary_simple_known_module() -> None:
    expected = "0000dead0000beef:MyModule:MyTemplate"
    actual = normalize("0000dead0000beef:MyModule:MyTemplate")
    assert actual == expected


def test_star_normalize() -> None:
    expected = "*:*"
    actual = normalize("*")
    assert actual == expected


def test_star_matching_normalizations() -> None:
    expected = ["*:*"]
    actual = matching_normalizations("*")
    assert actual == expected


def test_star_star_normalize() -> None:
    expected = "*:*"
    actual = normalize("*:*")
    assert actual == expected


def test_star_star_matching_normalizations() -> None:
    expected = ["*:*"]
    actual = matching_normalizations("*:*")
    assert actual == expected
