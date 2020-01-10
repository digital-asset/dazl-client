# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from dazl.util.dar import DarFile
from .dars import Pending


@pytest.mark.skip('Something about the way dazl compiles DARs currently causes this field to be blank')
def test_get_sdk_version():
    with DarFile(Pending) as dar:
        print(dar.get_manifest())
        assert '0.13.18' == dar.get_sdk_version()
