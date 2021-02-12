# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Stub setup file that defers to the contents of pyproject.toml.

This file is only used for editable installs because ``pip`` currently requires it:
     https://discuss.python.org/t/pip-19-1-and-installing-in-editable-mode-with-pyproject-toml/1553

Nothing that resides in pyproject.toml should reside here, and this file should only depend on
pure Python modules. This keeps the setup.py file suitable for use within a ``pip install --editable``
invocation.
"""

from ast import literal_eval
from configparser import ConfigParser
from pathlib import Path
from typing import Collection

from setuptools import setup


def get_setup_args():
    root_path = Path(__file__).parent
    setup_kwargs = dict()

    config = ConfigParser()
    config.read(root_path / "pyproject.toml")

    if "tool.poetry" in config:
        poetry_section = config["tool.poetry"]
        name = setup_kwargs["name"] = parse_value(poetry_section["name"])
        setup_kwargs["version"] = parse_value(poetry_section["version"])
        setup_kwargs["description"] = parse_value(poetry_section["description"])
    else:
        name = None

    if "tool.poetry.dependencies" in config:
        install_requires = []
        for dep, ver in config["tool.poetry.dependencies"].items():
            if dep != name and dep != "python":
                install_requires.append(f"{dep}")
        if install_requires:
            setup_kwargs["install_requires"] = install_requires

    if "tool.poetry.scripts" in config:
        entry_points = {"console_scripts": []}
        for key, entrypoint in config["tool.poetry.scripts"].items():
            entry_points["console_scripts"].append(f"{key}={parse_value(entrypoint)}")
        setup_kwargs["entry_points"] = entry_points

    setup_kwargs["packages"] = _find_packages(root_path)

    return setup_kwargs


def _find_packages(path: Path) -> "Collection[str]":
    packages = []
    for proposed_package in path.glob("**/__init__.py"):
        p = proposed_package.relative_to(path)
        if not str(p).startswith("."):
            packages.append(str(p.parent))
    return packages


def parse_value(v):
    return literal_eval(v)


setup(**get_setup_args())
