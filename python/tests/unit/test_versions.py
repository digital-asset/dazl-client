# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Make sure the various version files are consistent with each other.

In a perfect world, we'd only have one file where this is all declared; that would require more
work, and the cure may very well be worse than the disease though.
"""

from __future__ import annotations

from ast import literal_eval
from configparser import ConfigParser
from pathlib import Path

from dazl import __version__ as library_version

ROOT_DIR = Path(__file__).parent.parent.parent.parent


def test_versions_are_consistent():
    file_version = (ROOT_DIR / "VERSION").read_text().strip()

    config = ConfigParser()
    config.read(ROOT_DIR / "pyproject.toml")
    poetry_section = config["tool.poetry"]
    pyproject_version = literal_eval(poetry_section["version"])

    assert library_version == file_version
    assert library_version == pyproject_version
