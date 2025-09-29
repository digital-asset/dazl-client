# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.damlast import DarFile

from .dars import Pending


def test_get_sdk_version() -> None:
    with DarFile(Pending) as dar:
        print(dar.manifest())
        assert "2.10.1" == dar.sdk_version()
