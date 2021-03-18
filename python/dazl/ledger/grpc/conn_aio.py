# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This module contains the mapping between gRPC calls and Python/dazl types.
"""
from __future__ import annotations

import asyncio
from typing import AbstractSet, Any, AsyncIterable, Collection, Mapping, Optional, Sequence, Union
import uuid
import warnings

from grpc.aio import Channel

from ..._gen.com.daml.ledger.api.v1.active_contracts_service_pb2 import (
    GetActiveContractsRequest as G_GetActiveContractsRequest,
)
from ..._gen.com.daml.ledger.api.v1.active_contracts_service_pb2_grpc import (
    ActiveContractsServiceStub,
)
from ..._gen.com.daml.ledger.api.v1.admin.package_management_service_pb2 import (
    UploadDarFileRequest as G_UploadDarFileRequest,
)
from ..._gen.com.daml.ledger.api.v1.admin.package_management_service_pb2_grpc import (
    PackageManagementServiceStub,
)
from ..._gen.com.daml.ledger.api.v1.admin.party_management_service_pb2 import (
    AllocatePartyRequest as G_AllocatePartyRequest,
)
from ..._gen.com.daml.ledger.api.v1.admin.party_management_service_pb2_grpc import (
    PartyManagementServiceStub,
)
from ..._gen.com.daml.ledger.api.v1.command_service_pb2 import (
    SubmitAndWaitRequest as G_SubmitAndWaitRequest,
)
from ..._gen.com.daml.ledger.api.v1.command_service_pb2_grpc import CommandServiceStub
from ..._gen.com.daml.ledger.api.v1.commands_pb2 import Command as G_Command, Commands as G_Commands
from ..._gen.com.daml.ledger.api.v1.ledger_identity_service_pb2 import (
    GetLedgerIdentityRequest as G_GetLedgerIdentityRequest,
)
from ..._gen.com.daml.ledger.api.v1.ledger_identity_service_pb2_grpc import (
    LedgerIdentityServiceStub,
)
from ..._gen.com.daml.ledger.api.v1.package_service_pb2 import (
    GetPackageRequest as G_GetPackageRequest,
    ListPackagesRequest as G_ListPackagesRequest,
)
from ..._gen.com.daml.ledger.api.v1.package_service_pb2_grpc import PackageServiceStub
from ..._gen.com.daml.ledger.api.v1.transaction_filter_pb2 import (
    TransactionFilter as G_TransactionFilter,
)
from ..._gen.com.daml.ledger.api.v1.transaction_service_pb2 import (
    GetTransactionsRequest as G_GetTransactionsRequest,
)
from ..._gen.com.daml.ledger.api.v1.transaction_service_pb2_grpc import TransactionServiceStub
from ...damlast.daml_lf_1 import PackageRef, TypeConName
from ...prim import LEDGER_STRING_REGEX, ContractData, ContractId, Party
from ...query import Query
from ..api_types import ArchiveEvent, Boundary, Command, CreateEvent, ExerciseResponse, PartyInfo
from ..config import Config
from ..config.access import PropertyBasedAccessConfig
from ..errors import ProtocolWarning
from ..stream_aio import QueryStreamBase
from .channel import create_channel
from .codec_aio import Codec

__all__ = ["Connection", "QueryStream"]


class Connection:
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

    async def __aenter__(self) -> Connection:
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
            stub = LedgerIdentityServiceStub(self._channel)
            response = await stub.GetLedgerIdentity(G_GetLedgerIdentityRequest())
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

    async def do_commands(
        self,
        commands: Union[Command, Sequence[Command]],
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
        if commands is None:
            return
        elif isinstance(commands, Command):
            commands = [commands]

        stub = CommandServiceStub(self.channel)

        commands_pb = await asyncio.gather(*map(self._codec.encode_command, commands))
        request = G_SubmitAndWaitRequest(
            commands=G_Commands(
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
        template_id: Union[str, TypeConName],
        payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> CreateEvent:
        """
        Create a contract for a given template.

        :param template_id: The template of the contract to be created.
        :param payload: Template arguments for the contract to be created.
        :param workflow_id: An optional workflow ID.
        :param command_id: An optional command ID. If unspecified, a random one will be created.
        """
        stub = CommandServiceStub(self.channel)

        request = G_SubmitAndWaitRequest(
            commands=G_Commands(
                ledger_id=self._config.access.ledger_id,
                application_id=self._config.access.application_name,
                command_id=self._command_id(command_id),
                workflow_id=self._workflow_id(workflow_id),
                party=self._ensure_act_as(),
                commands=[await self._codec.encode_create_command(template_id, payload)],
                act_as=self._config.access.act_as,
                read_as=self._config.access.read_only_as,
            )
        )
        response = await stub.SubmitAndWaitForTransaction(request)

        return await self._codec.decode_created_event(response.transaction.events[0].created)

    async def exercise(
        self,
        contract_id: ContractId,
        choice_name: str,
        argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a contract identified by its contract ID.

        :param contract_id: The contract ID of the contract to exercise.
        :param choice_name: The name of the choice to exercise.
        :param argument: The choice arguments. Can be omitted for choices that take no argument.
        :param workflow_id: An optional workflow ID.
        :param command_id: An optional command ID. If unspecified, a random one will be created.
        :return: A response
        """
        stub = CommandServiceStub(self.channel)

        commands = [await self._codec.encode_exercise_command(contract_id, choice_name, argument)]
        request = self._submit_and_wait_request(commands, workflow_id, command_id)
        response = await stub.SubmitAndWaitForTransactionTree(request)

        return await self._codec.decode_exercise_response(response.transaction)

    async def create_and_exercise(
        self,
        template_id: Union[str, TypeConName],
        payload: ContractData,
        choice_name: str,
        argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> ExerciseResponse:
        stub = CommandServiceStub(self.channel)

        commands = [
            await self._codec.encode_create_and_exercise_command(
                template_id, payload, choice_name, argument
            )
        ]
        request = self._submit_and_wait_request(commands, workflow_id, command_id)
        response = await stub.SubmitAndWaitForTransactionTree(request)

        return await self._codec.decode_exercise_response(response.transaction)

    async def exercise_by_key(
        self,
        template_id: Union[str, TypeConName],
        choice_name: str,
        key: Any,
        argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> "ExerciseResponse":
        stub = CommandServiceStub(self.channel)

        commands = [
            await self._codec.encode_exercise_by_key_command(
                template_id, choice_name, key, argument
            )
        ]
        request = await self._submit_and_wait_request(commands, workflow_id, command_id)
        response = await stub.SubmitAndWaitForTransactionTree(request)

        return await self._codec.decode_exercise_response(response.transaction)

    async def archive(self, contract_id: ContractId) -> ArchiveEvent:
        await self.exercise(contract_id, "Archive")
        return ArchiveEvent(contract_id)

    async def archive_by_key(self, template_id: str, key: Any) -> ArchiveEvent:
        response = await self.exercise_by_key(template_id, "Archive", key)
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
        commands: Collection[G_Command],
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
    ) -> G_SubmitAndWaitRequest:
        return G_SubmitAndWaitRequest(
            commands=G_Commands(
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

    def query(self, template_id: str = "*", query: Query = None) -> QueryStream:
        return QueryStream(self, {template_id: query}, False)

    def query_many(self, queries: Optional[Mapping[str, Query]] = None) -> QueryStream:
        return QueryStream(self, queries, False)

    def stream(self, template_id: str = "*", query: Query = None) -> QueryStream:
        return QueryStream(self, {template_id: query}, True)

    def stream_many(self, queries: Optional[Mapping[str, Query]] = None) -> QueryStream:
        return QueryStream(self, queries, True)

    # endregion

    # region Party Management calls

    async def allocate_party(
        self, identifier_hint: str = None, display_name: str = None
    ) -> "PartyInfo":
        """
        Allocate a new party.
        """
        stub = PartyManagementServiceStub(self.channel)
        request = G_AllocatePartyRequest(party_id_hint=identifier_hint, display_name=display_name)
        response = await stub.AllocateParty(request)
        return Codec.decode_party_info(response.party_details)

    async def list_known_parties(self) -> Sequence[PartyInfo]:
        stub = PartyManagementServiceStub(self.channel)
        response = await stub.ListKnownParties()
        return [Codec.decode_party_info(pd) for pd in response.party_details]

    # endregion

    # region Package Management calls

    async def get_package(self, package_id: PackageRef) -> bytes:
        stub = PackageServiceStub(self.channel)
        request = G_GetPackageRequest(
            ledger_id=self._config.access.ledger_id, package_id=str(package_id)
        )
        response = await stub.GetPackage(request)
        return response.archive_payload

    async def list_package_ids(self) -> AbstractSet[PackageRef]:
        stub = PackageServiceStub(self.channel)
        request = G_ListPackagesRequest(ledger_id=self._config.access.ledger_id)
        response = await stub.ListPackages(request)
        return frozenset({PackageRef(pkg_id) for pkg_id in response.package_ids})

    async def upload_package(self, contents: bytes) -> None:
        stub = PackageManagementServiceStub(self.channel)
        request = G_UploadDarFileRequest(dar_file=contents)
        await stub.UploadDarFile(request)
        return

    # endregion


class QueryStream(QueryStreamBase):
    def __init__(
        self,
        conn: Connection,
        queries: Optional[Mapping[str, Query]],
        continue_stream: bool,
    ):
        self.conn = conn
        self._queries = queries
        self._continue_stream = continue_stream

        self._offset = None
        self._filter = None
        self._response_stream = None

    async def close(self) -> None:
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
        filters = await self.conn.codec.encode_filters(self._queries)
        filters_by_party = {party: filters for party in self.conn.config.access.read_as}
        tx_filter_pb = G_TransactionFilter(filters_by_party=filters_by_party)

        try:
            offset = None
            async for event in self._acs_events(tx_filter_pb):
                if isinstance(event, CreateEvent):
                    await self._emit_create(event)
                elif isinstance(event, Boundary):
                    offset = event.offset
                    await self._emit_boundary(event)
                else:
                    warnings.warn(f"Received an unknown event: {event}", ProtocolWarning)
                yield event

            if self._continue_stream:
                # now start returning events as they come off the transaction stream; note this
                # stream will never naturally close, so it's on the caller to call close() or to
                # otherwise exit our current context
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
        finally:
            await self.close()

    async def _acs_events(
        self, filter_pb: G_TransactionFilter
    ) -> AsyncIterable[Union[CreateEvent, Boundary]]:
        stub = ActiveContractsServiceStub(self.conn.channel)

        request = G_GetActiveContractsRequest(
            ledger_id=self.conn.config.access.ledger_id, filter=filter_pb
        )
        self._response_stream = stub.GetActiveContracts(request)

        offset = None
        async for response in self._response_stream:
            for event in response.active_contracts:
                yield await self.conn.codec.decode_created_event(event)
            # for ActiveContractSetResponse messages, only the last offset is actually relevant
            offset = response.offset
        yield Boundary(offset)

    async def _tx_events(
        self, filter_pb: G_TransactionFilter, begin_offset: Optional[str]
    ) -> AsyncIterable[Union[CreateEvent, ArchiveEvent, Boundary]]:
        stub = TransactionServiceStub(self.conn.channel)

        request = G_GetTransactionsRequest(
            ledger_id=self.conn.config.access.ledger_id,
            filter=filter_pb,
            begin=self.conn.codec.encode_begin_offset(begin_offset),
        )

        self._response_stream = stub.GetTransactions(request)
        async for response in self._response_stream:
            for event in response.events:
                event_type = event.WhichOneof("event")
                if event_type == "created":
                    yield await self.conn.codec.decode_created_event(event.created)
                elif event_type == "archived":
                    yield await self.conn.codec.decode_archived_event(event.archived)
                else:
                    warnings.warn(f"Unknown Event({event_type}=...)", ProtocolWarning)
            yield Boundary(response.offset)
