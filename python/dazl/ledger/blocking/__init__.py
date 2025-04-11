# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
:mod:`dazl.ledger.blocking`
===========================

Thread-blocking protocols and base classes for connecting to a Daml ledger.

.. autoclass:: Connection()

.. autoclass:: QueryStream()
"""

from __future__ import annotations

from typing import Optional, Protocol, runtime_checkable

__all__ = ["PackageService", "Connection", "QueryStream"]

from ...damlast.daml_lf_1 import PackageRef
from ...prim import TimeDeltaLike
from ..auth import TokenOrTokenProvider


class PackageService(Protocol):
    """
    Protocol that describe a service that provides package information. The :class:`Connection`
    protocol extends this interface.
    """

    def get_package(
        self,
        package_id: PackageRef,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> bytes:
        raise NotImplementedError

    def list_package_ids(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ):
        raise NotImplementedError


@runtime_checkable
class Connection(Protocol):
    """
    Protocol that describes the interface for a blocking connection to a Daml ledger. The methods of
    an implementation should be thread-safe, with the exception of :meth:`open` and :meth:`close`.

    Since ``dazl`` activity is typically dominated by I/O, using a blocking :class:`Connection` with
    multiple threads is usually more expensive than using connections. You should consider
    using the asyncio variant of this API (:class:`dazl.ledger.aio.Connection`) instead.
    """

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


@runtime_checkable
class QueryStream(Protocol):
    """
    A blocking stream of offsets and events from a Daml ledger.
    """

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
