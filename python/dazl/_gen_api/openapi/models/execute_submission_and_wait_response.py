# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExecuteSubmissionAndWaitResponse")


@_attrs_define
class ExecuteSubmissionAndWaitResponse:
    """
    Attributes:
        update_id (str): The id of the transaction that resulted from the submitted command.
            Must be a valid LedgerString (as described in ``value.proto``).
            Required
        completion_offset (int): The details of the offset field are described in ``community/ledger-api/README.md``.
            Required
    """

    update_id: str
    completion_offset: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        update_id = self.update_id

        completion_offset = self.completion_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updateId": update_id,
                "completionOffset": completion_offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        update_id = d.pop("updateId")

        completion_offset = d.pop("completionOffset")

        execute_submission_and_wait_response = cls(
            update_id=update_id,
            completion_offset=completion_offset,
        )

        execute_submission_and_wait_response.additional_properties = d
        return execute_submission_and_wait_response

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
