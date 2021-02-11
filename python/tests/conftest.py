# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from concurrent.futures.thread import ThreadPoolExecutor
from datetime import timedelta
import logging
import os
import subprocess

import pytest

from dazl.util import ProcessLogger, find_free_port, kill_process_tree, wait_for_process_port

DEFAULT_SDK_VERSION = "1.3.0"
SANDBOX_START_TIMEOUT = timedelta(seconds=10)


@pytest.fixture(scope="session")
def sandbox() -> str:
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
    url = os.environ.get("DAZL_TEST_DAML_LEDGER_URL")
    if url:
        logging.info("Using the sandbox at %s because `DAZL_TEST_DAML_LEDGER_URL` is defined", url)
        yield url
        return

    port = find_free_port()

    env = os.environ.copy()
    # Running dazl's tests against a different Sandbox merely requires the DAML_SDK_VERSION
    # variable be set to a different value
    if "DAML_SDK_VERSION" not in env:
        env["DAML_SDK_VERSION"] = DEFAULT_SDK_VERSION

    process = subprocess.Popen(
        ["daml", "sandbox", "--port", str(port)],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    try:
        ProcessLogger(process, logging.getLogger("sandbox")).start()
        wait_for_process_port(process, port, SANDBOX_START_TIMEOUT)

        yield f"http://localhost:{port}"

    finally:
        # Clean up the process that we started. Note that some versions of the SDK have issues that
        # leave dangling child processes running even after the parent process is killed, so make
        # sure that we find and destroy them too if the parent process doesn't kill its own children
        # quickly enough.
        kill_process_tree(process)


@pytest.fixture()
def executor() -> "ThreadPoolExecutor":
    with ThreadPoolExecutor(3) as executor:
        yield executor
