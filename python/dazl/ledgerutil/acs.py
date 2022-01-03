# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import asyncio
from asyncio import CancelledError, Future, InvalidStateError, ensure_future, get_event_loop, sleep
from collections.abc import Mapping as MappingBase
import sys
from types import MappingProxyType
from typing import (
    AsyncIterator,
    Awaitable,
    Collection,
    Dict,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)
import warnings

from ..damlast.daml_lf_1 import TypeConName
from ..damlast.lookup import matching_normalizations, normalize
from ..ledger import ArchiveEvent, Boundary, CreateEvent
from ..ledger.aio import Connection
from ..ledger.errors import ProtocolWarning
from ..prim import ContractData, ContractId
from ..query import ContractMatch, Queries, is_match

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ["ACS", "Snapshot", "snapshots"]


T = TypeVar("T")

# Literal types are a bit of a pain to declare, but we _do_ get type safety at the value level
# with all this boilerplate.
NOT_STARTED: Literal["NOT_STARTED"] = "NOT_STARTED"
CONNECTING: Literal["CONNECTING"] = "CONNECTING"
RUNNING: Literal["RUNNING"] = "RUNNING"
RECONNECTING: Literal["RECONNECTING"] = "RECONNECTING"
STOPPED: Literal["STOPPED"] = "STOPPED"
State = Literal["NOT_STARTED", "CONNECTING", "RUNNING", "RECONNECTING", "STOPPED"]


