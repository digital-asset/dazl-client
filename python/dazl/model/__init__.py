# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
:mod:`dazl.model` package
=========================

This module is deprecated. These types have generally moved to :mod:`dazl.client` (for the API
introduced in dazl v5) or :mod:`dazl.protocols` (for the API introduced in dazl v8).

.. automodule:: dazl.model.core
.. automodule:: dazl.model.ledger
.. automodule:: dazl.model.lookup
.. automodule:: dazl.model.network
.. automodule:: dazl.model.reading
.. automodule:: dazl.model.writing

"""

import warnings

from . import core, ledger, lookup, network, reading, writing

__all__ = ["core", "ledger", "lookup", "network", "reading", "writing"]

warnings.warn(
    "dazl.model is deprecated; these types have moved to either dazl.protocols or dazl.client.",
    DeprecationWarning,
)
