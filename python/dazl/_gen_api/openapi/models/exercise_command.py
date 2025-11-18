from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExerciseCommand")


@_attrs_define
class ExerciseCommand:
    """Exercise a choice on an existing contract.

    Attributes:
        template_id (str): The template or interface of the contract the client wants to exercise.
            Both package-name and package-id reference identifier formats for the template-id are supported.
            Note: The package-id reference identifier format is deprecated. We plan to end support for this format in
            version 3.4.
            To exercise a choice on an interface, specify the interface identifier in the template_id field.

            Required
        contract_id (str): The ID of the contract the client wants to exercise upon.
            Must be a valid LedgerString (as described in ``value.proto``).
            Required
        choice (str): The name of the choice the client wants to exercise.
            Must be a valid NameString (as described in ``value.proto``)
            Required
        choice_argument (Any): The argument for this choice.
            Required
    """

    template_id: str
    contract_id: str
    choice: str
    choice_argument: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        contract_id = self.contract_id

        choice = self.choice

        choice_argument = self.choice_argument

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "templateId": template_id,
                "contractId": contract_id,
                "choice": choice,
                "choiceArgument": choice_argument,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("templateId")

        contract_id = d.pop("contractId")

        choice = d.pop("choice")

        choice_argument = d.pop("choiceArgument")

        exercise_command = cls(
            template_id=template_id,
            contract_id=contract_id,
            choice=choice,
            choice_argument=choice_argument,
        )

        exercise_command.additional_properties = d
        return exercise_command

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
