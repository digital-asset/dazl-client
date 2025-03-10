# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from . import domain_parameters_pb2 as _domain_parameters_pb2
from . import sequencing_parameters_pb2 as _sequencing_parameters_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enums(_message.Message):
    __slots__ = ()
    class TopologyChangeOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOPOLOGY_CHANGE_OP_UNSPECIFIED: _ClassVar[Enums.TopologyChangeOp]
        TOPOLOGY_CHANGE_OP_ADD_REPLACE: _ClassVar[Enums.TopologyChangeOp]
        TOPOLOGY_CHANGE_OP_REMOVE: _ClassVar[Enums.TopologyChangeOp]
    TOPOLOGY_CHANGE_OP_UNSPECIFIED: Enums.TopologyChangeOp
    TOPOLOGY_CHANGE_OP_ADD_REPLACE: Enums.TopologyChangeOp
    TOPOLOGY_CHANGE_OP_REMOVE: Enums.TopologyChangeOp
    class ParticipantPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTICIPANT_PERMISSION_UNSPECIFIED: _ClassVar[Enums.ParticipantPermission]
        PARTICIPANT_PERMISSION_SUBMISSION: _ClassVar[Enums.ParticipantPermission]
        PARTICIPANT_PERMISSION_CONFIRMATION: _ClassVar[Enums.ParticipantPermission]
        PARTICIPANT_PERMISSION_OBSERVATION: _ClassVar[Enums.ParticipantPermission]
    PARTICIPANT_PERMISSION_UNSPECIFIED: Enums.ParticipantPermission
    PARTICIPANT_PERMISSION_SUBMISSION: Enums.ParticipantPermission
    PARTICIPANT_PERMISSION_CONFIRMATION: Enums.ParticipantPermission
    PARTICIPANT_PERMISSION_OBSERVATION: Enums.ParticipantPermission
    def __init__(self) -> None: ...

class NamespaceDelegation(_message.Message):
    __slots__ = ("namespace", "target_key", "is_root_delegation")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    target_key: _crypto_pb2.SigningPublicKey
    is_root_delegation: bool
    def __init__(self, namespace: _Optional[str] = ..., target_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ..., is_root_delegation: bool = ...) -> None: ...

class DecentralizedNamespaceDefinition(_message.Message):
    __slots__ = ("decentralized_namespace", "threshold", "owners")
    DECENTRALIZED_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    decentralized_namespace: str
    threshold: int
    owners: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, decentralized_namespace: _Optional[str] = ..., threshold: _Optional[int] = ..., owners: _Optional[_Iterable[str]] = ...) -> None: ...

class IdentifierDelegation(_message.Message):
    __slots__ = ("unique_identifier", "target_key")
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    unique_identifier: str
    target_key: _crypto_pb2.SigningPublicKey
    def __init__(self, unique_identifier: _Optional[str] = ..., target_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ...) -> None: ...

class OwnerToKeyMapping(_message.Message):
    __slots__ = ("member", "public_keys", "domain")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    member: str
    public_keys: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.PublicKey]
    domain: str
    def __init__(self, member: _Optional[str] = ..., public_keys: _Optional[_Iterable[_Union[_crypto_pb2.PublicKey, _Mapping]]] = ..., domain: _Optional[str] = ...) -> None: ...

class PartyToKeyMapping(_message.Message):
    __slots__ = ("party", "domain", "threshold", "signing_keys")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEYS_FIELD_NUMBER: _ClassVar[int]
    party: str
    domain: str
    threshold: int
    signing_keys: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.SigningPublicKey]
    def __init__(self, party: _Optional[str] = ..., domain: _Optional[str] = ..., threshold: _Optional[int] = ..., signing_keys: _Optional[_Iterable[_Union[_crypto_pb2.SigningPublicKey, _Mapping]]] = ...) -> None: ...

class DomainTrustCertificate(_message.Message):
    __slots__ = ("participant_uid", "domain", "transfer_only_to_given_target_domains", "target_domains")
    PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_ONLY_TO_GIVEN_TARGET_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    participant_uid: str
    domain: str
    transfer_only_to_given_target_domains: bool
    target_domains: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, participant_uid: _Optional[str] = ..., domain: _Optional[str] = ..., transfer_only_to_given_target_domains: bool = ..., target_domains: _Optional[_Iterable[str]] = ...) -> None: ...

