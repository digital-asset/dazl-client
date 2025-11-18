from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Identifier")


@_attrs_define
class Identifier:
    """
    Attributes:
        package_id (str):
        module_name (str):
        entity_name (str):
    """

    package_id: str
    module_name: str
    entity_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_id = self.package_id

        module_name = self.module_name

        entity_name = self.entity_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packageId": package_id,
                "moduleName": module_name,
                "entityName": entity_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_id = d.pop("packageId")

        module_name = d.pop("moduleName")

        entity_name = d.pop("entityName")

        identifier = cls(
            package_id=package_id,
            module_name=module_name,
            entity_name=entity_name,
        )

        identifier.additional_properties = d
        return identifier

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
