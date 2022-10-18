# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import get_event_loop
from contextlib import ExitStack
from datetime import timedelta
import logging
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
from typing import Any, Dict, Mapping, Optional, Sequence, Union, cast

from ..util import ProcessLogger, find_free_port, kill_process_tree, wait_for_process_port
from ._cert import Certificate, cert_gen

if sys.version_info >= (3, 11):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

__all__ = ["DEFAULT_TIMEOUT", "SandboxLauncher"]

DEFAULT_TIMEOUT = timedelta(seconds=30)


class ExternalURLSource:
    def __init__(self, url: str) -> None:
        self.url = url


class LocalURLSource:
    def __init__(self, port: int) -> None:
        self.port = port

    def __str__(self) -> str:
        return f"http://localhost:{self.port}"

    @property
    def url(self) -> str:
        return str(self)


URLSource: TypeAlias = Union[LocalURLSource, ExternalURLSource]


class SandboxLauncher:
    """
    A simple launcher for an in-memory Sandbox.
    """

    _url_source: URLSource

    def __init__(
        self,
        *,
        project_root: Union[None, str, os.PathLike] = None,
        version: Optional[str] = None,
        timeout: Optional[timedelta] = DEFAULT_TIMEOUT,
        ledger_id: Optional[str] = None,
        use_auth: bool = False,
        use_tls: bool = False,
        url: Optional[str] = None,
    ) -> None:
        """
        Initialize an instance of :class:`SandboxLauncher`.

        :param url:
            If supplied, a URL to an _already running_ sandbox that should instead be used.
            If NOT supplied, then take the value of the ``DAZL_TEST_DAML_LEDGER_URL`` if
            supplied, or start sandbox on a randomized local port.
        """
        self.log = logging.getLogger("sandbox")
        self._lock = threading.RLock()
        self._project_root = project_root
        self._version = version
        self._timeout = timeout
        self._ledger_id = ledger_id
        self._process = None  # type: Optional[subprocess.Popen]

        self._exit_stack = ExitStack()
        self._use_auth = use_auth
        self._use_tls = use_tls

        self._certificate = None  # type: Optional[Certificate]
        self._crt_file = None  # type: Optional[Path]
        self._key_file = None  # type: Optional[Path]

        if self._use_auth or self._use_tls:
            if self._project_root is not None:
                raise RuntimeError(
                    "use_auth/use_tls cannot be specified when specifying a project root"
                )

        # first, default the url to an environment variable if present
        if not url:
            url = os.environ.get("DAZL_TEST_DAML_LEDGER_URL")
            if url:
                logging.info(
                    "Using the sandbox at %s because `DAZL_TEST_DAML_LEDGER_URL` is defined", url
                )

        if url:
            self._url_source = ExternalURLSource(url)
        else:
            self._url_source = LocalURLSource(find_free_port())

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
        return self._url_source.url

    def start(self) -> None:
        """
        Start the sandbox and return a URL that can be used to connect to it.
        """
        if isinstance(self._url_source, ExternalURLSource):
            self.log.info("start() against an external sandbox: %s", self._url_source)
            return

        env = os.environ.copy()

        # Running dazl's tests against a different Sandbox merely requires the DAML_SDK_VERSION
        # variable be set to a different value
        if self._version is not None:
            env["DAML_SDK_VERSION"] = self._version
            major_version_str, _, _ = self._version.partition(".")
            major_version = int(major_version_str)
        else:
            # TODO: interrogate the local daml binary to figure out what version is defaulted;
            #  assume 1 for now
            major_version = 1

        if self._use_auth or self._use_tls:
            # We're supposed to launch with auth and/or TLS.
            # Both of these flags moved around from Daml 1.x to Daml 2.x,
            # so determine which set of flags to use.
            if self._version is None:
                raise RuntimeError("when tls/auth is on, a version must be specified")

        with self._lock:
            if self._process is not None:
                # this shouldn't ever happen, but we explicitly check for it because running
                # multiple sandbox processes could be very confusing
                raise RuntimeError("we somehow have a process without a URL")

            if self._use_auth or self._use_tls:
                self._certificate = cert_gen(subject_alternative_name="localhost")

                temp_dir = Path(self._exit_stack.enter_context(tempfile.TemporaryDirectory()))
                self._crt_file = temp_dir / "tmp.crt"
                self._key_file = temp_dir / "tmp.key"

                self._crt_file.write_bytes(self._certificate.public_cert)
                self._key_file.write_bytes(self._certificate.private_key)

            options = SandboxOptions(
                port=self._url_source.port,
                ledger_id=self._ledger_id,
                project_root=self._project_root,  # type: ignore
                use_auth=self._use_auth,
                use_tls=self._use_tls,
                cert_file=self._crt_file,
                key_file=self._key_file,
            )
            cmdline = options.daml_cmdline(major_version)

            self.log.info("Launching sandbox: %s", cmdline)

            self._process = subprocess.Popen(
                cmdline,
                env=env,
                cwd=self._project_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
            ProcessLogger(self._process, self.log).start()
            wait_for_process_port(self._process, self._url_source.port, DEFAULT_TIMEOUT)

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
        self._process = None
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


class SandboxOptions:
    port: int
    project_root: Optional[str] = None
    ledger_id: Optional[str] = None
    use_auth: bool = False
    use_tls: bool = False
    cert_file: Optional[Path] = None
    key_file: Optional[Path] = None

    def __init__(
        self,
        *,
        port: int,
        project_root: Optional[str] = None,
        ledger_id: Optional[str] = None,
        use_auth: bool = False,
        use_tls: bool = False,
        cert_file: Optional[Path] = None,
        key_file: Optional[Path] = None,
    ):
        object.__setattr__(self, "port", port)
        object.__setattr__(self, "project_root", project_root)
        object.__setattr__(self, "ledger_id", ledger_id)
        object.__setattr__(self, "use_auth", use_auth)
        object.__setattr__(self, "use_tls", use_tls)
        object.__setattr__(self, "cert_file", cert_file)
        object.__setattr__(self, "key_file", key_file)

    def daml_cmdline(self, __major_version: int) -> "Sequence[str]":
        if __major_version <= 1:
            return self._daml1_cmdline()
        elif __major_version == 2:
            return self._daml2_cmdline()
        else:
            raise ValueError("unknown Daml version")

    def _daml1_cmdline(self) -> Sequence[str]:
        if self.project_root:
            cmdline = ["daml", "start"]
            cmdline.extend(["--start-navigator=no", "--open-browser=no"])
            cmdline.append(f"--sandbox-port={self.port}")
        else:
            cmdline = ["daml", "sandbox", "--port", str(self.port)]

        if self.ledger_id:
            cmdline.extend(["--ledgerid", self.ledger_id])
        if self.use_auth:
            cmdline.extend(["--auth-jwt-rs256-crt", str(self.cert_file)])
        if self.use_tls:
            cmdline.extend(
                ["--crt", str(self.cert_file), "--pem", str(self.key_file), "--client-auth", "none"]
            )

        return cmdline

    def _daml2_cmdline(self) -> Sequence[str]:
        if self.ledger_id and (self.ledger_id != "sandbox"):
            raise ValueError('for Daml 2.x ledgers, ledger ID must be unset, or set to "sandbox"')

        participant_admin_port = find_free_port()
        domain_api_port = find_free_port()
        domain_admin_port = find_free_port()

        participant = "canton.participants.sandbox"
        domain = "canton.domains.local"

        cmdline = ["daml", "sandbox", "--port", str(self.port)]

        # for the time being, we don't use any of Canton's other ports, but it's important that
        # they are bound to random ports to avoid conflicts
        config_options = {
            f"{participant}.admin-api.port": str(participant_admin_port),
            f"{domain}.public-api.port": str(domain_api_port),
            f"{domain}.admin-api.port": str(domain_admin_port),
        }

        if self.use_auth:
            if self.cert_file is None:
                raise ValueError("cert_file must be specified when use_auth=True")

            config_options[f"{participant}.ledger-api.auth-services.0.type"] = "jwt-rs-256-crt"
            config_options[f"{participant}.ledger-api.auth-services.0.certificate"] = str(
                self.cert_file
            )
        if self.use_tls:
            # config_options["canton.participants.sandbox.ledger-api.host"] = "localhost"
            if self.cert_file is None:
                raise ValueError("cert_file must be specified when use_auth=True")
            if self.key_file is None:
                raise ValueError("cert_file must be specified when use_auth=True")

            config_options[f"{participant}.ledger-api.tls.cert-chain-file"] = str(self.cert_file)
            config_options[f"{participant}.ledger-api.tls.private-key-file"] = str(self.key_file)

        if config_options:
            cmdline.append("-C")
            cmdline.append(",".join(f"{key}={value}" for key, value in config_options.items()))

        return cmdline
