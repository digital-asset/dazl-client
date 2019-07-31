# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
:mod:`dazl.client` package
==========================

The :mod:`dazl.client` module a high-level view of the Ledger API in a friendly way.

It provides:

  * a callback-based API for interacting with events on the read-side of the Ledger API
  * convenient methods for creating arbitrary commands on the write-side of the Ledger API.

For a higher-level, more declarative API, see :mod:`dazl.query`.
"""

from . import config
from .api import simple_client, Network, PartyClient, AIOPartyClient, SimplePartyClient
from .runner import run
from ._base_model import ExitCode, LedgerRun
