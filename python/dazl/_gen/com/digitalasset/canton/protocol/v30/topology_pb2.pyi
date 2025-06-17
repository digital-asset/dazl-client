# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from . import sequencing_parameters_pb2 as _sequencing_parameters_pb2
from . import synchronizer_parameters_pb2 as _synchronizer_parameters_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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
    class TopologyMappingCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOPOLOGY_MAPPING_CODE_UNSPECIFIED: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_NAMESPACE_DELEGATION: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_DECENTRALIZED_NAMESPACE_DEFINITION: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_OWNER_TO_KEY_MAPPING: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_SYNCHRONIZER_TRUST_CERTIFICATE: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_PARTICIPANT_PERMISSION: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_PARTY_HOSTING_LIMITS: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_VETTED_PACKAGES: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_PARTY_TO_PARTICIPANT: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_SYNCHRONIZER_PARAMETERS_STATE: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_MEDIATOR_SYNCHRONIZER_STATE: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_SEQUENCER_SYNCHRONIZER_STATE: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_PURGE_TOPOLOGY_TXS: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_SEQUENCING_DYNAMIC_PARAMETERS_STATE: _ClassVar[Enums.TopologyMappingCode]
        TOPOLOGY_MAPPING_CODE_PARTY_TO_KEY_MAPPING: _ClassVar[Enums.TopologyMappingCode]
    TOPOLOGY_MAPPING_CODE_UNSPECIFIED: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_NAMESPACE_DELEGATION: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_DECENTRALIZED_NAMESPACE_DEFINITION: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_OWNER_TO_KEY_MAPPING: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_SYNCHRONIZER_TRUST_CERTIFICATE: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_PARTICIPANT_PERMISSION: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_PARTY_HOSTING_LIMITS: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_VETTED_PACKAGES: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_PARTY_TO_PARTICIPANT: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_SYNCHRONIZER_PARAMETERS_STATE: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_MEDIATOR_SYNCHRONIZER_STATE: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_SEQUENCER_SYNCHRONIZER_STATE: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_PURGE_TOPOLOGY_TXS: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_SEQUENCING_DYNAMIC_PARAMETERS_STATE: Enums.TopologyMappingCode
    TOPOLOGY_MAPPING_CODE_PARTY_TO_KEY_MAPPING: Enums.TopologyMappingCode
    def __init__(self) -> None: ...

class NamespaceDelegation(_message.Message):
    __slots__ = ("namespace", "target_key", "is_root_delegation", "can_sign_all_mappings", "can_sign_all_but_namespace_delegations", "can_sign_specific_mapings")
    class CanSignAllMappings(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CanSignAllButNamespaceDelegations(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CanSignSpecificMappings(_message.Message):
        __slots__ = ("mappings",)
        MAPPINGS_FIELD_NUMBER: _ClassVar[int]
        mappings: _containers.RepeatedScalarFieldContainer[Enums.TopologyMappingCode]
        def __init__(self, mappings: _Optional[_Iterable[_Union[Enums.TopologyMappingCode, str]]] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TARGET_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    CAN_SIGN_ALL_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    CAN_SIGN_ALL_BUT_NAMESPACE_DELEGATIONS_FIELD_NUMBER: _ClassVar[int]
    CAN_SIGN_SPECIFIC_MAPINGS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    target_key: _crypto_pb2.SigningPublicKey
    is_root_delegation: bool
    can_sign_all_mappings: NamespaceDelegation.CanSignAllMappings
    can_sign_all_but_namespace_delegations: NamespaceDelegation.CanSignAllButNamespaceDelegations
    can_sign_specific_mapings: NamespaceDelegation.CanSignSpecificMappings
    def __init__(self, namespace: _Optional[str] = ..., target_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ..., is_root_delegation: bool = ..., can_sign_all_mappings: _Optional[_Union[NamespaceDelegation.CanSignAllMappings, _Mapping]] = ..., can_sign_all_but_namespace_delegations: _Optional[_Union[NamespaceDelegation.CanSignAllButNamespaceDelegations, _Mapping]] = ..., can_sign_specific_mapings: _Optional[_Union[NamespaceDelegation.CanSignSpecificMappings, _Mapping]] = ...) -> None: ...

class DecentralizedNamespaceDefinition(_message.Message):
    __slots__ = ("decentralized_namespace", "threshold", "owners")
    DECENTRALIZED_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    decentralized_namespace: str
    threshold: int
    owners: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, decentralized_namespace: _Optional[str] = ..., threshold: _Optional[int] = ..., owners: _Optional[_Iterable[str]] = ...) -> None: ...

class OwnerToKeyMapping(_message.Message):
    __slots__ = ("member", "public_keys")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    member: str
    public_keys: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.PublicKey]
    def __init__(self, member: _Optional[str] = ..., public_keys: _Optional[_Iterable[_Union[_crypto_pb2.PublicKey, _Mapping]]] = ...) -> None: ...

class PartyToKeyMapping(_message.Message):
    __slots__ = ("party", "threshold", "signing_keys")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEYS_FIELD_NUMBER: _ClassVar[int]
    party: str
    threshold: int
    signing_keys: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.SigningPublicKey]
    def __init__(self, party: _Optional[str] = ..., threshold: _Optional[int] = ..., signing_keys: _Optional[_Iterable[_Union[_crypto_pb2.SigningPublicKey, _Mapping]]] = ...) -> None: ...

