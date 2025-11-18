from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_command import CreateCommand


T = TypeVar("T", bound="CommandType1")


@_attrs_define
class CommandType1:
    """
    Attributes:
        create_command (CreateCommand): Create a new contract instance based on a template.
    """

    create_command: CreateCommand
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_command = self.create_command.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CreateCommand": create_command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_command import CreateCommand

        d = dict(src_dict)
        create_command = CreateCommand.from_dict(d.pop("CreateCommand"))

        command_type_1 = cls(
            create_command=create_command,
        )

        command_type_1.additional_properties = d
        return command_type_1

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
