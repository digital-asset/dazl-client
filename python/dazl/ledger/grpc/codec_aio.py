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
from typing import Any, Collection, Optional, Sequence, Tuple, Union

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
from ...damlast.lookup import STAR, MultiPackageLookup
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
)
from ..auth import TokenOrTokenProvider
from ..pkgcache import SHARED_PACKAGE_DATABASE

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
        if isinstance(cmd, CreateCommand):
            return lapipb.Command(
                create=await self.encode_create_command(cmd.template_id, cmd.payload, token=token)
            )
        elif isinstance(cmd, ExerciseCommand):
            return lapipb.Command(
                exercise=await self.encode_exercise_command(
                    cmd.contract_id, cmd.choice, cmd.argument, token=token
                )
            )
        elif isinstance(cmd, ExerciseByKeyCommand):
            return lapipb.Command(
                exerciseByKey=await self.encode_exercise_by_key_command(
                    cmd.template_id, cmd.choice, cmd.key, cmd.argument, token=token
                )
            )
        elif isinstance(cmd, CreateAndExerciseCommand):
            return lapipb.Command(
                createAndExercise=await self.encode_create_and_exercise_command(
                    cmd.template_id, cmd.payload, cmd.choice, cmd.argument, token=token
                )
            )
        else:
            raise ValueError(f"unknown Command type: {cmd!r}")

    async def encode_create_command(
        self,
        template_id: Union[str, Any],
        payload: ContractData,
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> lapipb.CreateCommand:
        item_type = await self._loader.do_with_retry(
            lambda: self._lookup.template_name(template_id), token=token
        )
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
        template_id: Union[str, TypeConName],
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
        template_id: Union[str, TypeConName],
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
        requested_templates, requested_interfaces = await self._resolve(
            template_or_interface_ids, token=token
        )

        return lapipb.Filters(
            inclusive=lapipb.InclusiveFilters(
                template_ids=[self.encode_identifier(i) for i in requested_templates],
                interface_filters=[
                    lapipb.InterfaceFilter(
                        interface_id=self.encode_identifier(i), include_interface_view=True
                    )
                    for i in requested_interfaces
                ],
            )
        )

    async def _resolve(
        self,
        template_or_interface_ids: Sequence[TypeConName],
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> tuple[Sequence[TypeConName], Sequence[TypeConName]]:
        """
        Resolve a set of template or interface IDs to TypeConNames that can be sent to the
        Ledger API for querying.

        Concretely, this means disambiguating between templates and interfaces, handling
        templates/interfaces with missing package IDs, and handling Smart Contract Upgrade
        template references (those that start with ``'#'``).

        :param template_or_interface_ids:
            The set of template and/or interface IDs to fully resolve.
        :param token:
            An optional token to use when fetching template or interface IDs.
        :return:
            A set of template IDs and interface IDs that can be sent to the ledger.
        :raises NameNotFoundError:
            If a template or interface is missing a package ID, and we couldn't determine
            what that package ID should be.
        """
        requested_templates = set[TypeConName]()
        requested_interfaces = set[TypeConName]()

        for template_or_interface_id in template_or_interface_ids:
            resolved_template_ids = Codec._resolve_single_name(
                template_or_interface_id,
                await self._loader.do_with_retry(
                    lambda: self._lookup.template_names(template_or_interface_id), token=token
                ),
            )

            resolved_interface_ids = Codec._resolve_single_name(
                template_or_interface_id,
                await self._loader.do_with_retry(
                    lambda: self._lookup.interface_names(template_or_interface_id), token=token
                ),
            )

            if resolved_template_ids:
                requested_templates.update(resolved_template_ids)
            elif resolved_interface_ids:
                requested_interfaces.update(resolved_interface_ids)
            elif package_ref(template_or_interface_id) == STAR:
                # in the event that we can't resolve this to a template ID or interface ID on the
                # client, there's a pretty good chance this template doesn't exist on the server
                #
                # being able to specify a template reference without a package ID or package
                # name at all is strictly something dazl does on the client side to be nice;
                # there is no way for this operation to succeed on the server
                raise NameNotFoundError(template_or_interface_id)
            else:
                # just pass the user's string in exactly, and let the server return a
                # template-not-found error as expected
                requested_templates.add(template_or_interface_id)

        return sorted(requested_templates), sorted(requested_interfaces)

    @staticmethod
    def _resolve_single_name(
        original_name: TypeConName, resolved_names: Collection[TypeConName], /
    ) -> Collection[TypeConName]:
        original_package_ref = package_ref(original_name)
        if original_package_ref == STAR:
            # if the caller originally requested a name without a package reference,
            # then use the ones that we have resolved
            return resolved_names
        else:
            return [original_name]

    async def encode_value(
        self, item_type: Type, obj: Any, /, *, token: Optional[TokenOrTokenProvider] = None
    ) -> Tuple[str, Optional[Any]]:
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
        if right == Admin:
            return lapiadminpb.Right(participant_admin=lapiadminpb.Right.ParticipantAdmin())
        elif isinstance(right, ReadAs):
            return lapiadminpb.Right(can_read_as=lapiadminpb.Right.CanReadAs(party=right.party))
        elif isinstance(right, ActAs):
            return lapiadminpb.Right(can_act_as=lapiadminpb.Right.CanActAs(party=right.party))
        else:
            raise ValueError(f"unknown kind of right: {right!r}")

    @staticmethod
    def encode_begin_offset(offset: Optional[str], /) -> lapipb.LedgerOffset:
        if offset is None:
            return lapipb.LedgerOffset(boundary=lapipb.LedgerOffset.LEDGER_BEGIN)
        else:
            return lapipb.LedgerOffset(absolute=offset)

    @staticmethod
    def encode_end_offset(offset: Union[str, None, End], /) -> Optional[lapipb.LedgerOffset]:
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

        template = self._lookup.template(cid.value_type)
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

        events = list[Union[CreateEvent, ArchiveEvent]]()
        for event_id in tree.root_event_ids:
            event_pb = tree.events_by_id[event_id]
            event_pb_type = event_pb.WhichOneof("kind")
            if event_pb_type == "created":
                events.append(await self.decode_created_event(event_pb.created, token=token))
            elif event_pb_type == "exercised":
                # Find the "first" exercised node and grab its result value
                if cid is None:
                    cid = self.decode_contract_id(event_pb.exercised)

                    template_or_interface: TemplateOrInterface
                    if event_pb.exercised.interface_id.entity_name:
                        template_or_interface = self._lookup.interface(
                            Codec.decode_identifier(event_pb.exercised.interface_id)
                        )
                    else:
                        template_or_interface = self._lookup.template(cid.value_type)

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
            else:
                LOG.warning("Received an unknown event type: %s", event_pb_type)

        return ExerciseResponse(result, events)

    async def _decode_exercised_child_events(
        self,
        tree: lapipb.TransactionTree,
        event_ids: Sequence[str],
        /,
        *,
        token: Optional[TokenOrTokenProvider] = None,
    ) -> Sequence[Union[CreateEvent, ArchiveEvent]]:
        from ... import LOG

        events = list[Union[CreateEvent, ArchiveEvent]]()
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
        interface = self._lookup.interface(vt)
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
        self, event: Union[lapipb.CreatedEvent, lapipb.ExercisedEvent, lapipb.ArchivedEvent], /
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
        if kind == "participant_admin":
            return Admin
        elif kind == "can_read_as":
            return ReadAs(Party(right.can_read_as.party))
        elif kind == "can_act_as":
            return ActAs(Party(right.can_act_as.party))
        else:
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
    ) -> Tuple[TypeConName, TemplateChoice]:
        template_type = await self._loader.do_with_retry(
            lambda: self._lookup.template_or_interface_name(template_or_interface_id), token=token
        )
        template_or_interface = self._lookup.template_or_interface(template_type)
        for choice in template_or_interface.choices:
            if choice.name == choice_name:
                return template_type, choice
        raise ValueError(f"template {template_or_interface.name} has no choice named {choice_name}")

    async def _look_up_template_choice(
        self, template_id: Any, choice_name: str, /, *, token: Optional[TokenOrTokenProvider] = None
    ) -> Tuple[TypeConName, DefTemplate, TemplateChoice]:
        template_type = await self._loader.do_with_retry(
            lambda: self._lookup.template_name(template_id), token=token
        )
        template = self._lookup.template(template_type)
        for choice in template.choices:
            if choice.name == choice_name:
                return template_type, template, choice
        raise ValueError(f"template {template.tycon} has no choice named {choice_name}")