class SynchronizerTrustCertificate(_message.Message):
    __slots__ = ("participant_uid", "synchronizer_id")
    PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    participant_uid: str
    synchronizer_id: str
    def __init__(self, participant_uid: _Optional[str] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...

class ParticipantSynchronizerPermission(_message.Message):
    __slots__ = ("synchronizer_id", "participant_uid", "permission", "limits", "login_after")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_AFTER_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    participant_uid: str
    permission: Enums.ParticipantPermission
    limits: _synchronizer_parameters_pb2.ParticipantSynchronizerLimits
    login_after: int
    def __init__(self, synchronizer_id: _Optional[str] = ..., participant_uid: _Optional[str] = ..., permission: _Optional[_Union[Enums.ParticipantPermission, str]] = ..., limits: _Optional[_Union[_synchronizer_parameters_pb2.ParticipantSynchronizerLimits, _Mapping]] = ..., login_after: _Optional[int] = ...) -> None: ...

class PartyHostingLimits(_message.Message):
    __slots__ = ("synchronizer_id", "party")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    PARTY_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    party: str
    def __init__(self, synchronizer_id: _Optional[str] = ..., party: _Optional[str] = ...) -> None: ...

class VettedPackages(_message.Message):
    __slots__ = ("participant_uid", "package_ids", "packages")
    class VettedPackage(_message.Message):
        __slots__ = ("package_id", "valid_from", "valid_until")
        PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
        VALID_FROM_FIELD_NUMBER: _ClassVar[int]
        VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
        package_id: str
        valid_from: _timestamp_pb2.Timestamp
        valid_until: _timestamp_pb2.Timestamp
        def __init__(self, package_id: _Optional[str] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    participant_uid: str
    package_ids: _containers.RepeatedScalarFieldContainer[str]
    packages: _containers.RepeatedCompositeFieldContainer[VettedPackages.VettedPackage]
    def __init__(self, participant_uid: _Optional[str] = ..., package_ids: _Optional[_Iterable[str]] = ..., packages: _Optional[_Iterable[_Union[VettedPackages.VettedPackage, _Mapping]]] = ...) -> None: ...

class PartyToParticipant(_message.Message):
    __slots__ = ("party", "threshold", "participants")
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
    party: str
    threshold: int
    participants: _containers.RepeatedCompositeFieldContainer[PartyToParticipant.HostingParticipant]
    def __init__(self, party: _Optional[str] = ..., threshold: _Optional[int] = ..., participants: _Optional[_Iterable[_Union[PartyToParticipant.HostingParticipant, _Mapping]]] = ...) -> None: ...

class SynchronizerParametersState(_message.Message):
    __slots__ = ("synchronizer_id", "synchronizer_parameters")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    synchronizer_parameters: _synchronizer_parameters_pb2.DynamicSynchronizerParameters
    def __init__(self, synchronizer_id: _Optional[str] = ..., synchronizer_parameters: _Optional[_Union[_synchronizer_parameters_pb2.DynamicSynchronizerParameters, _Mapping]] = ...) -> None: ...

class DynamicSequencingParametersState(_message.Message):
    __slots__ = ("synchronizer_id", "sequencing_parameters")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCING_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    sequencing_parameters: _sequencing_parameters_pb2.DynamicSequencingParameters
    def __init__(self, synchronizer_id: _Optional[str] = ..., sequencing_parameters: _Optional[_Union[_sequencing_parameters_pb2.DynamicSequencingParameters, _Mapping]] = ...) -> None: ...

class MediatorSynchronizerState(_message.Message):
    __slots__ = ("synchronizer_id", "group", "threshold", "active", "observers")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    group: int
    threshold: int
    active: _containers.RepeatedScalarFieldContainer[str]
    observers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, synchronizer_id: _Optional[str] = ..., group: _Optional[int] = ..., threshold: _Optional[int] = ..., active: _Optional[_Iterable[str]] = ..., observers: _Optional[_Iterable[str]] = ...) -> None: ...

class SequencerSynchronizerState(_message.Message):
    __slots__ = ("synchronizer_id", "threshold", "active", "observers")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBSERVERS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    threshold: int
    active: _containers.RepeatedScalarFieldContainer[str]
    observers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, synchronizer_id: _Optional[str] = ..., threshold: _Optional[int] = ..., active: _Optional[_Iterable[str]] = ..., observers: _Optional[_Iterable[str]] = ...) -> None: ...

