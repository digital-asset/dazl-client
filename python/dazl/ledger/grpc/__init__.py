# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from ..config import Config
from .conn_aio import Connection

__all__ = ["connect", "Connection"]


def connect(**kwargs):
    """
    Connect to a gRPC Ledger API implementation and return a connection that uses asyncio.
    """
    config = Config.create(**kwargs)
    return Connection(config)
