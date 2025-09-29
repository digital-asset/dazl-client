# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.damlast.lookup import parse_type_con_name
from dazl.damlast.util import package_local_name, package_ref


def test_damlast_parse_type_con_name() -> None:
    name = parse_type_con_name("*")

    assert package_ref(name) == "*"
    assert package_local_name(name) == "*"


def test_damlast_parse_type_con_name_double_star() -> None:
    name = parse_type_con_name("*:*")

    assert package_ref(name) == "*"
    assert package_local_name(name) == "*"


def test_damlast_parse_type_con_name_unknown_package() -> None:
    name = parse_type_con_name("SomeModule:SomeEntity")

    assert package_ref(name) == "*"
    assert package_local_name(name) == "SomeModule:SomeEntity"


def test_damlast_parse_type_con_name_fully_qualified() -> None:
    name = parse_type_con_name("abc123def456abc123def456:SomeModule:SomeEntity")

    assert package_ref(name) == "abc123def456abc123def456"
    assert package_local_name(name) == "SomeModule:SomeEntity"


def test_damlast_parse_type_con_name_package_only() -> None:
    name = parse_type_con_name("abc123def456abc123def456:*")

    assert package_ref(name) == "abc123def456abc123def456"
    assert package_local_name(name) == "*"
