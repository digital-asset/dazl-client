# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import functools
import inspect
from pathlib import Path
from typing import (
    Any,
    Awaitable,
    BinaryIO,
    Callable,
    Collection,
    List,
    NoReturn,
    Optional,
    Set,
    Tuple,
    TypeVar,
    Union,
)
import warnings

from ..client.state import ActiveContractSet
from ..damlast.daml_lf_1 import TypeConName
from ..damlast.lookup import parse_type_con_name
from ..model.core import (
    ContractContextualData,
    ContractContextualDataCollection,
    ContractMatch,
    ContractsState,
)
from ..prim import ContractId, Party, TimeDeltaLike
from ..protocols.core import AEventHandler, ArchiveEvent, CreateEvent, ExerciseResponse
from ..protocols.ledgerapi import Connection
from ..protocols.ledgerapi.conn_aio import QueryStream
from ..util.io import get_bytes
from .v8 import CallbackReturnValueWarning, NotSupportedError
from .v8_events import ContractArchiveEvent, ContractCreateEvent, InitEvent, ReadyEvent

__all__ = ["AIOGlobalClient", "AIOPartyClient"]

InitFn = TypeVar("InitFn", bound=AEventHandler[InitEvent])
ReadyFn = TypeVar("ReadyFn", bound=AEventHandler[ReadyEvent])
CreateFn = TypeVar("CreateFn", bound=AEventHandler[CreateEvent])
ArchiveFn = TypeVar("ArchiveFn", bound=AEventHandler[ArchiveEvent])
DEFAULT_TIMEOUT_SECONDS = 30

_NS_SERIALIZER = "Serializer and PackageStore are not supported; use Connection.codec instead."
_NS_LEDGER_ID = (
    "LedgerMetadata.ledger_id is deprecated; use Connection.config.access.ledger_id instead."
)


