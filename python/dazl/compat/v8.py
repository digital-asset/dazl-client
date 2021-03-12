# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains symbols to aid in a gradual migration of v5-v7 code to v8. These symbols will
be marked as deprecated in v8, and be removed in v9.
"""
from typing import TypeVar

from ..protocols.core import AEventHandler, ArchiveEvent, CreateEvent, InitEvent, ReadyEvent

__all__ = ["ConnectionReuseWarning", "CallbackReturnValueWarning", "NotSupportedError"]

InitFn = TypeVar("InitFn", bound=AEventHandler[InitEvent])
ReadyFn = TypeVar("ReadyFn", bound=AEventHandler[ReadyEvent])
CreateFn = TypeVar("CreateFn", bound=AEventHandler[CreateEvent])
ArchiveFn = TypeVar("ArchiveFn", bound=AEventHandler[ArchiveEvent])
DEFAULT_TIMEOUT_SECONDS = 30


class NotSupportedError(Exception):
    """
    Error raised when calling an API that exists on :class:`Network` but is not supported on
    :class:`ConnectionFactory`.
    """


class ConnectionReuseWarning(DeprecationWarning):
    """
    Warning raised when Network.aio_party or Network.simple_party are called more than once with
    the same party literal. Connection sharing will no longer explicitly be provided by dazl in the
    v8 API; any connection sharing must be instead managed by your application.
    """


class CallbackReturnValueWarning(DeprecationWarning):
    """
    Warning raised when a callback returns a value instead of directly submitting a command itself.
    This style of callback is not supported by the dazl v8 API.
    """
