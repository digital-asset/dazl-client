# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Tuple

__all__ = ["get_root_name"]


def get_root_name(s: str, /) -> Tuple[str, str]:
    for suffix in ("_pb2_grpc.py", "_pb2.pyi", "_pb2.py", ".proto", "_grpc.pb.go", ".pb.go"):
        if s.endswith(suffix):
            return s[: -len(suffix)], s[-len(suffix) :]
    raise ValueError(f"unknown file name pattern: {s}")
