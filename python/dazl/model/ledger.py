# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Types that describe the behavior of the ledger itself.
"""

from dataclasses import dataclass
from typing import Any

from .writing import Serializer
from ..client.pkg_cache import PackageCache


@dataclass(frozen=True)
class LedgerMetadata:
    """
    Attributes that are invariant with respect to any party on the ledger.
    """
    ledger_id: str
    pkg_cache: 'PackageCache'
    serializer: 'Serializer[Any, Any]'
    protocol_version: str
