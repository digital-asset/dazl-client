from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.js_incomplete_unassigned import JsIncompleteUnassigned


T = TypeVar("T", bound="JsContractEntryType3")


@_attrs_define
class JsContractEntryType3:
    """
    Attributes:
        js_incomplete_unassigned (JsIncompleteUnassigned):
    """

    js_incomplete_unassigned: JsIncompleteUnassigned
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        js_incomplete_unassigned = self.js_incomplete_unassigned.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "JsIncompleteUnassigned": js_incomplete_unassigned,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_incomplete_unassigned import JsIncompleteUnassigned

        d = dict(src_dict)
        js_incomplete_unassigned = JsIncompleteUnassigned.from_dict(d.pop("JsIncompleteUnassigned"))

        js_contract_entry_type_3 = cls(
            js_incomplete_unassigned=js_incomplete_unassigned,
        )

        js_contract_entry_type_3.additional_properties = d
        return js_contract_entry_type_3

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
