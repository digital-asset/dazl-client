# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signature import Signature
    from ..models.signed_transaction import SignedTransaction


T = TypeVar("T", bound="AllocateExternalPartyRequest")


@_attrs_define
class AllocateExternalPartyRequest:
    """Required authorization: ``HasRight(ParticipantAdmin) OR IsAuthenticatedIdentityProviderAdmin(identity_provider_id)``

    Attributes:
        synchronizer (str): TODO(#27670) support synchronizer aliases
            Synchronizer ID on which to onboard the party
            Required
        identity_provider_id (str): The id of the ``Identity Provider``
            If not set, assume the party is managed by the default identity provider.
            Optional
        onboarding_transactions (list[SignedTransaction] | Unset): TopologyTransactions to onboard the external party
            Can contain:
            - A namespace for the party.
            This can be either a single NamespaceDelegation,
            or DecentralizedNamespaceDefinition along with its authorized namespace owners in the form of
            NamespaceDelegations.
            May be provided, if so it must be fully authorized by the signatures in this request combined with the existing
            topology state.
            - A PartyToKeyMapping to register the party's signing keys.
            May be provided, if so it must be fully authorized by the signatures in this request combined with the existing
            topology state.
            - A PartyToParticipant to register the hosting relationship of the party.
            Must be provided.
            Required
        multi_hash_signatures (list[Signature] | Unset): Optional signatures of the combined hash of all
            onboarding_transactions
            This may be used instead of providing signatures on each individual transaction
    """

    synchronizer: str
    identity_provider_id: str
    onboarding_transactions: list[SignedTransaction] | Unset = UNSET
    multi_hash_signatures: list[Signature] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synchronizer = self.synchronizer

        identity_provider_id = self.identity_provider_id

        onboarding_transactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.onboarding_transactions, Unset):
            onboarding_transactions = []
            for onboarding_transactions_item_data in self.onboarding_transactions:
                onboarding_transactions_item = (
                    onboarding_transactions_item_data.to_dict()
                )
                onboarding_transactions.append(onboarding_transactions_item)

        multi_hash_signatures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_hash_signatures, Unset):
            multi_hash_signatures = []
            for multi_hash_signatures_item_data in self.multi_hash_signatures:
                multi_hash_signatures_item = multi_hash_signatures_item_data.to_dict()
                multi_hash_signatures.append(multi_hash_signatures_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "synchronizer": synchronizer,
                "identityProviderId": identity_provider_id,
            }
        )
        if onboarding_transactions is not UNSET:
            field_dict["onboardingTransactions"] = onboarding_transactions
        if multi_hash_signatures is not UNSET:
            field_dict["multiHashSignatures"] = multi_hash_signatures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signature import Signature
        from ..models.signed_transaction import SignedTransaction

        d = dict(src_dict)
        synchronizer = d.pop("synchronizer")

        identity_provider_id = d.pop("identityProviderId")

        _onboarding_transactions = d.pop("onboardingTransactions", UNSET)
        onboarding_transactions: list[SignedTransaction] | Unset = UNSET
        if _onboarding_transactions is not UNSET:
            onboarding_transactions = []
            for onboarding_transactions_item_data in _onboarding_transactions:
                onboarding_transactions_item = SignedTransaction.from_dict(
                    onboarding_transactions_item_data
                )

                onboarding_transactions.append(onboarding_transactions_item)

        _multi_hash_signatures = d.pop("multiHashSignatures", UNSET)
        multi_hash_signatures: list[Signature] | Unset = UNSET
        if _multi_hash_signatures is not UNSET:
            multi_hash_signatures = []
            for multi_hash_signatures_item_data in _multi_hash_signatures:
                multi_hash_signatures_item = Signature.from_dict(
                    multi_hash_signatures_item_data
                )

                multi_hash_signatures.append(multi_hash_signatures_item)

        allocate_external_party_request = cls(
            synchronizer=synchronizer,
            identity_provider_id=identity_provider_id,
            onboarding_transactions=onboarding_transactions,
            multi_hash_signatures=multi_hash_signatures,
        )

        allocate_external_party_request.additional_properties = d
        return allocate_external_party_request

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
