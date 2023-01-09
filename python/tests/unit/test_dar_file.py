# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.damlast import DarFile

from .dars import Pending


def test_get_sdk_version():
    with DarFile(Pending) as dar:
        print(dar.manifest())
        assert "1.18.3" == dar.sdk_version()
