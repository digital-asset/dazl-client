# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signature import Signature
    from ..models.signed_transaction import SignedTransaction


T = TypeVar("T", bound="AllocateExternalPartyRequest")


@_attrs_define
class AllocateExternalPartyRequest:
    """Required authorization:
      ``HasRight(ParticipantAdmin) OR IsAuthenticatedIdentityProviderAdmin(identity_provider_id) OR
    IsAuthenticatedUser(user_id)``

        Attributes:
            synchronizer (str): TODO(#27670) support synchronizer aliases
                Synchronizer ID on which to onboard the party

                Required
            onboarding_transactions (list[SignedTransaction]): TopologyTransactions to onboard the external party
                Can contain:
                - A namespace for the party.
                This can be either a single NamespaceDelegation,
                or DecentralizedNamespaceDefinition along with its authorized namespace owners in the form of
                NamespaceDelegations.
                May be provided, if so it must be fully authorized by the signatures in this request combined with the existing
                topology state.
                - A PartyToParticipant to register the hosting relationship of the party, and the party's signing keys and
                threshold.
                Must be provided.

                Required: must be non-empty
            multi_hash_signatures (list[Signature] | Unset): Optional signatures of the combined hash of all
                onboarding_transactions
                This may be used instead of providing signatures on each individual transaction

                Optional: can be empty
            identity_provider_id (str | Unset): The id of the ``Identity Provider``
                If not set, assume the party is managed by the default identity provider.

                Optional
            wait_for_allocation (bool | Unset): When true, this RPC will attempt to wait for the party to be allocated on
                the synchronizer before returning.
                When false, the allocation will happen asynchronously.
                This is a best effort only as this synchronization is only possible for non decentralized parties (single
                hosting node).
                For decentralized parties, this flag is ignored.
                Defaults to true.

                Optional
            user_id (str | Unset): The user who will get the act_as rights to the newly allocated party.
                If set to an empty string (the default), no user will get rights to the party.

                Optional
    """

    synchronizer: str
    onboarding_transactions: list[SignedTransaction]
    multi_hash_signatures: list[Signature] | Unset = UNSET
    identity_provider_id: str | Unset = UNSET
    wait_for_allocation: bool | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synchronizer = self.synchronizer

        onboarding_transactions = []
        for onboarding_transactions_item_data in self.onboarding_transactions:
            onboarding_transactions_item = onboarding_transactions_item_data.to_dict()
            onboarding_transactions.append(onboarding_transactions_item)

        multi_hash_signatures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_hash_signatures, Unset):
            multi_hash_signatures = []
            for multi_hash_signatures_item_data in self.multi_hash_signatures:
                multi_hash_signatures_item = multi_hash_signatures_item_data.to_dict()
                multi_hash_signatures.append(multi_hash_signatures_item)

        identity_provider_id = self.identity_provider_id

        wait_for_allocation = self.wait_for_allocation

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "synchronizer": synchronizer,
                "onboardingTransactions": onboarding_transactions,
            }
        )
        if multi_hash_signatures is not UNSET:
            field_dict["multiHashSignatures"] = multi_hash_signatures
        if identity_provider_id is not UNSET:
            field_dict["identityProviderId"] = identity_provider_id
        if wait_for_allocation is not UNSET:
            field_dict["waitForAllocation"] = wait_for_allocation
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signature import Signature
        from ..models.signed_transaction import SignedTransaction

        d = dict(src_dict)
        synchronizer = d.pop("synchronizer")

        onboarding_transactions = []
        _onboarding_transactions = d.pop("onboardingTransactions")
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
                multi_hash_signatures_item = Signature.from_dict(multi_hash_signatures_item_data)

                multi_hash_signatures.append(multi_hash_signatures_item)

        identity_provider_id = d.pop("identityProviderId", UNSET)

        wait_for_allocation = d.pop("waitForAllocation", UNSET)

        user_id = d.pop("userId", UNSET)

        allocate_external_party_request = cls(
            synchronizer=synchronizer,
            onboarding_transactions=onboarding_transactions,
            multi_hash_signatures=multi_hash_signatures,
            identity_provider_id=identity_provider_id,
            wait_for_allocation=wait_for_allocation,
            user_id=user_id,
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
