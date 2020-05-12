# Copyright (c) 2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Implementation of a connection to the pre-v1.0 DAML SDK gRPC Ledger API endpoints.
"""

from threading import RLock
from typing import Any, Callable, Dict, Optional, Tuple

from .._gen.com.digitalasset.ledger.api.v1.value_pb2 import \
    Record as G_Record, \
    Record as G_Record, \
    Record as G_Record, \
    Enum as G_Enum, \
    GenMap as G_GenMap, \
    List as G_List, \
    Map as G_TextMap, \
    Optional as G_Optional, \
    Record as G_Record, \
    Variant as G_Variant
from .._gen.com.digitalasset.ledger.api.v1.commands_pb2 import \
    Command as G_Command, \
    Commands as G_Commands, \
    CreateCommand as G_CreateCommand, \
    CreateAndExerciseCommand as G_CreateAndExerciseCommand, \
    ExerciseCommand as G_ExerciseCommand, \
    ExerciseByKeyCommand as G_ExerciseByKeyCommand
from .._gen.com.digitalasset.ledger.api.v1.command_service_pb2 import \
    SubmitAndWaitRequest as G_SubmitAndWaitRequest
from .._gen.com.digitalasset.ledger.api.v1.command_service_pb2_grpc import \
    CommandServiceStub as G_CommandService
from .._gen.com.digitalasset.ledger.api.v1.ledger_identity_service_pb2 import \
    GetLedgerIdentityRequest as G_GetLedgerIdentityRequest
from .._gen.com.digitalasset.ledger.api.v1.ledger_identity_service_pb2_grpc import \
    LedgerIdentityServiceStub as G_LedgerIdentityService

from ..damlast.ledger_api import ValueSerializer, CommandSerializer
from ..damlast import ledger_api as api
from ..protocols.v1.pb_ser_command import pb_get_timestamp

from .. import LOG
from ..model.core import Party
from ..model.reading import \
    ContractCreateEvent, ContractExercisedEvent, ContractArchiveEvent
from ..model.writing import \
    CommandPayload, CreateCommand, CreateAndExerciseCommand, ExerciseCommand, ExerciseByKeyCommand
from .interfaces import LedgerConnectionPool, BlockingLedgerConnection


def create_channel(url: str, auth_token: 'Optional[str]') -> 'GRPCLedgerConnection':
    import grpc
    return grpc.insecure_channel(url)


class GRPCLedgerConnectionPool(LedgerConnectionPool):

    def __init__(self):
        self._connections = {}  # type: Dict[Tuple[str, str], Tuple[GRPCLedgerConnection, int]]
        self._lock = RLock()

    def connect(
            self, url: str, auth_token: 'Optional[str]' = None, party: 'Optional[Party]' = None) \
            -> 'GRPCLedgerConnection':
        with self._lock:
            channel, count = self._connections.get((url, auth_token), (None, 0))
            if channel is None:
                channel = create_channel(url, auth_token)

            self._connections[(url, auth_token)] = channel, count + 1

            return GRPCLedgerConnection(
                channel, auth_token=auth_token, party=party,
                on_close=lambda: self._release(url, auth_token))

    def _release(self, url: str, auth_token: 'Optional[str]') -> None:
        """
        Mark the gRPC channel for the given URL and auth token as invalid. This should NOT be called
        externally as it will almost certainly lead to connections being closed too early otherwise.
        """
        with self._lock:
            channel, count = self._connections.get((url, auth_token), (None, 0))
            if channel is None:
                LOG.warning("A connection to %s is being over-released", url)
            count -= 1
            if count == 0:
                del self._connections[(url, auth_token)]
                LOG.info("Closing the underlying channel for %s...")
                channel.close()


class GRPCLedgerConnection(BlockingLedgerConnection):
    def __init__(
            self,
            channel,
            party: 'Optional[Party]' = None,
            on_close: 'Optional[Callable[[], None]]' = None):
        self.channel = channel
        self.party = party
        self.on_close = on_close
        self._ledger_id = None  # type: Optional[str]

    def get_ledger_id(self) -> str:
        """
        Retrieve the ledger ID from the gRPC API endpoint.
        """
        if self._ledger_id is not None:
            service = G_LedgerIdentityService(self.channel)

            request = G_GetLedgerIdentityRequest()
            response = service.GetLedgerIdentity(request)

            self._ledger_id = response.ledger_id
        return self._ledger_id

    def submit(self, command: 'CommandPayload') -> None:
        service = G_CommandService(self.channel)

        request = G_SubmitAndWaitRequest(commands=G_Commands(
            ledger_id=self.get_ledger_id(),
            workflow_id=command.workflow_id,
            application_id=command.application_id,
            command_id=command.command_id,
            party=,
            commands=,
            ledger_effective_time=,
            maximum_record_time=
        ))
        _ = service.SubmitAndWait(request)

    def submit_create(self, command: 'CreateCommand') -> 'ContractCreateEvent':
        service = G_CommandService(self.channel)

        request = G_SubmitAndWaitRequest()
        response = service.SubmitAndWaitForTransaction(request)

        for tx in response.transaction:
            tx.events:

    def close(self):
        if self.on_close is not None:
            self.on_close()
        else:
            self.channel.close()


class GRPCCommandSerializer(CommandSerializer):

    def __init__(self):
        self.target = G_Commands()

    def write_create_command(self, command: 'CreateCommand'):
        api_type = self.types.find_api_type(command.template)
        self.target = G_Command(create=G_CreateCommand(
            template_id=command.template))

        self.value_serializer(self.target.create_arguments) \
            .write_record(api_type, command.arguments)

    def write_create_and_exercise_command(self, command: 'CreateAndExerciseCommand'):
        api_type = self.types.find_api_type(command.template)
        self.target = G_Command(create=G_ExerciseCommand(
            template_id=command.template,
            create_arguments=command.arguments))

        vs = self.value_serializer(self.target.create_arguments)
        vs.write_value(api_type, command.arguments)

    def write_exercise_command(self, command: 'ExerciseCommand'):
        api_type = self.types.find_api_type(command.template)
        self.target = G_Command(create=G_ExerciseCommand(
            template_id=command.template,
            create_arguments=command.arguments))

        vs = self.value_serializer(self.target.create_arguments)
        vs.write_value(api_type, command.arguments)

    def value_serializer(self, target) -> 'GRPCValueSerializer':
        return GRPCValueSerializer(self.types, "$", target)


class GRPCValueSerializer(ValueSerializer):

    def write_record(self, api_type: 'api.RecordType', obj: 'Any') -> None:
        self.target.record = G_Record()
        for name in api_type.field_names():
            field = self.target.record.fields.add()
            field.label = name

            serializer = self.descend(f'{self.path}.{name}', field)
            serializer.write_value(api_type.field_type(name), obj.get(name))

    def write_variant(self, api_type: 'api.VariantType', obj: 'Any') -> None:
        ctor, value = to_variant(obj)

        self.target.variant = G_Variant()
        self.target.variant.constructor = ctor

        serializer = self.descend(f'{self.path}.{ctor}', self.target.variant.value)
        serializer.write_value(api_type.field_type(ctor), value)

    def write_contract_id(self, _, obj):
        from ..util.prim_types import to_str
        self.target.contract_id = to_str(obj)

    def write_list(self, api_type: 'api.ListType', obj: 'Any') -> None:
        self.target.list = G_List()
        for i, item in enumerate(obj):
            value = self.target.list.elements.add()
            serializer = self.descend(f'{self.path}[{i}]', value)
            serializer.write_value(api_type.arg_type, item)

    def write_int(self, _, obj: Any) -> None:
        from ..util.prim_types import to_int
        self.target.int64 = to_int(obj)

    def write_numeric(self, _, obj: Any) -> None:
        from ..util.prim_types import to_decimal
        self.target.numeric = str(to_decimal(obj))

    def write_text(self, _, obj: Any) -> None:
        from ..util.prim_types import to_str
        self.target.text = to_str(obj)

    def write_datetime(self, _, obj: Any) -> None:
        from ..util.prim_types import to_datetime
        self.target.timestamp = pb_get_timestamp(to_datetime(obj))

    def write_party(self, _: 'api.PartyType', obj: 'Any') -> None:
        from ..util.prim_types import to_str
        self.target.party = to_str(obj)

    def write_bool(self, _: 'api.BoolType', obj: 'Any') -> None:
        from ..util.prim_types import to_boolean
        self.target.party = to_boolean(obj)

    def write_unit(self, _: 'api.UnitType', obj: 'Any') -> None:
        from google.protobuf.empty_pb2 import Empty
        self.target.unit = Empty()

    def write_date(self, _: 'api.DateType', obj: 'Any') -> None:
        from ..util.prim_types import to_date
        self.target.date = pb_get_date(to_date(obj))

    def write_optional(self, api_type: 'api.OptionalType', obj: 'Any') -> None:
        self.target.optional = G_Optional()
        if obj is not None:
            serializer = self.descend(self.path + "?", self.target.optional.value)
            serializer.write_value(api_type.arg_type, obj)

    def write_textmap(self, api_type: 'api.TextMapType', obj: 'Any') -> None:
        from ..util.prim_types import to_str
        self.target.map = G_TextMap()
        for key, value in obj.items():
            key_str = to_str(key)
            entry_pb = self.target.map.entries.add()
            entry_pb.key = key_str
            vs = self.descend(f'{self.path}[{key_str!r}]', entry_pb.value)
            vs.write_value(api_type.arg_type, value)

    def write_enum(self, api_type: 'api.EnumType', obj: 'Any') -> None:
        from ..util.prim_types import to_str
        self.target.enum = G_Enum()
        self.target.enum.constructor = to_str(obj)

    def write_genmap(self, api_type: 'api.GenMapType', obj: 'Any') -> None:
        self.target.gen_map = G_GenMap()
        for key, value in obj.items():
            entry_pb = self.target.gen_map.entries.add()
            ks = self.descend(f'{self.path}[{key}]', entry_pb.key)
            ks.write_value(api_type.key_type, key)
            vs = self.descend(f'{self.path}[{key}]', entry_pb.value)
            vs.write_value(api_type.value_type, value)

    def write_unknown(self, api_type: 'api.Type', obj: 'Any') -> None:
        raise ValueError(f"Could not serialize {obj!r} as {api_type!r}")


class GRPCTransactionReader()