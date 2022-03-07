# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from asyncio import get_event_loop
from contextlib import ExitStack
from datetime import timedelta
import logging
import os
from pathlib import Path
import subprocess
import tempfile
import threading
from typing import Any, Dict, Mapping, Optional, Union, cast

from ..util import ProcessLogger, find_free_port, kill_process_tree, wait_for_process_port
from ._cert import Certificate, cert_gen

__all__ = ["DEFAULT_TIMEOUT", "SandboxLauncher"]

DEFAULT_TIMEOUT = timedelta(seconds=10)


class SandboxLauncher:
    """
    A simple launcher for an in-memory Sandbox.
    """

    def __init__(
        self,
        *,
        project_root: "Union[None, str, os.PathLike]" = None,
        version: "Optional[str]" = None,
        timeout: "Optional[timedelta]" = DEFAULT_TIMEOUT,
        use_auth: bool = False,
        use_tls: bool = False,
    ):
        self._lock = threading.RLock()
        self._project_root = project_root
        self._version = version
        self._timeout = timeout
        self._process = None  # type: Optional[subprocess.Popen]
        self._url = None  # type: Optional[str]
        self._exit_stack = ExitStack()
        self._use_auth = use_auth
        self._use_tls = use_tls

        self._certificate = None  # type: Optional[Certificate]
        self._crt_file = None  # type: Optional[str]
        self._key_file = None  # type: Optional[str]

        if self._use_auth or self._use_tls:
            if self._project_root is not None:
                raise RuntimeError(
                    "use_auth/use_tls cannot be specified when specifying a project root"
                )

        url = os.environ.get("DAZL_TEST_DAML_LEDGER_URL")
        if url:
            # if we're supposed to use a different already-running implementation,
            # then do that instead
            logging.info(
                "Using the sandbox at %s because `DAZL_TEST_DAML_LEDGER_URL` is defined", url
            )
            self._url = url

    @property
    def public_cert(self) -> bytes:
        """
        Return the public key corresponding to the private key that was used to start the
        sandbox using TLS.
        """
        if self._certificate is None:
            raise RuntimeError("auth/tls was not enabled, so a public cert was not generated")

        return self._certificate.public_cert

    def sign_token(self, claims: "Mapping[str, Any]") -> str:
        """
        Sign a token using the private key that the sandbox was launched with.
        """
        if self._certificate is None:
            raise RuntimeError("this sandbox was not started with auth")

        import jwt

        return jwt.encode(
            # there is a bug in the jwt typing rules that falsely state the claims are
            # Dict[str, Any] when Mapping[str, Any] would actually work
            cast(Dict[str, Any], claims),
            self._certificate.private_key.decode("utf-8"),
            algorithm="RS256",
        )

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

            self._certificate = cert_gen(subject_alternative_name="localhost")

            crt_file = cast(str, self._exit_stack.push(tempfile.NamedTemporaryFile()).name)  # type: ignore
            key_file = cast(str, self._exit_stack.push(tempfile.NamedTemporaryFile()).name)  # type: ignore
            Path(crt_file).write_bytes(self._certificate.public_cert)
            Path(key_file).write_bytes(self._certificate.private_key)
            self._crt_file = crt_file
            self._key_file = key_file

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

            if self._use_auth or self._use_tls:
                # We're supposed to launch with auth and/or TLS.
                # Both of these flags moved around from Daml 1.x to Daml 2.x,
                # so determine which set of flags to use.
                if self._version is None:
                    raise RuntimeError("when tls/auth is on, a version must be specified")
                major_version, _, _ = self._version.partition(".")
                if major_version in ("0", "1"):
                    # assume Daml 1.x or earlier
                    if self._use_auth:
                        cmdline.extend(["--auth-jwt-rs256-crt", str(self._key_file)])
                    if self._use_tls:
                        cmdline.extend(
                            [
                                "--crt",
                                str(self._crt_file),
                                "--pem",
                                str(self._key_file),
                                "--client-auth",
                                "none",
                            ]
                        )
                else:
                    # assume Daml 2.x or later
                    if self._use_auth:
                        cmdline.extend(
                            [
                                "-D" + f"ledger-api.auth-services.type=jwt-rs-256-crt",
                                "-D" + f"ledger-api.auth-services.certificate={self._crt_file!r}",
                            ]
                        )
                    if self._use_tls:
                        cmdline.extend(
                            [
                                "-D" + f"ledger-api.tls.cert-chain-file={self._crt_file!r}",
                                "-D" + f"ledger-api.tls.private-key-file={self._key_file!r}",
                                "-D" + "ledger-api.tls.client-auth=none",
                            ]
                        )

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
        self._exit_stack.close()

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
