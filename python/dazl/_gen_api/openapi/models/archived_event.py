# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchivedEvent")


@_attrs_define
class ArchivedEvent:
    """Records that a contract has been archived, and choices may no longer be exercised on it.

    Attributes:
        offset (int): The offset of origin.
            Offsets are managed by the participant nodes.
            Transactions can thus NOT be assumed to have the same offsets on different participant nodes.
            Required, it is a valid absolute offset (positive integer)
        node_id (int): The position of this event in the originating transaction or reassignment.
            Node IDs are not necessarily equal across participants,
            as these may see different projections/parts of transactions.
            Required, must be valid node ID (non-negative integer)
        contract_id (str): The ID of the archived contract.
            Must be a valid LedgerString (as described in ``value.proto``).
            Required
        template_id (str): Identifies the template that defines the choice that archived the contract.
            This template's package-id may differ from the target contract's package-id
            if the target contract has been upgraded or downgraded.

            The identifier uses the package-id reference format.

            Required
        package_name (str): The package name of the contract.
            Required
        witness_parties (list[str] | Unset): The parties that are notified of this event. For an ``ArchivedEvent``,
            these are the intersection of the stakeholders of the contract in
            question and the parties specified in the ``TransactionFilter``. The
            stakeholders are the union of the signatories and the observers of
            the contract.
            Each one of its elements must be a valid PartyIdString (as described
            in ``value.proto``).
            Required
        implemented_interfaces (list[str] | Unset): The interfaces implemented by the target template that have been
            matched from the interface filter query.
            Populated only in case interface filters with include_interface_view set.

            If defined, the identifier uses the package-id reference format.

            Optional
    """

    offset: int
    node_id: int
    contract_id: str
    template_id: str
    package_name: str
    witness_parties: list[str] | Unset = UNSET
    implemented_interfaces: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        node_id = self.node_id

        contract_id = self.contract_id

        template_id = self.template_id

        package_name = self.package_name

        witness_parties: list[str] | Unset = UNSET
        if not isinstance(self.witness_parties, Unset):
            witness_parties = self.witness_parties

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
                "packageName": package_name,
            }
        )
        if witness_parties is not UNSET:
            field_dict["witnessParties"] = witness_parties
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

        package_name = d.pop("packageName")

        witness_parties = cast(list[str], d.pop("witnessParties", UNSET))

        implemented_interfaces = cast(list[str], d.pop("implementedInterfaces", UNSET))

        archived_event = cls(
            offset=offset,
            node_id=node_id,
            contract_id=contract_id,
            template_id=template_id,
            package_name=package_name,
            witness_parties=witness_parties,
            implemented_interfaces=implemented_interfaces,
        )

        archived_event.additional_properties = d
        return archived_event

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