class PurgeTopologyTransaction(_message.Message):
    __slots__ = ("synchronizer_id", "mappings")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    mappings: _containers.RepeatedCompositeFieldContainer[TopologyMapping]
    def __init__(self, synchronizer_id: _Optional[str] = ..., mappings: _Optional[_Iterable[_Union[TopologyMapping, _Mapping]]] = ...) -> None: ...

class TopologyMapping(_message.Message):
    __slots__ = ("namespace_delegation", "decentralized_namespace_definition", "owner_to_key_mapping", "synchronizer_trust_certificate", "participant_permission", "party_hosting_limits", "vetted_packages", "party_to_participant", "synchronizer_parameters_state", "mediator_synchronizer_state", "sequencer_synchronizer_state", "purge_topology_txs", "sequencing_dynamic_parameters_state", "party_to_key_mapping")
    NAMESPACE_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    DECENTRALIZED_NAMESPACE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    OWNER_TO_KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_TRUST_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PARTY_HOSTING_LIMITS_FIELD_NUMBER: _ClassVar[int]
    VETTED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    PARTY_TO_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_PARAMETERS_STATE_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_SYNCHRONIZER_STATE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_SYNCHRONIZER_STATE_FIELD_NUMBER: _ClassVar[int]
    PURGE_TOPOLOGY_TXS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCING_DYNAMIC_PARAMETERS_STATE_FIELD_NUMBER: _ClassVar[int]
    PARTY_TO_KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    namespace_delegation: NamespaceDelegation
    decentralized_namespace_definition: DecentralizedNamespaceDefinition
    owner_to_key_mapping: OwnerToKeyMapping
    synchronizer_trust_certificate: SynchronizerTrustCertificate
    participant_permission: ParticipantSynchronizerPermission
    party_hosting_limits: PartyHostingLimits
    vetted_packages: VettedPackages
    party_to_participant: PartyToParticipant
    synchronizer_parameters_state: SynchronizerParametersState
    mediator_synchronizer_state: MediatorSynchronizerState
    sequencer_synchronizer_state: SequencerSynchronizerState
    purge_topology_txs: PurgeTopologyTransaction
    sequencing_dynamic_parameters_state: DynamicSequencingParametersState
    party_to_key_mapping: PartyToKeyMapping
    def __init__(self, namespace_delegation: _Optional[_Union[NamespaceDelegation, _Mapping]] = ..., decentralized_namespace_definition: _Optional[_Union[DecentralizedNamespaceDefinition, _Mapping]] = ..., owner_to_key_mapping: _Optional[_Union[OwnerToKeyMapping, _Mapping]] = ..., synchronizer_trust_certificate: _Optional[_Union[SynchronizerTrustCertificate, _Mapping]] = ..., participant_permission: _Optional[_Union[ParticipantSynchronizerPermission, _Mapping]] = ..., party_hosting_limits: _Optional[_Union[PartyHostingLimits, _Mapping]] = ..., vetted_packages: _Optional[_Union[VettedPackages, _Mapping]] = ..., party_to_participant: _Optional[_Union[PartyToParticipant, _Mapping]] = ..., synchronizer_parameters_state: _Optional[_Union[SynchronizerParametersState, _Mapping]] = ..., mediator_synchronizer_state: _Optional[_Union[MediatorSynchronizerState, _Mapping]] = ..., sequencer_synchronizer_state: _Optional[_Union[SequencerSynchronizerState, _Mapping]] = ..., purge_topology_txs: _Optional[_Union[PurgeTopologyTransaction, _Mapping]] = ..., sequencing_dynamic_parameters_state: _Optional[_Union[DynamicSequencingParametersState, _Mapping]] = ..., party_to_key_mapping: _Optional[_Union[PartyToKeyMapping, _Mapping]] = ...) -> None: ...

