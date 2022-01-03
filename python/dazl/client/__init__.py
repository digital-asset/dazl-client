# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
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
from ._base_model import (
    CREATE_IF_MISSING,
    EXCEPTION_IF_MISSING,
    NONE_IF_MISSING,
    ExitCode,
    LedgerRun,
)
from ._network_client_impl import _NetworkImpl
from ._party_client_impl import _PartyClientImpl
from .api import (
    AIOPartyClient,
    Network,
    PartyClient,
    SimplePartyClient,
    async_network,
    simple_client,
)
from .bots import Bot, BotCollection, BotEntry
from .runner import run
