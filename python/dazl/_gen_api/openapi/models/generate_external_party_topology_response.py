# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="GenerateExternalPartyTopologyResponse")


@_attrs_define
class GenerateExternalPartyTopologyResponse:
    """Response message with topology transactions and the multi-hash to be signed.

    Attributes:
        party_id (str): The generated party id

            Required
        public_key_fingerprint (str): The fingerprint of the supplied public key

            Required
        topology_transactions (list[str]): The serialized topology transactions which need to be signed and submitted as
            part of the allocate party process
            Note that the serialization includes the versioning information. Therefore, the transaction here is serialized
            as an `UntypedVersionedMessage` which in turn contains the serialized `TopologyTransaction` in the version
            supported by the synchronizer.

            Required: must be non-empty
        multi_hash (str): the multi-hash which may be signed instead of each individual transaction

            Required: must be non-empty
    """

    party_id: str
    public_key_fingerprint: str
    topology_transactions: list[str]
    multi_hash: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party_id = self.party_id

        public_key_fingerprint = self.public_key_fingerprint

        topology_transactions = self.topology_transactions

        multi_hash = self.multi_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partyId": party_id,
                "publicKeyFingerprint": public_key_fingerprint,
                "topologyTransactions": topology_transactions,
                "multiHash": multi_hash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        party_id = d.pop("partyId")

        public_key_fingerprint = d.pop("publicKeyFingerprint")

        topology_transactions = cast(list[str], d.pop("topologyTransactions"))

        multi_hash = d.pop("multiHash")

        generate_external_party_topology_response = cls(
            party_id=party_id,
            public_key_fingerprint=public_key_fingerprint,
            topology_transactions=topology_transactions,
            multi_hash=multi_hash,
        )

        generate_external_party_topology_response.additional_properties = d
        return generate_external_party_topology_response

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
