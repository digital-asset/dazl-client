# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Simple callbacks manager.
"""

import asyncio
import inspect
import reprlib
from asyncio import ensure_future, Future, get_event_loop
from functools import wraps
from typing import Dict, Optional, List, Callable, Any, Awaitable

from dazl.util.asyncio_util import propagate
from ..util.typing import safe_cast

from .. import LOG


class CallbackManager:
    """
    A manager for callbacks, either normal ones or coroutines.
    """
    def __init__(self, normalize_name_fn=None):
        self._records = dict()  # type: Dict[str, CallbackRecord]
        if normalize_name_fn is not None:
            self._normalize_name = normalize_name_fn

    def add_listener(self, name, callback: Callable[..., Any], filter_fn=None, optional=False) -> 'CallbackDisconnector':
        """
        Add a listener to be invoked whenever ``for_listeners(name)`` is called.

        :param name:
            The name of the listener to attach.
        :param callback:
            A normal function or a coroutine function that returns something that resembles a
            Command.
        :param filter_fn:
            An optional callback that returns `True` or `False` on whether the corresponding
            callback should be invoked. This cannot be a coroutine function.
        :param optional:
            Track whether this callback has actually been invoked or not.
        """
        if not callable(callback):
            raise ValueError('callback must be callable')

        name = self._normalize_name(name)
        record = self._records.get(name)
        if record is None:
            record = CallbackRecord()
            self._records[name] = record
        record.append(callback, filter_fn)
        return CallbackDisconnector(record, callback)

    def remove_listener(self, name, callback) -> bool:
        name = self._normalize_name(name)
        record = self._records.get(name)
        if record is not None:
            try:
                record.remove(callback)
                return True
            except ValueError:
                pass

        return False

    def for_listeners(self, name) -> Callable[..., List['CallbackRecord']]:
        """
        Returns a proxy callback that takes parameters that are passed to each callback as is.
        Any return values are gathered and returned as a list of Future in the same order as the
        original callbacks.
        """
        try:
            hash(name)
        except TypeError:
            LOG.error('Tried to use %s as a key for looking up event handlers.', name)
            raise

        name = self._normalize_name(name)
        cb = self._records.get(name)
        return cb if cb is not None else lambda *_, **__: []

    def rewrite_keys(self, rewrite_fn):
        self._records = {rewrite_fn(key): value for key, value in self._records.items()}

    def keys(self):
        return self._records

    def __repr__(self):
        return f'CallbackManager(keys={reprlib.repr(sorted(self.keys()))})'

    def __bool__(self):
        return bool(self._records)

    _normalize_name = str


class EventHandlerTracker:
    """
    Track the internal state of a callback that is subscribed as an event handler.

    The primary purpose of this is to ensure a callback is never called reentrantly, as it may
    introduce race conditions. The implementation assumes it is being used from ``asyncio`` so
    no locking is required.
    """
    __slots__ = ('original_callback', 'callback', 'pendings')

    def __init__(self, callback: Callable[..., Any], filter_fn=None):
        self.original_callback = callback
        self.callback = _normalize_callback_implementation(callback)
        self.pendings = []  # type: List[_StartableCallable]

    def invoke_eventually(self, *args, **kwargs) -> Awaitable[Any]:
        """
        Either invoke the underlying callback immediately and return a :class:`Future`, or place
        the invocation on an internal queue and invoke the underlying callback as soon as the
        inflight callback is fully invoked.

        :param args: Positional arguments to the callback.
        :param kwargs: Keyword arguments to the callback.
        :return: A Future that is resolved when the underlying callback is invoked.
        """
        sc = _StartableCallable(lambda: self.callback(*args, **kwargs), start=not self.pendings, name=repr(self.callback))
        self.pendings.append(sc)
        sc.add_done_callback(self._maybe_execute_next)
        return sc

    def _maybe_execute_next(self, fut: Future) -> None:
        # get the next callback to be invoked; if the list is empty, then we nothing to do
        try:
            sc = self.pendings.pop(0)
        except IndexError:
            LOG.warning('Received a notification that a Future finished that we don\'t care about')
            return

        if sc._future is not fut:
            LOG.error('Awaitables are being triggered in an incorrect order!')

        if self.pendings:
            self.pendings[0].start()


class _StartableCallable:
    """
    A :class:`Future`-like object that invokes a callback to start a computation at a later point
    in time.
    """
    _asyncio_future_blocking = False

    def __init__(self, cb: Callable[[], Future], start=False, name=None):
        if not callable(cb):
            raise ValueError('cb must be callable')

        if start:
            self._future = cb()
            self._callback = None
        else:
            self._future = get_event_loop().create_future()
            self._callback = cb

        # This is required to be compatible with the interface of a Future.
        self._loop = self._future._loop
        self._name = name or repr(cb)

    def start(self) -> None:
        """
        Actually invoke the underlying function (but only if it hasn't been invoked already).
        """
        cb = self._callback
        if cb is not None:
            self._callback = None
            propagate(from_=ensure_future(cb()), to=self._future)

    def started(self) -> bool:
        return self._callback is None

    def cancelled(self) -> bool:
        return self._future.cancelled()

    def cancel(self) -> bool:
        self._callback = None
        return self._future.cancel()

    def result(self) -> Any:
        return self._future.result()

    def done(self) -> bool:
        return self._future.done()

    def exception(self) -> Optional[BaseException]:
        return self._future.exception()

    def add_done_callback(self, callback: Callable[[Future], Any]) -> None:
        self._future.add_done_callback(callback)

    def __await__(self):
        return self._future.__await__()

    def __repr__(self):
        state = self._future._state if self.started() else 'NOT_STARTED'
        return f'StartableFuture({self._name!r}, state={state})'


def _normalize_callback_implementation(callback: Callable[..., Any]) -> Callable[..., Future]:
    """
    Convert the allowable callback signatures to a function that
    :return:
    """
    if not callable(callback):
        raise ValueError('callback must be callable')

    @wraps(callback)
    def invoke_sync(*args, **kwargs) -> Future:
        loop = asyncio.get_event_loop()

        try:
            result = callback(*args, **kwargs)
            if isinstance(result, asyncio.Future):
                return result
            else:
                future = loop.create_future()
                future.set_result(result)
                return future
        except Exception as ex:
            future = loop.create_future()
            future.set_exception(ex)
            return future

    if inspect.iscoroutinefunction(callback):
        return lambda *args, **kwargs: ensure_future(callback(*args, **kwargs))
    else:
        return invoke_sync


class CallbackRecord:
    """
    Manages the internal list of callbacks for a particular event.
    """

    __slots__ = ('trackers',)

    def __init__(self):
        self.trackers = []  # type: List[EventHandlerTracker]

    def __call__(self, *args, **kwargs) -> List[Awaitable[Any]]:
        return [tracker.invoke_eventually(*args, **kwargs) for tracker in self.trackers]

    def append(self, callback: Callable[..., Any], filter_fn=None) -> None:
        self.trackers.append(EventHandlerTracker(callback, filter_fn))

    def remove(self, callback) -> bool:
        """
        Remove an existing callback from the list of callbacks that will be invoked whenever
        this record is called.
        """
        for i, tracker in enumerate(self.trackers):
            if tracker.original_callback == callback:
                del self.trackers[i]
                return True
        return False


class InflightTracker:

    __slots__ = ('future', 'callback', 'args', 'kwargs')

    @classmethod
    def immediate(cls, callback, args, kwargs):
        tracker = InflightTracker(None, callback, args, kwargs)
        tracker.future = tracker.start()
        return tracker

    @classmethod
    def deferred(cls, callback, args, kwargs):
        future = asyncio.get_event_loop().create_future()
        return InflightTracker(future, callback, args, kwargs)

    def __init__(self, future: Optional[Future], callback, args, kwargs):
        self.future = safe_cast(Future, future) if future is not None else None
        if callable(callback):
            self.callback = callback
        else:
            raise ValueError('callable required here')
        self.args = args
        self.kwargs = kwargs

    def start(self):
        LOG.debug("We're starting a thing...")
        return asyncio.ensure_future(self.callback(*self.args, **self.kwargs))


class CallbackDisconnector:
    __slots__ = ('record', 'callback')

    def __init__(self, record, callback):
        self.record = record
        self.callback = callback

    """
    Returned from ``CallbackManager.add_listener`` as an easy way of disconnecting the specified
    event handler.
    """
    def disconnect(self) -> bool:
        return self.record.remove(self, self.callback)
