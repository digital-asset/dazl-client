# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompletionStreamRequest")


@_attrs_define
class CompletionStreamRequest:
    """
    Attributes:
        parties (list[str]): Non-empty list of parties whose data should be included.
            The stream shows only completions of commands for which at least one of the ``act_as`` parties is in the given
            set of parties.
            Must be a valid PartyIdString (as described in ``value.proto``).

            Required: must be non-empty
        user_id (str | Unset): Only completions of commands submitted with the same user_id will be visible in the
            stream.
            Must be a valid UserIdString (as described in ``value.proto``).

            Required unless authentication is used with a user token.
            In that case, the token's user-id will be used for the request's user_id.

            Optional
        begin_exclusive (int | Unset): This optional field indicates the minimum offset for completions. This can be
            used to resume an earlier completion stream.
            If not set the ledger uses the ledger begin offset instead.
            If specified, it must be a valid absolute offset (positive integer) or zero (ledger begin offset).
            If the ledger has been pruned, this parameter must be specified and greater than the pruning offset.

            Optional
    """

    parties: list[str]
    user_id: str | Unset = UNSET
    begin_exclusive: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parties = self.parties

        user_id = self.user_id

        begin_exclusive = self.begin_exclusive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parties": parties,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if begin_exclusive is not UNSET:
            field_dict["beginExclusive"] = begin_exclusive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parties = cast(list[str], d.pop("parties"))

        user_id = d.pop("userId", UNSET)

        begin_exclusive = d.pop("beginExclusive", UNSET)

        completion_stream_request = cls(
            parties=parties,
            user_id=user_id,
            begin_exclusive=begin_exclusive,
        )

        completion_stream_request.additional_properties = d
        return completion_stream_request

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
