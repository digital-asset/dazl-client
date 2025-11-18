from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.js_status import JsStatus


T = TypeVar("T", bound="JsInterfaceView")


@_attrs_define
class JsInterfaceView:
    """View of a create event matched by an interface filter.

    Attributes:
        interface_id (str): The interface implemented by the matched event.
            The identifier uses the package-id reference format.

            Required
        view_status (JsStatus):
        view_value (Any | Unset): The value of the interface's view method on this event.
            Set if it was requested in the ``InterfaceFilter`` and it could be
            successfully computed.
            Optional
    """

    interface_id: str
    view_status: JsStatus
    view_value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_id = self.interface_id

        view_status = self.view_status.to_dict()

        view_value = self.view_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaceId": interface_id,
                "viewStatus": view_status,
            }
        )
        if view_value is not UNSET:
            field_dict["viewValue"] = view_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_status import JsStatus

        d = dict(src_dict)
        interface_id = d.pop("interfaceId")

        view_status = JsStatus.from_dict(d.pop("viewStatus"))

        view_value = d.pop("viewValue", UNSET)

        js_interface_view = cls(
            interface_id=interface_id,
            view_status=view_status,
            view_value=view_value,
        )

        js_interface_view.additional_properties = d
        return js_interface_view

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
