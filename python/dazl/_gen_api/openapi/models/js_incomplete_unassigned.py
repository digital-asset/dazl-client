# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.created_event import CreatedEvent
    from ..models.unassigned_event import UnassignedEvent


T = TypeVar("T", bound="JsIncompleteUnassigned")


@_attrs_define
class JsIncompleteUnassigned:
    """
    Attributes:
        created_event (CreatedEvent): Records that a contract has been created, and choices may now be exercised on it.
        unassigned_event (UnassignedEvent): Records that a contract has been unassigned, and it becomes unusable on the
            source synchronizer
    """

    created_event: CreatedEvent
    unassigned_event: UnassignedEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_event = self.created_event.to_dict()

        unassigned_event = self.unassigned_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdEvent": created_event,
                "unassignedEvent": unassigned_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_event import CreatedEvent
        from ..models.unassigned_event import UnassignedEvent

        d = dict(src_dict)
        created_event = CreatedEvent.from_dict(d.pop("createdEvent"))

        unassigned_event = UnassignedEvent.from_dict(d.pop("unassignedEvent"))

        js_incomplete_unassigned = cls(
            created_event=created_event,
            unassigned_event=unassigned_event,
        )

        js_incomplete_unassigned.additional_properties = d
        return js_incomplete_unassigned

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
