# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExercisedEvent")


@_attrs_define
class ExercisedEvent:
    """Records that a choice has been exercised on a target contract.

    Attributes:
        offset (int): The offset of origin.
            Offsets are managed by the participant nodes.
            Transactions can thus NOT be assumed to have the same offsets on different participant nodes.
            It is a valid absolute offset (positive integer)

            Required
        node_id (int): The position of this event in the originating transaction or reassignment.
            Node IDs are not necessarily equal across participants,
            as these may see different projections/parts of transactions.
            Must be valid node ID (non-negative integer)

            Required
        contract_id (str): The ID of the target contract.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
        template_id (str): Identifies the template that defines the executed choice.
            This template's package-id may differ from the target contract's package-id
            if the target contract has been upgraded or downgraded.

            The identifier uses the package-id reference format.

            Required
        choice (str): The choice that was exercised on the target contract.
            Must be a valid NameString (as described in ``value.proto``).

            Required
        choice_argument (Any): The argument of the exercised choice.

            Required
        acting_parties (list[str]): The parties that exercised the choice.
            Each element must be a valid PartyIdString (as described in ``value.proto``).

            Required: must be non-empty
        consuming (bool): If true, the target contract may no longer be exercised.

            Required
        witness_parties (list[str]): The parties that are notified of this event. The witnesses of an exercise
            node will depend on whether the exercise was consuming or not.
            If consuming, the witnesses are the union of the stakeholders,
            the actors and all informees of all the ancestors of this event this
            participant knows about.
            If not consuming, the witnesses are the union of the signatories,
            the actors and all informees of all the ancestors of this event this
            participant knows about.
            In both cases the witnesses are limited to the querying parties, or not
            limited in case anyParty filters are used.
            Note that the actors might not necessarily be observers
            and thus stakeholders. This is the case when the controllers of a
            choice are specified using "flexible controllers", using the
            ``choice ... controller`` syntax, and said controllers are not
            explicitly marked as observers.
            Each element must be a valid PartyIdString (as described in ``value.proto``).

            Required: must be non-empty
        last_descendant_node_id (int): Specifies the upper boundary of the node ids of the events in the same
            transaction that appeared as a result of
            this ``ExercisedEvent``. This allows unambiguous identification of all the members of the subtree rooted at this
            node. A full subtree can be constructed when all descendant nodes are present in the stream. If nodes are
            heavily
            filtered, it is only possible to determine if a node is in a consequent subtree or not.

            Required
        package_name (str): The package name of the contract.

            Required
        acs_delta (bool): Whether this event would be part of respective ACS_DELTA shaped stream,
            and should therefore considered when tracking contract activeness on the client-side.

            Required
        interface_id (str | Unset): The interface where the choice is defined, if inherited.
            If defined, the identifier uses the package-id reference format.

            Optional
        exercise_result (Any | Unset): The result of exercising the choice.

            Optional
        implemented_interfaces (list[str] | Unset): If the event is consuming, the interfaces implemented by the target
            template that have been
            matched from the interface filter query.
            Populated only in case interface filters with include_interface_view set.

            The identifier uses the package-id reference format.

            Optional: can be empty
    """

    offset: int
    node_id: int
    contract_id: str
    template_id: str
    choice: str
    choice_argument: Any
    acting_parties: list[str]
    consuming: bool
    witness_parties: list[str]
    last_descendant_node_id: int
    package_name: str
    acs_delta: bool
    interface_id: str | Unset = UNSET
    exercise_result: Any | Unset = UNSET
    implemented_interfaces: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        node_id = self.node_id

        contract_id = self.contract_id

        template_id = self.template_id

        choice = self.choice

        choice_argument = self.choice_argument

        acting_parties = self.acting_parties

        consuming = self.consuming

        witness_parties = self.witness_parties

        last_descendant_node_id = self.last_descendant_node_id

        package_name = self.package_name

        acs_delta = self.acs_delta

        interface_id = self.interface_id

        exercise_result = self.exercise_result

        implemented_interfaces: list[str] | Unset = UNSET
        if not isinstance(self.implemented_interfaces, Unset):
            implemented_interfaces = self.implemented_interfaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "nodeId": node_id,
                "contractId": contract_id,
                "templateId": template_id,
                "choice": choice,
                "choiceArgument": choice_argument,
                "actingParties": acting_parties,
                "consuming": consuming,
                "witnessParties": witness_parties,
                "lastDescendantNodeId": last_descendant_node_id,
                "packageName": package_name,
                "acsDelta": acs_delta,
            }
        )
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if exercise_result is not UNSET:
            field_dict["exerciseResult"] = exercise_result
        if implemented_interfaces is not UNSET:
            field_dict["implementedInterfaces"] = implemented_interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset")

        node_id = d.pop("nodeId")

        contract_id = d.pop("contractId")

        template_id = d.pop("templateId")

        choice = d.pop("choice")

        choice_argument = d.pop("choiceArgument")

        acting_parties = cast(list[str], d.pop("actingParties"))

        consuming = d.pop("consuming")

        witness_parties = cast(list[str], d.pop("witnessParties"))

        last_descendant_node_id = d.pop("lastDescendantNodeId")

        package_name = d.pop("packageName")

        acs_delta = d.pop("acsDelta")

        interface_id = d.pop("interfaceId", UNSET)

        exercise_result = d.pop("exerciseResult", UNSET)

        implemented_interfaces = cast(list[str], d.pop("implementedInterfaces", UNSET))

        exercised_event = cls(
            offset=offset,
            node_id=node_id,
            contract_id=contract_id,
            template_id=template_id,
            choice=choice,
            choice_argument=choice_argument,
            acting_parties=acting_parties,
            consuming=consuming,
            witness_parties=witness_parties,
            last_descendant_node_id=last_descendant_node_id,
            package_name=package_name,
            acs_delta=acs_delta,
            interface_id=interface_id,
            exercise_result=exercise_result,
            implemented_interfaces=implemented_interfaces,
        )

        exercised_event.additional_properties = d
        return exercised_event

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
