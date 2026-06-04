# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnassignedEvent")


@_attrs_define
class UnassignedEvent:
    """Records that a contract has been unassigned, and it becomes unusable on the source synchronizer

    Attributes:
        reassignment_id (str): The ID of the unassignment. This needs to be used as an input for a assign
            ReassignmentCommand.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
        contract_id (str): The ID of the reassigned contract.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
        template_id (str): The template of the reassigned contract.
            The identifier uses the package-id reference format.

            Required
        source (str): The ID of the source synchronizer
            Must be a valid synchronizer id

            Required
        target (str): The ID of the target synchronizer
            Must be a valid synchronizer id

            Required
        reassignment_counter (int): Each corresponding assigned and unassigned event has the same reassignment_counter.
            This strictly increases
            with each unassign command for the same contract. Creation of the contract corresponds to reassignment_counter
            equals zero.

            Required
        witness_parties (list[str]): The parties that are notified of this event.

            Required: must be non-empty
        package_name (str): The package name of the contract.

            Required
        offset (int): The offset of origin.
            Offsets are managed by the participant nodes.
            Reassignments can thus NOT be assumed to have the same offsets on different participant nodes.
            Must be a valid absolute offset (positive integer)

            Required
        node_id (int): The position of this event in the originating reassignment.
            Node IDs are not necessarily equal across participants,
            as these may see different projections/parts of reassignments.
            Must be valid node ID (non-negative integer)

            Required
        submitter (str | Unset): Party on whose behalf the unassign command was executed.
            Empty if the unassignment happened offline via the repair service.
            Must be a valid PartyIdString (as described in ``value.proto``).

            Optional
        assignment_exclusivity (str | Unset): Assignment exclusivity
            Before this time (measured on the target synchronizer), only the submitter of the unassignment can initiate the
            assignment
            Defined for reassigning participants.

            Optional
    """

    reassignment_id: str
    contract_id: str
    template_id: str
    source: str
    target: str
    reassignment_counter: int
    witness_parties: list[str]
    package_name: str
    offset: int
    node_id: int
    submitter: str | Unset = UNSET
    assignment_exclusivity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reassignment_id = self.reassignment_id

        contract_id = self.contract_id

        template_id = self.template_id

        source = self.source

        target = self.target

        reassignment_counter = self.reassignment_counter

        witness_parties = self.witness_parties

        package_name = self.package_name

        offset = self.offset

        node_id = self.node_id

        submitter = self.submitter

        assignment_exclusivity = self.assignment_exclusivity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reassignmentId": reassignment_id,
                "contractId": contract_id,
                "templateId": template_id,
                "source": source,
                "target": target,
                "reassignmentCounter": reassignment_counter,
                "witnessParties": witness_parties,
                "packageName": package_name,
                "offset": offset,
                "nodeId": node_id,
            }
        )
        if submitter is not UNSET:
            field_dict["submitter"] = submitter
        if assignment_exclusivity is not UNSET:
            field_dict["assignmentExclusivity"] = assignment_exclusivity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reassignment_id = d.pop("reassignmentId")

        contract_id = d.pop("contractId")

        template_id = d.pop("templateId")

        source = d.pop("source")

        target = d.pop("target")

        reassignment_counter = d.pop("reassignmentCounter")

        witness_parties = cast(list[str], d.pop("witnessParties"))

        package_name = d.pop("packageName")

        offset = d.pop("offset")

        node_id = d.pop("nodeId")

        submitter = d.pop("submitter", UNSET)

        assignment_exclusivity = d.pop("assignmentExclusivity", UNSET)

        unassigned_event = cls(
            reassignment_id=reassignment_id,
            contract_id=contract_id,
            template_id=template_id,
            source=source,
            target=target,
            reassignment_counter=reassignment_counter,
            witness_parties=witness_parties,
            package_name=package_name,
            offset=offset,
            node_id=node_id,
            submitter=submitter,
            assignment_exclusivity=assignment_exclusivity,
        )

        unassigned_event.additional_properties = d
        return unassigned_event

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
