from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateExternalPartyTopologyResponse")


@_attrs_define
class GenerateExternalPartyTopologyResponse:
    """Response message with topology transactions and the multi-hash to be signed.

    Attributes:
        party_id (str): the generated party id
        public_key_fingerprint (str): the fingerprint of the supplied public key
        multi_hash (str): the multi-hash which may be signed instead of each individual transaction
        topology_transactions (list[str] | Unset): The serialized topology transactions which need to be signed and
            submitted as part of the allocate party process
            Note that the serialization includes the versioning information. Therefore, the transaction here is serialized
            as an `UntypedVersionedMessage` which in turn contains the serialized `TopologyTransaction` in the version
            supported by the synchronizer.
    """

    party_id: str
    public_key_fingerprint: str
    multi_hash: str
    topology_transactions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party_id = self.party_id

        public_key_fingerprint = self.public_key_fingerprint

        multi_hash = self.multi_hash

        topology_transactions: list[str] | Unset = UNSET
        if not isinstance(self.topology_transactions, Unset):
            topology_transactions = self.topology_transactions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partyId": party_id,
                "publicKeyFingerprint": public_key_fingerprint,
                "multiHash": multi_hash,
            }
        )
        if topology_transactions is not UNSET:
            field_dict["topologyTransactions"] = topology_transactions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        party_id = d.pop("partyId")

        public_key_fingerprint = d.pop("publicKeyFingerprint")

        multi_hash = d.pop("multiHash")

        topology_transactions = cast(list[str], d.pop("topologyTransactions", UNSET))

        generate_external_party_topology_response = cls(
            party_id=party_id,
            public_key_fingerprint=public_key_fingerprint,
            multi_hash=multi_hash,
            topology_transactions=topology_transactions,
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