class ParticipantDomainPermission(_message.Message):
    __slots__ = ("domain", "participant_uid", "permission", "limits", "login_after")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_AFTER_FIELD_NUMBER: _ClassVar[int]
    domain: str
    participant_uid: str
    permission: Enums.ParticipantPermission
    limits: _domain_parameters_pb2.ParticipantDomainLimits
    login_after: _wrappers_pb2.Int64Value
    def __init__(self, domain: _Optional[str] = ..., participant_uid: _Optional[str] = ..., permission: _Optional[_Union[Enums.ParticipantPermission, str]] = ..., limits: _Optional[_Union[_domain_parameters_pb2.ParticipantDomainLimits, _Mapping]] = ..., login_after: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class PartyHostingLimits(_message.Message):
    __slots__ = ("domain", "party", "quota")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    domain: str
    party: str
    quota: int
    def __init__(self, domain: _Optional[str] = ..., party: _Optional[str] = ..., quota: _Optional[int] = ...) -> None: ...

class VettedPackages(_message.Message):
    __slots__ = ("participant_uid", "package_ids", "domain")
    PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    participant_uid: str
    package_ids: _containers.RepeatedScalarFieldContainer[str]
    domain: str
    def __init__(self, participant_uid: _Optional[str] = ..., package_ids: _Optional[_Iterable[str]] = ..., domain: _Optional[str] = ...) -> None: ...

class PartyToParticipant(_message.Message):
    __slots__ = ("party", "threshold", "participants", "group_addressing", "domain")
    class HostingParticipant(_message.Message):
        __slots__ = ("participant_uid", "permission")
        PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_FIELD_NUMBER: _ClassVar[int]
        participant_uid: str
        permission: Enums.ParticipantPermission
        def __init__(self, participant_uid: _Optional[str] = ..., permission: _Optional[_Union[Enums.ParticipantPermission, str]] = ...) -> None: ...
    PARTY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ADDRESSING_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    party: str
    threshold: int
    participants: _containers.RepeatedCompositeFieldContainer[PartyToParticipant.HostingParticipant]
    group_addressing: bool
    domain: str
    def __init__(self, party: _Optional[str] = ..., threshold: _Optional[int] = ..., participants: _Optional[_Iterable[_Union[PartyToParticipant.HostingParticipant, _Mapping]]] = ..., group_addressing: bool = ..., domain: _Optional[str] = ...) -> None: ...

class AuthorityOf(_message.Message):
    __slots__ = ("party", "threshold", "parties", "domain")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    party: str
    threshold: int
    parties: _containers.RepeatedScalarFieldContainer[str]
    domain: str
    def __init__(self, party: _Optional[str] = ..., threshold: _Optional[int] = ..., parties: _Optional[_Iterable[str]] = ..., domain: _Optional[str] = ...) -> None: ...

class DomainParametersState(_message.Message):
    __slots__ = ("domain", "domain_parameters")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    domain_parameters: _domain_parameters_pb2.DynamicDomainParameters
    def __init__(self, domain: _Optional[str] = ..., domain_parameters: _Optional[_Union[_domain_parameters_pb2.DynamicDomainParameters, _Mapping]] = ...) -> None: ...

class DynamicSequencingParametersState(_message.Message):
    __slots__ = ("domain", "sequencing_parameters")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SEQUENCING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    sequencing_parameters: _sequencing_parameters_pb2.DynamicSequencingParameters
    def __init__(self, domain: _Optional[str] = ..., sequencing_parameters: _Optional[_Union[_sequencing_parameters_pb2.DynamicSequencingParameters, _Mapping]] = ...) -> None: ...

class MediatorDomainState(_message.Message):
    __slots__ = ("domain", "group", "threshold", "active", "observers")
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

class SequencerDomainState(_message.Message):
    __slots__ = ("domain", "threshold", "active", "observers")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    threshold: int
    active: _containers.RepeatedScalarFieldContainer[str]
    observers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain: _Optional[str] = ..., threshold: _Optional[int] = ..., active: _Optional[_Iterable[str]] = ..., observers: _Optional[_Iterable[str]] = ...) -> None: ...

class PurgeTopologyTransaction(_message.Message):
    __slots__ = ("domain", "mappings")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    mappings: _containers.RepeatedCompositeFieldContainer[TopologyMapping]
    def __init__(self, domain: _Optional[str] = ..., mappings: _Optional[_Iterable[_Union[TopologyMapping, _Mapping]]] = ...) -> None: ...

