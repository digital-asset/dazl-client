# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import operator
from abc import abstractmethod
from asyncio import ensure_future, Future, Queue, gather, get_event_loop, InvalidStateError
from collections import defaultdict
from datetime import timedelta
from enum import Enum
from threading import RLock
from typing import overload, AbstractSet, Any, Awaitable, Callable, Collection, DefaultDict, List, \
    Optional, Sequence, TypeVar

from dataclasses import dataclass, field

from .. import LOG
from ..model.core import Party
from ..model.reading import BaseEvent, EventKey
from ..util.asyncio_util import to_coroutine, LongRunningAwaitable, completed, propagate


DEFAULT_BOT_STOP_TIMEOUT = timedelta(seconds=30)


E = TypeVar('E', bound=BaseEvent)
BotCallback = Callable[[E], Any]
BotFilter = Callable[[E], bool]


class Bot:
    def __init__(self, party: Party):
        self._handlers: DefaultDict[str, List[BotEntry]] = defaultdict(list)
        self._party = party
        self._queue = None
        self._state = BotState.STARTING

    def event_keys(self) -> 'AbstractSet[str]':
        """
        Return the set of keys that event handlers in this bot are configured to handle.
        """
        return frozenset(self._handlers)

    def wants_any_keys(self, keys: 'Collection[str]') -> bool:
        return bool(set(keys).intersection(self._handlers))

    def add_event_handler(self, key: str, handler: 'BotCallback', filter_fn: 'Optional[BotFilter]' = None) -> None:
        """
        Add a new event handler to this bot for the specified event.

        :param key:
            The key of the event (as returned by :meth:`EventKey.from_event`).
        :param filter_fn:
            An optional callback that returns `True` or `False` on whether the corresponding
            callback should be invoked. This cannot be a coroutine function.
        :param handler:
            An event handler to be invoked when an event with the specified key is raised.
        """
        if not isinstance(key, str):
            raise ValueError('expected a string key')
        if not callable(handler):
            raise ValueError('handler must be callable')

        self._handlers[key].append(BotEntry(to_coroutine(handler), filter_fn))

    async def _main(self):
        """
        The "main" coroutine of the bot. Invokes handlers on each event as they come in.
        """
        try:
            self._queue = Queue()
            while self._state not in (BotState.STOPPING, BotState.STOPPED):
                # the main queue contains either events we have not yet processed yet or ``None``
                # markers that merely indicate running status should be "re-checked"
                invocation = await self._queue.get()
                if invocation is not None:
                    try:
                        fut = ensure_future(self._handle_event(invocation.event))
                        propagate(fut, invocation.future)
                        await invocation.future
                    except Exception:
                        LOG.exception(f'An event handler in a bot has thrown an exception! '
                                      f'(offending event: {invocation.event})')
            self._queue = None
        except:
            LOG.exception('A bot thread died abnormally.')

    async def _handle_event(self, event: 'BaseEvent'):
        for event_key in EventKey.from_event(event):
            LOG.debug('Party %s dispatching event %r to its bots...', self.party, event_key)
            handlers = self._handlers.get(event_key)
            if handlers is not None:
                for handler in handlers:
                    try:
                        if handler.filter is None or handler.filter(event):
                            await handler.callback(event)
                    except Exception:
                        LOG.exception('An event handler in a bot has thrown an exception!')

    def notify(self, event: 'BaseEvent') -> 'Awaitable[None]':
        """
        Notifies handler(s) associated with this bot that the given event has occurred. Note that
        this notification is asynchronous: in other words, event handlers will not have processed
        this event by the time this function returns.

        :param event: The event to raise.
        """
        if not isinstance(event, BaseEvent):
            raise ValueError('expected a BaseEvent')

        if self._queue is None:
            raise InvalidStateError('Cannot notify on a bot whose main method is not running')
        bot_invocation = BotInvocation(event)
        self._queue.put_nowait(bot_invocation)
        return bot_invocation.future

    def _dispatch(self, event: 'BaseEvent') -> None:
        for event_key in EventKey.from_event(event):
            self._handlers.get(event_key)

    # <editor-fold desc="State control functions">

    def pause(self) -> None:
        """
        Immediately change the state of this bot to ``PAUSING``, and pause event handler
        invocations. The event handler currently running is allowed to complete. When that is
        completed, the state is changed to ``PAUSED``.
        """
        LOG.info('Pausing the bot thread for party %r...', self.party)
        if self._state not in (BotState.PAUSED, BotState.STOPPING, BotState.STOPPED):
            self._state = BotState.PAUSING
            self._queue.put_nowait(None)

    def resume(self) -> None:
        """
        Immediately change the state of this bot to ``RESUMING`` and process any events that have
        queued up while the bot was paused. When this queue is fully drained, the state is changed
        to ``RUNNING``.
        """
        LOG.info('Resuming the bot thread for party %r...', self.party)
        self._state = BotState.RESUMING
        self._queue.put_nowait(None)

    def stop(self):
        """
        Permanently stop this bot. If you need to be able to "restart" a stopped bot, use
        :meth:`pause` and :meth:`resume` instead.
        """
        LOG.info('Stopping the bot thread for party %r...', self.party)
        self._state = BotState.STOPPING
        self._queue.put_nowait(None)

    # </editor-fold>

    # <editor-fold desc="State query properties/functions">

    @property
    def party(self) -> 'Party':
        """
        Primary party that this bot receives events for (and potentially generates commands for).
        """
        return self._party

    @property
    def state(self) -> 'BotState':
        """
        Current running state of the bot.
        """
        return self._state

    @property
    def running(self) -> bool:
        """
        Return ``True`` if this bot is currently processing events.
        """
        return self._state in (
            BotState.PAUSING, BotState.RESUMING, BotState.RUNNING, BotState.STOPPING)

    # </editor-fold>


