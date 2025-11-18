from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.js_active_contract import JsActiveContract


T = TypeVar("T", bound="JsContractEntryType0")


@_attrs_define
class JsContractEntryType0:
    """
    Attributes:
        js_active_contract (JsActiveContract):
    """

    js_active_contract: JsActiveContract
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        js_active_contract = self.js_active_contract.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "JsActiveContract": js_active_contract,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_active_contract import JsActiveContract

        d = dict(src_dict)
        js_active_contract = JsActiveContract.from_dict(d.pop("JsActiveContract"))

        js_contract_entry_type_0 = cls(
            js_active_contract=js_active_contract,
        )

        js_contract_entry_type_0.additional_properties = d
        return js_contract_entry_type_0

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
