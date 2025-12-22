# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import object_meta_pb2 as _object_meta_pb2
from .. import crypto_pb2 as _crypto_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetParticipantIdRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetParticipantIdResponse(_message.Message):
    __slots__ = ("participant_id",)
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    participant_id: str
    def __init__(self, participant_id: _Optional[str] = ...) -> None: ...

class GetPartiesRequest(_message.Message):
    __slots__ = ("parties", "identity_provider_id")
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    identity_provider_id: str
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class GetPartiesResponse(_message.Message):
    __slots__ = ("party_details",)
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    party_details: _containers.RepeatedCompositeFieldContainer[PartyDetails]
    def __init__(self, party_details: _Optional[_Iterable[_Union[PartyDetails, _Mapping]]] = ...) -> None: ...

class ListKnownPartiesRequest(_message.Message):
    __slots__ = ("page_token", "page_size", "identity_provider_id")
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    page_token: str
    page_size: int
    identity_provider_id: str
    def __init__(self, page_token: _Optional[str] = ..., page_size: _Optional[int] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class ListKnownPartiesResponse(_message.Message):
    __slots__ = ("party_details", "next_page_token")
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    party_details: _containers.RepeatedCompositeFieldContainer[PartyDetails]
    next_page_token: str
    def __init__(self, party_details: _Optional[_Iterable[_Union[PartyDetails, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AllocatePartyRequest(_message.Message):
    __slots__ = ("party_id_hint", "local_metadata", "identity_provider_id", "synchronizer_id", "user_id")
    PARTY_ID_HINT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    party_id_hint: str
    local_metadata: _object_meta_pb2.ObjectMeta
    identity_provider_id: str
    synchronizer_id: str
    user_id: str
    def __init__(self, party_id_hint: _Optional[str] = ..., local_metadata: _Optional[_Union[_object_meta_pb2.ObjectMeta, _Mapping]] = ..., identity_provider_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class AllocatePartyResponse(_message.Message):
    __slots__ = ("party_details",)
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    party_details: PartyDetails
    def __init__(self, party_details: _Optional[_Union[PartyDetails, _Mapping]] = ...) -> None: ...

class AllocateExternalPartyRequest(_message.Message):
    __slots__ = ("synchronizer", "onboarding_transactions", "multi_hash_signatures", "identity_provider_id")
    class SignedTransaction(_message.Message):
        __slots__ = ("transaction", "signatures")
        TRANSACTION_FIELD_NUMBER: _ClassVar[int]
        SIGNATURES_FIELD_NUMBER: _ClassVar[int]
        transaction: bytes
        signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
        def __init__(self, transaction: _Optional[bytes] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...
    SYNCHRONIZER_FIELD_NUMBER: _ClassVar[int]
    ONBOARDING_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    MULTI_HASH_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    synchronizer: str
    onboarding_transactions: _containers.RepeatedCompositeFieldContainer[AllocateExternalPartyRequest.SignedTransaction]
    multi_hash_signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    identity_provider_id: str
    def __init__(self, synchronizer: _Optional[str] = ..., onboarding_transactions: _Optional[_Iterable[_Union[AllocateExternalPartyRequest.SignedTransaction, _Mapping]]] = ..., multi_hash_signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class AllocateExternalPartyResponse(_message.Message):
    __slots__ = ("party_id",)
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    def __init__(self, party_id: _Optional[str] = ...) -> None: ...

class UpdatePartyDetailsRequest(_message.Message):
    __slots__ = ("party_details", "update_mask")
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    party_details: PartyDetails
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, party_details: _Optional[_Union[PartyDetails, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdatePartyDetailsResponse(_message.Message):
    __slots__ = ("party_details",)
    PARTY_DETAILS_FIELD_NUMBER: _ClassVar[int]
    party_details: PartyDetails
    def __init__(self, party_details: _Optional[_Union[PartyDetails, _Mapping]] = ...) -> None: ...

class PartyDetails(_message.Message):
    __slots__ = ("party", "is_local", "local_metadata", "identity_provider_id")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    party: str
    is_local: bool
    local_metadata: _object_meta_pb2.ObjectMeta
    identity_provider_id: str
    def __init__(self, party: _Optional[str] = ..., is_local: bool = ..., local_metadata: _Optional[_Union[_object_meta_pb2.ObjectMeta, _Mapping]] = ..., identity_provider_id: _Optional[str] = ...) -> None: ...

class UpdatePartyIdentityProviderIdRequest(_message.Message):
    __slots__ = ("party", "source_identity_provider_id", "target_identity_provider_id")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_IDENTITY_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    party: str
    source_identity_provider_id: str
    target_identity_provider_id: str
    def __init__(self, party: _Optional[str] = ..., source_identity_provider_id: _Optional[str] = ..., target_identity_provider_id: _Optional[str] = ...) -> None: ...

class UpdatePartyIdentityProviderIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GenerateExternalPartyTopologyRequest(_message.Message):
    __slots__ = ("synchronizer", "party_hint", "public_key", "local_participant_observation_only", "other_confirming_participant_uids", "confirmation_threshold", "observing_participant_uids")
    SYNCHRONIZER_FIELD_NUMBER: _ClassVar[int]
    PARTY_HINT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PARTICIPANT_OBSERVATION_ONLY_FIELD_NUMBER: _ClassVar[int]
    OTHER_CONFIRMING_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    OBSERVING_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    synchronizer: str
    party_hint: str
    public_key: _crypto_pb2.SigningPublicKey
    local_participant_observation_only: bool
    other_confirming_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    confirmation_threshold: int
    observing_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, synchronizer: _Optional[str] = ..., party_hint: _Optional[str] = ..., public_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ..., local_participant_observation_only: bool = ..., other_confirming_participant_uids: _Optional[_Iterable[str]] = ..., confirmation_threshold: _Optional[int] = ..., observing_participant_uids: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateExternalPartyTopologyResponse(_message.Message):
    __slots__ = ("party_id", "public_key_fingerprint", "topology_transactions", "multi_hash")
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    MULTI_HASH_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    public_key_fingerprint: str
    topology_transactions: _containers.RepeatedScalarFieldContainer[bytes]
    multi_hash: bytes
    def __init__(self, party_id: _Optional[str] = ..., public_key_fingerprint: _Optional[str] = ..., topology_transactions: _Optional[_Iterable[bytes]] = ..., multi_hash: _Optional[bytes] = ...) -> None: ...