class ACS:
    """
    An accumulation of active contracts up to a certain point in time over a provided stream.

    This class is meant to represent a _local_ in-memory view of an active contract set. It is _not_
    a direct wrapper over the API; it is merely offered as a simple utility class to avoid
    repetitive code that looks like this:

    .. code-block: python

        class MyService:
            def __init__(self, conn):
                self._conn = conn
                self._widgets = dict()

            async def run(self):
                async with self._conn.stream("WidgetMod:Widget") as stream:
                    async for ev in stream.events():
                        if isinstance(ev, CreateEvent):
                            self._widgets[ev.contract_id] = ev.payload
                        elif isinstance(ev, ArchiveEvent):
                            self._widgets.pop(ev.contract_id)

            def widget_json(self, widget_id: str):
                for cdata in self._widgets.values():
                    if cdata['id'] == widget_id:
                        return cdata
                return None

    With the ACS helper class:

    .. code-block: python

        class MyService:
            def __init__(self, conn):
                self._conn = conn
                self._acs = ACS(conn, {"WidgetMod:Widget": {}})

            async def run(self):
                await self._acs.run()

            def widget_json(self, widget_id: str):
                snapshot = await self._acs.read()
                return snapshot.earliest_contract("WidgetMod:Widget", {"id": widget_id})

    """

    def __init__(self, conn: Connection, queries: Queries):
        self._conn = conn
        self._queries = queries
        self._snapshot = None  # type: Optional[Snapshot]
        self._snapshot_fut = None  # type: Optional[Future]
        self._task = None  # type: Optional[Future]
        self._state = NOT_STARTED  # type: State
        self._log = conn.config.logger

    def read(self) -> "Awaitable[Snapshot]":
        """
        Returns a snapshot of data.

        Despite being asynchronous, this call will generally return immediately unless:
        * :meth:`start` has not yet been called
        * the stream is still reading the initial Active Contract Set
        """
        if self._state == STOPPED:
            raise InvalidStateError("this ACS has already been cancelled")

        if self._snapshot_fut is None:
            self._snapshot_fut = get_event_loop().create_future()
        return self._snapshot_fut

    def read_immediately(self) -> "Optional[Snapshot]":
        """
        Returns the most recent snapshot of data, or ``None`` if this ACS was never started.

        This can be used as an alternative to :meth:`read` when the caller more interested in a
        non-``async`` call, and can tolerate reading data that is potentially slightly behind (or
        not yet present).

        :return: The last good ``Snapshot``, or ``None`` if the stream has not yet been started.
        :raises InvalidStateError: if the stream has already been stopped
        """
        if self._state == STOPPED:
            raise InvalidStateError("this ACS has already been cancelled")

        # if our Snapshot future is in a failed state, this method also throws in order to make
        # any read() exceptions known
        if self._snapshot_fut is not None:
            ex = self._snapshot_fut.exception()
            if ex is not None:
                raise ex

        return self._snapshot

    @property
    def state(self) -> State:
        """
        Return the current connection state:

        * ``NOT_STARTED``: :class:`ACS` has been created, but :meth:`run` has not yet been called.
        * ``CONNECTING``: :meth:`run` has been called, but the Active Contract Set has not yet been
          fully downloaded.
        * ``RUNNING``: the active contract set has been downloaded, and transaction event updates
          will be streamed as they are available.
        * ``RECONNECTING``: the stream was disconnected by the server;
        """
        return self._state

    async def start(self) -> None:
        """
        Have the ACS start subscribing for events from the server. This coroutine "blocks" until a
        snapshot is available.
        """
        if self._state != NOT_STARTED:
            raise InvalidStateError("this ACS is already running")

        # ensure that we "start" our read before we even connect to the stream, so that we can be
        # sure the future is triggered on the very first read
        fut = self.read()
        self._state = CONNECTING
        self._task = ensure_future(self._main())
        await fut

    async def stop(self) -> None:
        """
        Stop the underlying ACS stream. After this point, the stream is considered inoperable.
        """
        if self._task is not None:
            self._task.cancel()
            self._task = None
            self._state = STOPPED
        else:
            raise InvalidStateError("this ACS has already been stopped")

    async def _main(self) -> None:
        """
        The main coroutine. Calls :func:`snapshots` and accumulates relevant state.

        This coroutine NEVER throws because it is never actually awaited; exceptions that occur
        in the body of this method are propagated through the future returned by ``read()``.
        """
        try:
            log = self._conn.config.logger

            log.debug("ACS._main started.")
            async for state, snapshot in snapshots(self._conn, self._queries):
                log.debug("ACS transition: %s, %s", state, snapshot)
                self._state = state

                # any state change causes us to "reset" our read() Future
                if self._snapshot_fut is None or self._snapshot_fut.done():
                    self._snapshot_fut = get_event_loop().create_future()

                if snapshot is not None:
                    self._snapshot = snapshot
                    self._snapshot_fut.set_result(snapshot)
        except CancelledError:
            if self._snapshot_fut is not None and not self._snapshot_fut.done():
                self._snapshot_fut.cancel()
        except Exception as ex:
            # No one is actually waiting for our result, so if we don't move our exception to
            # an awaitable that people actually care about, it will never be seen!
            if self._snapshot_fut is None or self._snapshot_fut.done():
                self._snapshot_fut = get_event_loop().create_future()
            self._snapshot_fut.set_exception(ex)

    async def __aenter__(self) -> "ACS":
        """
        Allow :class:`ACS` to be used within ``async with`` blocks.
        """
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Allow :class:`ACS` to be used within ``async with`` blocks.
        """
        await self.stop()

    def __repr__(self):
        return f"ACS(state={self._state})"


async def snapshots(
    conn: Connection, queries: Queries
) -> "AsyncIterator[Tuple[State, Optional[Snapshot]]]":
    """
    Coroutine that returns regular "state" and "snapshot" updates aggregated over events off an
    event stream.
    """
    log = conn.config.logger

    yield CONNECTING, None

    snapshot = None  # type: Optional[Snapshot]
    offset = None  # type: Optional[str]
    recent_events = []  # type: List[Union[CreateEvent, ArchiveEvent]]
    backoff_time = 1.0
    at_least_one_snapshot = False

    while True:
        try:
            async with conn.stream_many(queries, offset=offset) as stream:
                async for obj in stream:
                    # reset the backoff time for subsequent stream disconnect/reconnects
                    backoff_time = 1.0

                    if isinstance(obj, Boundary):
                        offset = obj.offset
                        snapshot = create_snapshot(snapshot, recent_events, offset)

                        recent_events = []
                        at_least_one_snapshot = True
                        yield RUNNING, snapshot

                    elif isinstance(obj, (CreateEvent, ArchiveEvent)):
                        # Upon receiving at least one event, we're going to generate a new snapshot;
                        # inform the caller that a new snapshot is coming. These notifications are
                        # only posted once we have had at least one successful snapshot.
                        if not recent_events and at_least_one_snapshot:
                            yield RUNNING, None

                        # accumulate apps
                        recent_events.append(obj)
                    else:
                        warnings.warn(f"Unrecognized stream element: {obj!r}", ProtocolWarning)

        except CancelledError:
            # once we have been told to cancel, the stream is in the STOPPED state, and no further
            # interactions with it will be successful
            log.info("The ACS stream was asked to stop.")
            yield STOPPED, None
            raise

        except Exception:
            if conn.is_closed:
                yield STOPPED, None
                raise

            yield RECONNECTING, None
            log.exception(
                "The stream disconnected. Waiting %s seconds, then trying again (attempting "
                "to resume at offset %s)",
                backoff_time,
                offset,
            )
            await sleep(backoff_time)
            backoff_time = min(30.0, backoff_time * 2.0)


class Snapshot:
    """
    An immutable snapshot of contract data.
    """

    def __init__(self, creates: Mapping[ContractId, CreateEvent], offset: Optional[str]):
        self._offset = offset
        self._creates = MappingProxyType(dict(creates))
        self._contracts = ContractDataView(self._creates)
        self._template_ids = {
            cid.value_type: matching_normalizations(cid.value_type) for cid in self._creates
        }

    @property
    def offset(self) -> Optional[str]:
        """
        The offset point in a stream that contains all of the creates without offsetting archives
        in this snapshot.

        This value is ``None`` when connecting to a ledger that is completely empty.
        """
        return self._offset

    def earliest_contract(
        self, template_id: Union[str, TypeConName], match: Optional[ContractMatch] = None
    ) -> Optional[ContractData]:
        """
        Return the earliest contract in the Active Contract Set (in other words, _still_ active)
        that was created in the transaction stream that matches the specified filter, or ``None``
        if there are no matches.
        """
        ev = self.earliest_create(template_id, match)
        return ev.payload if ev is not None else None

    def matching_contracts(
        self, template_id: Union[str, TypeConName], match: Optional[ContractMatch] = None
    ) -> Mapping[ContractId, ContractData]:
        """"""
        return ContractDataView(self.matching_creates(template_id, match))

    def latest_contract(
        self, template_id: Union[str, TypeConName], match: Optional[ContractMatch] = None
    ) -> Optional[ContractData]:
        """
        Return the contract that was created last in the transaction stream that matches the
        specified filter, or ``None`` if there are no matches.
        """
        ev = self.latest_create(template_id, match)
        return ev.payload if ev is not None else None

    def earliest_create(
        self, template_id: Union[str, TypeConName], match: Optional[ContractMatch] = None
    ) -> Optional[CreateEvent]:
        """
        Return the earliest :class:`CreateEvent` in the Active Contract Set (in other words, the
        corresponding contract is _still_ active) that was created in the transaction stream that
        matches the specified filter, or ``None``
        if there are no matches.
        """
        wanted_template_ids = self._matching_template_ids(template_id)

        # in Python 3.9, dict values can be `reversed`; sadly we're not there yet
        for cev in reversed(list(self._creates.values())):
            if cev.contract_id.value_type in wanted_template_ids and is_match(match, cev.payload):
                return cev
        return None

    def matching_creates(
        self, template_id: Union[str, TypeConName], match: Optional[ContractMatch] = None
    ) -> Mapping[ContractId, CreateEvent]:
        """
        Return the :class:`CreateEvent`s (indexed by :class:`ContractId`) whose contracts match the
        specified criteria.
        """
        wanted_template_ids = self._matching_template_ids(template_id)
        matches = {}
        for cid, cev in self._creates.items():
            if cev.contract_id.value_type in wanted_template_ids and is_match(match, cev.payload):
                matches[cev.contract_id] = cev
        return MappingProxyType(matches)

    def latest_create(
        self, template_id: Union[str, TypeConName], match: Optional[ContractMatch] = None
    ) -> Optional[CreateEvent]:
        """
        Return the contract that was created last in the transaction stream that matches the
        specified filter, or ``None`` if there are no matches.
        """
        wanted_template_ids = self._matching_template_ids(template_id)
        for cev in self._creates.values():
            if cev.contract_id.value_type in wanted_template_ids and is_match(match, cev.payload):
                return cev
        return None

    def _matching_template_ids(
        self, template_id: Union[str, TypeConName]
    ) -> Collection[TypeConName]:
        t = normalize(template_id)
        return {tid for tid, matches in self._template_ids.items() if t in matches}

    @property
    def contracts(self) -> Mapping[ContractId, ContractData]:
        """
        A read-only map of contract IDs to contract data.
        """
        return self._contracts

    @property
    def creates(self) -> Mapping[ContractId, CreateEvent]:
        """
        A map of contract IDs to :class:`CreateEvent`s that represent the current set of contracts
        in this ACS.

        :class:`CreateEvent`'s expose additional information, including signatories and observers.
        """
        return self._creates

    def __bool__(self) -> bool:
        return bool(self._creates)

    def __len__(self) -> int:
        return len(self._creates)

    def __repr__(self) -> str:
        return f"Snapshot(len={len(self)})"


def create_snapshot(
    base_snapshot: Optional[Snapshot],
    events: Sequence[Union[CreateEvent, ArchiveEvent]],
    offset: Optional[str],
) -> Snapshot:
    """
    Produces a new snapshot with the data from an original snapshot and the supplied events.
    """
    snapshot_data: Dict[ContractId, CreateEvent] = (
        dict(base_snapshot.creates) if base_snapshot is not None else {}
    )
    for event in events:
        if isinstance(event, CreateEvent):
            snapshot_data[event.contract_id] = event
        elif isinstance(event, ArchiveEvent):
            snapshot_data.pop(event.contract_id, None)
    return Snapshot(snapshot_data, offset)


class ContractDataView(MappingBase):
    """
    A map of :class:`ContractId` -> ``ContractData``. This class is just a view over an instance of
    ``Mapping[:class:`ContractId`, :class:`CreateEvent`].
    """

    __slots__ = ("__m",)

    def __init__(self, m: Mapping[ContractId, CreateEvent]):
        self.__m = m

    def __getitem__(self, key: ContractId) -> ContractData:
        return self.__m[key].payload

    def __len__(self) -> int:
        return len(self.__m)

    def __iter__(self) -> Iterator[ContractId]:
        return iter(self.__m)
