# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Mapping, Optional, Tuple

from ...damlast import TypeConName
from ...damlast.daml_types import con
from ...damlast.lookup import MultiPackageLookup, parse_type_con_name
from ...damlast.protocols import SymbolLookup
from ...prim import ContractData, ContractId, Party
from ...values import JsonDecoder, JsonEncoder
from ..aio import PackageService
from ..aio._codec import CoreCodecFactory
from ..api_types import (
    ArchiveEvent,
    Command,
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    Event,
    ExerciseByKeyCommand,
    ExerciseCommand,
)

__all__ = ["Codec"]

CORE_CODEC_FACTORY = CoreCodecFactory(JsonEncoder(), JsonDecoder())


class Codec:
    def __init__(self, conn: PackageService, lookup: Optional[MultiPackageLookup] = None):
        self.conn = conn
        self._core = CORE_CODEC_FACTORY.build(conn, lookup)

    @property
    def lookup(self) -> "SymbolLookup":
        return self._core.lookup

    async def encode_command(self, __command: "Command") -> "Tuple[str, Mapping[str, Any]]":
        if isinstance(__command, CreateCommand):
            return "/v1/create", await self.encode_create_command(
                __command.template_id, __command.payload
            )
        elif isinstance(__command, ExerciseCommand):
            return "/v1/exercise", await self.encode_exercise_command(
                __command.contract_id, __command.choice, __command.argument
            )
        elif isinstance(__command, ExerciseByKeyCommand):
            return "/v1/exercise", await self.encode_exercise_by_key_command(
                __command.template_id, __command.choice, __command.key, __command.argument
            )
        elif isinstance(__command, CreateAndExerciseCommand):
            return "/v1/create-and-exercise", await self.encode_create_and_exercise_command(
                __command.template_id, __command.payload, __command.choice, __command.argument
            )
        else:
            raise ValueError(f"unknown Command type: {__command!r}")

    async def encode_create_command(
        self,
        __template_id: "TypeConName",
        __payload: "ContractData",
        *,
        command_id: "Optional[str]" = None,
    ) -> "Mapping[str, Any]":
        t = str(__template_id)
        p = await self._core.encode_value(con(__template_id), __payload)

        if command_id:
            return {"templateId": t, "payload": p, "meta": {"commandId": command_id}}
        else:
            return {"templateId": t, "payload": p}

    async def encode_exercise_command(
        self,
        __cid: "ContractId",
        __choice: str,
        __argument: "Optional[Any]",
        *,
        command_id: "Optional[str]" = None,
    ) -> "Mapping[str, Any]":
        item_type, _, choice = await self._core.lookup_up_choice(__cid.value_type, __choice)

        msg = {
            "templateId": str(__cid.value_type),
            "contractId": __cid.value,
            "choice": __choice,
            "argument": await self._core.encode_value(choice.arg_binder.type, __argument),
        }
        if command_id:
            msg["meta"] = {"commandId": command_id}
        return msg

    async def encode_exercise_by_key_command(
        self,
        __template_id: "TypeConName",
        __choice: str,
        __key: "Any",
        __argument: "Optional[ContractData]" = None,
        *,
        command_id: "Optional[str]" = None,
    ) -> "Mapping[str, Any]":
        item_type, template, choice = await self._core.look_up_choice(__template_id, __choice)
        if template.key is None:
            raise ValueError(
                f"cannot encode ExerciseByKeyCommand; template {__template_id} does not have a contract key defined"
            )

        msg = {
            "templateId": str(__template_id),
            "key": await self._core.encode_value(template.key.type, __key),
            "choice": __choice,
            "argument": await self._core.encode_value(choice.arg_binder.type, __argument),
        }

        if command_id:
            msg["meta"] = {"commandId": command_id}
        return msg

    async def encode_create_and_exercise_command(
        self,
        __template_id: "TypeConName",
        __payload: "ContractData",
        __choice: str,
        __argument: "Optional[Any]" = None,
        *,
        command_id: "Optional[str]" = None,
    ) -> "Mapping[str, Any]":
        item_type, _, choice = await self._core.look_up_choice(__template_id, __choice)

        payload = await self._core.encode_value(con(item_type), __payload)
        argument = await self._core.encode_value(choice.arg_binder.type, __argument)

        msg = {
            "templateId": str(__template_id),
            "payload": payload,
            "choice": __choice,
            "argument": argument,
        }

        if command_id:
            msg["meta"] = {"commandId": command_id}
        return msg

    async def decode_event(self, __obj) -> "Event":
        created = __obj.get("created")
        if created is not None:
            return await self.decode_create_event(created)
        archived = __obj.get("archived")
        if archived is not None:
            return await self.decode_archive_event(archived)

    async def decode_create_event(self, __event: "Mapping[str, Any]") -> "CreateEvent":
        cid = self.decode_contract_id(__event)
        cdata = await self._core.decode_value(con(cid.value_type), __event["payload"])

        template = self.lookup.template(cid.value_type)
        key = None
        if template is not None and template.key is not None:
            key = await self._core.decode_value(template.key.type, __event["key"])
        return CreateEvent(
            cid,
            cdata,
            tuple(Party(p) for p in __event.get("signatories", ())),
            tuple(Party(p) for p in __event.get("observers", ())),
            __event.get("agreementText"),
            key,
        )

    async def decode_archive_event(self, __event: "Mapping[str, Any]") -> "ArchiveEvent":
        cid = self.decode_contract_id(__event)
        return ArchiveEvent(cid)

    @staticmethod
    def decode_contract_id(__obj: "Mapping[str, Any]") -> "ContractId":
        return ContractId(parse_type_con_name(__obj["templateId"]), __obj["contractId"])
