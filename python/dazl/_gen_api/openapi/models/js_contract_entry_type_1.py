from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.js_empty import JsEmpty


T = TypeVar("T", bound="JsContractEntryType1")


@_attrs_define
class JsContractEntryType1:
    """
    Attributes:
        js_empty (JsEmpty):
    """

    js_empty: JsEmpty
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        js_empty = self.js_empty.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "JsEmpty": js_empty,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_empty import JsEmpty

        d = dict(src_dict)
        js_empty = JsEmpty.from_dict(d.pop("JsEmpty"))

        js_contract_entry_type_1 = cls(
            js_empty=js_empty,
        )

        js_contract_entry_type_1.additional_properties = d
        return js_contract_entry_type_1

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
