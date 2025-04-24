# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.damlast.lookup import validate_template


def test_scu_name():
    pkg_ref, name = validate_template("#name:Module.SubModule:Template")
    assert pkg_ref == "#name"
    assert name == "Module.SubModule:Template"
