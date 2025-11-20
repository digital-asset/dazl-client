from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrefetchContractKey")


@_attrs_define
class PrefetchContractKey:
    """Preload contracts

    Attributes:
        contract_key (Any): The key of the contract the client wants to prefetch.
            Required
        template_id (str | Unset): The template of contract the client wants to prefetch.
            Both package-name and package-id reference identifier formats for the template-id are supported.
            Note: The package-id reference identifier format is deprecated. We plan to end support for this format in
            version 3.4.

            Required
    """

    contract_key: Any
    template_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contract_key = self.contract_key

        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contractKey": contract_key,
            }
        )
        if template_id is not UNSET:
            field_dict["templateId"] = template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contract_key = d.pop("contractKey")

        template_id = d.pop("templateId", UNSET)

        prefetch_contract_key = cls(
            contract_key=contract_key,
            template_id=template_id,
        )

        prefetch_contract_key.additional_properties = d
        return prefetch_contract_key

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
