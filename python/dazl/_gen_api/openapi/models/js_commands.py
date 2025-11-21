# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.command_type_0 import CommandType0
    from ..models.command_type_1 import CommandType1
    from ..models.command_type_2 import CommandType2
    from ..models.command_type_3 import CommandType3
    from ..models.deduplication_period_type_0 import DeduplicationPeriodType0
    from ..models.deduplication_period_type_1 import DeduplicationPeriodType1
    from ..models.deduplication_period_type_2 import DeduplicationPeriodType2
    from ..models.disclosed_contract import DisclosedContract
    from ..models.duration import Duration
    from ..models.prefetch_contract_key import PrefetchContractKey


T = TypeVar("T", bound="JsCommands")


@_attrs_define
class JsCommands:
    """A composite command that groups multiple commands together.

    Attributes:
        command_id (str): Uniquely identifies the command.
            The triple (user_id, act_as, command_id) constitutes the change ID for the intended ledger change,
            where act_as is interpreted as a set of party names.
            The change ID can be used for matching the intended ledger changes with all their completions.
            Must be a valid LedgerString (as described in ``value.proto``).
            Required
        commands (list[CommandType0 | CommandType1 | CommandType2 | CommandType3] | Unset): Individual elements of this
            atomic command. Must be non-empty.
            Required
        act_as (list[str] | Unset): Set of parties on whose behalf the command should be executed.
            If ledger API authorization is enabled, then the authorization metadata must authorize the sender of the request
            to act on behalf of each of the given parties.
            Each element must be a valid PartyIdString (as described in ``value.proto``).
            Required, must be non-empty.
        user_id (str | Unset): Uniquely identifies the participant user that issued the command.
            Must be a valid UserIdString (as described in ``value.proto``).
            Required unless authentication is used with a user token.
            In that case, the token's user-id will be used for the request's user_id.
        read_as (list[str] | Unset): Set of parties on whose behalf (in addition to all parties listed in ``act_as``)
            contracts can be retrieved.
            This affects Daml operations such as ``fetch``, ``fetchByKey``, ``lookupByKey``, ``exercise``, and
            ``exerciseByKey``.
            Note: A participant node of a Daml network can host multiple parties. Each contract present on the participant
            node is only visible to a subset of these parties. A command can only use contracts that are visible to at least
            one of the parties in ``act_as`` or ``read_as``. This visibility check is independent from the Daml
            authorization
            rules for fetch operations.
            If ledger API authorization is enabled, then the authorization metadata must authorize the sender of the request
            to read contract data on behalf of each of the given parties.
            Optional
        workflow_id (str | Unset): Identifier of the on-ledger workflow that this command is a part of.
            Must be a valid LedgerString (as described in ``value.proto``).
            Optional
        deduplication_period (DeduplicationPeriodType0 | DeduplicationPeriodType1 | DeduplicationPeriodType2 | Unset):
            Specifies the deduplication period for the change ID.
            If omitted, the participant will assume the configured maximum deduplication time.
        min_ledger_time_abs (str | Unset): Lower bound for the ledger time assigned to the resulting transaction.
            Note: The ledger time of a transaction is assigned as part of command interpretation.
            Use this property if you expect that command interpretation will take a considerate amount of time, such that by
            the time the resulting transaction is sequenced, its assigned ledger time is not valid anymore.
            Must not be set at the same time as min_ledger_time_rel.
            Optional
        min_ledger_time_rel (Duration | Unset):
        submission_id (str | Unset): A unique identifier to distinguish completions for different submissions with the
            same change ID.
            Typically a random UUID. Applications are expected to use a different UUID for each retry of a submission
            with the same change ID.
            Must be a valid LedgerString (as described in ``value.proto``).

            If omitted, the participant or the committer may set a value of their choice.
            Optional
        disclosed_contracts (list[DisclosedContract] | Unset): Additional contracts used to resolve contract & contract
            key lookups.
            Optional
        synchronizer_id (str | Unset): Must be a valid synchronizer id
            Optional
        package_id_selection_preference (list[str] | Unset): The package-id selection preference of the client for
            resolving
            package names and interface instances in command submission and interpretation
        prefetch_contract_keys (list[PrefetchContractKey] | Unset): Fetches the contract keys into the caches to speed
            up the command processing.
            Should only contain contract keys that are expected to be resolved during interpretation of the commands.
            Keys of disclosed contracts do not need prefetching.

            Optional
    """

    command_id: str
    commands: (
        list[CommandType0 | CommandType1 | CommandType2 | CommandType3] | Unset
    ) = UNSET
    act_as: list[str] | Unset = UNSET
    user_id: str | Unset = UNSET
    read_as: list[str] | Unset = UNSET
    workflow_id: str | Unset = UNSET
    deduplication_period: (
        DeduplicationPeriodType0
        | DeduplicationPeriodType1
        | DeduplicationPeriodType2
        | Unset
    ) = UNSET
    min_ledger_time_abs: str | Unset = UNSET
    min_ledger_time_rel: Duration | Unset = UNSET
    submission_id: str | Unset = UNSET
    disclosed_contracts: list[DisclosedContract] | Unset = UNSET
    synchronizer_id: str | Unset = UNSET
    package_id_selection_preference: list[str] | Unset = UNSET
    prefetch_contract_keys: list[PrefetchContractKey] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.command_type_0 import CommandType0
        from ..models.command_type_1 import CommandType1
        from ..models.command_type_2 import CommandType2
        from ..models.deduplication_period_type_0 import DeduplicationPeriodType0
        from ..models.deduplication_period_type_1 import DeduplicationPeriodType1

        command_id = self.command_id

        commands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.commands, Unset):
            commands = []
            for commands_item_data in self.commands:
                commands_item: dict[str, Any]
                if isinstance(commands_item_data, CommandType0):
                    commands_item = commands_item_data.to_dict()
                elif isinstance(commands_item_data, CommandType1):
                    commands_item = commands_item_data.to_dict()
                elif isinstance(commands_item_data, CommandType2):
                    commands_item = commands_item_data.to_dict()
                else:
                    commands_item = commands_item_data.to_dict()

                commands.append(commands_item)

        act_as: list[str] | Unset = UNSET
        if not isinstance(self.act_as, Unset):
            act_as = self.act_as

        user_id = self.user_id

        read_as: list[str] | Unset = UNSET
        if not isinstance(self.read_as, Unset):
            read_as = self.read_as

        workflow_id = self.workflow_id

        deduplication_period: dict[str, Any] | Unset
        if isinstance(self.deduplication_period, Unset):
            deduplication_period = UNSET
        elif isinstance(self.deduplication_period, DeduplicationPeriodType0):
            deduplication_period = self.deduplication_period.to_dict()
        elif isinstance(self.deduplication_period, DeduplicationPeriodType1):
            deduplication_period = self.deduplication_period.to_dict()
        else:
            deduplication_period = self.deduplication_period.to_dict()

        min_ledger_time_abs = self.min_ledger_time_abs

        min_ledger_time_rel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_ledger_time_rel, Unset):
            min_ledger_time_rel = self.min_ledger_time_rel.to_dict()

        submission_id = self.submission_id

        disclosed_contracts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.disclosed_contracts, Unset):
            disclosed_contracts = []
            for disclosed_contracts_item_data in self.disclosed_contracts:
                disclosed_contracts_item = disclosed_contracts_item_data.to_dict()
                disclosed_contracts.append(disclosed_contracts_item)

        synchronizer_id = self.synchronizer_id

        package_id_selection_preference: list[str] | Unset = UNSET
        if not isinstance(self.package_id_selection_preference, Unset):
            package_id_selection_preference = self.package_id_selection_preference

        prefetch_contract_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prefetch_contract_keys, Unset):
            prefetch_contract_keys = []
            for prefetch_contract_keys_item_data in self.prefetch_contract_keys:
                prefetch_contract_keys_item = prefetch_contract_keys_item_data.to_dict()
                prefetch_contract_keys.append(prefetch_contract_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commandId": command_id,
            }
        )
        if commands is not UNSET:
            field_dict["commands"] = commands
        if act_as is not UNSET:
            field_dict["actAs"] = act_as
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if read_as is not UNSET:
            field_dict["readAs"] = read_as
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if deduplication_period is not UNSET:
            field_dict["deduplicationPeriod"] = deduplication_period
        if min_ledger_time_abs is not UNSET:
            field_dict["minLedgerTimeAbs"] = min_ledger_time_abs
        if min_ledger_time_rel is not UNSET:
            field_dict["minLedgerTimeRel"] = min_ledger_time_rel
        if submission_id is not UNSET:
            field_dict["submissionId"] = submission_id
        if disclosed_contracts is not UNSET:
            field_dict["disclosedContracts"] = disclosed_contracts
        if synchronizer_id is not UNSET:
            field_dict["synchronizerId"] = synchronizer_id
        if package_id_selection_preference is not UNSET:
            field_dict["packageIdSelectionPreference"] = package_id_selection_preference
        if prefetch_contract_keys is not UNSET:
            field_dict["prefetchContractKeys"] = prefetch_contract_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command_type_0 import CommandType0
        from ..models.command_type_1 import CommandType1
        from ..models.command_type_2 import CommandType2
        from ..models.command_type_3 import CommandType3
        from ..models.deduplication_period_type_0 import DeduplicationPeriodType0
        from ..models.deduplication_period_type_1 import DeduplicationPeriodType1
        from ..models.deduplication_period_type_2 import DeduplicationPeriodType2
        from ..models.disclosed_contract import DisclosedContract
        from ..models.duration import Duration
        from ..models.prefetch_contract_key import PrefetchContractKey

        d = dict(src_dict)
        command_id = d.pop("commandId")

        _commands = d.pop("commands", UNSET)
        commands: (
            list[CommandType0 | CommandType1 | CommandType2 | CommandType3] | Unset
        ) = UNSET
        if _commands is not UNSET:
            commands = []
            for commands_item_data in _commands:

                def _parse_commands_item(
                    data: object,
                ) -> CommandType0 | CommandType1 | CommandType2 | CommandType3:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_command_type_0 = CommandType0.from_dict(data)

                        return componentsschemas_command_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_command_type_1 = CommandType1.from_dict(data)

                        return componentsschemas_command_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_command_type_2 = CommandType2.from_dict(data)

                        return componentsschemas_command_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_command_type_3 = CommandType3.from_dict(data)

                    return componentsschemas_command_type_3

                commands_item = _parse_commands_item(commands_item_data)

                commands.append(commands_item)

        act_as = cast(list[str], d.pop("actAs", UNSET))

        user_id = d.pop("userId", UNSET)

        read_as = cast(list[str], d.pop("readAs", UNSET))

        workflow_id = d.pop("workflowId", UNSET)

        def _parse_deduplication_period(
            data: object,
        ) -> (
            DeduplicationPeriodType0
            | DeduplicationPeriodType1
            | DeduplicationPeriodType2
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deduplication_period_type_0 = (
                    DeduplicationPeriodType0.from_dict(data)
                )

                return componentsschemas_deduplication_period_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_deduplication_period_type_1 = (
                    DeduplicationPeriodType1.from_dict(data)
                )

                return componentsschemas_deduplication_period_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_deduplication_period_type_2 = (
                DeduplicationPeriodType2.from_dict(data)
            )

            return componentsschemas_deduplication_period_type_2

        deduplication_period = _parse_deduplication_period(
            d.pop("deduplicationPeriod", UNSET)
        )

        min_ledger_time_abs = d.pop("minLedgerTimeAbs", UNSET)

        _min_ledger_time_rel = d.pop("minLedgerTimeRel", UNSET)
        min_ledger_time_rel: Duration | Unset
        if isinstance(_min_ledger_time_rel, Unset):
            min_ledger_time_rel = UNSET
        else:
            min_ledger_time_rel = Duration.from_dict(_min_ledger_time_rel)

        submission_id = d.pop("submissionId", UNSET)

        _disclosed_contracts = d.pop("disclosedContracts", UNSET)
        disclosed_contracts: list[DisclosedContract] | Unset = UNSET
        if _disclosed_contracts is not UNSET:
            disclosed_contracts = []
            for disclosed_contracts_item_data in _disclosed_contracts:
                disclosed_contracts_item = DisclosedContract.from_dict(
                    disclosed_contracts_item_data
                )

                disclosed_contracts.append(disclosed_contracts_item)

        synchronizer_id = d.pop("synchronizerId", UNSET)

        package_id_selection_preference = cast(
            list[str], d.pop("packageIdSelectionPreference", UNSET)
        )

        _prefetch_contract_keys = d.pop("prefetchContractKeys", UNSET)
        prefetch_contract_keys: list[PrefetchContractKey] | Unset = UNSET
        if _prefetch_contract_keys is not UNSET:
            prefetch_contract_keys = []
            for prefetch_contract_keys_item_data in _prefetch_contract_keys:
                prefetch_contract_keys_item = PrefetchContractKey.from_dict(
                    prefetch_contract_keys_item_data
                )

                prefetch_contract_keys.append(prefetch_contract_keys_item)

        js_commands = cls(
            command_id=command_id,
            commands=commands,
            act_as=act_as,
            user_id=user_id,
            read_as=read_as,
            workflow_id=workflow_id,
            deduplication_period=deduplication_period,
            min_ledger_time_abs=min_ledger_time_abs,
            min_ledger_time_rel=min_ledger_time_rel,
            submission_id=submission_id,
            disclosed_contracts=disclosed_contracts,
            synchronizer_id=synchronizer_id,
            package_id_selection_preference=package_id_selection_preference,
            prefetch_contract_keys=prefetch_contract_keys,
        )

        js_commands.additional_properties = d
        return js_commands

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
