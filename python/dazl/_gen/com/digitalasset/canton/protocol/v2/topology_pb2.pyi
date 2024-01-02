# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from . import domain_params_pb2 as _domain_params_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TopologyChangeOpX(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    Replace: _ClassVar[TopologyChangeOpX]
    Remove: _ClassVar[TopologyChangeOpX]

class TrustLevelX(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingTrustLevel: _ClassVar[TrustLevelX]
    Ordinary: _ClassVar[TrustLevelX]
    Vip: _ClassVar[TrustLevelX]

class ParticipantPermissionX(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingParticipantPermission: _ClassVar[ParticipantPermissionX]
    Submission: _ClassVar[ParticipantPermissionX]
    Confirmation: _ClassVar[ParticipantPermissionX]
    Observation: _ClassVar[ParticipantPermissionX]
Replace: TopologyChangeOpX
Remove: TopologyChangeOpX
MissingTrustLevel: TrustLevelX
Ordinary: TrustLevelX
Vip: TrustLevelX
MissingParticipantPermission: ParticipantPermissionX
Submission: ParticipantPermissionX
Confirmation: ParticipantPermissionX
Observation: ParticipantPermissionX

class NamespaceDelegationX(_message.Message):
    __slots__ = ["namespace", "target_key", "is_root_delegation"]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    target_key: _crypto_pb2.SigningPublicKey
    is_root_delegation: bool
    def __init__(self, namespace: _Optional[str] = ..., target_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ..., is_root_delegation: bool = ...) -> None: ...

class UnionspaceDefinitionX(_message.Message):
    __slots__ = ["unionspace", "threshold", "owners"]
    UNIONSPACE_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    unionspace: str
    threshold: int
    owners: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, unionspace: _Optional[str] = ..., threshold: _Optional[int] = ..., owners: _Optional[_Iterable[str]] = ...) -> None: ...

class IdentifierDelegationX(_message.Message):
    __slots__ = ["unique_identifier", "target_key"]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    unique_identifier: str
    target_key: _crypto_pb2.SigningPublicKey
    def __init__(self, unique_identifier: _Optional[str] = ..., target_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ...) -> None: ...

class OwnerToKeyMappingX(_message.Message):
    __slots__ = ["member", "public_keys", "domain"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    member: str
    public_keys: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.PublicKey]
    domain: str
    def __init__(self, member: _Optional[str] = ..., public_keys: _Optional[_Iterable[_Union[_crypto_pb2.PublicKey, _Mapping]]] = ..., domain: _Optional[str] = ...) -> None: ...

class DomainTrustCertificateX(_message.Message):
    __slots__ = ["participant", "domain", "transfer_only_to_given_target_domains", "target_domains"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_ONLY_TO_GIVEN_TARGET_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    participant: str
    domain: str
    transfer_only_to_given_target_domains: bool
    target_domains: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, participant: _Optional[str] = ..., domain: _Optional[str] = ..., transfer_only_to_given_target_domains: bool = ..., target_domains: _Optional[_Iterable[str]] = ...) -> None: ...

class ParticipantDomainPermissionX(_message.Message):
    __slots__ = ["domain", "participant", "permission", "trust_level", "limits", "login_after"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    TRUST_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_AFTER_FIELD_NUMBER: _ClassVar[int]
    domain: str
    participant: str
    permission: ParticipantPermissionX
    trust_level: TrustLevelX
    limits: _domain_params_pb2.ParticipantDomainLimits
    login_after: _timestamp_pb2.Timestamp
    def __init__(self, domain: _Optional[str] = ..., participant: _Optional[str] = ..., permission: _Optional[_Union[ParticipantPermissionX, str]] = ..., trust_level: _Optional[_Union[TrustLevelX, str]] = ..., limits: _Optional[_Union[_domain_params_pb2.ParticipantDomainLimits, _Mapping]] = ..., login_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PartyHostingLimitsX(_message.Message):
    __slots__ = ["domain", "party", "quota"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    domain: str
    party: str
    quota: int
    def __init__(self, domain: _Optional[str] = ..., party: _Optional[str] = ..., quota: _Optional[int] = ...) -> None: ...

class VettedPackagesX(_message.Message):
    __slots__ = ["participant", "package_ids", "domain"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    participant: str
    package_ids: _containers.RepeatedScalarFieldContainer[str]
    domain: str
    def __init__(self, participant: _Optional[str] = ..., package_ids: _Optional[_Iterable[str]] = ..., domain: _Optional[str] = ...) -> None: ...

class PartyToParticipantX(_message.Message):
    __slots__ = ["party", "threshold", "participants", "group_addressing", "domain"]
    class HostingParticipant(_message.Message):
        __slots__ = ["participant", "permission"]
        PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        participant: str
        permission: ParticipantPermissionX
        def __init__(self, participant: _Optional[str] = ..., permission: _Optional[_Union[ParticipantPermissionX, str]] = ...) -> None: ...
    PARTY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ADDRESSING_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    party: str
    threshold: int
    participants: _containers.RepeatedCompositeFieldContainer[PartyToParticipantX.HostingParticipant]
    group_addressing: bool
    domain: str
    def __init__(self, party: _Optional[str] = ..., threshold: _Optional[int] = ..., participants: _Optional[_Iterable[_Union[PartyToParticipantX.HostingParticipant, _Mapping]]] = ..., group_addressing: bool = ..., domain: _Optional[str] = ...) -> None: ...

class AuthorityOfX(_message.Message):
    __slots__ = ["party", "threshold", "parties", "domain"]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    party: str
    threshold: int
    parties: _containers.RepeatedScalarFieldContainer[str]
    domain: str
    def __init__(self, party: _Optional[str] = ..., threshold: _Optional[int] = ..., parties: _Optional[_Iterable[str]] = ..., domain: _Optional[str] = ...) -> None: ...

class DomainParametersStateX(_message.Message):
    __slots__ = ["domain", "domain_parameters"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    domain_parameters: _domain_params_pb2.DynamicDomainParametersX
    def __init__(self, domain: _Optional[str] = ..., domain_parameters: _Optional[_Union[_domain_params_pb2.DynamicDomainParametersX, _Mapping]] = ...) -> None: ...

class MediatorDomainStateX(_message.Message):
    __slots__ = ["domain", "group", "threshold", "active", "observers"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    group: int
    threshold: int
    active: _containers.RepeatedScalarFieldContainer[str]
    observers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain: _Optional[str] = ..., group: _Optional[int] = ..., threshold: _Optional[int] = ..., active: _Optional[_Iterable[str]] = ..., observers: _Optional[_Iterable[str]] = ...) -> None: ...

class SequencerDomainStateX(_message.Message):
    __slots__ = ["domain", "threshold", "active", "observers"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    threshold: int
    active: _containers.RepeatedScalarFieldContainer[str]
    observers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain: _Optional[str] = ..., threshold: _Optional[int] = ..., active: _Optional[_Iterable[str]] = ..., observers: _Optional[_Iterable[str]] = ...) -> None: ...

class PurgeTopologyTransactionX(_message.Message):
    __slots__ = ["domain", "mappings"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    mappings: _containers.RepeatedCompositeFieldContainer[TopologyMappingX]
    def __init__(self, domain: _Optional[str] = ..., mappings: _Optional[_Iterable[_Union[TopologyMappingX, _Mapping]]] = ...) -> None: ...

class TrafficControlStateX(_message.Message):
    __slots__ = ["domain", "member", "total_extra_traffic_limit"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXTRA_TRAFFIC_LIMIT_FIELD_NUMBER: _ClassVar[int]
    domain: str
    member: str
    total_extra_traffic_limit: int
    def __init__(self, domain: _Optional[str] = ..., member: _Optional[str] = ..., total_extra_traffic_limit: _Optional[int] = ...) -> None: ...

class TopologyMappingX(_message.Message):
    __slots__ = ["namespace_delegation", "identifier_delegation", "unionspace_definition", "owner_to_key_mapping", "domain_trust_certificate", "participant_permission", "party_hosting_limits", "vetted_packages", "party_to_participant", "authority_of", "domain_parameters_state", "mediator_domain_state", "sequencer_domain_state", "purge_topology_txs", "traffic_control_state"]
    NAMESPACE_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    UNIONSPACE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    OWNER_TO_KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_TRUST_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PARTY_HOSTING_LIMITS_FIELD_NUMBER: _ClassVar[int]
    VETTED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    PARTY_TO_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_OF_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PARAMETERS_STATE_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_DOMAIN_STATE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_DOMAIN_STATE_FIELD_NUMBER: _ClassVar[int]
    PURGE_TOPOLOGY_TXS_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_CONTROL_STATE_FIELD_NUMBER: _ClassVar[int]
    namespace_delegation: NamespaceDelegationX
    identifier_delegation: IdentifierDelegationX
    unionspace_definition: UnionspaceDefinitionX
    owner_to_key_mapping: OwnerToKeyMappingX
    domain_trust_certificate: DomainTrustCertificateX
    participant_permission: ParticipantDomainPermissionX
    party_hosting_limits: PartyHostingLimitsX
    vetted_packages: VettedPackagesX
    party_to_participant: PartyToParticipantX
    authority_of: AuthorityOfX
    domain_parameters_state: DomainParametersStateX
    mediator_domain_state: MediatorDomainStateX
    sequencer_domain_state: SequencerDomainStateX
    purge_topology_txs: PurgeTopologyTransactionX
    traffic_control_state: TrafficControlStateX
    def __init__(self, namespace_delegation: _Optional[_Union[NamespaceDelegationX, _Mapping]] = ..., identifier_delegation: _Optional[_Union[IdentifierDelegationX, _Mapping]] = ..., unionspace_definition: _Optional[_Union[UnionspaceDefinitionX, _Mapping]] = ..., owner_to_key_mapping: _Optional[_Union[OwnerToKeyMappingX, _Mapping]] = ..., domain_trust_certificate: _Optional[_Union[DomainTrustCertificateX, _Mapping]] = ..., participant_permission: _Optional[_Union[ParticipantDomainPermissionX, _Mapping]] = ..., party_hosting_limits: _Optional[_Union[PartyHostingLimitsX, _Mapping]] = ..., vetted_packages: _Optional[_Union[VettedPackagesX, _Mapping]] = ..., party_to_participant: _Optional[_Union[PartyToParticipantX, _Mapping]] = ..., authority_of: _Optional[_Union[AuthorityOfX, _Mapping]] = ..., domain_parameters_state: _Optional[_Union[DomainParametersStateX, _Mapping]] = ..., mediator_domain_state: _Optional[_Union[MediatorDomainStateX, _Mapping]] = ..., sequencer_domain_state: _Optional[_Union[SequencerDomainStateX, _Mapping]] = ..., purge_topology_txs: _Optional[_Union[PurgeTopologyTransactionX, _Mapping]] = ..., traffic_control_state: _Optional[_Union[TrafficControlStateX, _Mapping]] = ...) -> None: ...

class TopologyTransactionX(_message.Message):
    __slots__ = ["operation", "serial", "mapping"]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    operation: TopologyChangeOpX
    serial: int
    mapping: TopologyMappingX
    def __init__(self, operation: _Optional[_Union[TopologyChangeOpX, str]] = ..., serial: _Optional[int] = ..., mapping: _Optional[_Union[TopologyMappingX, _Mapping]] = ...) -> None: ...

class SignedTopologyTransactionX(_message.Message):
    __slots__ = ["transaction", "signatures", "proposal"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    transaction: bytes
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    proposal: bool
    def __init__(self, transaction: _Optional[bytes] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., proposal: bool = ...) -> None: ...

class AcceptedTopologyTransactionsX(_message.Message):
    __slots__ = ["domain", "accepted"]
    class AcceptedRequest(_message.Message):
        __slots__ = ["request_id", "transactions"]
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
        request_id: str
        transactions: _containers.RepeatedCompositeFieldContainer[SignedTopologyTransactionX]
        def __init__(self, request_id: _Optional[str] = ..., transactions: _Optional[_Iterable[_Union[SignedTopologyTransactionX, _Mapping]]] = ...) -> None: ...
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    domain: str
    accepted: _containers.RepeatedCompositeFieldContainer[AcceptedTopologyTransactionsX.AcceptedRequest]
    def __init__(self, domain: _Optional[str] = ..., accepted: _Optional[_Iterable[_Union[AcceptedTopologyTransactionsX.AcceptedRequest, _Mapping]]] = ...) -> None: ...

class RegisterTopologyTransactionRequestX(_message.Message):
    __slots__ = ["requested_by", "requested_for", "request_id", "transactions", "domain"]
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    requested_by: str
    requested_for: str
    request_id: str
    transactions: _containers.RepeatedCompositeFieldContainer[SignedTopologyTransactionX]
    domain: str
    def __init__(self, requested_by: _Optional[str] = ..., requested_for: _Optional[str] = ..., request_id: _Optional[str] = ..., transactions: _Optional[_Iterable[_Union[SignedTopologyTransactionX, _Mapping]]] = ..., domain: _Optional[str] = ...) -> None: ...

class RegisterTopologyTransactionResponseX(_message.Message):
    __slots__ = ["requested_by", "requested_for", "request_id", "results", "domain"]
    class Result(_message.Message):
        __slots__ = ["state"]
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []  # type: ignore
            MISSING_STATE: _ClassVar[RegisterTopologyTransactionResponseX.Result.State]
            FAILED: _ClassVar[RegisterTopologyTransactionResponseX.Result.State]
            REJECTED: _ClassVar[RegisterTopologyTransactionResponseX.Result.State]
            ACCEPTED: _ClassVar[RegisterTopologyTransactionResponseX.Result.State]
            DUPLICATE: _ClassVar[RegisterTopologyTransactionResponseX.Result.State]
            OBSOLETE: _ClassVar[RegisterTopologyTransactionResponseX.Result.State]
        MISSING_STATE: RegisterTopologyTransactionResponseX.Result.State
        FAILED: RegisterTopologyTransactionResponseX.Result.State
        REJECTED: RegisterTopologyTransactionResponseX.Result.State
        ACCEPTED: RegisterTopologyTransactionResponseX.Result.State
        DUPLICATE: RegisterTopologyTransactionResponseX.Result.State
        OBSOLETE: RegisterTopologyTransactionResponseX.Result.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: RegisterTopologyTransactionResponseX.Result.State
        def __init__(self, state: _Optional[_Union[RegisterTopologyTransactionResponseX.Result.State, str]] = ...) -> None: ...
    REQUESTED_BY_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    requested_by: str
    requested_for: str
    request_id: str
    results: _containers.RepeatedCompositeFieldContainer[RegisterTopologyTransactionResponseX.Result]
    domain: str
    def __init__(self, requested_by: _Optional[str] = ..., requested_for: _Optional[str] = ..., request_id: _Optional[str] = ..., results: _Optional[_Iterable[_Union[RegisterTopologyTransactionResponseX.Result, _Mapping]]] = ..., domain: _Optional[str] = ...) -> None: ...
