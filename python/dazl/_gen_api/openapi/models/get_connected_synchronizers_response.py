from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connected_synchronizer import ConnectedSynchronizer


T = TypeVar("T", bound="GetConnectedSynchronizersResponse")


@_attrs_define
class GetConnectedSynchronizersResponse:
    """
    Attributes:
        connected_synchronizers (list[ConnectedSynchronizer] | Unset):
    """

    connected_synchronizers: list[ConnectedSynchronizer] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected_synchronizers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connected_synchronizers, Unset):
            connected_synchronizers = []
            for connected_synchronizers_item_data in self.connected_synchronizers:
                connected_synchronizers_item = connected_synchronizers_item_data.to_dict()
                connected_synchronizers.append(connected_synchronizers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected_synchronizers is not UNSET:
            field_dict["connectedSynchronizers"] = connected_synchronizers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connected_synchronizer import ConnectedSynchronizer

        d = dict(src_dict)
        _connected_synchronizers = d.pop("connectedSynchronizers", UNSET)
        connected_synchronizers: list[ConnectedSynchronizer] | Unset = UNSET
        if _connected_synchronizers is not UNSET:
            connected_synchronizers = []
            for connected_synchronizers_item_data in _connected_synchronizers:
                connected_synchronizers_item = ConnectedSynchronizer.from_dict(
                    connected_synchronizers_item_data
                )

                connected_synchronizers.append(connected_synchronizers_item)

        get_connected_synchronizers_response = cls(
            connected_synchronizers=connected_synchronizers,
        )

        get_connected_synchronizers_response.additional_properties = d
        return get_connected_synchronizers_response

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
