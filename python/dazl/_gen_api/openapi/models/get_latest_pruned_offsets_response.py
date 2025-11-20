from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="GetLatestPrunedOffsetsResponse")


@_attrs_define
class GetLatestPrunedOffsetsResponse:
    """
    Attributes:
        participant_pruned_up_to_inclusive (int): It will always be a non-negative integer.
            If positive, the absolute offset up to which the ledger has been pruned,
            disregarding the state of all divulged contracts pruning.
            If zero, the ledger has not been pruned yet.
        all_divulged_contracts_pruned_up_to_inclusive (int): It will always be a non-negative integer.
            If positive, the absolute offset up to which all divulged events have been pruned on the ledger.
            It can be at or before the ``participant_pruned_up_to_inclusive`` offset.
            For more details about all divulged events pruning,
            see ``PruneRequest.prune_all_divulged_contracts`` in ``participant_pruning_service.proto``.
            If zero, the divulged events have not been pruned yet.
    """

    participant_pruned_up_to_inclusive: int
    all_divulged_contracts_pruned_up_to_inclusive: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        participant_pruned_up_to_inclusive = self.participant_pruned_up_to_inclusive

        all_divulged_contracts_pruned_up_to_inclusive = (
            self.all_divulged_contracts_pruned_up_to_inclusive
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "participantPrunedUpToInclusive": participant_pruned_up_to_inclusive,
                "allDivulgedContractsPrunedUpToInclusive": all_divulged_contracts_pruned_up_to_inclusive,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        participant_pruned_up_to_inclusive = d.pop("participantPrunedUpToInclusive")

        all_divulged_contracts_pruned_up_to_inclusive = d.pop(
            "allDivulgedContractsPrunedUpToInclusive"
        )

        get_latest_pruned_offsets_response = cls(
            participant_pruned_up_to_inclusive=participant_pruned_up_to_inclusive,
            all_divulged_contracts_pruned_up_to_inclusive=all_divulged_contracts_pruned_up_to_inclusive,
        )

        get_latest_pruned_offsets_response.additional_properties = d
        return get_latest_pruned_offsets_response

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
