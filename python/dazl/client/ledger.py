# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Types that describe the behavior of the ledger itself.
"""
from dataclasses import dataclass

from dazl.ledger.pkgloader_aio import PackageLoader

from ..protocols.serializers import Serializer


@dataclass(init=False, frozen=True)
class LedgerMetadata:
    """
    Attributes that are invariant with respect to any party on the ledger.
    """

    ledger_id: str
    package_loader: "PackageLoader"
    serializer: "Serializer"
    protocol_version: str

    def __init__(self, ledger_id, package_loader, serializer, protocol_version):
        object.__setattr__(self, "ledger_id", ledger_id)
        object.__setattr__(self, "package_loader", package_loader)
        object.__setattr__(self, "serializer", serializer)
        object.__setattr__(self, "protocol_version", protocol_version)
