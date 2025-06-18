# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import argparse
from pathlib import Path

parser = argparse.ArgumentParser("_dazl")
parser.add_argument("-T", "--temp-dir")
parser.add_argument("--log-level", default="info")

subparsers = parser.add_subparsers()

update_parser = subparsers.add_parser("update")
update_parser.add_argument("protopack")

args = parser.parse_args()

from . import _logging

_logging.initialize(args.log_level)

from . import update

update.update(Path(args.protopack))
