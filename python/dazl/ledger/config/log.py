# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from logging import Logger
from typing import Optional, TypedDict

__all__ = ["LoggerArgs"]


class LoggerArgs(TypedDict, total=False):
    logger: Optional[Logger]
