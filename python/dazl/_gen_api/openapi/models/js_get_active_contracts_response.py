# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.js_contract_entry_type_0 import JsContractEntryType0
    from ..models.js_contract_entry_type_1 import JsContractEntryType1
    from ..models.js_contract_entry_type_2 import JsContractEntryType2
    from ..models.js_contract_entry_type_3 import JsContractEntryType3


T = TypeVar("T", bound="JsGetActiveContractsResponse")


@_attrs_define
class JsGetActiveContractsResponse:
    """
    Attributes:
        workflow_id (str): The workflow ID used in command submission which corresponds to the contract_entry. Only set
            if
            the ``workflow_id`` for the command was set.
            Must be a valid LedgerString (as described in ``value.proto``).
            Optional
        contract_entry (JsContractEntryType0 | JsContractEntryType1 | JsContractEntryType2 | JsContractEntryType3): For
            a contract there could be multiple contract_entry-s in the entire snapshot. These together define
            the state of one contract in the snapshot.
            A contract_entry is included in the result, if and only if there is at least one stakeholder party of the
            contract
            that is hosted on the synchronizer at the time of the event and the party satisfies the
            ``TransactionFilter`` in the query.
    """

    workflow_id: str
    contract_entry: (
        JsContractEntryType0
        | JsContractEntryType1
        | JsContractEntryType2
        | JsContractEntryType3
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.js_contract_entry_type_0 import JsContractEntryType0
        from ..models.js_contract_entry_type_1 import JsContractEntryType1
        from ..models.js_contract_entry_type_2 import JsContractEntryType2

        workflow_id = self.workflow_id

        contract_entry: dict[str, Any]
        if isinstance(self.contract_entry, JsContractEntryType0):
            contract_entry = self.contract_entry.to_dict()
        elif isinstance(self.contract_entry, JsContractEntryType1):
            contract_entry = self.contract_entry.to_dict()
        elif isinstance(self.contract_entry, JsContractEntryType2):
            contract_entry = self.contract_entry.to_dict()
        else:
            contract_entry = self.contract_entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflowId": workflow_id,
                "contractEntry": contract_entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_contract_entry_type_0 import JsContractEntryType0
        from ..models.js_contract_entry_type_1 import JsContractEntryType1
        from ..models.js_contract_entry_type_2 import JsContractEntryType2
        from ..models.js_contract_entry_type_3 import JsContractEntryType3

        d = dict(src_dict)
        workflow_id = d.pop("workflowId")

        def _parse_contract_entry(
            data: object,
        ) -> (
            JsContractEntryType0
            | JsContractEntryType1
            | JsContractEntryType2
            | JsContractEntryType3
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_js_contract_entry_type_0 = (
                    JsContractEntryType0.from_dict(data)
                )

                return componentsschemas_js_contract_entry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_js_contract_entry_type_1 = (
                    JsContractEntryType1.from_dict(data)
                )

                return componentsschemas_js_contract_entry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_js_contract_entry_type_2 = (
                    JsContractEntryType2.from_dict(data)
                )

                return componentsschemas_js_contract_entry_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_js_contract_entry_type_3 = JsContractEntryType3.from_dict(
                data
            )

            return componentsschemas_js_contract_entry_type_3

        contract_entry = _parse_contract_entry(d.pop("contractEntry"))

        js_get_active_contracts_response = cls(
            workflow_id=workflow_id,
            contract_entry=contract_entry,
        )

        js_get_active_contracts_response.additional_properties = d
        return js_get_active_contracts_response

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
