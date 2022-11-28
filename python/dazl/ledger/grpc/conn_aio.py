# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This module contains the mapping between gRPC calls and Python/dazl types.
"""

import asyncio
from asyncio import wait_for
from datetime import datetime, timedelta
from typing import (
    AbstractSet,
    Any,
    AsyncIterable,
    Collection,
    Dict,
    List,
    Mapping,
    Optional,
    Sequence,
    Union,
    cast,
)
import warnings

from grpc import ChannelConnectivity
from grpc.aio import Channel, UnaryStreamCall

from .. import aio
from ... import LOG
from ..._gen.com.daml.ledger.api import v1 as lapipb
from ..._gen.com.daml.ledger.api.v1 import admin as lapiadminpb
from ...damlast.daml_lf_1 import PackageRef, TypeConName
from ...damlast.util import is_match
from ...prim import (
    ContractData,
    ContractId,
    Party,
    TimeDeltaLike,
    datetime_to_timestamp,
    to_parties,
    to_timedelta,
)
from ...query import Filter, Queries, Query, parse_query
from .._offsets import END, End, LedgerOffsetRange, from_offset_until_forever
from .._retry import retry
from ..api_types import (
    ActAs,
    Admin,
    ArchiveEvent,
    Boundary,
    Command,
    CommandMeta,
    CreateEvent,
    ExerciseResponse,
    MeteringReport,
    PartyInfo,
    ReadAs,
    Right,
    User,
    Version,
)
from ..config import Config
from ..config.access import TokenBasedAccessConfig
from ..errors import ProtocolWarning, _allow_cancel, _translate_exceptions
from .channel import create_channel
from .codec_aio import Codec

__all__ = ["Connection", "QueryStream"]


class Connection(aio.Connection):
    """
    An asynchronous (``asyncio``) connection to the Daml gRPC Ledger API.
    """

    def __init__(self, config: Config):
        self._config = config
        self._logger = config.logger
        self._channel = create_channel(config)
        self._codec = Codec(self, lookup=config.lookup)

    @property
    def config(self) -> Config:
        return self._config

    @property
    def channel(self) -> Channel:
        """
        Provides access to the underlying gRPC channel.
        """
        return self._channel

    @property
    def codec(self) -> Codec:
        return self._codec

    @property
    def is_closed(self) -> bool:
        return self._channel.get_state(try_to_connect=False) == ChannelConnectivity.SHUTDOWN

    async def __aenter__(self) -> "Connection":
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def open(self) -> None:
        """
        Does final validation of the token, including possibly fetching the ledger ID if it is not
        yet known.
        """
        if self._config.access.token_version == 2:
            # Daml 2.0 tokens do not contain party information, so an extra call to the server is
            # required in order to resolve our current set of rights
            if hasattr(self._config.access, "_set"):
                admin = False
                read_as = []  # type: List[Party]
                act_as = []  # type: List[Party]
                for right in await self.list_user_rights():
                    if right == Admin:
                        admin = True
                    elif isinstance(right, ReadAs):
                        read_as.append(right.party)
                    elif isinstance(right, ActAs):
                        act_as.append(right.party)

                # noinspection PyProtectedMember
                cast(TokenBasedAccessConfig, self._config.access)._set(
                    read_as=read_as, act_as=act_as, admin=admin
                )

        elif not self._config.access.ledger_id:
            # most calls to Daml 1.x ledgers require a ledger ID; if it wasn't supplied as part of
            # our token or we were never given a token in the first place, fetch the ledger ID from
            # the destination
            stub = lapipb.LedgerIdentityServiceStub(self._channel)
            response = await stub.GetLedgerIdentity(lapipb.GetLedgerIdentityRequest())

            self._logger.info("Connected to gRPC Ledger API, ledger ID: %s", response.ledger_id)
            self._config.access.ledger_id = response.ledger_id

    async def close(self) -> None:
        """
        Close the underlying channel. Once the channel is closed, future command submissions,
        streams in progress, and any future streams will fail.
        """
        await self._channel.close()

    def _retry_timeout(self, timeout: Optional[TimeDeltaLike]) -> timedelta:
        return to_timedelta(timeout) if timeout is not None else self._config.url.retry_timeout

    # region Write API

    async def submit(
        self,
        __commands: Union[Command, Sequence[Command]],
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> None:
        """
        Submit one or more commands to the Ledger API.

        You should generally prefer trying to use :meth:`create`, :meth:`exercise`,
        :meth:`exercise_by_key`, or :meth:`create_and_exercise`, as they are available over both
        the gRPC Ledger API and HTTP JSON API; additionally those methods can provide more
        information about what happened.

        This method can be used to submit multiple disparate commands as a single transaction, but
        if you find yourself needing to do this, you may want to consider moving more of your logic
        into Daml so that only a single command is needed from the outside in order to satisfy your
        use case.
        """
        if __commands is None:
            return
        elif isinstance(__commands, Command):
            __commands = [__commands]
        retry_timeout = self._retry_timeout(timeout)
        stub = lapipb.CommandServiceStub(self.channel)

        meta = self._command_meta(
            workflow_id=workflow_id, command_id=command_id, read_as=read_as, act_as=act_as
        )
        commands = await asyncio.gather(*map(self._codec.encode_command, __commands))
        request = self._submit_and_wait_request(commands, meta)
        await retry(
            lambda: stub.SubmitAndWait(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )

    async def create(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> CreateEvent:
        """
        Create a contract for a given template.

        :param __template_id:
            The template of the contract to be created.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param timeout:
            The length of time to wait before giving up on this submission. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        :return:
            The :class:`CreateEvent` that represents the contract that was successfully created.
        """
        retry_timeout = self._retry_timeout(timeout)
        stub = lapipb.CommandServiceStub(self.channel)

        meta = self._command_meta(
            workflow_id=workflow_id, command_id=command_id, read_as=read_as, act_as=act_as
        )
        commands = [
            lapipb.Command(create=await self._codec.encode_create_command(__template_id, __payload))
        ]
        request = self._submit_and_wait_request(commands, meta)

        response = await retry(
            lambda: stub.SubmitAndWaitForTransaction(
                request, timeout=retry_timeout.total_seconds()
            ),
            timeout=retry_timeout,
        )
        return await self._codec.decode_created_event(response.transaction.events[0].created)

    async def exercise(
        self,
        __contract_id: ContractId,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a contract identified by its contract ID.

        :param __contract_id:
            The contract ID of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param timeout:
            The length of time to wait before giving up on this submission. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        retry_timeout = self._retry_timeout(timeout)
        stub = lapipb.CommandServiceStub(self.channel)

        meta = self._command_meta(
            workflow_id=workflow_id, command_id=command_id, read_as=read_as, act_as=act_as
        )
        commands = [
            lapipb.Command(
                exercise=await self._codec.encode_exercise_command(
                    __contract_id, __choice_name, __argument
                )
            )
        ]
        request = self._submit_and_wait_request(commands, meta)

        response = await retry(
            lambda: stub.SubmitAndWaitForTransactionTree(
                request, timeout=retry_timeout.total_seconds()
            ),
            timeout=retry_timeout,
        )
        return await self._codec.decode_exercise_response(response.transaction)

    async def create_and_exercise(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a newly-created contract, in a single transaction.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument (positional
            argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        retry_timeout = self._retry_timeout(timeout)
        stub = lapipb.CommandServiceStub(self.channel)

        meta = self._command_meta(
            workflow_id=workflow_id, command_id=command_id, read_as=read_as, act_as=act_as
        )
        commands = [
            lapipb.Command(
                createAndExercise=await self._codec.encode_create_and_exercise_command(
                    __template_id, __payload, __choice_name, __argument
                )
            )
        ]
        request = self._submit_and_wait_request(commands, meta)

        response = await retry(
            lambda: stub.SubmitAndWaitForTransactionTree(
                request, timeout=retry_timeout.total_seconds()
            ),
            timeout=retry_timeout,
        )
        return await self._codec.decode_exercise_response(response.transaction)

    async def exercise_by_key(
        self,
        __template_id: Union[str, TypeConName],
        __choice_name: str,
        __key: Any,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> "ExerciseResponse":
        """
        Exercise a choice on a contract identified by its contract key.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __key:
            The key of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        retry_timeout = self._retry_timeout(timeout)
        stub = lapipb.CommandServiceStub(self.channel)

        meta = self._command_meta(
            workflow_id=workflow_id, command_id=command_id, read_as=read_as, act_as=act_as
        )
        commands = [
            lapipb.Command(
                exerciseByKey=await self._codec.encode_exercise_by_key_command(
                    __template_id, __choice_name, __key, __argument
                )
            )
        ]
        request = self._submit_and_wait_request(commands, meta)
        response = await stub.SubmitAndWaitForTransactionTree(request)

        return await self._codec.decode_exercise_response(response.transaction)

    async def archive(
        self,
        __contract_id: ContractId,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> ArchiveEvent:
        """
        Archive a choice on a contract identified by its contract ID.

        :param __contract_id:
            The contract ID of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        await self.exercise(
            __contract_id,
            "Archive",
            workflow_id=workflow_id,
            command_id=command_id,
            read_as=read_as,
            act_as=act_as,
            timeout=timeout,
        )
        return ArchiveEvent(__contract_id)

    async def archive_by_key(
        self,
        __template_id: str,
        __key: Any,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> ArchiveEvent:
        """
        Exercise a choice on a contract identified by its contract key.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __key:
            The key of the contract to exercise.

            Note that future versions reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        response = await self.exercise_by_key(
            __template_id,
            "Archive",
            __key,
            workflow_id=workflow_id,
            command_id=command_id,
            read_as=read_as,
            act_as=act_as,
            timeout=timeout,
        )
        return next(iter(event for event in response.events if isinstance(event, ArchiveEvent)))

    def _submit_and_wait_request(
        self,
        commands: Collection[lapipb.Command],
        meta: CommandMeta,
    ) -> lapipb.SubmitAndWaitRequest:
        # this is support for versions of Daml Connect prior to 1.9.0
        act_as = meta.act_as
        if act_as is not None:
            act_as_party = act_as[0] if act_as else None
        else:
            raise ValueError("current access rights do not include any act-as parties")

        return lapipb.SubmitAndWaitRequest(
            commands=lapipb.Commands(
                ledger_id=self._config.access.ledger_id,
                application_id=self._config.access.application_name,
                command_id=meta.command_id,
                workflow_id=meta.workflow_id,
                party=act_as_party,
                commands=commands,
                act_as=meta.act_as,
                read_as=meta.read_as,
            )
        )

    def _command_meta(
        self,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ):
        read_as = self._read_as(read_as)
        if act_as is None:
            act_as = self._config.access.act_as

        return CommandMeta(
            workflow_id=workflow_id, command_id=command_id, read_as=read_as, act_as=act_as
        )

    # endregion

    # region Read API

    async def get_ledger_end(self, *, timeout: Optional[TimeDeltaLike] = None) -> str:
        """
        Return the offset at the end of the ledger.
        """
        retry_timeout = self._retry_timeout(timeout)
        stub = lapipb.TransactionServiceStub(self.channel)

        request = lapipb.GetLedgerEndRequest(ledger_id=self._config.access.ledger_id)
        response = await retry(
            lambda: stub.GetLedgerEnd(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return response.offset.absolute

    def query(
        self,
        __template_id: Union[str, TypeConName] = "*",
        __query: Query = None,
        *,
        begin_offset: Optional[str] = None,
        end_offset: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> "QueryStream":
        """
        Return the create events from the active contract set service as a stream.

        If you find yourself repeatedly calling :meth:`query` or :meth:`query_many` over the same
        set of templates, you may want to consider :class:`ACS` instead, which is a utility class
        that helps you maintain a "live" state of the ACS.

        :param __template_id:
            The name of the template for which to fetch contracts.
        :param __query:
            A filter to apply to the set of returned contracts.
        :param begin_offset:
            The starting offset at which to read an active contract set. If ``None``, contracts
            are read from the beginning, and using the Active Contract Set Service instead of the
            Transaction Service.
        :param end_offset:
            The ending offset. If ``None``, contracts are read until the end of the stream.
            In order to read indefinitely, use :meth:`stream` instead.
        :param read_as:
            An optional set of read-as parties to use to submit this query. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        """
        offset = LedgerOffsetRange(begin_offset, end_offset if end_offset is not None else END)
        return QueryStream(
            self,
            parse_query({__template_id: __query}, server_side_filters=False),
            offset,
            self._read_as(read_as),
            self._retry_timeout(timeout),
        )

    def query_many(
        self,
        *queries: Queries,
        begin_offset: Optional[str] = None,
        end_offset: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> "QueryStream":
        """
        Return the create events from the active contract set service as a stream.

        If you find yourself repeatedly calling :meth:`query` or :meth:`query_many` over the same
        set of templates, you may want to consider :class:`ACS` instead, which is a utility class
        that helps you maintain a "live" state of the ACS.

        :param queries:
            A map of template IDs to filter to apply to the set of returned contracts.
        :param begin_offset:
            The starting offset at which to read an active contract set. If ``None``, contracts
            are read from the beginning, and using the Active Contract Set Service instead of the
            Transaction Service.
        :param end_offset:
            The ending offset. If ``None``, contracts are read until the end of the stream.
            In order to read indefinitely, use :meth:`stream_many` instead.
        :param read_as:
            An optional set of read-as parties to use to submit this query. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        """
        offset = LedgerOffsetRange(begin_offset, end_offset if end_offset is not None else END)
        return QueryStream(
            self,
            parse_query(*queries, server_side_filters=False),
            offset,
            self._read_as(read_as),
            self._retry_timeout(timeout),
        )

    def stream(
        self,
        __template_id: Union[str, TypeConName] = "*",
        __query: Query = None,
        *,
        offset: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> "QueryStream":
        """
        Stream create/archive events.

        When ``offset`` is ``None``, create events from the active contract set are returned first,
        followed by a continuous stream of updates (creates/archives).

        Otherwise, ``offset`` can be supplied to resume a stream from a prior point where a
        ``Boundary`` was returned from a previous stream.

        :param __template_id:
            The name of the template for which to fetch contracts.
        :param __query:
            A filter to apply to the set of returned contracts. Note that this does not filter
            :class:`ArchiveEvent`; readers of the stream MUST be able to cope with "mismatched"
            archives that come from the result of applying a filter.
        :param offset:
            An optional offset at which to start receiving events. If ``None``, start from the
            beginning.
        :param read_as:
            An optional set of read-as parties to use to submit this query. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        """
        return QueryStream(
            self,
            parse_query({__template_id: __query}, server_side_filters=False),
            from_offset_until_forever(offset),
            self._read_as(read_as),
            self._retry_timeout(timeout),
        )

    def stream_many(
        self,
        *queries: Queries,
        offset: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> "QueryStream":
        """
        Stream create/archive events from more than one template ID in the same stream.

        When ``offset`` is ``None``, create events from the active contract set are returned first,
        followed by a continuous stream of updates (creates/archives).

        Otherwise, ``offset`` can be supplied to resume a stream from a prior point where a
        ``Boundary`` was returned from a previous stream.

        :param queries:
            A map of template IDs to filter to apply to the set of returned contracts. Note that
            this does not filter :class:`ArchiveEvent`; readers of the stream MUST be able to cope
            with "mismatched" archives that come from the result of applying a filter.
        :param offset:
            An optional offset at which to start receiving events. If ``None``, start from the
            beginning.
        :param read_as:
            An optional set of read-as parties to use to submit this query. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        """
        return QueryStream(
            self,
            parse_query(*queries, server_side_filters=False),
            from_offset_until_forever(offset),
            self._read_as(read_as),
            self._retry_timeout(timeout),
        )

    def _read_as(self, read_as: Union[None, Party, Collection[Party]] = None) -> Collection[Party]:
        if read_as is None:
            return self.config.access.read_as
        else:
            return to_parties(read_as)

    # endregion

    async def get_version(self, *, timeout: Optional[TimeDeltaLike] = None) -> "Version":
        retry_timeout = self._retry_timeout(timeout)
        stub = lapipb.VersionServiceStub(self.channel)
        request = lapipb.GetLedgerApiVersionRequest(ledger_id=self._config.access.ledger_id)

        response = await retry(
            lambda: stub.GetLedgerApiVersion(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return Codec.decode_version(response)

    # region User Management calls

    async def get_user(
        self, user_id: Optional[str] = None, *, timeout: Optional[TimeDeltaLike] = None
    ) -> User:
        retry_timeout = self._retry_timeout(timeout)
        stub = lapiadminpb.UserManagementServiceStub(self.channel)
        request = lapiadminpb.GetUserRequest(user_id=user_id)

        response = await retry(
            lambda: stub.GetUser(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return Codec.decode_user(response.user)

    async def create_user(
        self,
        user: User,
        rights: Optional[Sequence[Right]] = None,
        *,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> User:
        retry_timeout = self._retry_timeout(timeout)
        stub = lapiadminpb.UserManagementServiceStub(self.channel)
        request = lapiadminpb.CreateUserRequest(user=Codec.encode_user(user))
        if rights is not None:
            request.rights.extend(Codec.encode_right(right) for right in rights)

        response = await retry(
            lambda: stub.CreateUser(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return Codec.decode_user(response.user)

    async def list_users(self, *, timeout: Optional[TimeDeltaLike] = None) -> Sequence[User]:
        retry_timeout = self._retry_timeout(timeout)
        stub = lapiadminpb.UserManagementServiceStub(self.channel)
        request = lapiadminpb.ListUsersRequest()

        response = await retry(
            lambda: stub.ListUsers(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return [Codec.decode_user(user) for user in response.users]

    async def list_user_rights(
        self, user_id: Optional[str] = None, *, timeout: Optional[TimeDeltaLike] = None
    ) -> Sequence[Right]:
        retry_timeout = self._retry_timeout(timeout)
        stub = lapiadminpb.UserManagementServiceStub(self.channel)
        request = lapiadminpb.ListUserRightsRequest(user_id=user_id)

        response = await retry(
            lambda: stub.ListUserRights(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return [Codec.decode_right(user) for user in response.rights]

    # endregion

    # region Party Management calls

    async def allocate_party(
        self,
        *,
        identifier_hint: str = None,
        display_name: str = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> PartyInfo:
        """
        Allocate a new party.
        """
        retry_timeout = self._retry_timeout(timeout)
        stub = lapiadminpb.PartyManagementServiceStub(self.channel)
        request = lapiadminpb.AllocatePartyRequest(
            party_id_hint=Party(identifier_hint) if identifier_hint else None,
            display_name=display_name,
        )

        response = await retry(
            lambda: stub.AllocateParty(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return Codec.decode_party_info(response.party_details)

    async def list_known_parties(
        self, *, timeout: Optional[TimeDeltaLike] = None
    ) -> Sequence[PartyInfo]:
        retry_timeout = self._retry_timeout(timeout)
        stub = lapiadminpb.PartyManagementServiceStub(self.channel)
        request = lapiadminpb.ListKnownPartiesRequest()

        response = await retry(
            lambda: stub.ListKnownParties(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return [Codec.decode_party_info(pd) for pd in response.party_details]

    # endregion

    # region Package Management calls

    async def get_package(
        self, package_id: PackageRef, *, timeout: Optional[TimeDeltaLike] = None
    ) -> bytes:
        retry_timeout = self._retry_timeout(timeout)
        stub = lapipb.PackageServiceStub(self.channel)
        request = lapipb.GetPackageRequest(
            ledger_id=self._config.access.ledger_id, package_id=package_id
        )

        response = await retry(
            lambda: stub.GetPackage(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return response.archive_payload

    async def list_package_ids(
        self, *, timeout: Optional[TimeDeltaLike] = None
    ) -> AbstractSet[PackageRef]:
        retry_timeout = self._retry_timeout(timeout)
        stub = lapipb.PackageServiceStub(self.channel)
        request = lapipb.ListPackagesRequest(ledger_id=self._config.access.ledger_id)

        response = await retry(
            lambda: stub.ListPackages(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return frozenset({PackageRef(pkg_id) for pkg_id in response.package_ids})

    async def upload_package(
        self, contents: bytes, *, timeout: Optional[TimeDeltaLike] = None
    ) -> None:
        retry_timeout = self._retry_timeout(timeout)
        stub = lapiadminpb.PackageManagementServiceStub(self.channel)
        request = lapiadminpb.UploadDarFileRequest(dar_file=contents)

        await retry(
            lambda: stub.UploadDarFile(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )

    # endregion

    # region Metering Report calls

    async def get_metering_report(
        self,
        from_: datetime,
        to: Optional[datetime] = None,
        application_id: Optional[str] = None,
        *,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> MeteringReport:
        retry_timeout = self._retry_timeout(timeout)
        stub = lapiadminpb.MeteringReportServiceStub(self.channel)

        # This slightly awkward construction is due to Protobuf's Python type not escaping field
        # names that happen to match keywords. Unfortunately mypy can't follow what is going on
        # when we do this, so we must be careful!
        kwargs = {"from": datetime_to_timestamp(from_)}  # type: Dict[str, Any]
        if to is not None:
            kwargs["to"] = datetime_to_timestamp(to)
        if application_id is not None:
            kwargs["application_id"] = application_id
        request = lapiadminpb.GetMeteringReportRequest(**kwargs)  # type: ignore

        response = await retry(
            lambda: stub.GetMeteringReport(request, timeout=retry_timeout.total_seconds()),
            timeout=retry_timeout,
        )
        return Codec.decode_get_metering_report_response(response)

    # endregion


class QueryStream(aio.QueryStreamBase):
    def __init__(
        self,
        conn: Connection,
        filters: Optional[Mapping[TypeConName, Filter]],
        offset_range: LedgerOffsetRange,
        read_as: Collection[Party],
        timeout: timedelta,
    ):
        self.conn = conn
        self._filters = filters
        self._offset_range = offset_range
        self._read_as = read_as
        self._timeout = timeout
        self._response_stream = None  # type: Optional[UnaryStreamCall]
        self._closed = False

    @property
    def is_closed(self) -> bool:
        return self._closed

    async def close(self) -> None:
        # make sure to mark the object as "closed"; when we're closed, we don't mind cancellation
        # errors, because we're the one triggering the cancellation
        self._closed = True
        if self._response_stream is not None:
            self._response_stream.cancel()
            self._response_stream = None

    async def items(self):
        """
        Return an asynchronous stream of events.

        .. code-block:: python

            async with conn.query('SampleApp:Iou') as query:
                async for r in query:
                    print(f"Offset: {r.offset}")
                    for event in r.events:
                        print(f"  Event: {event}")

        :return:
            A stream of responses, where each response contains one or more events at a particular
            offset.

            At least one initial :class:`Boundary` is always returned, even if the stream is empty.
            In this case, the first returned object is a :class:`Boundary` with ``offset=None``.
        """
        log = self.conn.config.logger
        async with _translate_exceptions(self.conn), self, _allow_cancel(lambda: self._closed):
            filters = await self.conn.codec.encode_filters(self._filters)
            filters_by_party = {party: filters for party in self._read_as}
            tx_filter_pb = lapipb.TransactionFilter(filters_by_party=filters_by_party)

            offset = self._offset_range.begin
            if offset:
                log.debug("Skipped reading from the ACS because begin offset is %r", offset)
            else:
                # when starting from the beginning of the ledger, the Active Contract Set service
                # lets us catch up more quickly than having to parse every create/archive event
                # ourselves
                log.debug("Reading from the ACS...")
                async for event in self._acs_events(tx_filter_pb):
                    if isinstance(event, CreateEvent):
                        await self._emit_create(event)
                    elif isinstance(event, Boundary):
                        offset = event.offset
                        await self._emit_boundary(event)
                    else:
                        warnings.warn(f"Received an unknown event: {event}", ProtocolWarning)
                    yield event

                # when reading from the Active Contract Set service, if we're supposed to stop
                # at "the end", then the Active Contract Set data is all that we'll return
                if self._offset_range.end == END:
                    log.debug(
                        "Not reading from transaction stream because we were only asked for a snapshot."
                    )
                    return

            # now start returning events as they come off the transaction stream; note this
            # stream will never naturally close, so it's on the caller to call close() or to
            # otherwise exit our current context
            log.debug("Reading a transaction stream: %s", self._offset_range)
            async for event in self._tx_events(tx_filter_pb, offset, self._offset_range.end):
                log.debug("Received an event: %s", event)
                if isinstance(event, CreateEvent):
                    await self._emit_create(event)
                elif isinstance(event, ArchiveEvent):
                    await self._emit_archive(event)
                elif isinstance(event, Boundary):
                    await self._emit_boundary(event)
                else:
                    warnings.warn(f"Received an unknown event: {event}", ProtocolWarning)
                yield event

    async def _acs_events(
        self, filter_pb: lapipb.TransactionFilter
    ) -> AsyncIterable[Union[CreateEvent, Boundary]]:
        stub = lapipb.ActiveContractsServiceStub(self.conn.channel)

        request = lapipb.GetActiveContractsRequest(
            ledger_id=self.conn.config.access.ledger_id, filter=filter_pb
        )
        self._response_stream = response_stream = stub.GetActiveContracts(request)

        offset = None

        # Unidirectional gRPC streams cannot sensibly have a deadline because the stream may be
        # open indefinitely. However, if fetching an individual message from the stream takes a
        # long time here, we can reasonably assume that the stream is dead, because Active
        # Contract Set messages are really supposed to be sent as quickly as the server can send
        # them. In other words, a long timeout pause in the middle of pulling down ACS messages
        # would be highly unusual, so we treat them as fatal
        i = response_stream.__aiter__()
        while True:
            try:
                response = await wait_for(i.__anext__(), timeout=self._timeout.total_seconds())
            except StopAsyncIteration:
                break

            LOG.debug(
                "ACS start (offset %r, %d event(s))",
                response.offset,
                len(response.active_contracts),
            )
            for event in response.active_contracts:
                c_evt = await self.conn.codec.decode_created_event(event)
                if self._is_match(c_evt):
                    yield c_evt
            # for ActiveContractSetResponse messages, only the last offset is actually relevant
            LOG.debug("ACS end (offset %r)", response.offset)
            offset = response.offset
        yield Boundary(offset)

    async def _tx_events(
        self,
        filter_pb: lapipb.TransactionFilter,
        begin_offset: Optional[str],
        end_offset: "Union[None, str, End]",
    ) -> AsyncIterable[Union[CreateEvent, ArchiveEvent, Boundary]]:
        stub = lapipb.TransactionServiceStub(self.conn.channel)

        last_offset = begin_offset

        while True:
            request = lapipb.GetTransactionsRequest(
                ledger_id=self.conn.config.access.ledger_id,
                filter=filter_pb,
                begin=self.conn.codec.encode_begin_offset(last_offset),
                end=self.conn.codec.encode_end_offset(end_offset),
            )

            self._response_stream = response_stream = stub.GetTransactions(request)
            i = response_stream.__aiter__()

            while True:
                try:
                    response = await wait_for(i.__anext__(), timeout=self._timeout.total_seconds())
                except StopAsyncIteration:
                    # a TransactionStream stopped with an EOF sent from the server. This means
                    # our work in reading this stream is done too.
                    return
                except asyncio.TimeoutError:
                    # There was an unusually large gap in time between transactions.
                    # Abort the current stream because we can't be sure whether the stream died
                    # or if the server is merely quiet. If the stream re-establishment fails,
                    # we have our answer.
                    #
                    # Note that this _SHOULD_ be transparent to our callers, because we only
                    # perform this check on a Transaction boundary, and if the stream resumes
                    # successfully, we pick up from the point where we disconnected.
                    LOG.debug("terminating a transaction stream because of inactivity")

                    try:
                        # clean up the old stream; we ignore errors since we're about to retry
                        # the connection anyway
                        response_stream.cancel()
                    except Exception:  # noqa
                        pass

                    # Perform a GetLedgerEnd request _purely_ to assert that the remote is healthy,
                    # because we can't reliably distinguish between a condition where transactions
                    # aren't streaming because of no activity, or because of an unresponsive server.
                    # If this operation fails, let the exception bubble up the stack.
                    await self.conn.get_ledger_end(timeout=self._timeout)

                    # abort the loop in which we read events from a stream, and start over again
                    # trying to establish a stream connection
                    break

                for tx in response.transactions:
                    for event in tx.events:
                        event_type = event.WhichOneof("event")
                        if event_type == "created":
                            c_evt = await self.conn.codec.decode_created_event(event.created)
                            if self._is_match(c_evt):
                                yield c_evt
                        elif event_type == "archived":
                            yield await self.conn.codec.decode_archived_event(event.archived)
                        else:
                            warnings.warn(f"Unknown Event({event_type}=...)", ProtocolWarning)
                    last_offset = tx.offset
                    yield Boundary(tx.offset)

    def _is_match(self, event: CreateEvent) -> bool:
        # if there are no filters, then everything is a match
        if self._filters is None:
            return True

        for name, f in self._filters.items():
            # for each filter, if this contract type could be interpreted as a match for the current
            # filter, then apply a client-side filter
            if is_match(name, event.contract_id.value_type):
                return f.client_side is None or f.client_side(event.payload)

        # we checked every name, but none of them matched
        return False
