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


T = TypeVar("T", bound="JsAssignedEvent")


@_attrs_define
class JsAssignedEvent:
    """Records that a contract has been assigned, and it can be used on the target synchronizer.

    Attributes:
        source (str): The ID of the source synchronizer.
            Must be a valid synchronizer id.
            Required
        target (str): The ID of the target synchronizer.
            Must be a valid synchronizer id.
            Required
        reassignment_id (str): The ID from the unassigned event.
            For correlation capabilities.
            Must be a valid LedgerString (as described in ``value.proto``).
            Required
        submitter (str): Party on whose behalf the assign command was executed.
            Empty if the assignment happened offline via the repair service.
            Must be a valid PartyIdString (as described in ``value.proto``).
            Optional
        reassignment_counter (int): Each corresponding assigned and unassigned event has the same reassignment_counter.
            This strictly increases
            with each unassign command for the same contract. Creation of the contract corresponds to reassignment_counter
            equals zero.
            Required
        created_event (CreatedEvent): Records that a contract has been created, and choices may now be exercised on it.
    """

    source: str
    target: str
    reassignment_id: str
    submitter: str
    reassignment_counter: int
    created_event: CreatedEvent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        target = self.target

        reassignment_id = self.reassignment_id

        submitter = self.submitter

        reassignment_counter = self.reassignment_counter

        created_event = self.created_event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "target": target,
                "reassignmentId": reassignment_id,
                "submitter": submitter,
                "reassignmentCounter": reassignment_counter,
                "createdEvent": created_event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.created_event import CreatedEvent

        d = dict(src_dict)
        source = d.pop("source")

        target = d.pop("target")

        reassignment_id = d.pop("reassignmentId")

        submitter = d.pop("submitter")

        reassignment_counter = d.pop("reassignmentCounter")

        created_event = CreatedEvent.from_dict(d.pop("createdEvent"))

        js_assigned_event = cls(
            source=source,
            target=target,
            reassignment_id=reassignment_id,
            submitter=submitter,
            reassignment_counter=reassignment_counter,
            created_event=created_event,
        )

        js_assigned_event.additional_properties = d
        return js_assigned_event

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
