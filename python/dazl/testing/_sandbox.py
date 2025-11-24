# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

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
from types import TracebackType
from typing import Any, Mapping, Optional, Sequence, cast

from ..util import ProcessLogger, find_free_port, kill_process_tree, wait_for_process_port
from ._cert import Certificate, cert_gen

if sys.version_info >= (3, 11):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

__all__ = ["DEFAULT_TIMEOUT", "SandboxLauncher"]

DEFAULT_TIMEOUT = timedelta(seconds=90)


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


URLSource: TypeAlias = LocalURLSource | ExternalURLSource


class SandboxLauncher:
    """
    A simple launcher for an in-memory Sandbox.
    """

    _url_source: URLSource

    def __init__(
        self,
        *,
        project_root: Optional[str | os.PathLike] = None,
        version: Optional[str] = None,
        protocol_version: Optional[int] = None,
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

        if version is None:
            version = self._detect_daml_version()

        self._version = version
        self._protocol_version = protocol_version
        self._timeout = timeout
        self._ledger_id = ledger_id
        self._process = None  # type: Optional[subprocess.Popen]

        self._exit_stack = ExitStack()
        self._use_auth = use_auth
        self._use_tls = use_tls

        self._certificate = None  # type: Optional[Certificate]
        self._crt_file = None  # type: Optional[Path]
        self._key_file = None  # type: Optional[Path]
        self._json_api_port = None  # type: Optional[int]

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

    def _detect_daml_version(self) -> Optional[str]:
        try:
            result = subprocess.run(
                ["daml", "version"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                for line in result.stdout.split("\n"):
                    stripped = line.strip()
                    if stripped and stripped[0].isdigit():
                        version = stripped.split()[0]
                        if "(default" in stripped:
                            return version
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        return None

    @property
    def public_cert(self) -> bytes:
        """
        Return the public key corresponding to the private key that was used to start the
        sandbox using TLS.
        """
        if self._certificate is None:
            raise RuntimeError("auth/tls was not enabled, so a public cert was not generated")

        return self._certificate.public_cert

    def sign_token(self, claims: Mapping[str, Any], allow_insecure: bool = False) -> str:
        """
        Sign a token using the private key that the sandbox was launched with.

        :param allow_insecure:
            When set to True, allows tokens to be minted for sandboxes started
            without authentication.
        """
        import jwt

        if self._certificate is None:
            if not allow_insecure:
                raise RuntimeError("this sandbox was not started with auth")

            return jwt.encode(cast(dict[str, Any], claims), "secret", algorithm="HS256")

        return jwt.encode(
            # there is a bug in the jwt typing rules that falsely state the claims are
            # dict[str, Any] when Mapping[str, Any] would actually work
            cast(dict[str, Any], claims),
            self._certificate.private_key.decode("utf-8"),
            algorithm="RS256",
        )

    @property
    def url(self) -> str:
        """
        Return a URL that can be used to connect to this running Sandbox.
        This always returns the gRPC URL for compatibility with admin API calls.
        For Canton 3.x JSON API, use json_api_url property instead.
        """
        return self._url_source.url

    @property
    def json_api_url(self) -> Optional[str]:
        """
        Return the JSON API URL for Canton 3.x+, or None for Canton 2.x.
        """
        if hasattr(self, "_json_api_port") and self._json_api_port:
            return f"http://localhost:{self._json_api_port}"
        return None

    def start(self) -> None:
        """
        Start the sandbox and return a URL that can be used to connect to it.
        """
        if isinstance(self._url_source, ExternalURLSource):
            self.log.info("start() against an external sandbox: %s", self._url_source)
            return

        env = os.environ.copy()

        daml_bin = os.path.expanduser("~/.daml/bin")
        current_path = env.get("PATH", "")
        path_entries = [p for p in current_path.split(":") if p and p != "/.daml/bin"]

        essential_paths = ["/usr/bin", "/bin", "/usr/sbin", "/sbin", "/usr/local/bin"]
        for essential_path in essential_paths:
            if essential_path not in path_entries:
                path_entries.append(essential_path)

        if daml_bin not in path_entries:
            path_entries.insert(0, daml_bin)
        env["PATH"] = ":".join(path_entries)

        # Running dazl's tests against a different Sandbox merely requires the DAML_SDK_VERSION
        # variable be set to a different value
        if self._version is not None:
            env["DAML_SDK_VERSION"] = self._version

        with self._lock:
            if self._process is not None:
                # this shouldn't ever happen, but we explicitly check for it because running
                # multiple sandbox processes could be very confusing
                raise RuntimeError("we somehow have a process without a URL")

            if self._use_auth or self._use_tls:
                self._certificate = cert_gen(subject_alternative_name=["127.0.0.1", "localhost"])

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
                version=self._version,
            )
            cmdline = options.daml2_cmdline()

            self._json_api_port = options.json_api_port

            self.log.info("Launching sandbox: %s", cmdline)

            is_v3_or_later = self._version and (
                self._version.startswith("3.") or self._version.startswith("4.")
            )

            if is_v3_or_later:
                self._process = subprocess.Popen(
                    cmdline,
                    env=env,
                    cwd=self._project_root,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            else:
                self._process = subprocess.Popen(
                    cmdline,
                    env=env,
                    cwd=self._project_root,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True,
                )
                ProcessLogger(self._process, self.log).start()

            if is_v3_or_later:
                wait_for_process_port(
                    self._process,
                    self._url_source.port,
                    DEFAULT_TIMEOUT,
                )
                if self._json_api_port:
                    import time

                    from ..util.io import is_port_alive

                    self.log.info(
                        "Waiting for JSON API port %s to be ready...", self._json_api_port
                    )
                    json_api_timeout = 60
                    for _ in range(json_api_timeout):
                        if is_port_alive(self._json_api_port):
                            self.log.info("JSON API port %s is ready", self._json_api_port)
                            break
                        if self._process.poll() is not None:
                            raise RuntimeError(
                                f"Sandbox process died with code {self._process.returncode}"
                            )
                        time.sleep(1)
                    else:
                        raise TimeoutError(
                            f"JSON API port {self._json_api_port} did not become available within {json_api_timeout} seconds"
                        )
            else:
                wait_for_process_port(
                    self._process,
                    self._url_source.port,
                    DEFAULT_TIMEOUT,
                    participant_admin_port=options.participant_admin_port,
                )

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

    def __enter__(self) -> SandboxLauncher:
        """
        Start the sandbox.
        """
        self.start()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        Stop the sandbox.
        """
        self.stop()

    async def __aenter__(self) -> SandboxLauncher:
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
    participant_admin_port: int
    json_api_port: Optional[int] = None
    project_root: Optional[str] = None
    ledger_id: Optional[str] = None
    protocol_version: Optional[int] = None
    use_auth: bool = False
    use_tls: bool = False
    cert_file: Optional[Path] = None
    key_file: Optional[Path] = None
    version: Optional[str] = None

    def __init__(
        self,
        *,
        port: int,
        participant_admin_port: Optional[int] = None,
        json_api_port: Optional[int] = None,
        project_root: Optional[str] = None,
        ledger_id: Optional[str] = None,
        protocol_version: Optional[int] = None,
        use_auth: bool = False,
        use_tls: bool = False,
        cert_file: Optional[Path] = None,
        key_file: Optional[Path] = None,
        version: Optional[str] = None,
    ):
        object.__setattr__(self, "port", port)
        object.__setattr__(
            self, "participant_admin_port", participant_admin_port or find_free_port()
        )
        object.__setattr__(self, "json_api_port", json_api_port)
        object.__setattr__(self, "project_root", project_root)
        object.__setattr__(self, "ledger_id", ledger_id)
        object.__setattr__(self, "protocol_version", protocol_version)
        object.__setattr__(self, "use_auth", use_auth)
        object.__setattr__(self, "use_tls", use_tls)
        object.__setattr__(self, "cert_file", cert_file)
        object.__setattr__(self, "key_file", key_file)
        object.__setattr__(self, "version", version)

    def daml2_cmdline(self) -> Sequence[str]:
        if self.ledger_id and (self.ledger_id != "sandbox"):
            raise ValueError('for Daml 2.x ledgers, ledger ID must be unset, or set to "sandbox"')

        is_v3_or_later = self.version and (
            self.version.startswith("3.") or self.version.startswith("4.")
        )

        cmdline = ["daml", "sandbox", "--port", str(self.port)]

        if is_v3_or_later:
            if not self.json_api_port:
                object.__setattr__(self, "json_api_port", find_free_port())

            cmdline.extend(["--admin-api-port", str(self.participant_admin_port)])
            cmdline.extend(["--json-api-port", str(self.json_api_port)])
            return cmdline

        domain_api_port = find_free_port()
        domain_admin_port = find_free_port()

        participant = "canton.participants.sandbox"
        domain = "canton.domains.local"

        config_options = {
            f"{participant}.admin-api.port": str(self.participant_admin_port),
            f"{domain}.public-api.port": str(domain_api_port),
            f"{domain}.admin-api.port": str(domain_admin_port),
        }

        if self.protocol_version is not None:
            config_options[f"{domain}.init.domain-parameters.protocol-version"] = str(
                self.protocol_version
            )

        if self.use_auth:
            if self.cert_file is None:
                raise ValueError("cert_file must be specified when use_auth=True")

            config_options[f"{participant}.ledger-api.auth-services.0.type"] = "jwt-rs-256-crt"
            config_options[f"{participant}.ledger-api.auth-services.0.certificate"] = str(
                self.cert_file
            )
        if self.use_tls:
            if self.cert_file is None:
                raise ValueError("cert_file must be specified when use_auth=True")
            if self.key_file is None:
                raise ValueError("key_file must be specified when use_auth=True")

            config_options[f"{participant}.ledger-api.address"] = "localhost"
            config_options[f"{participant}.ledger-api.tls.cert-chain-file"] = str(self.cert_file)
            config_options[f"{participant}.ledger-api.tls.private-key-file"] = str(self.key_file)

        if config_options:
            cmdline.append("-C")
            cmdline.append(",".join(f"{key}={value}" for key, value in config_options.items()))

        return cmdline
