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
    from ..models.js_interface_view import JsInterfaceView


T = TypeVar("T", bound="CreatedEvent")


@_attrs_define
class CreatedEvent:
    """Records that a contract has been created, and choices may now be exercised on it.

    Attributes:
        offset (int): The offset of origin, which has contextual meaning, please see description at messages that
            include a CreatedEvent.
            Offsets are managed by the participant nodes.
            Transactions can thus NOT be assumed to have the same offsets on different participant nodes.
            Required, it is a valid absolute offset (positive integer)
        node_id (int): The position of this event in the originating transaction or reassignment.
            The origin has contextual meaning, please see description at messages that include a CreatedEvent.
            Node IDs are not necessarily equal across participants,
            as these may see different projections/parts of transactions.
            Required, must be valid node ID (non-negative integer)
        contract_id (str): The ID of the created contract.
            Must be a valid LedgerString (as described in ``value.proto``).
            Required
        template_id (str): The template of the created contract.
            The identifier uses the package-id reference format.

            Required
        created_event_blob (str): Opaque representation of contract create event payload intended for forwarding
            to an API server as a contract disclosed as part of a command
            submission.
            Optional
        created_at (str): Ledger effective time of the transaction that created the contract.
            Required
        package_name (str): The package name of the created contract.
            Required
        representative_package_id (str): A package-id present in the participant package store that typechecks the
            contract's argument.
            This may differ from the package-id of the template used to create the contract.
            For contracts created before Canton 3.4, this field matches the contract's creation package-id.

            NOTE: Experimental, server internal concept, not for client consumption. Subject to change without notice.

            Required
        acs_delta (bool): Whether this event would be part of respective ACS_DELTA shaped stream,
            and should therefore considered when tracking contract activeness on the client-side.
            Required
        contract_key (Any | Unset): The key of the created contract.
            This will be set if and only if ``template_id`` defines a contract key.
            Optional
        create_argument (Any | Unset):
        interface_views (list[JsInterfaceView] | Unset): Interface views specified in the transaction filter.
            Includes an ``InterfaceView`` for each interface for which there is a ``InterfaceFilter`` with

            - its party in the ``witness_parties`` of this event,
            - and which is implemented by the template of this event,
            - and which has ``include_interface_view`` set.

            Optional
        witness_parties (list[str] | Unset): The parties that are notified of this event. When a ``CreatedEvent``
            is returned as part of a transaction tree or ledger-effects transaction, this will include all
            the parties specified in the ``TransactionFilter`` that are witnesses  of the event
            (the stakeholders of the contract and all informees of all the ancestors
            of this create action that this participant knows about).
            If served as part of a ACS delta transaction those will
            be limited to all parties specified in the ``TransactionFilter`` that
            are stakeholders of the contract (i.e. either signatories or observers).
            If the ``CreatedEvent`` is returned as part of an AssignedEvent,
            ActiveContract or IncompleteUnassigned (so the event is related to
            an assignment or unassignment): this will include all parties of the
            ``TransactionFilter`` that are stakeholders of the contract.

            The behavior of reading create events visible to parties not hosted
            on the participant node serving the Ledger API is undefined. Concretely,
            there is neither a guarantee that the participant node will serve all their
            create events on the ACS stream, nor is there a guarantee that matching archive
            events are delivered for such create events.

            For most clients this is not a problem, as they only read events for parties
            that are hosted on the participant node. If you need to read events
            for parties that may not be hosted at all times on the participant node,
            subscribe to the ``TopologyEvent``s for that party by setting a corresponding
            ``UpdateFormat``.  Using these events, query the ACS as-of an offset where the
            party is hosted on the participant node, and ignore create events at offsets
            where the party is not hosted on the participant node.
            Required
        signatories (list[str] | Unset): The signatories for this contract as specified by the template.
            Required
        observers (list[str] | Unset): The observers for this contract as specified explicitly by the template or
            implicitly as choice controllers.
            This field never contains parties that are signatories.
            Required
    """

    offset: int
    node_id: int
    contract_id: str
    template_id: str
    created_event_blob: str
    created_at: str
    package_name: str
    representative_package_id: str
    acs_delta: bool
    contract_key: Any | Unset = UNSET
    create_argument: Any | Unset = UNSET
    interface_views: list[JsInterfaceView] | Unset = UNSET
    witness_parties: list[str] | Unset = UNSET
    signatories: list[str] | Unset = UNSET
    observers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        node_id = self.node_id

        contract_id = self.contract_id

        template_id = self.template_id

        created_event_blob = self.created_event_blob

        created_at = self.created_at

        package_name = self.package_name

        representative_package_id = self.representative_package_id

        acs_delta = self.acs_delta

        contract_key = self.contract_key

        create_argument = self.create_argument

        interface_views: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interface_views, Unset):
            interface_views = []
            for interface_views_item_data in self.interface_views:
                interface_views_item = interface_views_item_data.to_dict()
                interface_views.append(interface_views_item)

        witness_parties: list[str] | Unset = UNSET
        if not isinstance(self.witness_parties, Unset):
            witness_parties = self.witness_parties

        signatories: list[str] | Unset = UNSET
        if not isinstance(self.signatories, Unset):
            signatories = self.signatories

        observers: list[str] | Unset = UNSET
        if not isinstance(self.observers, Unset):
            observers = self.observers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "nodeId": node_id,
                "contractId": contract_id,
                "templateId": template_id,
                "createdEventBlob": created_event_blob,
                "createdAt": created_at,
                "packageName": package_name,
                "representativePackageId": representative_package_id,
                "acsDelta": acs_delta,
            }
        )
        if contract_key is not UNSET:
            field_dict["contractKey"] = contract_key
        if create_argument is not UNSET:
            field_dict["createArgument"] = create_argument
        if interface_views is not UNSET:
            field_dict["interfaceViews"] = interface_views
        if witness_parties is not UNSET:
            field_dict["witnessParties"] = witness_parties
        if signatories is not UNSET:
            field_dict["signatories"] = signatories
        if observers is not UNSET:
            field_dict["observers"] = observers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_interface_view import JsInterfaceView

        d = dict(src_dict)
        offset = d.pop("offset")

        node_id = d.pop("nodeId")

        contract_id = d.pop("contractId")

        template_id = d.pop("templateId")

        created_event_blob = d.pop("createdEventBlob")

        created_at = d.pop("createdAt")

        package_name = d.pop("packageName")

        representative_package_id = d.pop("representativePackageId")

        acs_delta = d.pop("acsDelta")

        contract_key = d.pop("contractKey", UNSET)

        create_argument = d.pop("createArgument", UNSET)

        _interface_views = d.pop("interfaceViews", UNSET)
        interface_views: list[JsInterfaceView] | Unset = UNSET
        if _interface_views is not UNSET:
            interface_views = []
            for interface_views_item_data in _interface_views:
                interface_views_item = JsInterfaceView.from_dict(
                    interface_views_item_data
                )

                interface_views.append(interface_views_item)

        witness_parties = cast(list[str], d.pop("witnessParties", UNSET))

        signatories = cast(list[str], d.pop("signatories", UNSET))

        observers = cast(list[str], d.pop("observers", UNSET))

        created_event = cls(
            offset=offset,
            node_id=node_id,
            contract_id=contract_id,
            template_id=template_id,
            created_event_blob=created_event_blob,
            created_at=created_at,
            package_name=package_name,
            representative_package_id=representative_package_id,
            acs_delta=acs_delta,
            contract_key=contract_key,
            create_argument=create_argument,
            interface_views=interface_views,
            witness_parties=witness_parties,
            signatories=signatories,
            observers=observers,
        )

        created_event.additional_properties = d
        return created_event

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
