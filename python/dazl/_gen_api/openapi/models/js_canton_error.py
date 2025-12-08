# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_string import MapString


T = TypeVar("T", bound="JsCantonError")


@_attrs_define
class JsCantonError:
    """
    Attributes:
        code (str):
        cause (str):
        context (MapString):
        error_category (int):
        correlation_id (str | Unset):
        trace_id (str | Unset):
        resources (list[list[str]] | Unset):
        grpc_code_value (int | Unset):
        retry_info (str | Unset):
        definite_answer (bool | Unset):
    """

    code: str
    cause: str
    context: MapString
    error_category: int
    correlation_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET
    resources: list[list[str]] | Unset = UNSET
    grpc_code_value: int | Unset = UNSET
    retry_info: str | Unset = UNSET
    definite_answer: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        cause = self.cause

        context = self.context.to_dict()

        error_category = self.error_category

        correlation_id = self.correlation_id

        trace_id = self.trace_id

        resources: list[list[str]] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data

                resources.append(resources_item)

        grpc_code_value = self.grpc_code_value

        retry_info = self.retry_info

        definite_answer = self.definite_answer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "cause": cause,
                "context": context,
                "errorCategory": error_category,
            }
        )
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id
        if resources is not UNSET:
            field_dict["resources"] = resources
        if grpc_code_value is not UNSET:
            field_dict["grpcCodeValue"] = grpc_code_value
        if retry_info is not UNSET:
            field_dict["retryInfo"] = retry_info
        if definite_answer is not UNSET:
            field_dict["definiteAnswer"] = definite_answer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_string import MapString

        d = dict(src_dict)
        code = d.pop("code")

        cause = d.pop("cause")

        context = MapString.from_dict(d.pop("context"))

        error_category = d.pop("errorCategory")

        correlation_id = d.pop("correlationId", UNSET)

        trace_id = d.pop("traceId", UNSET)

        _resources = d.pop("resources", UNSET)
        resources: list[list[str]] | Unset = UNSET
        if _resources is not UNSET:
            resources = []
            for resources_item_data in _resources:
                resources_item = cast(list[str], resources_item_data)

                resources.append(resources_item)

        grpc_code_value = d.pop("grpcCodeValue", UNSET)

        retry_info = d.pop("retryInfo", UNSET)

        definite_answer = d.pop("definiteAnswer", UNSET)

        js_canton_error = cls(
            code=code,
            cause=cause,
            context=context,
            error_category=error_category,
            correlation_id=correlation_id,
            trace_id=trace_id,
            resources=resources,
            grpc_code_value=grpc_code_value,
            retry_info=retry_info,
            definite_answer=definite_answer,
        )

        js_canton_error.additional_properties = d
        return js_canton_error

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
