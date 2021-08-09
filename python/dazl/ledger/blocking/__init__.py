# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
:mod:`dazl.ledger.blocking`
===========================

Thread-blocking protocols and base classes for connecting to a Daml ledger.

.. autoclass:: Connection()

.. autoclass:: QueryStream()
"""

import sys
from typing import Any

from .. import Connection as _Connection, QueryStream as _QueryStream
from .._stream import ARCHIVE_EVENT, BOUNDARY, CREATE_EVENT, Callbacks, check_return_type
from ..api_types import ArchiveEvent, Boundary, CreateEvent

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable


__all__ = ["PackageService", "Connection", "QueryStream", "PackageLoader"]


class PackageService(Protocol):
    """
    Protocol that describe a service that provides package information. The :class:`Connection`
    protocol extends this interface.
    """

    async def get_package(self, __package_id) -> bytes:
        raise NotImplementedError

    async def list_package_ids(self):
        raise NotImplementedError


@runtime_checkable
class Connection(_Connection, Protocol):
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
class QueryStream(_QueryStream, Protocol):
    """
    A blocking stream of offsets and events from a Daml ledger.
    """

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError


class QueryStreamBase(Callbacks, QueryStream):
    """
    Base implementation of the :class:`QueryStream` protocol for blocking connections.
    """

    def __enter__(self):
        """
        Prepare the stream.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the stream.
        """
        self.close()

    def close(self) -> None:
        """
        Close and dispose of any resources used by this stream.
        """

    def run(self) -> None:
        """
        "Runs" the stream. This can be called as an alternative to :meth:`items` when using
        callback-based APIs.
        """
        for _ in self:
            pass

    def creates(self):
        """
        Return a stream of :class:`CreateEvent`s. This will include the contracts of the
        Active Contract Set, as well as create events over subsequent transactions.
        """
        for item in self.items():
            if isinstance(item, CreateEvent):
                yield item

    def events(self):
        """
        Return a stream of :class:`CreateEvent`s. This will include the contracts of the
        Active Contract Set, as well as create and archive events over subsequent transactions.
        """
        for item in self.items():
            if isinstance(item, CreateEvent) or isinstance(item, ArchiveEvent):
                yield item

    def items(self):
        """
        Must be overridden by subclasses to provide a stream of events. The implementation is
        expected to call :meth:`_emit_create` and :meth:`_emit_archive` for every encountered event.
        """
        raise NotImplementedError

    def __aiter__(self):
        """
        Returns :meth:`items`, which includes all create and archive events, and boundaries.
        """
        return self.items()

    def _emit(self, name: str, obj: "Any"):
        for cb in self._callbacks[name]:
            result = cb(obj)

            check_return_type(result)

    def _emit_create(self, event: "CreateEvent"):
        self._emit(CREATE_EVENT, event)

    def _emit_archive(self, event: "ArchiveEvent"):
        self._emit(ARCHIVE_EVENT, event)

    def _emit_boundary(self, event: "Boundary"):
        self._emit(BOUNDARY, event)


# Imports internal to this package are at the bottom of the file to avoid circular dependencies
from .pkgloader import PackageLoader  # noqa
