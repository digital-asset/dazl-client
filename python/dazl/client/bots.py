# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import inspect
import operator
from abc import abstractmethod
from asyncio import ensure_future, Future, gather, get_event_loop, InvalidStateError
from collections import defaultdict
from dataclasses import dataclass, field, replace
from datetime import timedelta
from enum import auto, Enum
from functools import wraps
from threading import RLock
from typing import overload, AbstractSet, Any, Awaitable, Callable, Collection, DefaultDict, List, \
    Optional, Sequence, TypeVar, Union, TYPE_CHECKING
from uuid import uuid4

from .. import LOG
from ..model.core import Party, SourceLocation
from ..model.reading import BaseEvent, EventKey
from ..model.writing import Command, CommandBuilder
from ..util.asyncio_util import LongRunningAwaitable, completed, propagate, failed, Signal

if TYPE_CHECKING:
    from .api import PartyClient

DEFAULT_BOT_STOP_TIMEOUT = timedelta(seconds=30)


E = TypeVar('E', bound=BaseEvent)
BotCallback = Callable[[E], Any]
BotFilter = Callable[[E], bool]


class _BotRunLevel(Enum):
    CONTINUE = auto()
    SUSPEND = auto()
    TERMINATE = auto()


class Bot:
    def __init__(self, party_client: 'Optional[PartyClient]', name: str):
        self._handlers: DefaultDict[str, List[BotEntry]] = defaultdict(list)
        self._party_client = party_client
        self._id = uuid4().hex
        self._name = name
        self._queue = []
        self._signal = None  # type: Optional[Signal]
        self._idle = True
        self._run_level = _BotRunLevel.CONTINUE

    def event_keys(self) -> 'AbstractSet[str]':
        """
        Return the set of keys that event handlers in this bot are configured to handle.
        """
        return frozenset(self._handlers)

    def wants_any_keys(self, keys: 'Collection[str]') -> bool:
        return bool(set(keys).intersection(self._handlers))

    def add_event_handler(
            self, keys: 'Union[str, Collection[str]]', handler: 'BotCallback',
            filter_fn: 'Optional[BotFilter]' = None) -> None:
        """
        Add a new event handler to this bot for the specified event.

        :param keys:
            The key(s) of the event (as returned by :meth:`EventKey.from_event`).
        :param filter_fn:
            An optional callback that returns `True` or `False` on whether the corresponding
            callback should be invoked. This cannot be a coroutine function.
        :param handler:
            An event handler to be invoked when an event with the specified key is raised.
        """
        if isinstance(keys, str):
            keys = [keys]
        else:
            keys = tuple(keys)
            for key in keys:
                if not isinstance(key, str):
                    raise ValueError('expected a string key')
        if not callable(handler):
            raise ValueError('handler must be callable')

        # noinspection PyBroadException
        try:
            source_file = inspect.getsourcefile(inspect.unwrap(handler))
            lines, start_line = inspect.getsourcelines(handler)
            end_line = start_line + len(lines)
            source_loc = SourceLocation(source_file, start_line, end_line)
        except Exception:  # noqa
            LOG.warning('Could not compute original source information for %r', handler, exc_info=True)
            source_loc = None

        if self._party_client is not None:
            # noinspection PyProtectedMember
            impl = self._party_client._impl
            handler = wrap_as_command_submission(impl.write_commands, handler, filter_fn)

        for key in keys:
            self._handlers[key].append(BotEntry(key, handler, filter_fn, source_loc))

    def ledger_created(self, template: Any):
        def _register_created(fn):
            self.add_event_handler(EventKey.contract_created(True, template), fn)
        return _register_created

    async def _main(self):
        """
        The "main" coroutine of the bot. Invokes handlers on each event as they come in.
        """
        # noinspection PyBroadException
        try:
            self._signal = Signal()
            while self._run_level != _BotRunLevel.TERMINATE:
                # the main queue contains either events we have not yet processed yet or ``None``
                # markers that merely indicate running status should be "re-checked"
                self._idle = False
                while self._queue:
                    invocation = self._queue.pop(0)
                    # noinspection PyBroadException
                    try:
                        fut = ensure_future(self._handle_event(invocation.event))
                        propagate(fut, invocation.future)
                        await invocation.future
                    except Exception:  # noqa
                        LOG.exception(f'An event handler in a bot has thrown an exception! '
                                      f'(offending event: {invocation.event})')
                self._idle = True
                await self._signal.wait()
            self._signal = None
        except Exception:  # noqa
            LOG.exception('A bot thread died abnormally.')

    async def _handle_event(self, event: 'BaseEvent') -> None:
        """
        Process an event, mostly by calling appropriate callbacks.

        :param event: The event to process.
        """
        # The _PartyClientImpl and Bot classes are the ones raising events, but to the user, they
        # registered from the perspective of a client with a certain thread affinity. Replace the
        # "source" of the event with the client that the user originally used.
        if self._party_client is not None:
            new_event = replace(event, client=self._party_client)
        else:
            new_event = event

        for event_key in EventKey.from_event(new_event):
            LOG.debug('Party %s dispatching event %r to its bots...', self.party, event_key)
            handlers = self._handlers.get(event_key)
            if handlers is not None:
                for handler in handlers:
                    # noinspection PyBroadException
                    try:
                        if handler.filter is None or handler.filter(new_event):
                            await handler.callback(new_event)
                    except Exception:  # noqa
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
        self._queue.append(bot_invocation)
        if self._signal is not None:
            self._signal.notify_all()
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
        self._run_level = _BotRunLevel.SUSPEND
        if self._signal is not None:
            self._signal.notify_all()

    def resume(self) -> None:
        """
        Immediately change the state of this bot to ``RESUMING`` and process any events that have
        queued up while the bot was paused. When this queue is fully drained, the state is changed
        to ``RUNNING``.
        """
        LOG.info('Resuming the bot thread for party %r...', self.party)
        self._run_level = _BotRunLevel.CONTINUE
        if self._signal is not None:
            self._signal.notify_all()

    def stop(self):
        """
        Permanently stop this bot. If you need to be able to "restart" a stopped bot, use
        :meth:`pause` and :meth:`resume` instead.
        """
        LOG.info('Stopping the bot thread for party %r...', self.party)
        self._run_level = _BotRunLevel.TERMINATE
        if self._signal is not None:
            self._signal.notify_all()

    # </editor-fold>

    # <editor-fold desc="State query properties/functions">

    @property
    def id(self) -> str:
        """
        The ID of this bot, generated at runtime.
        """
        return self._id

    @property
    def name(self):
        """
        The name of this bot. Defaults to the name of the original event handler if unspecified.
        """
        return self._name

    @property
    def party(self) -> 'Party':
        """
        Primary party that this bot receives events for (and potentially generates commands for).
        """
        return self._party_client.party if self._party_client is not None else None

    def entries(self) -> 'Sequence[BotEntry]':
        """
        The collection of individual event handlers in a bot, in the order that they will be
        executed.
        """
        return tuple(entry for collection in self._handlers.values() for entry in collection)

    @property
    def state(self) -> 'BotState':
        """
        Current running state of the bot.
        """
        if self._run_level == _BotRunLevel.CONTINUE:
            return BotState.RUNNING if self._signal is not None else BotState.STARTING
        elif self._run_level == _BotRunLevel.TERMINATE:
            return BotState.STOPPED if self._idle else BotState.STOPPING
        elif self._run_level == _BotRunLevel.SUSPEND:
            return BotState.PAUSED if self._idle else BotState.PAUSING

    @property
    def running(self) -> bool:
        """
        Return ``True`` if this bot is currently processing events.
        """
        return self._signal is not None and \
            (self._run_level == _BotRunLevel.CONTINUE or not self._idle)

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

    def __init__(self, party: 'Optional[Party]'):
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

    def add_new(self, name: str, party_client: 'Optional[PartyClient]' = None) -> 'Bot':
        bot = Bot(party_client, name)
        with self._lock:
            self._bots.append(bot)
            if self._fut is not None:
                # the _main coroutine has already started, so just add this bot's main method to the
                # set of coroutines we track
                # noinspection PyProtectedMember
                self._fut.append(ensure_future(bot._main()))
        return bot

    def add_single(
            self,
            keys: 'Union[str, Sequence[str]]',
            handler: 'BotCallback',
            filter_fn: 'Optional[BotFilter]' = None,
            name: 'Optional[str]' = None,
            party_client: 'Optional[PartyClient]' = None) -> 'Bot':
        """
        Convenience method for creating a bot with a single event handler.
        """
        if name is None:
            # by default, the name of a single-event-handler bot is simply the name of the passed
            # in function
            name = handler.__name__
        if isinstance(keys, str):
            keys = [keys]

        bot = self.add_new(name, party_client)
        for key in keys:
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
    event_key: str
    callback: BotCallback
    filter: Optional[BotFilter] = None
    source_location: Optional[SourceLocation] = None


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


