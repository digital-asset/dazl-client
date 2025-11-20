from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DisclosedContract")


@_attrs_define
class DisclosedContract:
    """An additional contract that is used to resolve
    contract & contract key lookups.

        Attributes:
            contract_id (str): The contract id

                If provided, used to validate the contract id of the contract serialized in the created_event_blob.
                Optional
            created_event_blob (str): Opaque byte string containing the complete payload required by the Daml engine
                to reconstruct a contract not known to the receiving participant.
                Required
            synchronizer_id (str): The ID of the synchronizer where the contract is currently assigned
                Optional
            template_id (str | Unset): The template id of the contract.
                The identifier uses the package-id reference format.

                If provided, used to validate the template id of the contract serialized in the created_event_blob.
                Optional
    """

    contract_id: str
    created_event_blob: str
    synchronizer_id: str
    template_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_id = self.contract_id

        created_event_blob = self.created_event_blob

        synchronizer_id = self.synchronizer_id

        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contractId": contract_id,
                "createdEventBlob": created_event_blob,
                "synchronizerId": synchronizer_id,
            }
        )
        if template_id is not UNSET:
            field_dict["templateId"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_id = d.pop("contractId")

        created_event_blob = d.pop("createdEventBlob")

        synchronizer_id = d.pop("synchronizerId")

        template_id = d.pop("templateId", UNSET)

        disclosed_contract = cls(
            contract_id=contract_id,
            created_event_blob=created_event_blob,
            synchronizer_id=synchronizer_id,
            template_id=template_id,
        )

        disclosed_contract.additional_properties = d
        return disclosed_contract

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
