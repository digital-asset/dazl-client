# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This module contains the mapping between Protobuf objects and Python/dazl types.
"""

from __future__ import annotations

# Earlier versions (before v8) had an API that mapped less directly to the gRPC Ledger API.
# But with the HTTP JSON API, many common ledger methods now have much more direct translations that
# still manage to adhere quite closely to dazl's historical behavior.
#
# References:
#  * https://github.com/digital-asset/daml/blob/main/ledger-service/http-json/src/main/scala/com/digitalasset/http/CommandService.scala
from collections.abc import Mapping as _Mapping
import sys
from typing import Any, Collection, Optional, Sequence

from google.protobuf.json_format import MessageToDict

from ..._gen.com.daml.ledger.api import v1 as lapipb
from ..._gen.com.daml.ledger.api.v1 import admin as lapiadminpb
from ...damlast.daml_lf_1 import (
    DefTemplate,
    DottedName,
    ModuleRef,
    PackageRef,
    TemplateChoice,
    Type,
    TypeConName,
)
from ...damlast.daml_types import ContractId as ContractIdType, con
from ...damlast.errors import NameNotFoundError
from ...damlast.lookup import STAR, LookupResult, MultiPackageLookup
from ...damlast.protocols import SymbolLookup, TemplateOrInterface
from ...damlast.util import module_local_name, module_name, package_local_name, package_ref
from ...ledger.aio import PackageService
from ...prim import ContractData, ContractId, Party
from ...values import Context
from ...values.protobuf import ProtobufDecoder, ProtobufEncoder, set_value
from .._offsets import End
from ..aio import PackageLoader
from ..api_types import (
    ActAs,
    Admin,
    ArchiveEvent,
    Command,
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    ExerciseByKeyCommand,
    ExerciseCommand,
    ExerciseResponse,
    IdentityProviderAdmin,
    InterfaceView,
    MeteringReport,
    MeteringReportApplication,
    MeteringReportRequest,
    PartyInfo,
    ReadAs,
    Right,
    User,
    Version,
    VersionFeatures,
    VersionUserManagementFeature,
    _Admin,
    _IdentityProviderAdmin,
)
from ..auth import TokenOrTokenProvider
from ..pkgcache import SHARED_PACKAGE_DATABASE

if sys.version_info >= (3, 11):
    from typing import assert_never
else:
    from typing_extensions import assert_never

__all__ = ["Codec"]


class Codec:
    """
    Contains methods for converting to/from Protobuf Ledger API types.

    Some encode/decode methods require package information to be available, which is why a
    connection must be supplied in order to use the codec.

    By default, the package database is _globally_ shared; this is safe to do because we make the
    same assumption that the remote gRPC Ledger API implementation makes: that package IDs uniquely
    identify package contents.
    """

    def __init__(
        self, conn: Optional[PackageService] = None, lookup: Optional[MultiPackageLookup] = None
    ):
        self.conn = conn
        self._lookup = lookup or SHARED_PACKAGE_DATABASE
        self._loader = PackageLoader(self._lookup, conn)
        self._encode_context = Context(ProtobufEncoder(), self._lookup)
        self._decode_context = Context(ProtobufDecoder(), self._lookup)

    @property
    def lookup(self) -> SymbolLookup:
        return self._lookup

    async def preload(self, contents) -> None:
        await self._loader.preload(contents)

    async def encode_command(
        self, cmd: Command, /, *, token: Optional[TokenOrTokenProvider] = None
    ) -> lapipb.Command:
        match (cmd):
            case CreateCommand(template_id, payload):
                return lapipb.Command(
                    create=await self.encode_create_command(template_id, payload, token=token)
                )
            case ExerciseCommand(contract_id, choice, argument):
                return lapipb.Command(
                    exercise=await self.encode_exercise_command(
                        contract_id, choice, argument, token=token
                    )
                )
            case ExerciseByKeyCommand(template_id, key, choice, argument):
                return lapipb.Command(
                    exerciseByKey=await self.encode_exercise_by_key_command(
                        template_id, choice, key, argument, token=token
                    )
                )
            case CreateAndExerciseCommand(template_id, payload, choice, argument):
                return lapipb.Command(
                    createAndExercise=await self.encode_create_and_exercise_command(
                        template_id, payload, choice, argument, token=token
                    )
                )
            case _:
                assert_never(cmd)

    async def encode_create_command(
        self,
        template_id: str | TypeConName,
        payload: ContractData,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> lapipb.CreateCommand:
        symbols = await self._loader.search(template_id, token=token)
        if str(template_id).startswith("#"):
            item_type = symbols.templates.single().package_name_ref
            if item_type is None:
                raise ValueError(
                    "passed in a smart-contract-upgrade compatible name, but did not find a corresponding package name"
                )
        else:
            item_type = symbols.templates.single().package_id_ref

        _, value = await self.encode_value(con(item_type), payload, token=token)
        return lapipb.CreateCommand(
            template_id=self.encode_identifier(item_type), create_arguments=value
        )

    async def encode_exercise_command(
        self,
        contract_id: ContractId,
        choice_name: str,
        argument: Optional[Any] = None,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> lapipb.ExerciseCommand:
        item_type, choice = await self._look_up_choice(
            contract_id.value_type, choice_name, token=token
        )

        cmd_pb = lapipb.ExerciseCommand(
            template_id=self.encode_identifier(item_type),
            contract_id=contract_id.value,
            choice=choice_name,
        )
        value_field, value_pb = await self.encode_value(
            choice.arg_binder.type, argument, token=token
        )
        set_value(cmd_pb.choice_argument, value_field, value_pb)

        return cmd_pb

    async def encode_create_and_exercise_command(
        self,
        template_id: str | TypeConName,
        payload: ContractData,
        choice_name: str,
        argument: Optional[Any] = None,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> lapipb.CreateAndExerciseCommand:
        item_type, choice = await self._look_up_choice(template_id, choice_name, token=token)

        payload_field, payload_pb = await self.encode_value(con(item_type), payload, token=token)
        if payload_field != "record":
            raise ValueError("unexpected non-record type when constructing payload")
        argument_field, argument_pb = await self.encode_value(
            choice.arg_binder.type, argument, token=token
        )
        cmd_pb = lapipb.CreateAndExerciseCommand(
            create_arguments=payload_pb,
            template_id=self.encode_identifier(item_type),
            choice=choice_name,
        )
        set_value(cmd_pb.choice_argument, argument_field, argument_pb)

        return cmd_pb

    async def encode_exercise_by_key_command(
        self,
        template_id: str | TypeConName,
        choice_name: str,
        key: Any,
        argument: Optional[ContractData] = None,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> lapipb.ExerciseByKeyCommand:
        item_type, template, choice = await self._look_up_template_choice(
            template_id, choice_name, token=token
        )
        if template.key is None:
            raise ValueError(
                f"cannot encode ExerciseByKeyCommand; template {template_id} does not have a contract key defined"
            )

        cmd_pb = lapipb.ExerciseByKeyCommand(
            template_id=self.encode_identifier(item_type),
            choice=choice_name,
        )
        key_field, key_pb = await self.encode_value(template.key.type, key, token=token)
        value_field, value_pb = await self.encode_value(
            choice.arg_binder.type, argument, token=token
        )
        set_value(cmd_pb.contract_key, key_field, key_pb)
        set_value(cmd_pb.choice_argument, value_field, value_pb)

        return cmd_pb

    async def encode_filters(
        self,
        template_or_interface_ids: Sequence[TypeConName],
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> lapipb.Filters:
        # Search for a reference to the "wildcard" template; if any of the requested
        # template_or_interface_ids is "*", then return results for all templates.
        # We do this first because resolving template IDs otherwise requires do_with_retry,
        # which can be expensive.
        if not template_or_interface_ids or any(
            package_ref(t) == "*" and package_local_name(t) == "*"
            for t in template_or_interface_ids
        ):
            # if any of the keys references the "wildcard" template, (or no values were supplied)
            # then this means we need to fetch values for all templates
            return lapipb.Filters()

        # No wildcard template IDs, so inspect and resolve all template references to concrete
        # template or interface IDs
        templates = list[TypeConName]()
        interfaces = list[TypeConName]()
        for template_or_interface_id in template_or_interface_ids:
            pkg_ref = package_ref(template_or_interface_id)
            local_name = package_local_name(template_or_interface_id)

            matches = await self._loader.search(template_or_interface_id, token=token)
            if pkg_ref.startswith("#"):
                # if the user asked for SCU names, continue to use that in the constructed query
                templates.extend(matches.templates.package_name_refs())
                interfaces.extend(matches.interfaces.package_name_refs())
            else:
                # for everything else, use explicit package ID references
                templates.extend(matches.templates.package_id_refs())
                interfaces.extend(matches.interfaces.package_id_refs())

        return lapipb.Filters(
            inclusive=lapipb.InclusiveFilters(
                template_ids=[self.encode_identifier(i) for i in templates],
                interface_filters=[
                    lapipb.InterfaceFilter(
                        interface_id=self.encode_identifier(i), include_interface_view=True
                    )
                    for i in interfaces
                ],
            )
        )

    async def encode_value(
        self, item_type: Type, obj: Any, /, *, token: Optional[TokenOrTokenProvider] = None
    ) -> tuple[str, Optional[Any]]:
        """
        Convert a dazl/Python value to its Protobuf equivalent.
        """
        return await self._loader.do_with_retry(
            lambda: self._encode_context.convert(item_type, obj),
            token=token,
        )

    @staticmethod
    def encode_identifier(name: TypeConName, /) -> lapipb.Identifier:
        return lapipb.Identifier(
            package_id=package_ref(name),
            module_name=str(module_name(name)),
            entity_name=module_local_name(name),
        )

    @staticmethod
    def encode_user(user: User, /) -> lapiadminpb.User:
        return lapiadminpb.User(
            id=user.id,
            primary_party=user.primary_party,
            metadata=lapiadminpb.ObjectMeta(
                resource_version=user.resource_version, annotations=user.annotations
            ),
        )

    @staticmethod
    def encode_right(right: Right, /) -> lapiadminpb.Right:
        match right:
            case _Admin():
                return lapiadminpb.Right(participant_admin=lapiadminpb.Right.ParticipantAdmin())
            case _IdentityProviderAdmin():
                return lapiadminpb.Right(
                    identity_provider_admin=lapiadminpb.Right.IdentityProviderAdmin()
                )
            case ReadAs(party):
                return lapiadminpb.Right(can_read_as=lapiadminpb.Right.CanReadAs(party=party))
            case ActAs(party):
                return lapiadminpb.Right(can_act_as=lapiadminpb.Right.CanActAs(party=party))
            case _:
                assert_never(right)

    @staticmethod
    def encode_begin_offset(offset: Optional[str], /) -> lapipb.LedgerOffset:
        if offset is None:
            return lapipb.LedgerOffset(boundary=lapipb.LedgerOffset.LEDGER_BEGIN)
        else:
            return lapipb.LedgerOffset(absolute=offset)

    @staticmethod
    def encode_end_offset(offset: Optional[str | End], /) -> Optional[lapipb.LedgerOffset]:
        if offset is None:
            # there is no ending offset (the stream will never naturally terminate)
            return None
        elif isinstance(offset, End):
            # the offset goes up until the current end of the ledger
            return lapipb.LedgerOffset(boundary=lapipb.LedgerOffset.LEDGER_END)
        else:
            # the offset is absolute
            return lapipb.LedgerOffset(absolute=offset)

    async def decode_created_event(
        self, event: lapipb.CreatedEvent, /, *, token: Optional[TokenOrTokenProvider] = None
    ) -> CreateEvent:
        cid = self.decode_contract_id(event)
        cdata = await self.decode_value(con(cid.value_type), event.create_arguments, token=token)
        if not isinstance(cdata, _Mapping):
            raise ValueError(
                f"expected create_arguments to result in a dict, but got {cdata!r} instead"
            )

        lookup = self._lookup.search(cid.value_type)
        template = next(iter(lookup.templates.values()))
        key = None
        if template is not None and template.key is not None:
            key = await self.decode_value(template.key.type, event.contract_key, token=token)

        return CreateEvent(
            cid,
            cdata,
            tuple(Party(p) for p in event.signatories),
            tuple(Party(p) for p in event.observers),
            event.agreement_text.value,
            key,
            created_event_blob=event.created_event_blob or None,
            interface_views=[
                await self.decode_interface_view(v, token=token) for v in event.interface_views
            ],
        )

    async def decode_archived_event(self, event: lapipb.ArchivedEvent, /) -> ArchiveEvent:
        cid = self.decode_contract_id(event)
        return ArchiveEvent(cid)

    async def decode_exercise_response(
        self, tree: lapipb.TransactionTree, /, *, token: Optional[TokenOrTokenProvider] = None
    ) -> ExerciseResponse:
        """
        Convert a Protobuf TransactionTree response to an ExerciseResponse. The TransactionTree is
        expected to only contain a single exercise node at the root level.
        """
        from ... import LOG

        found_choice = None
        result = None
        cid = None

        events = list[CreateEvent | ArchiveEvent]()
        for event_id in tree.root_event_ids:
            event_pb = tree.events_by_id[event_id]
            event_pb_type = event_pb.WhichOneof("kind")

            match event_pb_type:
                case "created":
                    events.append(await self.decode_created_event(event_pb.created, token=token))
                case "exercised":
                    # Find the "first" exercised node and grab its result value
                    if cid is None:
                        cid = self.decode_contract_id(event_pb.exercised)

                        template_or_interface: TemplateOrInterface
                        if event_pb.exercised.interface_id.entity_name:
                            symbols = self._lookup.search(
                                Codec.decode_identifier(event_pb.exercised.interface_id)
                            )
                            template_or_interface = symbols.interfaces.single().object
                        else:
                            symbols = self._lookup.search(cid.value_type)
                            template_or_interface = symbols.templates.single().object

                        if found_choice is None:
                            for choice in template_or_interface.choices:
                                if choice.name == event_pb.exercised.choice:
                                    found_choice = choice
                                    break
                            if found_choice is not None:
                                result = await self.decode_value(
                                    found_choice.ret_type,
                                    event_pb.exercised.exercise_result,
                                    token=token,
                                )
                            else:
                                LOG.error(
                                    "Received an exercise node that referred to a choice that doesn't exist!"
                                )

                    events.extend(
                        await self._decode_exercised_child_events(tree, [event_id], token=token)
                    )
                case _:
                    LOG.warning("Received an unknown event type: %s", event_pb_type)

        return ExerciseResponse(result, events)

    async def _decode_exercised_child_events(
        self,
        tree: lapipb.TransactionTree,
        event_ids: Sequence[str],
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> Sequence[CreateEvent | ArchiveEvent]:
        from ... import LOG

        events = list[CreateEvent | ArchiveEvent]()
        for event_id in event_ids:
            event_pb = tree.events_by_id[event_id]
            event_pb_type = event_pb.WhichOneof("kind")
            if event_pb_type == "created":
                events.append(await self.decode_created_event(event_pb.created, token=token))
            elif event_pb_type == "exercised":
                if event_pb.exercised.consuming:
                    events.append(ArchiveEvent(self.decode_contract_id(event_pb.exercised)))
                events.extend(
                    await self._decode_exercised_child_events(
                        tree, event_pb.exercised.child_event_ids, token=token
                    )
                )
            else:
                LOG.warning("Received an unknown event type: %s", event_pb_type)
        return events

    async def decode_interface_view(
        self, pb: lapipb.InterfaceView, /, *, token: Optional[TokenOrTokenProvider] = None
    ) -> InterfaceView:
        vt = Codec.decode_identifier(pb.interface_id)

        symbols = self._lookup.search(vt)
        interface = symbols.interfaces.single().object
        view_value = await self.decode_value(interface.view, pb.view_value, token=token)
        return InterfaceView(vt, view_value)

    async def decode_value(
        self, item_type: Type, obj: Any, /, *, token: Optional[TokenOrTokenProvider] = None
    ) -> Optional[Any]:
        """
        Convert a Protobuf Ledger API value to its dazl/Python equivalent.
        """
        return await self._loader.do_with_retry(
            lambda: self._decode_context.convert(item_type, obj), token=token
        )

    def decode_contract_id(
        self, event: lapipb.CreatedEvent | lapipb.ExercisedEvent | lapipb.ArchivedEvent, /
    ) -> ContractId:
        vt = Codec.decode_identifier(event.template_id)
        return self._decode_context.convert(ContractIdType(con(vt)), event.contract_id)

    @staticmethod
    def decode_identifier(identifier: lapipb.Identifier, /) -> TypeConName:
        return TypeConName(
            ModuleRef(
                PackageRef(identifier.package_id), DottedName(identifier.module_name.split("."))
            ),
            DottedName(identifier.entity_name.split(".")).segments,
        )

    @staticmethod
    def decode_user(user: lapiadminpb.User, /) -> User:
        return User(
            id=user.id,
            primary_party=Party(user.primary_party),
            resource_version=user.metadata.resource_version,
            annotations=dict(user.metadata.annotations),
        )

    @staticmethod
    def decode_right(right: lapiadminpb.Right, /) -> Right:
        kind = right.WhichOneof("kind")
        match kind:
            case "participant_admin":
                return Admin
            case "identity_provider_admin":
                return IdentityProviderAdmin
            case "can_read_as":
                return ReadAs(Party(right.can_read_as.party))
            case "can_act_as":
                return ActAs(Party(right.can_act_as.party))
            case _:
                raise ValueError(f"unexpected kind of right: {kind}")

    @staticmethod
    def decode_party_info(party_details: lapiadminpb.PartyDetails, /) -> PartyInfo:
        return PartyInfo(
            Party(party_details.party), party_details.display_name, party_details.is_local
        )

    @staticmethod
    def decode_version(obj: lapipb.GetLedgerApiVersionResponse, /) -> Version:
        return Version(
            version=obj.version,
            features=VersionFeatures(
                user_management=VersionUserManagementFeature(
                    supported=obj.features.user_management.supported,
                    max_rights_per_user=obj.features.user_management.max_rights_per_user,
                    max_users_page_size=obj.features.user_management.max_users_page_size,
                ),
            ),
        )

    @staticmethod
    def decode_get_metering_report_response(
        obj: lapiadminpb.GetMeteringReportResponse, /
    ) -> MeteringReport:
        # unfortunately with a JSON-based format, we lose a considerable degree
        # of type safety, and this (rightfully) makes mypy complain loudly
        report_json = MessageToDict(obj.metering_report_json)

        return MeteringReport(
            request=MeteringReportRequest(
                report_json.get("application"),  # type: ignore
                report_json.get("from"),  # type: ignore
                report_json.get("to"),  # type: ignore
            ),
            participant=report_json["participant"],  # type: ignore
            final=report_json["final"],  # type: ignore
            applications=[
                MeteringReportApplication(
                    o["application"],  # type: ignore
                    int(o["events"]),  # type: ignore
                )
                for o in report_json["applications"]
            ],
        )

    async def _look_up_choice(
        self,
        template_or_interface_id: Any,
        choice_name: str,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> tuple[TypeConName, TemplateChoice]:
        result = await self._loader.search(template_or_interface_id, token=token)

        for template_id, template in result.templates.items():
            for choice in template.choices:
                if choice.name == choice_name:
                    return template_id, choice

        for interface_id, interface in result.interfaces.items():
            for choice in interface.choices:
                if choice.name == choice_name:
                    return interface_id, choice

        raise ValueError(
            f"template/interface {template_or_interface_id} has no choice named {choice_name}"
        )

    async def _look_up_template_choice(
        self, template_id: Any, choice_name: str, /, *, token: Optional[TokenOrTokenProvider] = None
    ) -> tuple[TypeConName, DefTemplate, TemplateChoice]:
        result = await self._loader.search(template_id, token=token)

        for template_id, template in result.templates.items():
            for choice in template.choices:
                if choice.name == choice_name:
                    return template_id, template, choice

        raise ValueError(f"template {template_id} has no choice named {choice_name}")