# noinspection PyShadowingBuiltins
def wrap_as_command_submission(submit_fn, callback, filter) \
        -> Callable[[BaseEvent], Awaitable[Any]]:
    """
    Normalize a callback to something that takes a single contract ID and contract data, and
    return an awaitable that is resolved when the underlying command has been fully submitted.
    """
    import inspect

    @wraps(callback)
    def implementation(*args, **kwargs):
        if filter is not None and not filter(*args, **kwargs):
            return completed(None)

        try:
            ret = callback(*args, **kwargs)
        except BaseException as exception:
            LOG.exception('The callback %r threw an exception!', callback)
            return failed(exception)

        if ret is None:
            return completed(None)
        elif isinstance(ret, (CommandBuilder, Command, list, tuple)):
            try:
                ret_fut = submit_fn(ret)
            except BaseException as exception:
                LOG.exception('The callback %r returned commands that could not be submitted! (%s)',
                              callback, ret)
                return failed(exception)
            return ret_fut
        elif inspect.isawaitable(ret):
            # the user-provided callback returned an Awaitable
            cmd_fut = ensure_future(ret)
            if cmd_fut.done():
                if cmd_fut.cancelled() or cmd_fut.exception() is not None:
                    # a cancelled or failed user-provided callback Future is the same as the
                    # command submission itself failing
                    return cmd_fut

                # functionally equivalent to the non-Awaitable case if the Awaitable has already
                # completed
                return submit_fn(cmd_fut.result())
            else:
                # create `fut`, which we'll give to the user; wait for `cmd_fut` to finish, then
                # take the result of that awaitable and try to submit a command with that result
                fut = get_event_loop().create_future()

                def cmd_future_finished(_):
                    ret = cmd_fut.result()
                    if ret is None:
                        fut.set_result(None)
                    elif isinstance(ret, (CommandBuilder, Command, list, tuple)):
                        propagate(ensure_future(submit_fn(ret)), fut)
                    elif inspect.isawaitable(ret):
                        LOG.error('A callback cannot return an Awaitable of an Awaitable')
                        raise InvalidStateError(
                            'A callback cannot return an Awaitable of an Awaitable')

                cmd_fut.add_done_callback(cmd_future_finished)

                return fut
        else:
            LOG.error('the callback %r returned a value of an unexpected type: %s', callback, ret)
            raise ValueError('unexpected return type from a callback')

    return implementation
