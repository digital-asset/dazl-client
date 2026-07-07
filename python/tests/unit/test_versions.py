# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Make sure the various version files are consistent with each other.

In a perfect world, we'd only have one file where this is all declared; that would require more
work, and the cure may very well be worse than the disease though.
"""

from __future__ import annotations

from pathlib import Path
import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

from dazl import __version__ as library_version

ROOT_DIR = Path(__file__).parent.parent.parent.parent


def test_versions_are_consistent() -> None:
    file_version = (ROOT_DIR / "VERSION").read_text().strip()

    with (ROOT_DIR / "pyproject.toml").open("rb") as f:
        config = tomllib.load(f)
    pyproject_version = config["project"]["version"]

    assert library_version == file_version
    assert library_version == pyproject_version
