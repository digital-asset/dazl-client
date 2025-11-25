# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
import logging
import os
import subprocess
from typing import Any, Generator

import httpx
import pytest

from dazl import testing


def get_installed_daml_versions() -> list[str]:
    try:
        result = subprocess.run(
            ["daml", "version"],
            capture_output=True,
            text=True,
            env={
                **os.environ,
                "PATH": f"{os.path.expanduser('~/.daml/bin')}:{os.environ.get('PATH', '')}",
            },
        )
        versions = []
        in_sdk_section = False
        for line in result.stdout.split("\n"):
            if "SDK versions:" in line:
                in_sdk_section = True
                continue
            if in_sdk_section:
                if line.strip() and not line.startswith(" "):
                    break
                parts = line.strip().split()
                if parts:
                    version = parts[0]
                    if version[0].isdigit():
                        versions.append(version)
        return versions
    except Exception:
        return ["2.10.2"]


INSTALLED_VERSIONS = get_installed_daml_versions()


class SandboxV3Wrapper:
    def __init__(self, sandbox: testing.SandboxLauncher):
        self._sandbox = sandbox
        self._synchronizer_id: str | None = None
        self._wait_for_synchronizers()

    @property
    def url(self) -> str:
        return self._sandbox.json_api_url or self._sandbox.url

    @property
    def synchronizer_id(self) -> str | None:
        return self._synchronizer_id

    def _wait_for_synchronizers(self) -> None:
        async def _async_wait() -> str | None:
            from dazl.api import AuthenticatedClient, get_v2_state_connected_synchronizers

            timeout = httpx.Timeout(10.0, connect=5.0)
            async with AuthenticatedClient(
                base_url=self.url, token="test-token", timeout=timeout
            ) as client:
                max_retries = 30
                for attempt in range(max_retries):
                    try:
                        sync_response = await get_v2_state_connected_synchronizers.asyncio(
                            client=client
                        )
                        if sync_response and hasattr(sync_response, "connected_synchronizers"):
                            from dazl._gen_api.openapi.types import UNSET

                            if (
                                sync_response.connected_synchronizers is not UNSET
                                and sync_response.connected_synchronizers
                            ):
                                synchronizer_id = sync_response.connected_synchronizers[
                                    0
                                ].synchronizer_id
                                logging.info(f"Found synchronizer: {synchronizer_id}")
                                return synchronizer_id
                    except Exception as e:
                        logging.debug(
                            f"Attempt {attempt + 1}/{max_retries} to get synchronizers failed: {e}"
                        )
                    if attempt < max_retries - 1:
                        await asyncio.sleep(1)
                return None

        try:
            self._synchronizer_id = asyncio.run(_async_wait())
        except Exception as e:
            logging.warning(f"Failed to wait for synchronizers: {e}")
            self._synchronizer_id = None

    def __getattr__(self, name: str):
        return getattr(self._sandbox, name)


@pytest.fixture(scope="session")
def sandbox() -> Generator[testing.SandboxLauncher, None, None]:
    version = "2.10.2" if "2.10.2" in INSTALLED_VERSIONS else INSTALLED_VERSIONS[0]
    with testing.sandbox(version=version) as sb:
        yield sb


@pytest.fixture(scope="session")
def sandbox_v2_10() -> Generator[testing.SandboxLauncher, None, None]:
    if "2.10.2" not in INSTALLED_VERSIONS and "2.10.1" not in INSTALLED_VERSIONS:
        pytest.skip("Daml 2.10.x not installed")
    version = "2.10.2" if "2.10.2" in INSTALLED_VERSIONS else "2.10.1"
    with testing.sandbox(version=version) as sb:
        yield sb


@pytest.fixture(scope="session")
def sandbox_v3() -> Generator[SandboxV3Wrapper, None, None]:
    v3_versions = [v for v in INSTALLED_VERSIONS if v.startswith("3.")]
    if not v3_versions:
        pytest.skip("Daml 3.x not installed")
    version = os.environ.get("DAML_V3_VERSION", v3_versions[0])
    with testing.sandbox(version=version) as sb:
        yield SandboxV3Wrapper(sb)


@pytest.fixture(scope="session", params=["2.10", "3.x"])
def sandbox_multi_version(request: Any) -> Generator[testing.SandboxLauncher, None, None]:
    if request.param == "2.10":
        if not any(v.startswith("2.10") for v in INSTALLED_VERSIONS):
            pytest.skip("Daml 2.10.x not installed")
        version = next(v for v in INSTALLED_VERSIONS if v.startswith("2.10"))
    else:
        v3_versions = [v for v in INSTALLED_VERSIONS if v.startswith("3.")]
        if not v3_versions:
            pytest.skip("Daml 3.x not installed")
        version = v3_versions[0]

    with testing.sandbox(version=version) as sb:
        yield sb


@pytest.fixture()
def executor() -> Generator[ThreadPoolExecutor, None, None]:
    with ThreadPoolExecutor(3) as executor:
        yield executor
