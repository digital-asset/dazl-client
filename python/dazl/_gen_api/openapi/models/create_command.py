from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="CreateCommand")


@_attrs_define
class CreateCommand:
    """Create a new contract instance based on a template.

    Attributes:
        template_id (str): The template of contract the client wants to create.
            Both package-name and package-id reference identifier formats for the template-id are supported.
            Note: The package-id reference identifier format is deprecated. We plan to end support for this format in
            version 3.4.

            Required
        create_arguments (Any): The arguments required for creating a contract from this template.
            Required
    """

    template_id: str
    create_arguments: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        create_arguments = self.create_arguments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateId": template_id,
                "createArguments": create_arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("templateId")

        create_arguments = d.pop("createArguments")

        create_command = cls(
            template_id=template_id,
            create_arguments=create_arguments,
        )

        create_command.additional_properties = d
        return create_command

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
