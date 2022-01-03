# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import get_event_loop
from datetime import timedelta
import logging
import os
import subprocess
import threading
from typing import Optional, Union

from ..util import ProcessLogger, find_free_port, kill_process_tree, wait_for_process_port

DEFAULT_TIMEOUT = timedelta(seconds=10)


class SandboxLauncher:
    """
    A simple launcher for an in-memory Sandbox.
    """

    def __init__(
        self,
        *,
        project_root: "Union[None, str, os.PathLike]",
        version: "Optional[str]" = None,
        timeout: "Optional[timedelta]" = DEFAULT_TIMEOUT,
    ):
        self._version = version
        self._timeout = timeout
        self._lock = threading.RLock()
        self._project_root = project_root
        self._process = None  # type: Optional[subprocess.Popen]
        self._url = None  # type: Optional[str]

        url = os.environ.get("DAZL_TEST_DAML_LEDGER_URL")
        if url:
            # if we're supposed to use a different already-running implementation,
            # then do that instead
            logging.info(
                "Using the sandbox at %s because `DAZL_TEST_DAML_LEDGER_URL` is defined", url
            )
            self._url = url

    @property
    def url(self) -> str:
        """
        Return a URL that can be used to connect to this running Sandbox.
        """
        u = self._url
        if u is not None:
            return u
        else:
            raise RuntimeError("the sandbox is not running (did you call start()?)")

    def start(self) -> None:
        """
        Start the sandbox and return a URL that can be used to connect to it.
        """
        if self._url is not None:
            return

        port = find_free_port()

        env = os.environ.copy()
        # Running dazl's tests against a different Sandbox merely requires the DAML_SDK_VERSION
        # variable be set to a different value
        if self._version is not None:
            env["DAML_SDK_VERSION"] = self._version

        with self._lock:
            # one last check inside the lock
            if self._url is not None:
                return

            if self._process is not None:
                # this shouldn't ever happen, but we explicitly check for it because running
                # multiple sandbox processes could be very confusing
                raise RuntimeError("we somehow have a process without a URL")

            cwd = None  # type: Union[None, str, os.PathLike]
            if self._project_root:
                cmdline = [
                    "daml",
                    "start",
                    "--start-navigator=no",
                    "--open-browser=no",
                    f"--sandbox-port={port}",
                ]
                cwd = self._project_root
            else:
                cmdline = ["daml", "sandbox", "--port", str(port)]

            self._process = subprocess.Popen(
                cmdline,
                env=env,
                cwd=cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
            ProcessLogger(self._process, logging.getLogger("sandbox")).start()
            wait_for_process_port(self._process, port, DEFAULT_TIMEOUT)

            self._url = f"http://localhost:{port}"

    def stop(self) -> None:
        """
        Stop the sandbox.
        """
        process = self._process
        if process is not None:
            # Clean up the process that we started. Note that some really old versions of the SDK
            # had issues that left dangling child processes running even after the parent process is
            # killed, so make sure that we find and destroy them too if the parent process doesn't
            # kill its own children quickly enough.
            try:
                kill_process_tree(process)
            finally:
                self._url = None

    def __enter__(self) -> "SandboxLauncher":
        """
        Start the sandbox.
        """
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Stop the sandbox.
        """
        self.stop()

    async def __aenter__(self) -> "SandboxLauncher":
        """
        Start the sandbox.
        """
        loop = get_event_loop()
        await loop.run_in_executor(None, self.start)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Stop the sandbox.
        """
        loop = get_event_loop()
        await loop.run_in_executor(None, self.stop)
