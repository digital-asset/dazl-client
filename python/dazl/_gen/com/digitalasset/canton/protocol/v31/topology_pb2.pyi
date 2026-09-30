# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from ..v30 import topology_pb2 as _topology_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartyToParticipant(_message.Message):
    __slots__ = ("party", "threshold", "participants", "party_signing_keys", "is_offline")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    PARTY_SIGNING_KEYS_FIELD_NUMBER: _ClassVar[int]
    IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    party: str
    threshold: int
    participants: _containers.RepeatedCompositeFieldContainer[_topology_pb2.PartyToParticipant.HostingParticipant]
    party_signing_keys: _crypto_pb2.SigningKeysWithThreshold
    is_offline: bool
    def __init__(self, party: _Optional[str] = ..., threshold: _Optional[int] = ..., participants: _Optional[_Iterable[_Union[_topology_pb2.PartyToParticipant.HostingParticipant, _Mapping]]] = ..., party_signing_keys: _Optional[_Union[_crypto_pb2.SigningKeysWithThreshold, _Mapping]] = ..., is_offline: _Optional[bool] = ...) -> None: ...

class TopologyMapping(_message.Message):
    __slots__ = ("namespace_delegation", "decentralized_namespace_definition", "owner_to_key_mapping", "synchronizer_trust_certificate", "participant_permission", "party_hosting_limits", "vetted_packages", "party_to_participant", "synchronizer_parameters_state", "mediator_synchronizer_state", "sequencer_synchronizer_state", "sequencing_dynamic_parameters_state", "party_to_key_mapping", "synchronizer_upgrade_announcement", "sequencer_connection_successor")
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
    SEQUENCING_DYNAMIC_PARAMETERS_STATE_FIELD_NUMBER: _ClassVar[int]
    PARTY_TO_KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_UPGRADE_ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCER_CONNECTION_SUCCESSOR_FIELD_NUMBER: _ClassVar[int]
    namespace_delegation: _topology_pb2.NamespaceDelegation
    decentralized_namespace_definition: _topology_pb2.DecentralizedNamespaceDefinition
    owner_to_key_mapping: _topology_pb2.OwnerToKeyMapping
    synchronizer_trust_certificate: _topology_pb2.SynchronizerTrustCertificate
    participant_permission: _topology_pb2.ParticipantSynchronizerPermission
    party_hosting_limits: _topology_pb2.PartyHostingLimits
    vetted_packages: _topology_pb2.VettedPackages
    party_to_participant: PartyToParticipant
    synchronizer_parameters_state: _topology_pb2.SynchronizerParametersState
    mediator_synchronizer_state: _topology_pb2.MediatorSynchronizerState
    sequencer_synchronizer_state: _topology_pb2.SequencerSynchronizerState
    sequencing_dynamic_parameters_state: _topology_pb2.DynamicSequencingParametersState
    party_to_key_mapping: _topology_pb2.PartyToKeyMapping
    synchronizer_upgrade_announcement: _topology_pb2.LsuAnnouncement
    sequencer_connection_successor: _topology_pb2.LsuSequencerConnectionSuccessor
    def __init__(self, namespace_delegation: _Optional[_Union[_topology_pb2.NamespaceDelegation, _Mapping]] = ..., decentralized_namespace_definition: _Optional[_Union[_topology_pb2.DecentralizedNamespaceDefinition, _Mapping]] = ..., owner_to_key_mapping: _Optional[_Union[_topology_pb2.OwnerToKeyMapping, _Mapping]] = ..., synchronizer_trust_certificate: _Optional[_Union[_topology_pb2.SynchronizerTrustCertificate, _Mapping]] = ..., participant_permission: _Optional[_Union[_topology_pb2.ParticipantSynchronizerPermission, _Mapping]] = ..., party_hosting_limits: _Optional[_Union[_topology_pb2.PartyHostingLimits, _Mapping]] = ..., vetted_packages: _Optional[_Union[_topology_pb2.VettedPackages, _Mapping]] = ..., party_to_participant: _Optional[_Union[PartyToParticipant, _Mapping]] = ..., synchronizer_parameters_state: _Optional[_Union[_topology_pb2.SynchronizerParametersState, _Mapping]] = ..., mediator_synchronizer_state: _Optional[_Union[_topology_pb2.MediatorSynchronizerState, _Mapping]] = ..., sequencer_synchronizer_state: _Optional[_Union[_topology_pb2.SequencerSynchronizerState, _Mapping]] = ..., sequencing_dynamic_parameters_state: _Optional[_Union[_topology_pb2.DynamicSequencingParametersState, _Mapping]] = ..., party_to_key_mapping: _Optional[_Union[_topology_pb2.PartyToKeyMapping, _Mapping]] = ..., synchronizer_upgrade_announcement: _Optional[_Union[_topology_pb2.LsuAnnouncement, _Mapping]] = ..., sequencer_connection_successor: _Optional[_Union[_topology_pb2.LsuSequencerConnectionSuccessor, _Mapping]] = ...) -> None: ...

class TopologyTransaction(_message.Message):
    __slots__ = ("operation", "serial", "mapping")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    MAPPING_FIELD_NUMBER: _ClassVar[int]
    operation: _topology_pb2.Enums.TopologyChangeOp
    serial: int
    mapping: TopologyMapping
    def __init__(self, operation: _Optional[_Union[_topology_pb2.Enums.TopologyChangeOp, str]] = ..., serial: _Optional[int] = ..., mapping: _Optional[_Union[TopologyMapping, _Mapping]] = ...) -> None: ...
