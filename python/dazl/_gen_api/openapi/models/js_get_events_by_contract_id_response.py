from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.js_archived import JsArchived
    from ..models.js_created import JsCreated


T = TypeVar("T", bound="JsGetEventsByContractIdResponse")


@_attrs_define
class JsGetEventsByContractIdResponse:
    """
    Attributes:
        created (JsCreated | Unset):
        archived (JsArchived | Unset):
    """

    created: JsCreated | Unset = UNSET
    archived: JsArchived | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        archived: dict[str, Any] | Unset = UNSET
        if not isinstance(self.archived, Unset):
            archived = self.archived.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.js_archived import JsArchived
        from ..models.js_created import JsCreated

        d = dict(src_dict)
        _created = d.pop("created", UNSET)
        created: JsCreated | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = JsCreated.from_dict(_created)

        _archived = d.pop("archived", UNSET)
        archived: JsArchived | Unset
        if isinstance(_archived, Unset):
            archived = UNSET
        else:
            archived = JsArchived.from_dict(_archived)

        js_get_events_by_contract_id_response = cls(
            created=created,
            archived=archived,
        )

        js_get_events_by_contract_id_response.additional_properties = d
        return js_get_events_by_contract_id_response

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
