from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceContext")


@_attrs_define
class TraceContext:
    """
    Attributes:
        traceparent (str | Unset): https://www.w3.org/TR/trace-context/
        tracestate (str | Unset):
    """

    traceparent: str | Unset = UNSET
    tracestate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        traceparent = self.traceparent

        tracestate = self.tracestate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if traceparent is not UNSET:
            field_dict["traceparent"] = traceparent
        if tracestate is not UNSET:
            field_dict["tracestate"] = tracestate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        traceparent = d.pop("traceparent", UNSET)

        tracestate = d.pop("tracestate", UNSET)

        trace_context = cls(
            traceparent=traceparent,
            tracestate=tracestate,
        )

        trace_context.additional_properties = d
        return trace_context

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
