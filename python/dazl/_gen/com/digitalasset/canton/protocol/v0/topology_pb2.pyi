# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from . import sequencing_pb2 as _sequencing_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TopologyChangeOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    Add: _ClassVar[TopologyChangeOp]
    Remove: _ClassVar[TopologyChangeOp]
    Replace: _ClassVar[TopologyChangeOp]

class TrustLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingTrustLevel: _ClassVar[TrustLevel]
    Ordinary: _ClassVar[TrustLevel]
    Vip: _ClassVar[TrustLevel]

class ParticipantPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingParticipantPermission: _ClassVar[ParticipantPermission]
    Submission: _ClassVar[ParticipantPermission]
    Confirmation: _ClassVar[ParticipantPermission]
    Observation: _ClassVar[ParticipantPermission]
    Disabled: _ClassVar[ParticipantPermission]

class RequestSide(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingRequestSide: _ClassVar[RequestSide]
    Both: _ClassVar[RequestSide]
    From: _ClassVar[RequestSide]
    To: _ClassVar[RequestSide]
Add: TopologyChangeOp
Remove: TopologyChangeOp
Replace: TopologyChangeOp
MissingTrustLevel: TrustLevel
Ordinary: TrustLevel
Vip: TrustLevel
MissingParticipantPermission: ParticipantPermission
Submission: ParticipantPermission
Confirmation: ParticipantPermission
Observation: ParticipantPermission
Disabled: ParticipantPermission
MissingRequestSide: RequestSide
Both: RequestSide
From: RequestSide
To: RequestSide

class ParticipantState(_message.Message):
    __slots__ = ["side", "domain", "participant", "permission", "trust_level"]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    TRUST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    side: RequestSide
    domain: str
    participant: str
    permission: ParticipantPermission
    trust_level: TrustLevel
    def __init__(self, side: _Optional[_Union[RequestSide, str]] = ..., domain: _Optional[str] = ..., participant: _Optional[str] = ..., permission: _Optional[_Union[ParticipantPermission, str]] = ..., trust_level: _Optional[_Union[TrustLevel, str]] = ...) -> None: ...

class PartyToParticipant(_message.Message):
    __slots__ = ["side", "party", "participant", "permission"]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    side: RequestSide
    party: str
    participant: str
    permission: ParticipantPermission
    def __init__(self, side: _Optional[_Union[RequestSide, str]] = ..., party: _Optional[str] = ..., participant: _Optional[str] = ..., permission: _Optional[_Union[ParticipantPermission, str]] = ...) -> None: ...

class MediatorDomainState(_message.Message):
    __slots__ = ["side", "domain", "mediator"]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    side: RequestSide
    domain: str
    mediator: str
    def __init__(self, side: _Optional[_Union[RequestSide, str]] = ..., domain: _Optional[str] = ..., mediator: _Optional[str] = ...) -> None: ...

class NamespaceDelegation(_message.Message):
    __slots__ = ["namespace", "target_key", "is_root_delegation"]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    target_key: _crypto_pb2.SigningPublicKey
    is_root_delegation: bool
    def __init__(self, namespace: _Optional[str] = ..., target_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ..., is_root_delegation: bool = ...) -> None: ...

class IdentifierDelegation(_message.Message):
    __slots__ = ["unique_identifier", "target_key"]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    unique_identifier: str
    target_key: _crypto_pb2.SigningPublicKey
    def __init__(self, unique_identifier: _Optional[str] = ..., target_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ...) -> None: ...

class OwnerToKeyMapping(_message.Message):
    __slots__ = ["key_owner", "public_key"]
    KEY_OWNER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    key_owner: str
    public_key: _crypto_pb2.PublicKey
    def __init__(self, key_owner: _Optional[str] = ..., public_key: _Optional[_Union[_crypto_pb2.PublicKey, _Mapping]] = ...) -> None: ...

class SignedLegalIdentityClaim(_message.Message):
    __slots__ = ["claim", "signature"]
    CLAIM_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    claim: bytes
    signature: _crypto_pb2.Signature
    def __init__(self, claim: _Optional[bytes] = ..., signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class LegalIdentityClaim(_message.Message):
    __slots__ = ["unique_identifier", "x509_cert"]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    X509_CERT_FIELD_NUMBER: _ClassVar[int]
    unique_identifier: str
    x509_cert: bytes
    def __init__(self, unique_identifier: _Optional[str] = ..., x509_cert: _Optional[bytes] = ...) -> None: ...

class VettedPackages(_message.Message):
    __slots__ = ["participant", "package_ids"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    participant: str
    package_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, participant: _Optional[str] = ..., package_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class TopologyStateUpdate(_message.Message):
    __slots__ = ["operation", "id", "namespace_delegation", "identifier_delegation", "owner_to_key_mapping", "party_to_participant", "signed_legal_identity_claim", "participant_state", "vetted_packages", "mediator_domain_state"]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_TO_KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    PARTY_TO_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    SIGNED_LEGAL_IDENTITY_CLAIM_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_STATE_FIELD_NUMBER: _ClassVar[int]
    VETTED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_DOMAIN_STATE_FIELD_NUMBER: _ClassVar[int]
    operation: TopologyChangeOp
    id: str
    namespace_delegation: NamespaceDelegation
    identifier_delegation: IdentifierDelegation
    owner_to_key_mapping: OwnerToKeyMapping
    party_to_participant: PartyToParticipant
    signed_legal_identity_claim: SignedLegalIdentityClaim
    participant_state: ParticipantState
    vetted_packages: VettedPackages
    mediator_domain_state: MediatorDomainState
    def __init__(self, operation: _Optional[_Union[TopologyChangeOp, str]] = ..., id: _Optional[str] = ..., namespace_delegation: _Optional[_Union[NamespaceDelegation, _Mapping]] = ..., identifier_delegation: _Optional[_Union[IdentifierDelegation, _Mapping]] = ..., owner_to_key_mapping: _Optional[_Union[OwnerToKeyMapping, _Mapping]] = ..., party_to_participant: _Optional[_Union[PartyToParticipant, _Mapping]] = ..., signed_legal_identity_claim: _Optional[_Union[SignedLegalIdentityClaim, _Mapping]] = ..., participant_state: _Optional[_Union[ParticipantState, _Mapping]] = ..., vetted_packages: _Optional[_Union[VettedPackages, _Mapping]] = ..., mediator_domain_state: _Optional[_Union[MediatorDomainState, _Mapping]] = ...) -> None: ...

class DomainParametersChange(_message.Message):
    __slots__ = ["domain", "domain_parameters"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    domain_parameters: _sequencing_pb2.DynamicDomainParameters
    def __init__(self, domain: _Optional[str] = ..., domain_parameters: _Optional[_Union[_sequencing_pb2.DynamicDomainParameters, _Mapping]] = ...) -> None: ...

class DomainGovernanceTransaction(_message.Message):
    __slots__ = ["domain_parameters_change"]
    DOMAIN_PARAMETERS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    domain_parameters_change: DomainParametersChange
    def __init__(self, domain_parameters_change: _Optional[_Union[DomainParametersChange, _Mapping]] = ...) -> None: ...

class TopologyTransaction(_message.Message):
    __slots__ = ["state_update", "domain_governance"]
    STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_GOVERNANCE_FIELD_NUMBER: _ClassVar[int]
    state_update: TopologyStateUpdate
    domain_governance: DomainGovernanceTransaction
    def __init__(self, state_update: _Optional[_Union[TopologyStateUpdate, _Mapping]] = ..., domain_governance: _Optional[_Union[DomainGovernanceTransaction, _Mapping]] = ...) -> None: ...

class SignedTopologyTransaction(_message.Message):
    __slots__ = ["transaction", "key", "signature"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    transaction: bytes
    key: _crypto_pb2.SigningPublicKey
    signature: _crypto_pb2.Signature
    def __init__(self, transaction: _Optional[bytes] = ..., key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ..., signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class DomainTopologyTransactionMessage(_message.Message):
    __slots__ = ["signature", "domain_id", "transactions"]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    signature: _crypto_pb2.Signature
    domain_id: str
    transactions: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., domain_id: _Optional[str] = ..., transactions: _Optional[_Iterable[bytes]] = ...) -> None: ...

class RegisterTopologyTransactionRequest(_message.Message):
    __slots__ = ["requested_by", "participant", "request_id", "signed_topology_transactions", "domain_id"]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNED_TOPOLOGY_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    requested_by: str
    participant: str
    request_id: str
    signed_topology_transactions: _containers.RepeatedScalarFieldContainer[bytes]
    domain_id: str
    def __init__(self, requested_by: _Optional[str] = ..., participant: _Optional[str] = ..., request_id: _Optional[str] = ..., signed_topology_transactions: _Optional[_Iterable[bytes]] = ..., domain_id: _Optional[str] = ...) -> None: ...

class RegisterTopologyTransactionResponse(_message.Message):
    __slots__ = ["requested_by", "participant", "request_id", "results", "domain_id"]
    class Result(_message.Message):
        __slots__ = ["unique_path", "state", "error_message"]
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []  # type: ignore
            MISSING_STATE: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            REQUESTED: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            FAILED: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            REJECTED: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            ACCEPTED: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            DUPLICATE: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            OBSOLETE: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
        MISSING_STATE: RegisterTopologyTransactionResponse.Result.State
        REQUESTED: RegisterTopologyTransactionResponse.Result.State
        FAILED: RegisterTopologyTransactionResponse.Result.State
        REJECTED: RegisterTopologyTransactionResponse.Result.State
        ACCEPTED: RegisterTopologyTransactionResponse.Result.State
        DUPLICATE: RegisterTopologyTransactionResponse.Result.State
        OBSOLETE: RegisterTopologyTransactionResponse.Result.State
        UNIQUE_PATH_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        unique_path: str
        state: RegisterTopologyTransactionResponse.Result.State
        error_message: str
        def __init__(self, unique_path: _Optional[str] = ..., state: _Optional[_Union[RegisterTopologyTransactionResponse.Result.State, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    requested_by: str
    participant: str
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[RegisterTopologyTransactionResponse.Result]
    domain_id: str
    def __init__(self, requested_by: _Optional[str] = ..., participant: _Optional[str] = ..., request_id: _Optional[str] = ..., results: _Optional[_Iterable[_Union[RegisterTopologyTransactionResponse.Result, _Mapping]]] = ..., domain_id: _Optional[str] = ...) -> None: ...
