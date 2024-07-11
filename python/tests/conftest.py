# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from concurrent.futures.thread import ThreadPoolExecutor
from typing import Generator

from dazl import testing
import pytest


@pytest.fixture(scope="session", params=["1", "2"])
def sandbox(request, sandbox_v1, sandbox_v2) -> "Generator[testing.SandboxLauncher, None, None]":
    """
    Run an instance of the Sandbox, or use one configured through environment variables.

    Some environment variables change the nature of the Sandbox used in these tests:

     * DAZL_TEST_DAML_LEDGER_URL: If set, it is assumed to be an already-running ledger, and we
       merely return that URL instead of starting up our own sandbox. This is the way that the tests
       run in CI.
     * DAML_SDK_VERSION: If set AND DAZL_TEST_DAML_LEDGER_URL is not specified, this controls the
       version of the Sandbox that is launched through this wrapper. This value can be overridden
       to test dazl against newer (or older) versions of the SDK without making code changes:
         ```
         DAML_SDK_VERSION=1.0.0 make test
         ```
    """
    if request.param == "1":
        yield sandbox_v1
    else:
        yield sandbox_v2


@pytest.fixture(scope="session")
def sandbox_v1() -> "Generator[testing.SandboxLauncher, None, None]":
    with testing.sandbox(project_root=None, version="1.18.1") as sb:
        yield sb


@pytest.fixture(scope="session")
def sandbox_v2() -> "Generator[testing.SandboxLauncher, None, None]":
    with testing.sandbox(
        project_root=None, version="2.5.0-snapshot.20221201.11065.0.caac1d10"
    ) as sb:
        yield sb


@pytest.fixture()
def executor() -> "Generator[ThreadPoolExecutor, None, None]":
    with ThreadPoolExecutor(3) as executor:
        yield executor
