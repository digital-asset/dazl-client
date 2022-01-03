# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Types that describe the behavior of the ledger itself.
"""
from dataclasses import dataclass
from typing import TYPE_CHECKING
import warnings

from ..ledger.aio import PackageLoader
from ..protocols.serializers import Serializer

if TYPE_CHECKING:
    from ..model.types_store import PackageStore

__all__ = ["LedgerMetadata"]


@dataclass(init=False, frozen=True)
class LedgerMetadata:
    """
    Attributes that are invariant with respect to any party on the ledger.
    """

    ledger_id: str
    package_loader: "PackageLoader"
    serializer: "Serializer"
    protocol_version: str
    _store: "PackageStore"

    def __init__(self, ledger_id, package_loader, serializer, protocol_version, store):
        object.__setattr__(self, "ledger_id", ledger_id)
        object.__setattr__(self, "package_loader", package_loader)
        object.__setattr__(self, "serializer", serializer)
        object.__setattr__(self, "protocol_version", protocol_version)
        object.__setattr__(self, "_store", store)

    @property
    def store(self) -> "PackageStore":
        if self._store is None:
            raise Exception("eager_package_fetch is disabled, which disables the PackageStore")

        warnings.warn(
            "PackageStore is deprecated; use SymbolLookup "
            "(accessible from Network.lookup) instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._store
