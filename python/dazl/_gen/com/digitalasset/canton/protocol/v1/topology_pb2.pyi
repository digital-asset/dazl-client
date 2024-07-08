# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from ..v0 import topology_pb2 as _topology_pb2
from . import sequencing_pb2 as _sequencing_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    operation: _topology_pb2.TopologyChangeOp
    id: str
    namespace_delegation: _topology_pb2.NamespaceDelegation
    identifier_delegation: _topology_pb2.IdentifierDelegation
    owner_to_key_mapping: _topology_pb2.OwnerToKeyMapping
    party_to_participant: _topology_pb2.PartyToParticipant
    signed_legal_identity_claim: _topology_pb2.SignedLegalIdentityClaim
    participant_state: _topology_pb2.ParticipantState
    vetted_packages: _topology_pb2.VettedPackages
    mediator_domain_state: _topology_pb2.MediatorDomainState
    def __init__(self, operation: _Optional[_Union[_topology_pb2.TopologyChangeOp, str]] = ..., id: _Optional[str] = ..., namespace_delegation: _Optional[_Union[_topology_pb2.NamespaceDelegation, _Mapping]] = ..., identifier_delegation: _Optional[_Union[_topology_pb2.IdentifierDelegation, _Mapping]] = ..., owner_to_key_mapping: _Optional[_Union[_topology_pb2.OwnerToKeyMapping, _Mapping]] = ..., party_to_participant: _Optional[_Union[_topology_pb2.PartyToParticipant, _Mapping]] = ..., signed_legal_identity_claim: _Optional[_Union[_topology_pb2.SignedLegalIdentityClaim, _Mapping]] = ..., participant_state: _Optional[_Union[_topology_pb2.ParticipantState, _Mapping]] = ..., vetted_packages: _Optional[_Union[_topology_pb2.VettedPackages, _Mapping]] = ..., mediator_domain_state: _Optional[_Union[_topology_pb2.MediatorDomainState, _Mapping]] = ...) -> None: ...

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

class RegisterTopologyTransactionResponse(_message.Message):
    __slots__ = ["requested_by", "participant", "request_id", "results", "domain_id"]
    class Result(_message.Message):
        __slots__ = ["state", "error_message"]
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []  # type: ignore
            MISSING_STATE: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            FAILED: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            REJECTED: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            ACCEPTED: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            DUPLICATE: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
            OBSOLETE: _ClassVar[RegisterTopologyTransactionResponse.Result.State]
        MISSING_STATE: RegisterTopologyTransactionResponse.Result.State
        FAILED: RegisterTopologyTransactionResponse.Result.State
        REJECTED: RegisterTopologyTransactionResponse.Result.State
        ACCEPTED: RegisterTopologyTransactionResponse.Result.State
        DUPLICATE: RegisterTopologyTransactionResponse.Result.State
        OBSOLETE: RegisterTopologyTransactionResponse.Result.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        state: RegisterTopologyTransactionResponse.Result.State
        error_message: str
        def __init__(self, state: _Optional[_Union[RegisterTopologyTransactionResponse.Result.State, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
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

class DomainTopologyTransactionMessage(_message.Message):
    __slots__ = ["signature", "domain_id", "not_sequenced_after", "transactions"]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    NOT_SEQUENCED_AFTER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    signature: _crypto_pb2.Signature
    domain_id: str
    not_sequenced_after: _timestamp_pb2.Timestamp
    transactions: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., domain_id: _Optional[str] = ..., not_sequenced_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., transactions: _Optional[_Iterable[bytes]] = ...) -> None: ...
