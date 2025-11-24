# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from concurrent.futures.thread import ThreadPoolExecutor
import os
import subprocess
from typing import Any, Generator

from dazl import testing
import pytest


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
def sandbox_v3() -> Generator[testing.SandboxLauncher, None, None]:
    v3_versions = [v for v in INSTALLED_VERSIONS if v.startswith("3.")]
    if not v3_versions:
        pytest.skip("Daml 3.x not installed")
    version = os.environ.get("DAML_V3_VERSION", v3_versions[0])
    with testing.sandbox(version=version) as sb:
        yield sb


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
