# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from concurrent.futures.thread import ThreadPoolExecutor
import sys
from typing import Generator

from dazl import testing
import pytest

# match statements are syntax errors in Python 3.8 and 3.9; we must exclude them from
# test discovery or pytest will fail to discover tests properly
if sys.version_info < (3, 10):
    collect_ignore_glob = ["*_py3_10.py"]


@pytest.fixture(scope="session")
def sandbox() -> Generator[testing.SandboxLauncher, None, None]:
    with testing.sandbox() as sb:
        yield sb


@pytest.fixture()
def executor() -> Generator[ThreadPoolExecutor, None, None]:
    with ThreadPoolExecutor(3) as executor:
        yield executor
