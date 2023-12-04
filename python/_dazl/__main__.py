# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import argparse
from pathlib import Path

parser = argparse.ArgumentParser("_dazl")
parser.add_argument("-T", "--temp-dir")
parser.add_argument("--log-level", default="info")

subparsers = parser.add_subparsers()

update_parser = subparsers.add_parser("update")
update_parser.add_argument("daml_sdk_version")
update_parser.add_argument(
    "-C", "--cache-dir", default=str(Path.home() / ".cache" / "dazlbuild" / "download")
)

args = parser.parse_args()

from . import _logging

_logging.initialize(args.log_level)

from . import update

update.update(
    daml_sdk_version=args.daml_sdk_version,
    cache_dir=Path(args.cache_dir),
    temp_dir=Path(args.temp_dir) if args.temp_dir is not None else None,
)
