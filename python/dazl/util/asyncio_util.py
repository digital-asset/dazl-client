# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains utilities to help work with ``asyncio``.
"""
from __future__ import annotations

from asyncio import (
    AbstractEventLoop,
    CancelledError,
    Future,
    InvalidStateError,
    Queue as AQueue,
    ensure_future,
    gather,
    get_event_loop,
    get_running_loop,
)
from dataclasses import dataclass
from functools import wraps
from inspect import isawaitable, iscoroutinefunction
from typing import (
    Any,
    Awaitable,
    Callable,
    Generator,
    Generic,
    Iterable,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    cast,
    no_type_check,
)
import warnings

from .. import LOG
from ..prim.datetime import TimeDeltaLike, to_timedelta

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)
U = TypeVar("U")

_PENDING = "PENDING"
_CANCELLED = "CANCELLED"
_FINISHED = "FINISHED"


def await_then(awaitable: Awaitable[T_co], func: Callable[[T_co], U]) -> Awaitable[U]:
    """
    Call a function on the result of an Awaitable, and then return an Awaitable that is resolved
    with that result.

    If the Awaitable is already "done", then the function is invoked immediately with the result
    of that Awaitable and an immediately-completed Future is returned with the result of that
    callback.

    If either the Awaitable or the function throws an exception, that is returned as a failed
    Future. If the Awaitable is cancelled, the returned Future is also cancelled.

    :param awaitable:
    :param func:
    :return:
    """
    try:
        fut = ensure_future(awaitable)
    except TypeError:
        raise TypeError(f"expected a valid awaitable (got {awaitable} instead)")
    if fut.done():
        if fut.cancelled() or fut.exception() is not None:
            return fut  # type: ignore
        else:
            try:
                return completed(func(fut.result()))
            except Exception as ex:
                fut = get_event_loop().create_future()  # type: ignore
                fut.set_exception(ex)
                return fut  # type: ignore
    else:
        g = get_event_loop().create_future()

        def _propagate(_):
            if fut.cancelled():
                g.cancel()
            elif fut.exception() is not None:
                g.set_exception(fut.exception())
            else:
                try:
                    g.set_result(func(fut.result()))
                except Exception as ex2:
                    g.set_exception(ex2)

        fut.add_done_callback(_propagate)
        return g  # type: ignore


@dataclass
class FailedInvocation:
    """Marker used within execute_in_loop to propagate exceptions thrown
    by coro_fn through the result queue in a way that can be easily detected
    by the queue's reader.
    """

    ex: Exception


def execute_in_loop(
    loop: AbstractEventLoop,
    coro_fn: Callable[[], Union[Awaitable[T_co], T_co]],
    timeout: Optional[TimeDeltaLike] = 30.0,
) -> T_co:
    """
    Run a coroutine in a target loop. Exceptions thrown by the coroutine are
    propagated to the caller. Must NOT be called from a coroutine on the same
    loop!

    :param loop:
    :param coro_fn:
    :param timeout: Seconds to wait for the termination of the coroutine.
    :return: The return value from the coroutine.
    """
    from functools import wraps
    from queue import Queue

    q = Queue()  # type: ignore

    def coro_fn_complete(fut):
        LOG.debug("coro_fn_complete: %s", fut)
        if fut.exception() is None:
            q.put_nowait(fut.result())
        else:
            q.put_nowait(FailedInvocation(fut.exception()))

    @wraps(coro_fn)
    def run():
        if iscoroutinefunction(coro_fn):
            fut = ensure_future(coro_fn())
            fut.add_done_callback(lambda _: coro_fn_complete(fut))

        elif isawaitable(coro_fn):
            fut = ensure_future(coro_fn)
            fut.add_done_callback(lambda _: coro_fn_complete(fut))

        elif callable(coro_fn):
            result = coro_fn()
            if isawaitable(result):
                fut = ensure_future(result)
                fut.add_done_callback(lambda _: coro_fn_complete(fut))
            else:
                q.put_nowait(result)
        else:
            raise ValueError("Received an unknown kind of callback")

    loop.call_soon_threadsafe(run)

    timeout_in_seconds = to_timedelta(timeout).total_seconds()
    result = q.get(timeout=timeout_in_seconds)

    if isinstance(result, FailedInvocation):
        raise result.ex

    return result


def completed(value) -> Future:
    fut = get_event_loop().create_future()
    fut.set_result(value)
    return fut


def failed(exception: BaseException) -> Future:
    fut = get_event_loop().create_future()
    fut.set_exception(exception)
    return fut


def propagate(from_: Future, to: Future) -> None:
    """
    Copy the value that ``from_`` is completed with to ``to``, whenever ``from_`` is completed.
    """
    if from_.done():
        copy_result(from_, to)
    else:
        from_.add_done_callback(lambda _: copy_result(from_, to))


def copy_result(from_: Future, to: Future) -> None:
    if not from_.done():
        raise ValueError("from_ must be a completed Future")
    if to.done():
        raise ValueError("to must NOT be a completed Future")

    if from_.cancelled():
        to.cancel()
    else:
        exception = from_.exception()
        if exception is not None:
            to.set_exception(exception)
        else:
            result = from_.result()
            to.set_result(result)


def to_coroutine(callback: Callable[..., Any]) -> Callable[..., Future]:
    """
    Wrap a function or a coroutine, always producing a coroutine.

    In other words, for a function like

    ```
    def double(x):
        return x + x
    ```

    the result of ``to_coroutine(double)`` would be a function that is equivalent to:

    ```
    async def double(x):
        return x + x
    ```

    For functions that are already coroutines, their behavior is unaffected by the wrapper generated
    from this function.

    :param callback:
        The callback to convert to a coroutine.
    :return:
        A coroutine that calls the specified function.
    """
    if not callable(callback):
        raise ValueError("callback must be callable")

    @wraps(callback)
    def invoke_sync(*args, **kwargs) -> Future:
        loop = get_event_loop()

        try:
            result = callback(*args, **kwargs)
            if isinstance(result, Future):
                return result
            else:
                future = loop.create_future()
                future.set_result(result)
                return future
        except Exception as ex:
            future = loop.create_future()
            future.set_exception(ex)
            return future

    if iscoroutinefunction(callback):
        return lambda *args, **kwargs: ensure_future(callback(*args, **kwargs))
    else:
        return invoke_sync


class LongRunningAwaitable:
    """
    An :class:`Awaitable` that "finishes" once all of the futures that have been added to it are
    finished.
    """

    def __init__(self) -> None:
        self._fut = get_event_loop().create_future()
        self._coros = []  # type: List[Awaitable[Any]]

    def append(self, *awaitables: Awaitable[Any]) -> None:
        self.extend(awaitables)

    def extend(self, awaitables: Iterable[Awaitable[Any]]):
        for a in awaitables:
            f = ensure_future(a)
            f.add_done_callback(self._future_finished)
            self._coros.append(f)

    def _future_finished(self, fut):
        self._coros.remove(fut)
        if not self._coros:
            self._fut.set_result(None)

    def __await__(self):
        return self._fut.__await__()


class ServiceQueue(Generic[T]):
    # noinspection PyDeprecation
    def __init__(self) -> None:
        warnings.warn(
            "ServiceQueue is deprecated; there is no planned replacement",
            DeprecationWarning,
            stacklevel=2,
        )
        self._q = []  # type: Union[List[Tuple[T, Future]], AQueue[Tuple[T, Future]]]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            self._service_fut = safe_create_future()
        self._prev_fut = None

    # noinspection PyDeprecation
    def put(self, value: T) -> Awaitable[None]:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            fut = safe_create_future()
        if isinstance(self._q, list):
            self._q.append((value, fut))
        else:
            self._q.put_nowait((value, fut))
        return fut

    def start(self) -> None:
        """
        Allow open asynchronous iterators to begin reading data from the queue. Calling this method
        more than once has no effect.
        """
        if not self._service_fut.done():
            existing_items = cast(list, self._q)  # type: List[Tuple[T, Future]]
            self._q = AQueue()
            for item in existing_items:
                self._q.put_nowait(item)
            self._service_fut.set_result(None)

    def stop(self):
        if not self._service_fut.done():
            raise RuntimeError("Cannot stop an unstarted ServiceQueue")

        loop = get_event_loop()
        fut = loop.create_future()
        self._q.put_nowait((None, fut))
        return fut

    async def next(self) -> Optional[T_co]:
        if not self._service_fut.done():
            await self._service_fut

        if self._prev_fut is not None:
            self._prev_fut.set_result(None)
            self._prev_fut = None

        q = cast(AQueue, self._q)  # type: AQueue[Tuple[T_co, Future]]
        value, fut = await q.get()
        if value is None:
            fut.set_result(None)
            return None
        else:
            self._prev_fut = fut  # type: ignore
            return value

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self.next()
        if value is not None:
            return value
        else:
            raise StopAsyncIteration

    def __bool__(self):
        return len(self) > 0

    def __len__(self):
        if isinstance(self._q, list):
            return len(self._q)
        else:
            return self._q.qsize()

    def __repr__(self):
        return repr(self._q)


class ContextFreeFuture(Awaitable[T_co]):
    """
    An awaitable whose loop is defined at the time of either a :meth:`set_result` call or an
    `await`. These futures are more expensive than normal asyncio futures because they are
    thread-safe.
    """

    _result: Optional[T_co] = None
    _exception: Optional[Exception] = None
    _log_traceback = False
    _asyncio_future_blocking = False

    def __init__(self, *, loop: Optional[AbstractEventLoop] = None):
        """
        Initialize the future.

        The optional ``loop`` argument allows explicitly setting the event loop object used by the
        future. Unlike :class:`Future`, If it is not provided, the future does NOT have a loop set,
        and it is assigned at the time that :class:`set_result` or an `await` expression is called,
        or when :class:`set_loop` is explicitly called.

        You may want to provide a loop ahead of time if you know it, and you're really only
        utilizing this class for its thread-safe nature.

        :param loop: An optional loop to assign to the :class:`ContextFreeFuture`.
        """
        if loop is not None and not isinstance(loop, AbstractEventLoop):
            raise ValueError("The provided loop must be a valid event loop")

        from threading import RLock

        self._lock = RLock()
        self._callbacks = []  # type: List[Callable[[ContextFreeFuture[T_co]], None]]
        self._state = _PENDING
        self.__loop = loop  # type: Optional[AbstractEventLoop]
        self._source_traceback = None

    @property
    def _loop(self):
        """
        Return the current loop.

        Because many functions in the asyncio library directly attempt to access the loop of a
        Future for validation purposes, it is necessary for this property to behave in strange ways.
        If this property is accessed in a context where this is a currently running loop, this
        Future will adopt the current running loop as its own, but ONLY if a loop has not yet been
        set. This will usually do the right thing, but in some cases it may be necessary for callers
        to invoke :meth:`set_loop` directly.
        """
        if self.__loop is None:
            try:
                self.__loop = get_running_loop()
            except RuntimeError:
                pass
        return self.__loop

    def set_loop(self, loop: AbstractEventLoop) -> None:
        """
        Set the loop affinity for this future.

        It is an error to call this function more than once with different values for the loop.

        :param loop:
        """
        with self._lock:
            if self.__loop is None:
                self.__loop = loop
            elif self.__loop is not loop:
                raise InvalidStateError("This future is already associated with a specific loop.")

    def cancel(self) -> bool:
        """
        Cancel this future.
        :return:
        """
        with self._lock:
            self._log_traceback = False
            if self._state != _PENDING:
                return False

            self._state = _CANCELLED
            self._schedule_callbacks()
            return True

    def set_result(self, result):
        """Mark the future done and set its result.

        If the future is already done when this method is called, raises
        InvalidStateError.
        """
        with self._lock:
            if self._state != _PENDING:
                raise InvalidStateError("{}: {!r}".format(self._state, self))
            self._result = result
            self._state = _FINISHED
            self._schedule_callbacks()

    def set_exception(self, exception):
        """Mark the future done and set an exception.

        If the future is already done when this method is called, raises
        InvalidStateError.
        """
        with self._lock:
            if self._state != _PENDING:
                raise InvalidStateError("{}: {!r}".format(self._state, self))
            if isinstance(exception, type):
                exception = exception()
            if type(exception) is StopIteration:
                raise TypeError(
                    "StopIteration interacts badly with generators "
                    "and cannot be raised into a Future"
                )
            self._exception = exception
            self._state = _FINISHED
            self._schedule_callbacks()
            self._log_traceback = True

    def add_done_callback(
        self, fn: "Callable[[ContextFreeFuture[T_co]], None]", context=None
    ) -> None:
        if context is not None:
            # This used to be a warning, but in newer versions of Python a context
            # is sometimes supplied and nothing seems to particularly go wrong by
            # simply doing nothing with this information.
            pass
        with self._lock:
            if self._loop is not None and self._state != _PENDING:
                self._loop.call_soon_threadsafe(fn, self)
            else:
                self._callbacks.append(fn)

    def _schedule_callbacks(self):
        with self._lock:
            if self.__loop is None:
                self.__loop = get_event_loop()

            # clear out the callbacks list and prevent further additions
            local_callbacks = self._callbacks
            self._callbacks = ()

            for fn in local_callbacks:
                self.__loop.call_soon_threadsafe(fn, self)

    def cancelled(self):
        """Return True if the future was cancelled."""
        with self._lock:
            return self._state == _CANCELLED

    # Don't implement running(); see http://bugs.python.org/issue18699

    def done(self):
        """Return True if the future is done.

        Done means either that a result / exception are available, or that the
        future was cancelled.
        """
        with self._lock:
            return self._state != _PENDING

    def result(self):
        """Return the result this future represents.

        If the future has been cancelled, raises CancelledError.  If the
        future's result isn't yet available, raises InvalidStateError.  If
        the future is done and has an exception set, this exception is raised.
        """
        with self._lock:
            if self._state == _CANCELLED:
                raise CancelledError
            if self._state != _FINISHED:
                raise InvalidStateError("Result is not ready.")
            self._log_traceback = False
            if self._exception is not None:
                raise self._exception
            return self._result

    def exception(self):
        """Return the exception that was set on this future.

        The exception (or None if no exception was set) is returned only if
        the future is done.  If the future has been cancelled, raises
        CancelledError.  If the future isn't done yet, raises
        InvalidStateError.
        """
        with self._lock:
            if self._state == _CANCELLED:
                raise CancelledError
            if self._state != _FINISHED:
                raise InvalidStateError("Exception is not set.")
            self._log_traceback = False
            return self._exception

    def __await__(self) -> Generator[Any, None, T_co]:
        if not self.done():
            self._asyncio_future_blocking = True
            yield self  # This tells Task to wait for completion.
        assert self.done(), "yield from wasn't used with future"
        return self.result()  # May raise too.


# noinspection PyDeprecation
def safe_create_future():
    warnings.warn(
        "safe_create_future() is deprecated; there is no planned replacement.",
        DeprecationWarning,
        stacklevel=2,
    )
    try:
        loop = get_running_loop()
    except RuntimeError:
        loop = None
    return loop.create_future() if loop is not None else ContextFreeFuture()


@no_type_check
def named_gather(name: str, *awaitables, return_exceptions=False):
    g = gather(*awaitables, return_exceptions=return_exceptions)
    g.__repr__ = staticmethod(lambda _: f"<Gather {name}>")
    return g


class Signal:
    """
    A simple guard that "wakes" up a coroutine from another coroutine.
    """

    # noinspection PyDeprecation
    def __init__(self):
        warnings.warn(
            "Signal is deprecated; there is no planned replacement",
            DeprecationWarning,
            stacklevel=2,
        )
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            self._fut = safe_create_future()

    def notify_all(self) -> None:
        """
        Schedule a notification to all coroutines that are `wait`ing.
        """
        if self._fut is not None:
            self._fut.set_result(None)
            self._fut = None

    # noinspection PyDeprecation
    def wait(self) -> Awaitable[None]:
        if self._fut is None:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", DeprecationWarning)
                self._fut = safe_create_future()
        return self._fut