class TopologyMapping(_message.Message):
    __slots__ = ("namespace_delegation", "identifier_delegation", "decentralized_namespace_definition", "owner_to_key_mapping", "domain_trust_certificate", "participant_permission", "party_hosting_limits", "vetted_packages", "party_to_participant", "authority_of", "domain_parameters_state", "mediator_domain_state", "sequencer_domain_state", "purge_topology_txs", "sequencing_dynamic_parameters_state", "party_to_key_mapping")
    NAMESPACE_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    DECENTRALIZED_NAMESPACE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
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
    SEQUENCING_DYNAMIC_PARAMETERS_STATE_FIELD_NUMBER: _ClassVar[int]
    PARTY_TO_KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    namespace_delegation: NamespaceDelegation
    identifier_delegation: IdentifierDelegation
    decentralized_namespace_definition: DecentralizedNamespaceDefinition
    owner_to_key_mapping: OwnerToKeyMapping
    domain_trust_certificate: DomainTrustCertificate
    participant_permission: ParticipantDomainPermission
    party_hosting_limits: PartyHostingLimits
    vetted_packages: VettedPackages
    party_to_participant: PartyToParticipant
    authority_of: AuthorityOf
    domain_parameters_state: DomainParametersState
    mediator_domain_state: MediatorDomainState
    sequencer_domain_state: SequencerDomainState
    purge_topology_txs: PurgeTopologyTransaction
    sequencing_dynamic_parameters_state: DynamicSequencingParametersState
    party_to_key_mapping: PartyToKeyMapping
    def __init__(self, namespace_delegation: _Optional[_Union[NamespaceDelegation, _Mapping]] = ..., identifier_delegation: _Optional[_Union[IdentifierDelegation, _Mapping]] = ..., decentralized_namespace_definition: _Optional[_Union[DecentralizedNamespaceDefinition, _Mapping]] = ..., owner_to_key_mapping: _Optional[_Union[OwnerToKeyMapping, _Mapping]] = ..., domain_trust_certificate: _Optional[_Union[DomainTrustCertificate, _Mapping]] = ..., participant_permission: _Optional[_Union[ParticipantDomainPermission, _Mapping]] = ..., party_hosting_limits: _Optional[_Union[PartyHostingLimits, _Mapping]] = ..., vetted_packages: _Optional[_Union[VettedPackages, _Mapping]] = ..., party_to_participant: _Optional[_Union[PartyToParticipant, _Mapping]] = ..., authority_of: _Optional[_Union[AuthorityOf, _Mapping]] = ..., domain_parameters_state: _Optional[_Union[DomainParametersState, _Mapping]] = ..., mediator_domain_state: _Optional[_Union[MediatorDomainState, _Mapping]] = ..., sequencer_domain_state: _Optional[_Union[SequencerDomainState, _Mapping]] = ..., purge_topology_txs: _Optional[_Union[PurgeTopologyTransaction, _Mapping]] = ..., sequencing_dynamic_parameters_state: _Optional[_Union[DynamicSequencingParametersState, _Mapping]] = ..., party_to_key_mapping: _Optional[_Union[PartyToKeyMapping, _Mapping]] = ...) -> None: ...

class TopologyTransaction(_message.Message):
    __slots__ = ("operation", "serial", "mapping")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    operation: Enums.TopologyChangeOp
    serial: int
    mapping: TopologyMapping
    def __init__(self, operation: _Optional[_Union[Enums.TopologyChangeOp, str]] = ..., serial: _Optional[int] = ..., mapping: _Optional[_Union[TopologyMapping, _Mapping]] = ...) -> None: ...

class SignedTopologyTransaction(_message.Message):
    __slots__ = ("transaction", "signatures", "proposal")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    transaction: bytes
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    proposal: bool
    def __init__(self, transaction: _Optional[bytes] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., proposal: bool = ...) -> None: ...

class TopologyTransactionsBroadcast(_message.Message):
    __slots__ = ("domain", "broadcasts")
    class Broadcast(_message.Message):
        __slots__ = ("broadcast_id", "transactions")
        BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
        TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
        broadcast_id: str
        transactions: _containers.RepeatedCompositeFieldContainer[SignedTopologyTransaction]
        def __init__(self, broadcast_id: _Optional[str] = ..., transactions: _Optional[_Iterable[_Union[SignedTopologyTransaction, _Mapping]]] = ...) -> None: ...
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    BROADCASTS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    broadcasts: _containers.RepeatedCompositeFieldContainer[TopologyTransactionsBroadcast.Broadcast]
    def __init__(self, domain: _Optional[str] = ..., broadcasts: _Optional[_Iterable[_Union[TopologyTransactionsBroadcast.Broadcast, _Mapping]]] = ...) -> None: ...