class BotCollection(Sequence[Bot]):
    """
    A collection of bots for a party.

    This class is thread-safe except for :meth:`notify` and :meth:`_main` in order to support adding
    event handlers from any thread. The most common use of this is for ``SimplePartyClient``
    instances, where event registration is done from the main thread (from the perspective of the
    caller) and event notifications are done on an asyncio event loop thread (hidden from the
    caller).
    """

    def __init__(self, party: Party):
        self.party = party
        self._bots = []  # type: List[Bot]
        self._fut = None  # type: Optional[LongRunningAwaitable]
        self._lock = RLock()

    def __len__(self) -> int:
        with self._lock:
            return len(self._bots)

    @overload
    @abstractmethod
    def __getitem__(self, i: int) -> Bot: ...

    @overload
    @abstractmethod
    def __getitem__(self, s: slice) -> Sequence[Bot]: ...

    def __getitem__(self, i: int) -> Bot:
        with self._lock:
            return operator.getitem(self._bots, i)

    def __iter__(self):
        with self._lock:
            bots = list(self._bots)
        return iter(bots)

    def add_new(self) -> 'Bot':
        bot = Bot(self.party)
        with self._lock:
            self._bots.append(bot)
            if self._fut is not None:
                # the _main coroutine has already started, so just add this bot's main method to the
                # set of coroutines we track
                # noinspection PyProtectedMember
                self._fut.append(ensure_future(bot._main()))
        return bot

    def add_single(self, key: str, handler: 'BotCallback', filter_fn: 'Optional[BotFilter]' = None) -> 'Bot':
        """
        Convenience method for creating a bot with a single event handler.
        """
        bot = self.add_new()
        bot.add_event_handler(key, handler, filter_fn)
        return bot

    def notify(self, event: 'BaseEvent'):
        futures = []
        try:
            event_keys = EventKey.from_event(event)
            for bot in self._bots:
                if bot.wants_any_keys(event_keys):
                    futures.append(ensure_future(bot.notify(event)))
        except:  # noqa
            # This exception indicates a problem with the scheduling code and not user bot code.
            # Exceptions thrown by user code would be propagated through the Future
            LOG.exception('Failed to notify event for party %s: %r', self.party, event)
            raise

        if len(futures) == 0:
            return completed(None)
        elif len(futures) == 1:
            return futures[0]
        else:
            return gather(*futures, return_exceptions=True)

    async def _main(self):
        if self.party is not None:
            LOG.info('Party %s bots coroutine started.', self.party)
        else:
            LOG.info('Network bots coroutine started.')

        with self._lock:
            self._fut = LongRunningAwaitable()
            # noinspection PyProtectedMember
            self._fut.extend(ensure_future(bot._main()) for bot in self._bots)

        await self._fut

        with self._lock:
            self._fut = None

        if self.party is not None:
            LOG.info('Party %s bots coroutine finished.', self.party)
        else:
            LOG.info('Network bots coroutine finished.')

    def stop_all(self):
        with self._lock:
            # LongRunningAwaitable suspends itself until all futures are completed. It also keeps
            # itself open waiting for the very first future. In the case that no other futures have
            # been added, take this opportunity to feed LongRunningAwaitable a future that
            # immediately resolves, which will have the effect of resolving that overall future
            # if there are no other futures (or the other futures are resolved as well); otherwise
            # this has no effect.
            self._fut.append(completed(None))
            for bot in list(self._bots):
                bot.stop()
            self._bots.clear()


@dataclass(frozen=True)
class BotEntry:
    callback: BotCallback
    filter: Optional[BotFilter] = None


@dataclass(frozen=True)
class BotInvocation:
    event: BaseEvent
    future: Future = field(default_factory=lambda: get_event_loop().create_future())


class BotState(Enum):
    """
    Possible states of a :class:`Bot`.
    """

    STARTING = 'STARTING'  #: The bot is starting (has not yet received the "ready" event).
    PAUSING = 'PAUSING'  #: This bot has been told to pause, but has not yet completed processing events in flight.
    PAUSED = 'PAUSED'  #:
    RESUMING = 'RESUMING'
    RUNNING = 'RUNNING'
    STOPPING = 'STOPPING'
    STOPPED = 'STOPPED'
