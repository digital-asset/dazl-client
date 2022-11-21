# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import asyncio
import concurrent.futures
from typing import TYPE_CHECKING, Callable, Optional, TypeVar

if TYPE_CHECKING:
    from . import Connection


Fn = TypeVar("Fn", bound=Callable)

__all__ = [
    "CallbackReturnWarning",
    "ProtocolWarning",
    "ConnectionClosedError",
    "_rewrite_exceptions",
    "_translate_exceptions",
    "_allow_cancel",
]


class CallbackReturnWarning(Warning):
    """
    Raised when a user callback on a stream returns a value. These objects have no meaning and are
    ignored by dazl.

    This warning is raised primarily because older versions interpreted returning commands
    from a callback as a request to send commands to the underlying ledger, and this is not
    supported in newer APIs.
    """


class ProtocolWarning(Warning):
    """
    Warnings that are raised when dazl detects incompatibilities between the Ledger API server-side
    implementation and dazl.
    """


class ConnectionClosedError(Exception):
    """
    Raised when trying to call methods on a closed :class:`dazl.ledger.Connection`.
    """


def _rewrite_exceptions(fn: Fn) -> Fn:
    """
    Translate and re-raised internal gRPC exceptions to dazl's own error hierarchy. This
    decorator expects to wrap methods off of :class:`dazl.ledger.Connection` objects, or
    objects with a ``conn`` property (usually QueryStreams).

    Unfortunately gRPC does not have a standardized set of well-defined exceptions.
    Additionally the async API and the non-async API throw exceptions from different class
    hierarchies!
    """

    # Unfortunately the error types raised by the gRPC async API are not actually public
    # symbols...if a new version of the gRPC library changes this, then we'll fall back
    # to handling all Exceptions until this code is modified to handle this case.
    try:
        # noinspection PyProtectedMember
        from grpc._cython.cygrpc import UsageError  # type: ignore
    except ImportError:
        # noinspection PyPep8Naming
        UsageError = Exception

    def _rewrite_exception(self, *args, **kwargs):
        try:
            return fn(self, *args, **kwargs)
        except UsageError:
            conn = getattr(self, "conn", self)
            if conn.is_closed:
                raise ConnectionClosedError()
            else:
                raise

    return _rewrite_exception  # type: ignore


class ExceptionTranslator:
    def __init__(self, conn: "Connection"):
        self.conn = conn

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None and self.conn.is_closed:
            raise ConnectionClosedError() from exc_val

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None and self.conn.is_closed:
            raise ConnectionClosedError() from exc_val


class AllowCancellation:
    def __init__(self, allow: Callable[[], bool]):
        self.allow = allow

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> Optional[bool]:
        if exc_val is not None:
            # These two exceptions are actually the same type under the hood--however, nothing
            # that I can find in the Python docs suggest that this HAS to be the case. Either
            # way, suppress cancellation errors that happen when we are closed, because .
            return self.allow() and (
                exc_type is asyncio.CancelledError or exc_type is concurrent.futures.CancelledError
            )

        return None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> Optional[bool]:
        if exc_val is not None:
            # These two exceptions are actually the same type under the hood--however, nothing
            # that I can find in the Python docs suggest that this HAS to be the case. Either
            # way, suppress cancellation errors that happen when we are closed, because .
            return self.allow() and (
                exc_type is asyncio.CancelledError or exc_type is concurrent.futures.CancelledError
            )

        return None


def _translate_exceptions(conn: "Connection") -> ExceptionTranslator:
    """
    Return an (async) context manager that translates exceptions thrown from low-level gRPC calls
    to high-level dazl exceptions.
    """
    return ExceptionTranslator(conn)


def _allow_cancel(allow: Callable[[], bool]) -> AllowCancellation:
    return AllowCancellation(allow)
