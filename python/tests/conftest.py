# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from concurrent.futures.thread import ThreadPoolExecutor
import sys
from typing import Generator

from dazl import testing
import pytest


@pytest.fixture(scope="session")
def sandbox() -> Generator[testing.SandboxLauncher, None, None]:
    with testing.sandbox() as sb:
        yield sb


@pytest.fixture()
def executor() -> Generator[ThreadPoolExecutor, None, None]:
    with ThreadPoolExecutor(3) as executor:
        yield executor
