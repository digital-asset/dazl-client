# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This module contains the mapping between gRPC calls and Python/dazl types.
"""

from __future__ import annotations

import asyncio
from asyncio import wait_for
import contextlib
from datetime import datetime, timedelta
import sys
from typing import (
    AbstractSet,
    Any,
    AsyncIterable,
    Collection,
    ContextManager,
    Iterator,
    Mapping,
    Optional,
    Sequence,
    overload,
)
import warnings

from grpc import ChannelConnectivity
from grpc.aio import Channel, UnaryStreamCall, UsageError

from .. import aio
from ... import LOG
from ..._gen.com.daml.ledger.api import v1 as lapipb
from ..._gen.com.daml.ledger.api.v1 import admin as lapiadminpb
from ...damlast.daml_lf_1 import PackageRef, TypeConName
from ...damlast.util import is_match
from ...prim import (
    ContractData,
    ContractId,
    Parties,
    Party,
    TimeDeltaLike,
    datetime_to_timestamp,
    to_parties,
    to_timedelta,
)
from ...query import Filter, Queries, Query, parse_query
from .._call import (
    AnyCallParameters,
    CachedParameters,
    CallParameters,
    ConnectionParameters,
    ReadCallParameters,
    WriteCallParameters,
)
from .._offsets import END, End, LedgerOffsetRange, from_offset_until_forever
from .._retry import retry
from ..api_types import (
    ArchiveEvent,
    Boundary,
    CommandMeta,
    Commands,
    CreateEvent,
    ExerciseResponse,
    MeteringReport,
    PartyInfo,
    Right,
    User,
    Version,
    to_commands,
)
from ..auth import TokenOrTokenProvider
from ..config import Config
from ..errors import ProtocolWarning, _allow_cancel, _translate_exceptions
from ._args_aio import CallContext
from .channel import create_channel
from .codec_aio import Codec

if sys.version_info >= (3, 11):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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
        self._cache: Optional[CachedParameters] = None

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

    async def __aenter__(self) -> Connection:
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def open(self) -> None:
        """
        Does nothing, and is only supplied for symmetry with :meth:`close`.
        """

    async def close(self) -> None:
        """
        Close the underlying channel. Once the channel is closed, future command submissions,
        streams in progress, and any future streams will fail.
        """
        # TODO: grpc-stubs have a bug here; close does not require a parameter
        await self._channel.close()  # type: ignore

    def _retry_timeout(self, timeout: Optional[TimeDeltaLike]) -> timedelta:
        return to_timedelta(timeout) if timeout is not None else self._config.url.retry_timeout

    # region Write API

    @overload
    def _call(self, **kwargs: Unpack[CallParameters]) -> ContextManager[CallContext]: ...

    @overload
    def _call(self, **kwargs: Unpack[ReadCallParameters]) -> ContextManager[CallContext]: ...

    @overload
    def _call(self, **kwargs: Unpack[WriteCallParameters]) -> ContextManager[CallContext]: ...

    @contextlib.contextmanager
    def _call(self, **call_kwargs: Unpack[AnyCallParameters]) -> Iterator[CallContext]:
        connection_params = ConnectionParameters(
            read_as=to_parties(self._config.access.read_as),
            act_as=to_parties(self._config.access.act_as),
            ledger_id=self._config.access.ledger_id,
            user_id_or_application_name=self._config.access.user_id
            or self._config.access.application_name,
            token=self._config.access.token,
            timeout=self._config.url.retry_timeout,
        )
        call = CallContext.compute(call_kwargs, self._cache, connection_params)
        call.channel = self.channel
        yield call
        self._cache = call.get_cache()

    async def submit(
        self,
        commands: Commands,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        application_name: Optional[str] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
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
        with self._call(
            workflow_id=workflow_id,
            command_id=command_id,
            read_as=read_as,
            act_as=act_as,
            application_name=application_name,
            user_id=user_id,
            token=token,
            timeout=timeout,
        ) as call:
            commands = to_commands(commands)
            if not commands:
                return

            if len(commands) == 1:
                command_seq = [await self._codec.encode_command(commands[0], token=token)]
            else:
                command_seq = await asyncio.gather(
                    *(self._codec.encode_command(command, token=token) for command in commands)
                )

            stub = call.grpc_stub(lapipb.CommandServiceStub)
            request = self._submit_and_wait_request(command_seq, await call.command_meta())
            await retry(
                lambda: stub.SubmitAndWait(request, **call.grpc_kwargs),
                timeout=call.timeout,
            )

    async def create(
        self,
        template_id: str | TypeConName,
        payload: ContractData,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        application_name: Optional[str] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> CreateEvent:
        """
        Create a contract for a given template.

        :param template_id:
            The template of the contract to be created.
        :param payload:
            Template arguments for the contract to be created.
        :param workflow_id:
            An optional workflow ID.
        :param command_id:
            An optional command ID. If unspecified, a random one will be created.
        :param token:
            An optional authorization token. If unspecified, the one specified at connection
            creation time is used.
        :param read_as:
            An optional set of read-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param act_as:
            An optional set of act-as parties to use to submit this command. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param application_name:
            An optional application name to use instead of the one configured at connection
            creation time. Cannot be specified with ``user_id``.
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``. Cannot be specified with
            ``application_name``.
        :param timeout:
            The length of time to wait before giving up on this submission. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        :return:
            The :class:`CreateEvent` that represents the contract that was successfully created.
        """
        with self._call(
            workflow_id=workflow_id,
            command_id=command_id,
            read_as=read_as,
            act_as=act_as,
            application_name=application_name,
            user_id=user_id,
            token=token,
            timeout=timeout,
        ) as call:
            commands = [
                lapipb.Command(
                    create=await self._codec.encode_create_command(
                        template_id, payload, token=token
                    )
                )
            ]

            stub = call.grpc_stub(lapipb.CommandServiceStub)
            request = self._submit_and_wait_request(commands, await call.command_meta())
            response = await retry(
                lambda: stub.SubmitAndWaitForTransaction(request, **call.grpc_kwargs),
                timeout=call.timeout,
            )
            return await self._codec.decode_created_event(
                response.transaction.events[0].created, token=token
            )

    async def exercise(
        self,
        contract_id: ContractId,
        choice_name: str,
        argument: Optional[ContractData] = None,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        application_name: Optional[str] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a contract identified by its contract ID.

        :param contract_id:
            The contract ID of the contract to exercise.
        :param choice_name:
            The name of the choice to exercise.
        :param argument:
            The choice arguments. Can be omitted for choices that take no argument.
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
        :param application_name:
            An optional application name to use instead of the one configured at connection
            creation time. Cannot be specified with ``user_id``.
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``. Cannot be specified with
            ``application_name``.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on this submission. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        with self._call(
            workflow_id=workflow_id,
            command_id=command_id,
            read_as=read_as,
            act_as=act_as,
            application_name=application_name,
            user_id=user_id,
            token=token,
            timeout=timeout,
        ) as call:
            commands = [
                lapipb.Command(
                    exercise=await self._codec.encode_exercise_command(
                        contract_id, choice_name, argument, token=call.token
                    )
                )
            ]

            stub = call.grpc_stub(lapipb.CommandServiceStub)
            request = self._submit_and_wait_request(commands, await call.command_meta())
            response = await retry(
                lambda: stub.SubmitAndWaitForTransactionTree(request, **call.grpc_kwargs),
                timeout=call.timeout,
            )
            return await self._codec.decode_exercise_response(
                response.transaction, token=call.token
            )

    async def create_and_exercise(
        self,
        template_id: str | TypeConName,
        payload: ContractData,
        choice_name: str,
        argument: Optional[ContractData] = None,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        application_name: Optional[str] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a newly-created contract, in a single transaction.

        :param template_id:
            The template of the contract to be created (positional argument only).
        :param payload:
            Template arguments for the contract to be created (positional argument only).
        :param choice_name:
            The name of the choice to exercise (positional argument only).
        :param argument:
            The choice arguments. Can be omitted for choices that take no argument (positional
            argument only).
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
        :param application_name:
            An optional application name to use instead of the one configured at connection
            creation time. Cannot be specified with ``user_id``.
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``. Cannot be specified with
            ``application_name``.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on this submission. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        with self._call(
            workflow_id=workflow_id,
            command_id=command_id,
            read_as=read_as,
            act_as=act_as,
            application_name=application_name,
            user_id=user_id,
            token=token,
            timeout=timeout,
        ) as call:
            commands = [
                lapipb.Command(
                    createAndExercise=await self._codec.encode_create_and_exercise_command(
                        template_id, payload, choice_name, argument, token=call.token
                    )
                )
            ]

            stub = call.grpc_stub(lapipb.CommandServiceStub)
            request = self._submit_and_wait_request(commands, await call.command_meta())
            response = await retry(
                lambda: stub.SubmitAndWaitForTransactionTree(request, **call.grpc_kwargs),
                timeout=call.timeout,
            )
            return await self._codec.decode_exercise_response(
                response.transaction, token=call.token
            )

    async def exercise_by_key(
        self,
        template_id: str | TypeConName,
        choice_name: str,
        key: Any,
        argument: Optional[ContractData] = None,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        application_name: Optional[str] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> ExerciseResponse:
        """
        Exercise a choice on a contract identified by its contract key.

        :param template_id:
            The template of the contract to be created (positional argument only).
        :param choice_name:
            The name of the choice to exercise.
        :param key:
            The key of the contract to exercise.
        :param argument:
            The choice arguments. Can be omitted for choices that take no argument.
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
        :param application_name:
            An optional application name to use instead of the one configured at connection
            creation time. Cannot be specified with ``user_id``.
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``. Cannot be specified with
            ``application_name``.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on this submission. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        with self._call(
            workflow_id=workflow_id,
            command_id=command_id,
            read_as=read_as,
            act_as=act_as,
            application_name=application_name,
            user_id=user_id,
            token=token,
            timeout=timeout,
        ) as call:
            commands = [
                lapipb.Command(
                    exerciseByKey=await self._codec.encode_exercise_by_key_command(
                        template_id, choice_name, key, argument, token=call.token
                    )
                )
            ]

            stub = call.grpc_stub(lapipb.CommandServiceStub)
            request = self._submit_and_wait_request(commands, await call.command_meta())
            response = await stub.SubmitAndWaitForTransactionTree(request, **call.grpc_kwargs)

            return await self._codec.decode_exercise_response(
                response.transaction, token=call.token
            )

    async def archive(
        self,
        contract_id: ContractId,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        application_name: Optional[str] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> ArchiveEvent:
        """
        Archive a choice on a contract identified by its contract ID.

        :param contract_id:
            The contract ID of the contract to exercise.
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
        :param application_name:
            An optional application name to use instead of the one configured at connection
            creation time. Cannot be specified with ``user_id``.
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``. Cannot be specified with
            ``application_name``.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on this submission. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        :return:
            The :class:`ArchiveEvent` that indicates this contract was archived.
        """
        await self.exercise(
            contract_id,
            "Archive",
            workflow_id=workflow_id,
            command_id=command_id,
            read_as=read_as,
            act_as=act_as,
            application_name=application_name,
            user_id=user_id,
            token=token,
            timeout=timeout,
        )
        return ArchiveEvent(contract_id)

    async def archive_by_key(
        self,
        template_id: str,
        key: Any,
        /,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Optional[Parties] = None,
        act_as: Optional[Parties] = None,
        application_name: Optional[str] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> ArchiveEvent:
        """
        Exercise a choice on a contract identified by its contract key.

        :param template_id:
            The template of the contract to be created (positional argument only).
        :param key:
            The key of the contract to exercise.
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
        :param application_name:
            An optional application name to use instead of the one configured at connection
            creation time. Cannot be specified with ``user_id``.
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``. Cannot be specified with
            ``application_name``.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on this submission. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        :return:
            The return value of the choice, together with a list of events that occurred as a result
            of exercising the choice.
        """
        response = await self.exercise_by_key(
            template_id,
            "Archive",
            key,
            workflow_id=workflow_id,
            command_id=command_id,
            read_as=read_as,
            act_as=act_as,
            application_name=application_name,
            user_id=user_id,
            token=token,
            timeout=timeout,
        )
        return next(iter(event for event in response.events if isinstance(event, ArchiveEvent)))

    def _submit_and_wait_request(
        self,
        commands: Collection[lapipb.Command],
        meta: CommandMeta,
        /,
        ledger_id: Optional[str] = None,
    ) -> lapipb.SubmitAndWaitRequest:
        return lapipb.SubmitAndWaitRequest(
            commands=lapipb.Commands(
                ledger_id=ledger_id,
                application_id=meta.application_name,
                command_id=meta.command_id,
                workflow_id=meta.workflow_id,
                commands=commands,
                act_as=meta.act_as,
                read_as=meta.read_as,
            )
        )

    # endregion

    # region Read API

    async def get_ledger_end(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> str:
        """
        Return the offset at the end of the ledger.

        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on this submission. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        """
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapipb.TransactionServiceStub)
            request = lapipb.GetLedgerEndRequest(ledger_id=call.ledger_id)
            response = await retry(
                lambda: stub.GetLedgerEnd(request, **call.grpc_kwargs),
                timeout=call.timeout,
            )
            return response.offset.absolute

    def query(
        self,
        template_or_interface_id: str | TypeConName = "*",
        query: Query = None,
        /,
        *,
        begin_offset: Optional[str] = None,
        end_offset: Optional[str] = None,
        read_as: Optional[Parties] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> QueryStream:
        """
        Return the create events from the active contract set service as a stream.

        If you find yourself repeatedly calling :meth:`query` or :meth:`query_many` over the same
        set of templates, you may want to consider :class:`ACS` instead, which is a utility class
        that helps you maintain a "live" state of the ACS.

        :param template_or_interface_id:
            The name of the template or interface for which to fetch contracts.
        :param query:
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
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on a query. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        """
        with self._call(read_as=read_as, user_id=user_id, token=token, timeout=timeout) as call:
            offset = LedgerOffsetRange(begin_offset, end_offset if end_offset is not None else END)
            return QueryStream(
                self,
                parse_query({template_or_interface_id: query}, server_side_filters=False),
                offset,
                call,
            )

    def query_many(
        self,
        *queries: Queries,
        begin_offset: Optional[str] = None,
        end_offset: Optional[str] = None,
        read_as: Optional[Parties] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> QueryStream:
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
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on a query. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        """
        with self._call(read_as=read_as, user_id=user_id, token=token, timeout=timeout) as call:
            offset = LedgerOffsetRange(begin_offset, end_offset if end_offset is not None else END)

            return QueryStream(
                self,
                parse_query(*queries, server_side_filters=False),
                offset,
                call,
            )

    def stream(
        self,
        template_or_interface_id: str | TypeConName = "*",
        query: Query = None,
        /,
        *,
        offset: Optional[str] = None,
        read_as: Optional[Parties] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> QueryStream:
        """
        Stream create/archive events.

        When ``offset`` is ``None``, create events from the active contract set are returned first,
        followed by a continuous stream of updates (creates/archives).

        Otherwise, ``offset`` can be supplied to resume a stream from a prior point where a
        ``Boundary`` was returned from a previous stream.

        :param template_or_interface_id:
            The name of the template or interface for which to fetch contracts.
        :param query:
            A filter to apply to the set of returned contracts. Note that this does not filter
            :class:`ArchiveEvent`; readers of the stream MUST be able to cope with "mismatched"
            archives that come from the result of applying a filter.
        :param offset:
            An optional offset at which to start receiving events. If ``None``, start from the
            beginning.
        :param read_as:
            An optional set of read-as parties to use to submit this query. Note that for a
            ledger with authorization, these parties must be a subset of the parties in the token.
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on a query. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        """
        with self._call(read_as=read_as, user_id=user_id, token=token, timeout=timeout) as call:
            return QueryStream(
                self,
                parse_query({template_or_interface_id: query}, server_side_filters=False),
                from_offset_until_forever(offset),
                call,
            )

    def stream_many(
        self,
        *queries: Queries,
        offset: Optional[str] = None,
        read_as: Optional[Parties] = None,
        user_id: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> QueryStream:
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
        :param user_id:
            An optional user ID to use instead of the one configured at connection creation time
            or from the ``sub`` claim of the ``token``.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The length of time to wait before giving up on a query. If unspecified, the
            configuration value of ``retry_timeout`` is used.
        """
        with self._call(read_as=read_as, user_id=user_id, token=token, timeout=timeout) as call:
            return QueryStream(
                self,
                parse_query(*queries, server_side_filters=False),
                from_offset_until_forever(offset),
                call,
            )

    # endregion

    async def get_version(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> Version:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapipb.VersionServiceStub)
            request = lapipb.GetLedgerApiVersionRequest(ledger_id=call.ledger_id)

            response = await retry(
                lambda: stub.GetLedgerApiVersion(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return Codec.decode_version(response)

    # region User Management calls

    async def get_user(
        self,
        user_id: Optional[str] = None,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> User:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapiadminpb.UserManagementServiceStub)
            request = lapiadminpb.GetUserRequest(user_id=user_id)
            response = await retry(
                lambda: stub.GetUser(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return Codec.decode_user(response.user)

    async def create_user(
        self,
        user: User,
        rights: Optional[Sequence[Right]] = None,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> User:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapiadminpb.UserManagementServiceStub)
            request = lapiadminpb.CreateUserRequest(user=Codec.encode_user(user))
            if rights is not None:
                request.rights.extend(Codec.encode_right(right) for right in rights)
            response = await retry(
                lambda: stub.CreateUser(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return Codec.decode_user(response.user)

    async def list_users(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> Sequence[User]:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapiadminpb.UserManagementServiceStub)
            request = lapiadminpb.ListUsersRequest()
            response = await retry(
                lambda: stub.ListUsers(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return [Codec.decode_user(user) for user in response.users]

    async def list_user_rights(
        self,
        user_id: Optional[str] = None,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> Sequence[Right]:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapiadminpb.UserManagementServiceStub)
            request = lapiadminpb.ListUserRightsRequest(user_id=user_id)
            response = await retry(
                lambda: stub.ListUserRights(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return [Codec.decode_right(user) for user in response.rights]

    # endregion

    # region Party Management calls

    async def allocate_party(
        self,
        *,
        identifier_hint: Optional[str] = None,
        display_name: Optional[str] = None,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> PartyInfo:
        """
        Allocate a new party.
        """
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapiadminpb.PartyManagementServiceStub)
            request = lapiadminpb.AllocatePartyRequest(
                party_id_hint=Party(identifier_hint) if identifier_hint else None,
                display_name=display_name,
            )
            response = await retry(
                lambda: stub.AllocateParty(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return Codec.decode_party_info(response.party_details)

    async def list_known_parties(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> Sequence[PartyInfo]:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapiadminpb.PartyManagementServiceStub)
            request = lapiadminpb.ListKnownPartiesRequest()
            response = await retry(
                lambda: stub.ListKnownParties(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return [Codec.decode_party_info(pd) for pd in response.party_details]

    # endregion

    # region Package Management calls

    async def get_package(
        self,
        package_id: PackageRef,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> bytes:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapipb.PackageServiceStub)
            request = lapipb.GetPackageRequest(ledger_id=call.ledger_id, package_id=package_id)

            response = await retry(
                lambda: stub.GetPackage(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return response.archive_payload

    async def list_package_ids(
        self,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> AbstractSet[PackageRef]:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapipb.PackageServiceStub)
            request = lapipb.ListPackagesRequest(ledger_id=call.ledger_id)
            response = await retry(
                lambda: stub.ListPackages(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return frozenset({PackageRef(pkg_id) for pkg_id in response.package_ids})

    async def upload_package(
        self,
        contents: bytes,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> None:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapiadminpb.PackageManagementServiceStub)
            request = lapiadminpb.UploadDarFileRequest(dar_file=contents)
            await retry(
                lambda: stub.UploadDarFile(request, **call.grpc_kwargs), timeout=call.timeout
            )

            # assuming the package has been uploaded, go ahead and load that locally too
            await self._codec.preload(contents)

    # endregion

    # region Metering Report calls

    async def get_metering_report(
        self,
        from_: datetime,
        to: Optional[datetime] = None,
        application_id: Optional[str] = None,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> MeteringReport:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapiadminpb.MeteringReportServiceStub)

            # This slightly awkward construction is due to Protobuf's Python type not escaping field
            # names that happen to match keywords. Unfortunately mypy can't follow what is going on
            # when we do this, so we must be careful!
            kwargs = {"from": datetime_to_timestamp(from_)}  # type: dict[str, Any]
            if to is not None:
                kwargs["to"] = datetime_to_timestamp(to)
            if application_id is not None:
                kwargs["application_id"] = application_id
            request = lapiadminpb.GetMeteringReportRequest(**kwargs)  # type: ignore

            response = await retry(
                lambda: stub.GetMeteringReport(request, **call.grpc_kwargs), timeout=call.timeout
            )
            return Codec.decode_get_metering_report_response(response)

    # endregion

    # region Miscellaneous admin calls

    async def prune(
        self,
        up_to: str,
        submission_id: Optional[str] = None,
        prune_all_divulged_contracts=False,
        *,
        token: Optional[TokenOrTokenProvider] = None,
        timeout: Optional[TimeDeltaLike] = None,
    ) -> None:
        with self._call(token=token, timeout=timeout) as call:
            stub = call.grpc_stub(lapiadminpb.ParticipantPruningServiceStub)

            request = lapiadminpb.PruneRequest(
                prune_up_to=up_to,
                submission_id=submission_id,
                prune_all_divulged_contracts=prune_all_divulged_contracts,
            )
            await retry(lambda: stub.Prune(request, **call.grpc_kwargs), timeout=call.timeout)

    # endregion


class QueryStream(aio.QueryStreamBase):
    def __init__(
        self,
        conn: Connection,
        filters: Optional[Mapping[TypeConName, Filter]],
        offset_range: LedgerOffsetRange,
        call: CallContext,
    ):
        self.conn = conn
        self._filters = filters
        self._offset_range = offset_range
        self._call = call
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
            try:
                self._response_stream.cancel()
            except UsageError:
                # doesn't matter if we're closed when...we're trying to close
                pass
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
            # the token may change over time, but fix the "read_as" parties at the start,
            # even if those rights are changed over time
            read_as = await self._call.get_read_as()
            filters = await self.conn.codec.encode_filters(self._filters, token=self._call.token)
            filters_by_party = {party: filters for party in read_as}
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
                    match event:
                        case CreateEvent():
                            await self._emit_create(event)
                        case Boundary():
                            await self._emit_boundary(event)
                            offset = event.offset
                        case _:
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
            log.debug("Reading a transaction stream: %s to %s", offset, self._offset_range.end)
            async for event in self._tx_events(tx_filter_pb, offset, self._offset_range.end):
                log.debug("Received an event: %s", event)
                match event:
                    case CreateEvent():
                        await self._emit_create(event)
                    case ArchiveEvent():
                        await self._emit_archive(event)
                    case Boundary():
                        await self._emit_boundary(event)
                    case _:
                        warnings.warn(f"Received an unknown event: {event}", ProtocolWarning)
                yield event

    async def _acs_events(
        self, filter_pb: lapipb.TransactionFilter
    ) -> AsyncIterable[CreateEvent | Boundary]:
        stub = self._call.grpc_stub(lapipb.ActiveContractsServiceStub)
        request = lapipb.GetActiveContractsRequest(ledger_id=self._call.ledger_id, filter=filter_pb)
        self._response_stream = response_stream = stub.GetActiveContracts(
            request,
            **self._call.grpc_kwargs,
        )

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
                response = await wait_for(i.__anext__(), timeout=self._call.timeout_seconds)
            except StopAsyncIteration:
                break

            LOG.debug(
                "ACS start (offset %r, %d event(s))",
                response.offset,
                len(response.active_contracts),
            )
            for event in response.active_contracts:
                c_evt = await self.conn.codec.decode_created_event(event, token=self._call.token)
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
        end_offset: Optional[str | End],
    ) -> AsyncIterable[CreateEvent | ArchiveEvent | Boundary]:
        stub = self._call.grpc_stub(lapipb.TransactionServiceStub)

        last_offset = begin_offset

        while True:
            request = lapipb.GetTransactionsRequest(
                ledger_id=self._call.ledger_id,
                filter=filter_pb,
                begin=self.conn.codec.encode_begin_offset(last_offset),
                end=self.conn.codec.encode_end_offset(end_offset),
            )

            self._response_stream = response_stream = stub.GetTransactions(
                request,
                **self._call.grpc_kwargs,
            )
            i = response_stream.__aiter__()

            while True:
                try:
                    response = await wait_for(i.__anext__(), timeout=self._call.timeout_seconds)
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
                    await self.conn.get_ledger_end(
                        token=self._call.token, timeout=self._call.timeout
                    )

                    # abort the loop in which we read events from a stream, and start over again
                    # trying to establish a stream connection
                    break

                for tx in response.transactions:
                    for event in tx.events:
                        event_type = event.WhichOneof("event")
                        if event_type == "created":
                            c_evt = await self.conn.codec.decode_created_event(
                                event.created, token=self._call.token
                            )
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

        # TODO: We checked every name, but none of them matched. This means we received an event for an
        #  unexpected template name, and that could happen if the query was _interface_ based, as
        #  opposed to _template_ based. For now, return True so that interface-based queries work at all,
        #  but a better fix would be to check templates against a filter on the interface. This requires
        #  us to have a bit more intelligence about the types coming over the wire.
        return True