class TopologyTransaction(_message.Message):
    __slots__ = ("operation", "serial", "mapping")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    operation: Enums.TopologyChangeOp
    serial: int
    mapping: TopologyMapping
    def __init__(self, operation: _Optional[_Union[Enums.TopologyChangeOp, str]] = ..., serial: _Optional[int] = ..., mapping: _Optional[_Union[TopologyMapping, _Mapping]] = ...) -> None: ...

class MultiTransactionSignatures(_message.Message):
    __slots__ = ("transaction_hashes", "signatures")
    TRANSACTION_HASHES_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    transaction_hashes: _containers.RepeatedScalarFieldContainer[bytes]
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    def __init__(self, transaction_hashes: _Optional[_Iterable[bytes]] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...

class SignedTopologyTransaction(_message.Message):
    __slots__ = ("transaction", "signatures", "proposal", "multi_transaction_signatures")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    MULTI_TRANSACTION_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    transaction: bytes
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    proposal: bool
    multi_transaction_signatures: _containers.RepeatedCompositeFieldContainer[MultiTransactionSignatures]
    def __init__(self, transaction: _Optional[bytes] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ..., proposal: bool = ..., multi_transaction_signatures: _Optional[_Iterable[_Union[MultiTransactionSignatures, _Mapping]]] = ...) -> None: ...

class SignedTopologyTransactions(_message.Message):
    __slots__ = ("signed_transaction",)
    SIGNED_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    signed_transaction: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, signed_transaction: _Optional[_Iterable[bytes]] = ...) -> None: ...

class TopologyTransactionsBroadcast(_message.Message):
    __slots__ = ("synchronizer_id", "signed_transactions")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNED_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    signed_transactions: SignedTopologyTransactions
    def __init__(self, synchronizer_id: _Optional[str] = ..., signed_transactions: _Optional[_Union[SignedTopologyTransactions, _Mapping]] = ...) -> None: ...
