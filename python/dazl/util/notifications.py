# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Internal process communications that apply globally. These include signal handlers.
"""

from collections import defaultdict
from threading import RLock
from typing import Any, Callable

from .. import LOG

_HANDLER_LOCK = RLock()
_HANDLERS = defaultdict(list)


def add_handler(key: str, cb: Callable[[Any], None]):
    if key is None:
        raise ValueError("key is required")
    if cb is None:
        raise ValueError("callable is required")

    with _HANDLER_LOCK:
        _HANDLERS[key].append(cb)


def remove_handler(key: str, cb: Callable[[Any], None]):
    if key is None:
        raise ValueError("key is required")
    if cb is None:
        raise ValueError("callable is required")

    with _HANDLER_LOCK:
        _HANDLERS[key].remove(cb)


def invoke_handlers(key: str, arg: Any):
    with _HANDLER_LOCK:
        if key in _HANDLERS:
            handlers = list(_HANDLERS[key])
        else:
            return

    for handler in handlers:
        try:
            handler(arg)
        except:
            LOG.exception()
