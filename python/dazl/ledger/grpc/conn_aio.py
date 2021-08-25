# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This module contains the mapping between gRPC calls and Python/dazl types.
"""

import asyncio
from typing import AbstractSet, Any, AsyncIterable, Collection, Mapping, Optional, Sequence, Union
import uuid
import warnings

from grpc import ChannelConnectivity
from grpc.aio import Channel, UnaryStreamCall

from .. import aio
from ..._gen.com.daml.ledger.api import v1 as lapipb
from ..._gen.com.daml.ledger.api.v1 import admin as lapiadminpb
from ...damlast.daml_lf_1 import PackageRef, TypeConName
from ...damlast.util import is_match
from ...prim import LEDGER_STRING_REGEX, ContractData, ContractId, Party
from ...query import Filter, Queries, Query, parse_query
from .._offsets import UNTIL_END, LedgerOffsetRange, from_offset_until_forever
from ..api_types import ArchiveEvent, Boundary, Command, CreateEvent, ExerciseResponse, PartyInfo
from ..config import Config
from ..config.access import PropertyBasedAccessConfig
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
        self._codec = Codec(self)

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
        if not self._config.access.ledger_id:
            # most calls require a ledger ID; if it wasn't supplied as part of our token or we were
            # never given a token in the first place, fetch the ledger ID from the destination
            stub = lapipb.LedgerIdentityServiceStub(self._channel)
            response = await stub.GetLedgerIdentity(lapipb.GetLedgerIdentityRequest())
            if isinstance(self._config.access, PropertyBasedAccessConfig):
                self._logger.info("Connected to gRPC Ledger API, ledger ID: %s", response.ledger_id)
                self._config.access.ledger_id = response.ledger_id
            else:
                raise ValueError("when using token-based access, the token must contain ledger ID")

    async def close(self) -> None:
        """
        Close the underlying channel. Once the channel is closed, future command submissions,
        streams in progress, and any future streams will fail.
        """
        await self._channel.close()

    # region Write API

    async def submit(
        self,
        __commands: Union[Command, Sequence[Command]],
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> "None":
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

        stub = lapipb.CommandServiceStub(self.channel)

        commands_pb = await asyncio.gather(*map(self._codec.encode_command, __commands))
        request = lapipb.SubmitAndWaitRequest(
            commands=lapipb.Commands(
                ledger_id=self._config.access.ledger_id,
                application_id=self._config.access.application_name,
                command_id=self._command_id(command_id),
                workflow_id=self._workflow_id(workflow_id),
                party=self._ensure_act_as(),
                commands=commands_pb,
                act_as=self._config.access.act_as,
                read_as=self._config.access.read_only_as,
            )
        )
        await stub.SubmitAndWait(request)

    async def create(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> CreateEvent:
        """
        Create a contract for a given template.

        :param __template_id:
            The template of the contract to be created.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The :class:`CreateEvent` that represents the contract that was successfully created.
        """
        stub = lapipb.CommandServiceStub(self.channel)

        commands = [
            lapipb.Command(create=await self._codec.encode_create_command(__template_id, __payload))
        ]
        request = lapipb.SubmitAndWaitRequest(
            commands=lapipb.Commands(
                ledger_id=self._config.access.ledger_id,
                application_id=self._config.access.application_name,
                command_id=self._command_id(command_id),
                workflow_id=self._workflow_id(workflow_id),
                party=self._ensure_act_as(),
                commands=commands,
                act_as=self._config.access.act_as,
                read_as=self._config.access.read_only_as,
            )
        )
        response = await stub.SubmitAndWaitForTransaction(request)

        return await self._codec.decode_created_event(response.transaction.events[0].created)

    async def exercise(
        self,
        __contract_id: ContractId,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a contract identified by its contract ID.

        :param __contract_id:
            The contract ID of the contract to exercise.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        stub = lapipb.CommandServiceStub(self.channel)

        commands = [
            lapipb.Command(
                exercise=await self._codec.encode_exercise_command(
                    __contract_id, __choice_name, __argument
                )
            )
        ]
        request = self._submit_and_wait_request(commands, workflow_id, command_id)
        response = await stub.SubmitAndWaitForTransactionTree(request)

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
    ) -> ExerciseResponse:
        """
        Exercise a choice on a newly-created contract, in a single transaction.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __payload:
            Template arguments for the contract to be created (positional argument only).

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise (positional argument only).

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument (positional
            argument only).

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        stub = lapipb.CommandServiceStub(self.channel)

        commands = [
            lapipb.Command(
                createAndExercise=await self._codec.encode_create_and_exercise_command(
                    __template_id, __payload, __choice_name, __argument
                )
            )
        ]
        request = self._submit_and_wait_request(commands, workflow_id, command_id)
        response = await stub.SubmitAndWaitForTransactionTree(request)

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
    ) -> "ExerciseResponse":
        """
        Exercise a choice on a contract identified by its contract key.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __choice_name:
            The name of the choice to exercise.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __key:
            The key of the contract to exercise.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __argument:
            The choice arguments. Can be omitted for choices that take no argument.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        stub = lapipb.CommandServiceStub(self.channel)

        commands = [
            lapipb.Command(
                exerciseByKey=await self._codec.encode_exercise_by_key_command(
                    __template_id, __choice_name, __key, __argument
                )
            )
        ]
        request = self._submit_and_wait_request(commands, workflow_id, command_id)
        response = await stub.SubmitAndWaitForTransactionTree(request)

        return await self._codec.decode_exercise_response(response.transaction)

    async def archive(
        self,
        __contract_id: ContractId,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ArchiveEvent:
        """
        Archive a choice on a contract identified by its contract ID.

        :param __contract_id:
            The contract ID of the contract to exercise.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        await self.exercise(
            __contract_id, "Archive", workflow_id=workflow_id, command_id=command_id
        )
        return ArchiveEvent(__contract_id)

    async def archive_by_key(
        self,
        __template_id: str,
        __key: Any,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ArchiveEvent:
        """
        Exercise a choice on a contract identified by its contract key.

        :param __template_id:
            The template of the contract to be created (positional argument only).

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param __key:
            The key of the contract to exercise.

            Note that future versions of dazl reserve the right to rename this parameter name at any
            time; it should be passed in as a positional parameter and never by name.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        response = await self.exercise_by_key(
            __template_id, "Archive", __key, workflow_id=workflow_id, command_id=command_id
        )
        return next(iter(event for event in response.events if isinstance(event, ArchiveEvent)))

    def _ensure_act_as(self) -> Party:
        act_as_party = next(iter(self._config.access.act_as), None)
        if not act_as_party:
            raise ValueError("current access rights do not include any act-as parties")
        return act_as_party

    @staticmethod
    def _workflow_id(workflow_id: Optional[str]) -> Optional[str]:
        if workflow_id:
            if not LEDGER_STRING_REGEX.match(workflow_id):
                raise ValueError("workflow_id must be a valid ledger string")
            return workflow_id
        else:
            return None

    @staticmethod
    def _command_id(command_id: Optional[str]) -> str:
        if command_id:
            if not LEDGER_STRING_REGEX.match(command_id):
                raise ValueError("command_id must be a valid ledger string")
            return command_id
        else:
            return uuid.uuid4().hex

    def _submit_and_wait_request(
        self,
        commands: Collection[lapipb.Command],
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> lapipb.SubmitAndWaitRequest:
        return lapipb.SubmitAndWaitRequest(
            commands=lapipb.Commands(
                ledger_id=self._config.access.ledger_id,
                application_id=self._config.access.application_name,
                command_id=self._command_id(command_id),
                workflow_id=self._workflow_id(workflow_id),
                party=self._ensure_act_as(),
                commands=commands,
                act_as=self._config.access.act_as,
                read_as=self._config.access.read_only_as,
            )
        )

    # endregion

    # region Read API

    def query(
        self, __template_id: Union[str, TypeConName] = "*", __query: Query = None
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
        """
        return QueryStream(
            self, parse_query({__template_id: __query}, server_side_filters=False), UNTIL_END
        )

    def query_many(self, *queries: Queries) -> "QueryStream":
        """
        Return the create events from the active contract set service as a stream.

        If you find yourself repeatedly calling :meth:`query` or :meth:`query_many` over the same
        set of templates, you may want to consider :class:`ACS` instead, which is a utility class
        that helps you maintain a "live" state of the ACS.

        :param queries:
            A map of template IDs to filter to apply to the set of returned contracts.
        """
        return QueryStream(self, parse_query(*queries, server_side_filters=False), UNTIL_END)

    def stream(
        self,
        __template_id: Union[str, TypeConName] = "*",
        __query: Query = None,
        *,
        offset: Optional[str] = None,
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
        """
        return QueryStream(
            self,
            parse_query({__template_id: __query}, server_side_filters=False),
            from_offset_until_forever(offset),
        )

    def stream_many(self, *queries: Queries, offset: Optional[str] = None) -> "QueryStream":
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
        """
        return QueryStream(
            self,
            parse_query(*queries, server_side_filters=False),
            from_offset_until_forever(offset),
        )

    # endregion

    # region Party Management calls

    async def allocate_party(
        self, *, identifier_hint: str = None, display_name: str = None
    ) -> "PartyInfo":
        """
        Allocate a new party.
        """
        stub = lapiadminpb.PartyManagementServiceStub(self.channel)
        request = lapiadminpb.AllocatePartyRequest(
            party_id_hint=Party(identifier_hint) if identifier_hint else None,
            display_name=display_name,
        )
        response = await stub.AllocateParty(request)
        return Codec.decode_party_info(response.party_details)

    async def list_known_parties(self) -> Sequence[PartyInfo]:
        stub = lapiadminpb.PartyManagementServiceStub(self.channel)
        request = lapiadminpb.ListKnownPartiesRequest()
        response = await stub.ListKnownParties(request)
        return [Codec.decode_party_info(pd) for pd in response.party_details]

    # endregion

    # region Package Management calls

    async def get_package(self, package_id: PackageRef) -> bytes:
        stub = lapipb.PackageServiceStub(self.channel)
        request = lapipb.GetPackageRequest(
            ledger_id=self._config.access.ledger_id, package_id=package_id
        )
        response = await stub.GetPackage(request)
        return response.archive_payload

    async def list_package_ids(self) -> AbstractSet[PackageRef]:
        stub = lapipb.PackageServiceStub(self.channel)
        request = lapipb.ListPackagesRequest(ledger_id=self._config.access.ledger_id)
        response = await stub.ListPackages(request)
        return frozenset({PackageRef(pkg_id) for pkg_id in response.package_ids})

    async def upload_package(self, contents: bytes) -> None:
        stub = lapiadminpb.PackageManagementServiceStub(self.channel)
        request = lapiadminpb.UploadDarFileRequest(dar_file=contents)
        await stub.UploadDarFile(request)
        return

    # endregion


class QueryStream(aio.QueryStreamBase):
    def __init__(
        self,
        conn: Connection,
        filters: Optional[Mapping[TypeConName, Filter]],
        offset_range: LedgerOffsetRange,
    ):
        self.conn = conn
        self._filters = filters
        self._offset_range = offset_range
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
            filters_by_party = {party: filters for party in self.conn.config.access.read_as}
            tx_filter_pb = lapipb.TransactionFilter(filters_by_party=filters_by_party)

            offset = None
            if self._offset_range.begin is None:
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
            else:
                log.debug(
                    "Skipped reading from the ACS because begin offset is %r",
                    self._offset_range.begin,
                )

            if self._offset_range != UNTIL_END:
                # now start returning events as they come off the transaction stream; note this
                # stream will never naturally close, so it's on the caller to call close() or to
                # otherwise exit our current context
                log.debug("Reading a transaction stream: %s", self._offset_range)
                async for event in self._tx_events(tx_filter_pb, offset):
                    if isinstance(event, CreateEvent):
                        await self._emit_create(event)
                    elif isinstance(event, ArchiveEvent):
                        await self._emit_archive(event)
                    elif isinstance(event, Boundary):
                        await self._emit_boundary(event)
                    else:
                        warnings.warn(f"Received an unknown event: {event}", ProtocolWarning)
                    yield event
            else:
                log.debug(
                    "Not reading from transaction stream because we were only asked for a snapshot."
                )

    async def _acs_events(
        self, filter_pb: lapipb.TransactionFilter
    ) -> AsyncIterable[Union[CreateEvent, Boundary]]:
        stub = lapipb.ActiveContractsServiceStub(self.conn.channel)

        request = lapipb.GetActiveContractsRequest(
            ledger_id=self.conn.config.access.ledger_id, filter=filter_pb
        )
        self._response_stream = response_stream = stub.GetActiveContracts(request)

        offset = None
        async for response in response_stream:
            for event in response.active_contracts:
                c_evt = await self.conn.codec.decode_created_event(event)
                if self._is_match(c_evt):
                    yield c_evt
            # for ActiveContractSetResponse messages, only the last offset is actually relevant
            offset = response.offset
        yield Boundary(offset)

    async def _tx_events(
        self, filter_pb: lapipb.TransactionFilter, begin_offset: Optional[str]
    ) -> AsyncIterable[Union[CreateEvent, ArchiveEvent, Boundary]]:
        stub = lapipb.TransactionServiceStub(self.conn.channel)

        request = lapipb.GetTransactionsRequest(
            ledger_id=self.conn.config.access.ledger_id,
            filter=filter_pb,
            begin=self.conn.codec.encode_begin_offset(begin_offset),
        )

        self._response_stream = response_stream = stub.GetTransactions(request)
        async for response in response_stream:
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
