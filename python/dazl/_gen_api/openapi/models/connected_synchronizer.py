from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connected_synchronizer_permission import ConnectedSynchronizerPermission

T = TypeVar("T", bound="ConnectedSynchronizer")


@_attrs_define
class ConnectedSynchronizer:
    """
    Attributes:
        synchronizer_alias (str):
        synchronizer_id (str):
        permission (ConnectedSynchronizerPermission):
    """

    synchronizer_alias: str
    synchronizer_id: str
    permission: ConnectedSynchronizerPermission
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synchronizer_alias = self.synchronizer_alias

        synchronizer_id = self.synchronizer_id

        permission = self.permission.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "synchronizerAlias": synchronizer_alias,
                "synchronizerId": synchronizer_id,
                "permission": permission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        synchronizer_alias = d.pop("synchronizerAlias")

        synchronizer_id = d.pop("synchronizerId")

        permission = ConnectedSynchronizerPermission(d.pop("permission"))

        connected_synchronizer = cls(
            synchronizer_alias=synchronizer_alias,
            synchronizer_id=synchronizer_id,
            permission=permission,
        )

        connected_synchronizer.additional_properties = d
        return connected_synchronizer

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
