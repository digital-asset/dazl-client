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
    from ..models.tree_event_type_0 import TreeEventType0
    from ..models.tree_event_type_1 import TreeEventType1


T = TypeVar("T", bound="MapIntTreeEvent")


@_attrs_define
class MapIntTreeEvent:
    """ """

    additional_properties: dict[str, TreeEventType0 | TreeEventType1] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.tree_event_type_0 import TreeEventType0

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, TreeEventType0):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tree_event_type_0 import TreeEventType0
        from ..models.tree_event_type_1 import TreeEventType1

        d = dict(src_dict)
        map_int_tree_event = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> TreeEventType0 | TreeEventType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_tree_event_type_0 = TreeEventType0.from_dict(data)

                    return componentsschemas_tree_event_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tree_event_type_1 = TreeEventType1.from_dict(data)

                return componentsschemas_tree_event_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        map_int_tree_event.additional_properties = additional_properties
        return map_int_tree_event

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> TreeEventType0 | TreeEventType1:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: TreeEventType0 | TreeEventType1) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
