# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="CostEstimation")


@_attrs_define
class CostEstimation:
    """Estimation of the cost of submitting the prepared transaction
    The estimation is done against the synchronizer chosen during preparation of the transaction
    (or the one explicitly requested).
    The cost of re-assigning contracts to another synchronizer when necessary is not included in the estimation.

        Attributes:
            estimation_timestamp (str): Timestamp at which the estimation was made

                Required
            confirmation_request_traffic_cost_estimation (int): Estimated traffic cost of the confirmation request
                associated with the transaction

                Required
            confirmation_response_traffic_cost_estimation (int): Estimated traffic cost of the confirmation response
                associated with the transaction
                This field can also be used as an indication of the cost that other potential confirming nodes
                of the party will incur to approve or reject the transaction

                Required
            total_traffic_cost_estimation (int): Sum of the fields above

                Required
    """

    estimation_timestamp: str
    confirmation_request_traffic_cost_estimation: int
    confirmation_response_traffic_cost_estimation: int
    total_traffic_cost_estimation: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        estimation_timestamp = self.estimation_timestamp

        confirmation_request_traffic_cost_estimation = (
            self.confirmation_request_traffic_cost_estimation
        )

        confirmation_response_traffic_cost_estimation = (
            self.confirmation_response_traffic_cost_estimation
        )

        total_traffic_cost_estimation = self.total_traffic_cost_estimation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "estimationTimestamp": estimation_timestamp,
                "confirmationRequestTrafficCostEstimation": confirmation_request_traffic_cost_estimation,
                "confirmationResponseTrafficCostEstimation": confirmation_response_traffic_cost_estimation,
                "totalTrafficCostEstimation": total_traffic_cost_estimation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        estimation_timestamp = d.pop("estimationTimestamp")

        confirmation_request_traffic_cost_estimation = d.pop(
            "confirmationRequestTrafficCostEstimation"
        )

        confirmation_response_traffic_cost_estimation = d.pop(
            "confirmationResponseTrafficCostEstimation"
        )

        total_traffic_cost_estimation = d.pop("totalTrafficCostEstimation")

        cost_estimation = cls(
            estimation_timestamp=estimation_timestamp,
            confirmation_request_traffic_cost_estimation=confirmation_request_traffic_cost_estimation,
            confirmation_response_traffic_cost_estimation=confirmation_response_traffic_cost_estimation,
            total_traffic_cost_estimation=total_traffic_cost_estimation,
        )

        cost_estimation.additional_properties = d
        return cost_estimation

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
