# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.damlast import DarFile
from .dars import Pending


def test_get_sdk_version():
    with DarFile(Pending) as dar:
        print(dar.manifest())
        assert '1.3.0' == dar.sdk_version()
