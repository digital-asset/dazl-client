# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from concurrent.futures.thread import ThreadPoolExecutor
from datetime import timedelta
import logging
import os
import subprocess
import sys
from typing import Any, Generator

from dazl import testing
from dazl.util import ProcessLogger, find_free_port, kill_process_tree, wait_for_process_port
import pytest


@pytest.fixture(scope="session")
def sandbox() -> Generator[testing.SandboxLauncher, None, None]:
    with testing.sandbox() as sb:
        yield sb


@pytest.fixture(scope="session")
def sandbox_v3() -> Generator[Any, None, None]:
    grpc_port = find_free_port()
    json_api_port = find_free_port()

    cmdline = [
        "daml",
        "sandbox",
        "--port",
        str(grpc_port),
        "--json-api-port",
        str(json_api_port),
    ]

    log = logging.getLogger("sandbox_v3")
    log.info("Launching Canton 3.x sandbox: %s", cmdline)

    env = os.environ.copy()
    daml_path = os.path.expanduser("~/.daml/bin")
    if daml_path not in env.get("PATH", ""):
        env["PATH"] = f"{daml_path}:{env.get('PATH', '')}"

    process = subprocess.Popen(
        cmdline,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    ProcessLogger(process, log).start()

    try:
        wait_for_process_port(process, json_api_port, timedelta(seconds=60))

        class SandboxV3:
            @property
            def url(self):
                return f"http://localhost:{json_api_port}"

        yield SandboxV3()
    finally:
        kill_process_tree(process)


@pytest.fixture()
def executor() -> Generator[ThreadPoolExecutor, None, None]:
    with ThreadPoolExecutor(3) as executor:
        yield executor
