# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from pathlib import Path

import dazl

python_dir = Path(dazl.__file__).absolute().parent.parent
root_dir = python_dir.parent


def test_structure():
    """
    Some basic structure and style checks that are not covered by black and isort.
    """
    with (root_dir / "COPYRIGHT").open("r", encoding="utf-8") as f:
        required_header = "".join(f"# {line.strip()}\n" for line in f.readlines())

    logging.info("Required header:")
    for line in required_header.splitlines():
        logging.info(line)

    file_count = 0
    violations = 0

    py_files = list(python_dir.rglob("*.py"))
    pyi_files = list(python_dir.rglob("*.py"))

    for path in (*py_files, *pyi_files):
        text = path.read_text()
        if not text.startswith(required_header):
            logging.error("File %s is missing the required copyright header!", path)
            violations += 1

        file_count += 1

    logging.info("Scanned %d file(s).", file_count)
    assert violations == 0
