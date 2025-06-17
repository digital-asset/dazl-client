# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from pathlib import Path

from . import codegen

repo_root = Path(__file__).parent.parent.parent

logger = logging.getLogger("_dazl")

__all__ = ["update"]


def update(proto_pack: Path) -> None:
    """
    Update the parts of the dazl codebase that are code-generated.
    """
    python_gen_dir = repo_root / "python" / "dazl" / "_gen"
    go_gen_dir = repo_root / "go" / "api"

    # now generate our various files
    codegen.python_files(from_=proto_pack, to=python_gen_dir)
    codegen.go_files(from_=proto_pack, to=go_gen_dir)
