# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
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
.. automodule:: dazl.model.types
.. automodule:: dazl.model.types_store
.. automodule:: dazl.model.writing

"""

import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    from . import core, ledger, lookup, network, reading, types, writing

__all__ = ["core", "ledger", "lookup", "network", "reading", "writing"]

warnings.warn(
    "dazl.model is deprecated; these types have moved to either dazl.ledger or dazl.client.",
    DeprecationWarning,
    stacklevel=2,
)