class AIOClientBase:
    def __init__(self, conn: "Connection"):
        self._conn = conn

    async def ensure_dar(
        self,
        contents: "Union[str, Path, bytes, BinaryIO]",
        timeout: "TimeDeltaLike" = DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        """
        Validate that the ledger has the packages specified by the given contents (as a byte array).
        Throw an exception if the specified DARs do not exist within the specified timeout.

        :param contents: The DAR or DALF to ensure.
        :param timeout: The maximum length of time to wait before giving up.
        """
        await asyncio.wait_for(self._conn.upload_package(get_bytes(contents)), timeout=timeout)


class AIOGlobalClient(AIOClientBase):
    """
    A transitional replacement for :class:`dazl.client.api.AIOGlobalClient` that keeps the same
    superficial API, but changes some of the semantics to match the newer API.
    """

    async def ensure_packages(self, package_ids: "Collection[str]"):
        pass

    async def metadata(self) -> "LedgerMetadata":
        return LedgerMetadata(self._conn.config.access.ledger_id)


class LedgerMetadata:
    def __init__(self, ledger_id: str):
        self._ledger_id = ledger_id

    def ledger_id(self) -> str:
        warnings.warn(_NS_LEDGER_ID, DeprecationWarning, stacklevel=2)
        return self._ledger_id

    @property
    def store(self) -> "NoReturn":
        warnings.warn(_NS_SERIALIZER, DeprecationWarning, stacklevel=2)
        raise NotSupportedError(_NS_SERIALIZER)


class AIOPartyClient(AIOClientBase):
    """
    A transitional replacement for :class:`dazl.client.AIOPartyClient` that keeps the same
    superficial API, but changes some of the semantics to match the newer API.
    """

    def __init__(self, conn: "Connection"):
        super().__init__(conn)
        self._acs = ActiveContractSet(None, conn.codec.lookup)
        self._ready = asyncio.Event()
        self._templates = set()  # type: Set[TypeConName]
        self._init_callbacks = []  # type: List[AEventHandler[InitEvent]]
        self._ready_callbacks = []  # type: List[AEventHandler[ReadyEvent]]
        self._create_callbacks = (
            []
        )  # type: List[Tuple[Callable[[CreateEvent], bool], AEventHandler[CreateEvent]]]
        self._archive_callbacks = (
            []
        )  # type: List[Tuple[Callable[[ArchiveEvent], bool], AEventHandler[ArchiveEvent]]]
        self._stream = None

    # region Event handler registration

    def ledger_init(self) -> "Callable[[InitFn], InitFn]":
        def register(fn: "InitFn") -> "InitFn":
            self.add_ledger_init(fn)
            return fn

        return register

    def add_ledger_init(self, handler: "InitFn") -> None:
        self._init_callbacks.append(handler)

    def ledger_ready(self) -> "Callable[[ReadyFn], ReadyFn]":
        def register(fn: "ReadyFn") -> "ReadyFn":
            self.add_ledger_ready(fn)
            return fn

        return register

    def add_ledger_ready(self, handler) -> None:
        self._ready_callbacks.append(handler)

    @staticmethod
    def ledger_packages_added(*_, **__):
        """
        This function is no longer supported.
        """
        warnings.warn("ledger_packages_added is not supported", DeprecationWarning, stacklevel=2)
        raise Exception("ledger_packages_added is not supported")

    @staticmethod
    def add_ledger_packages_added(*_, **__):
        """
        This function is no longer supported.
        """
        warnings.warn(
            "add_ledger_packages_added is not supported", DeprecationWarning, stacklevel=2
        )
        raise Exception("add_ledger_packages_added is not supported")

    @staticmethod
    def ledger_exercised(*_, **__):
        """
        This function is no longer supported.
        """
        warnings.warn("ledger_exercised is not supported", DeprecationWarning, stacklevel=2)
        raise Exception("ledger_exercised is not supported")

    @staticmethod
    def add_ledger_exercised(*_, **__):
        """
        This function is no longer supported.
        """
        warnings.warn("add_ledger_exercised is not supported", DeprecationWarning, stacklevel=2)
        raise Exception("add_ledger_exercised is not supported")

    def ledger_created(
        self, template: "Union[str, TypeConName]", match: "Optional[ContractMatch]" = None
    ) -> "CreateFn":
        def register(fn: "CreateFn") -> "CreateFn":
            self.add_ledger_created(template, fn, match=match)
            return fn

        return register

    def add_ledger_created(
        self,
        template: "Union[str, TypeConName]",
        handler: "CreateFn",
        match: "Optional[ContractMatch]" = None,
    ) -> None:
        name = parse_type_con_name(template)
        self._templates.add(name)
        self._create_callbacks.append((create_filter(name, match), handler))

    def ledger_archived(
        self, template: "Union[str, TypeConName]", match: "Optional[ContractMatch]" = None
    ) -> "ArchiveFn":
        def register(fn: "ArchiveFn") -> "ArchiveFn":
            self.add_ledger_archived(template, fn, match=match)
            return fn

        return register

    def add_ledger_archived(
        self,
        template: "Union[str, TypeConName]",
        handler: "ArchiveFn",
        match: "Optional[ContractMatch]" = None,
    ) -> None:
        name = parse_type_con_name(template)
        self._templates.add(name)
        self._create_callbacks.append((create_filter(name, match), handler))

    # endregion

    # region Command Submission

    async def submit(self, commands, workflow_id: "Optional[str]" = None):
        return await self._conn.do_commands(commands, workflow_id=workflow_id)

    async def submit_create(
        self,
        template_name: "Union[str, TypeConName]",
        arguments: "Optional[dict]" = None,
        workflow_id: "Optional[str]" = None,
    ):
        """
        Submit a single create command.

        :param template_name:
            The name of the template.
        :param arguments:
            The arguments to the create (as a ``dict``).
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :return:
            A future that resolves when the command has made it to the ledger _or_ an error
            occurred when trying to process them.
        """
        return await self._conn.create(template_name, arguments, workflow_id=workflow_id)

    async def submit_exercise(
        self,
        cid: "ContractId",
        choice_name: str,
        arguments: "Optional[dict]" = None,
        workflow_id: "Optional[str]" = None,
    ) -> "ExerciseResponse":
        """
        Submit an exercise choice.

        :param cid:
            The :class:`ContractId` on which a choice is being exercised.
        :param choice_name:
            The name of the choice to exercise.
        :param arguments:
            The arguments to the exercise (as a ``dict``). Can be omitted (``None``) for no-argument
            choices.
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        :return:
            A future that resolves when the command has made it to the ledger _or_ an error
            occurred when trying to process them.
        """
        return await self._conn.exercise(cid, choice_name, arguments, workflow_id=workflow_id)

    async def submit_exercise_by_key(
        self,
        template_name: "Union[str, TypeConName]",
        contract_key: "Any",
        choice_name: str,
        arguments: "Optional[dict]" = None,
        workflow_id: "Optional[str]" = None,
    ) -> "ExerciseResponse":
        """
        Synchronously submit a single exercise choice. Equivalent to calling :meth:`submit` with a
        single ``exercise_by_key``.

        :param template_name:
            The name of the template on which to do an exercise-by-key.
        :param contract_key:
            The value that should uniquely identify a contract for the specified template.
        :param choice_name:
            The name of the choice to exercise.
        :param arguments:
            The arguments to the create (as a ``dict``). Can be omitted (``None``) for no-argument
            choices.
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        """
        return await self._conn.exercise_by_key(
            template_name, contract_key, choice_name, arguments, workflow_id=workflow_id
        )

    async def submit_create_and_exercise(
        self,
        template_name: "Union[str, TypeConName]",
        arguments: "dict",
        choice_name: str,
        choice_arguments: "Optional[dict]" = None,
        workflow_id: "Optional[str]" = None,
    ) -> "ExerciseResponse":
        """
        Synchronously submit a single create-and-exercise command. Equivalent to calling
        :meth:`submit` with a single ``create_and_exercise``.

        :param template_name:
            The name of the template on which to do an exercise-by-key.
        :param arguments:
            The arguments to the create (as a ``dict``).
        :param choice_name:
            The name of the choice to exercise.
        :param choice_arguments:
            The arguments to the exercise (as a ``dict``). Can be omitted (``None``) for no-argument
        :param workflow_id:
            The optional workflow ID to stamp on the outgoing command.
        """
        return await self._conn.create_and_exercise(
            template_name, arguments, choice_name, choice_arguments, workflow_id=workflow_id
        )

    # endregion

    # region Active contract set

    def find_by_id(self, cid: "Union[str, ContractId]") -> "Optional[ContractContextualData]":
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        return self._acs.get(cid)

    def find(
        self, template: "Any", match: "ContractMatch" = None, include_archived: bool = False
    ) -> "ContractContextualDataCollection":
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        return self._acs.read_full(template, match, include_archived=include_archived)

    def find_one(self, template: Any, match: ContractMatch = None) -> "ContractsState":
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        return self._acs.read_active(template, match)

    def find_historical(
        self, template: Any, match: ContractMatch = None
    ) -> "ContractContextualDataCollection":
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        return self._acs.read_full(template, match, include_archived=True)

    def find_nonempty(
        self, template: Any, match: ContractMatch, min_count: int = 1, timeout: float = 30
    ):
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        return self._acs.read_async(template, match, min_count=min_count)

    # endregion

    # region Ledger/client metadata

    @staticmethod
    def set_config(*_, **__):
        """
        This function is no longer supported.
        """
        warnings.warn("set_config is not supported", DeprecationWarning, stacklevel=2)
        raise Exception("set_config is not supported")

    async def ready(self) -> None:
        """
        Block until the underlying stream has finished reading its active contract set.
        """
        await self._ready.wait()

    @property
    def party(self) -> "Party":
        """
        Return the party for the connection that triggered this event.

        Note that with multi-party submissions, there may not be a such thing as a singular "Party"
        for a connection any more; if you are using this property, you will need to find another
        mechanism for identifying the relevant Party in order to be compatible with multi-party
        submissions. As such, this property is deprecated.
        """
        warnings.warn(
            "reading `party` from a connection is ambiguous when multi-party submissions are "
            "being used; consider an alternate way of determining the relevant party",
            DeprecationWarning,
            stacklevel=2,
        )
        return next(iter(self._conn.config.access.act_as))

    # endregion

    async def _open(self) -> None:
        await self._conn.open()

    async def _run(self, keep_open: bool) -> None:
        """
        Called by :class:`ConnectionFactory` to start our internal stream.
        """
        query = {t: None for t in self._templates}

        try:
            async with self._create_stream(query, keep_open) as stream:
                self._stream = stream
                for cb in self._init_callbacks:
                    stream.on_init(self._new_style_callback(None, cb, lambda _: InitEvent(self)))
                stream.on_ready(lambda _: self._ready.set())
                for cb in self._ready_callbacks:
                    stream.on_ready(self._new_style_callback(None, cb, lambda _: ReadyEvent(self)))
                for f, cb in self._create_callbacks:
                    stream.on_create(
                        self._new_style_callback(f, cb, lambda ev: ContractCreateEvent(self, ev))
                    )
                for f, cb in self._archive_callbacks:
                    stream.on_archive(
                        self._new_style_callback(f, cb, lambda ev: ContractArchiveEvent(self, ev))
                    )
                await stream.run()
        finally:
            self._stream = None

    async def _stop(self):
        if self._stream is not None:
            await self._stream.close()

    def _create_stream(self, query, keep_open) -> "QueryStream[Union[CreateEvent, ArchiveEvent]]":
        return self._conn.stream_many(query) if keep_open else self._conn.query_many(query)

    def _new_style_callback(
        self, event_filter, callback: "Callable[[E1], Any]", event_mapper: "Callable[[E0], E1]"
    ) -> "Callable[[E0], Awaitable[None]]":
        """
        Wrap an old-style callback (that can return commands) into the form a new-style callback
        (that does not do anything with returned values).
        """

        @functools.wraps(callback)
        async def impl(event):
            if event_filter is None or event_filter(event):
                compat_event = event_mapper(event)
                ret = callback(compat_event)
                if inspect.iscoroutine(ret):
                    ret = await ret
                if ret is not None:
                    warnings.warn(
                        "callbacks should not return anything", CallbackReturnValueWarning
                    )
                    await self._conn.do_commands(ret)

        return impl


E0 = TypeVar("E0")
E1 = TypeVar("E1")


def create_filter(name: "TypeConName", match: "ContractMatch") -> "Callable[[CreateEvent], bool]":
    def event_filter(event: "CreateEvent") -> bool:
        if event.cid.value_type == name:
            return True
        return False

    return event_filter
