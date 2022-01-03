# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module has been relocated to ``dazl.client.ledger``.
"""
import warnings

from ..client.ledger import LedgerMetadata

__all__ = ["LedgerMetadata"]

warnings.warn("dazl.model.ledger is deprecated; use dazl.client.ledger instead", DeprecationWarning)
