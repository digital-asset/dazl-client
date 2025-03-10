# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import domain_parameters_pb2 as _domain_parameters_pb2
from ....protocol.v30 import topology_pb2 as _topology_pb2
from . import topology_ext_pb2 as _topology_ext_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaseQuery(_message.Message):
    __slots__ = ("filter_store", "proposals", "operation", "snapshot", "head_state", "range", "filter_signed_key", "protocol_version")
    class TimeRange(_message.Message):
        __slots__ = ("until",)
        FROM_FIELD_NUMBER: _ClassVar[int]
        UNTIL_FIELD_NUMBER: _ClassVar[int]
        until: _timestamp_pb2.Timestamp
        def __init__(self, until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...
    FILTER_STORE_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    HEAD_STATE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    FILTER_SIGNED_KEY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    filter_store: Store
    proposals: bool
    operation: _topology_pb2.Enums.TopologyChangeOp
    snapshot: _timestamp_pb2.Timestamp
    head_state: _empty_pb2.Empty
    range: BaseQuery.TimeRange
    filter_signed_key: str
    protocol_version: _wrappers_pb2.Int32Value
    def __init__(self, filter_store: _Optional[_Union[Store, _Mapping]] = ..., proposals: bool = ..., operation: _Optional[_Union[_topology_pb2.Enums.TopologyChangeOp, str]] = ..., snapshot: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., head_state: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., range: _Optional[_Union[BaseQuery.TimeRange, _Mapping]] = ..., filter_signed_key: _Optional[str] = ..., protocol_version: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class Store(_message.Message):
    __slots__ = ("authorized", "domain")
    class Authorized(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Domain(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    authorized: Store.Authorized
    domain: Store.Domain
    def __init__(self, authorized: _Optional[_Union[Store.Authorized, _Mapping]] = ..., domain: _Optional[_Union[Store.Domain, _Mapping]] = ...) -> None: ...

class BaseResult(_message.Message):
    __slots__ = ("store", "sequenced", "valid_from", "valid_until", "operation", "transaction_hash", "serial", "signed_by_fingerprints")
    STORE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCED_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FINGERPRINTS_FIELD_NUMBER: _ClassVar[int]
    store: Store
    sequenced: _timestamp_pb2.Timestamp
    valid_from: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    operation: _topology_pb2.Enums.TopologyChangeOp
    transaction_hash: bytes
    serial: int
    signed_by_fingerprints: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store: _Optional[_Union[Store, _Mapping]] = ..., sequenced: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., operation: _Optional[_Union[_topology_pb2.Enums.TopologyChangeOp, str]] = ..., transaction_hash: _Optional[bytes] = ..., serial: _Optional[int] = ..., signed_by_fingerprints: _Optional[_Iterable[str]] = ...) -> None: ...

class ListNamespaceDelegationRequest(_message.Message):
    __slots__ = ("base_query", "filter_namespace", "filter_target_key_fingerprint")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    FILTER_TARGET_KEY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_namespace: str
    filter_target_key_fingerprint: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_namespace: _Optional[str] = ..., filter_target_key_fingerprint: _Optional[str] = ...) -> None: ...

class ListNamespaceDelegationResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.NamespaceDelegation
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.NamespaceDelegation, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListNamespaceDelegationResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListNamespaceDelegationResponse.Result, _Mapping]]] = ...) -> None: ...

class ListDecentralizedNamespaceDefinitionRequest(_message.Message):
    __slots__ = ("base_query", "filter_namespace")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_namespace: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_namespace: _Optional[str] = ...) -> None: ...

class ListDecentralizedNamespaceDefinitionResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.DecentralizedNamespaceDefinition
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.DecentralizedNamespaceDefinition, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListDecentralizedNamespaceDefinitionResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListDecentralizedNamespaceDefinitionResponse.Result, _Mapping]]] = ...) -> None: ...

class ListIdentifierDelegationRequest(_message.Message):
    __slots__ = ("base_query", "filter_uid", "filter_target_key_fingerprint")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    FILTER_TARGET_KEY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    filter_target_key_fingerprint: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ..., filter_target_key_fingerprint: _Optional[str] = ...) -> None: ...

class ListIdentifierDelegationResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.IdentifierDelegation
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.IdentifierDelegation, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListIdentifierDelegationResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListIdentifierDelegationResponse.Result, _Mapping]]] = ...) -> None: ...

class ListOwnerToKeyMappingRequest(_message.Message):
    __slots__ = ("base_query", "filter_key_owner_type", "filter_key_owner_uid")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_KEY_OWNER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_KEY_OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_key_owner_type: str
    filter_key_owner_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_key_owner_type: _Optional[str] = ..., filter_key_owner_uid: _Optional[str] = ...) -> None: ...

class ListOwnerToKeyMappingResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.OwnerToKeyMapping
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.OwnerToKeyMapping, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListOwnerToKeyMappingResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListOwnerToKeyMappingResponse.Result, _Mapping]]] = ...) -> None: ...

class ListPartyToKeyMappingRequest(_message.Message):
    __slots__ = ("base_query", "filter_party")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTY_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_party: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_party: _Optional[str] = ...) -> None: ...

class ListPartyToKeyMappingResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.PartyToKeyMapping
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.PartyToKeyMapping, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListPartyToKeyMappingResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListPartyToKeyMappingResponse.Result, _Mapping]]] = ...) -> None: ...

class ListDomainTrustCertificateRequest(_message.Message):
    __slots__ = ("base_query", "filter_uid")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListDomainTrustCertificateResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.DomainTrustCertificate
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.DomainTrustCertificate, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListDomainTrustCertificateResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListDomainTrustCertificateResponse.Result, _Mapping]]] = ...) -> None: ...

class ListParticipantDomainPermissionRequest(_message.Message):
    __slots__ = ("base_query", "filter_uid")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListParticipantDomainPermissionResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.ParticipantDomainPermission
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.ParticipantDomainPermission, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListParticipantDomainPermissionResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListParticipantDomainPermissionResponse.Result, _Mapping]]] = ...) -> None: ...

class ListPartyHostingLimitsRequest(_message.Message):
    __slots__ = ("base_query", "filter_uid")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListPartyHostingLimitsResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.PartyHostingLimits
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.PartyHostingLimits, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListPartyHostingLimitsResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListPartyHostingLimitsResponse.Result, _Mapping]]] = ...) -> None: ...

class ListVettedPackagesRequest(_message.Message):
    __slots__ = ("base_query", "filter_participant")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_participant: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_participant: _Optional[str] = ...) -> None: ...

class ListVettedPackagesResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.VettedPackages
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.VettedPackages, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListVettedPackagesResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListVettedPackagesResponse.Result, _Mapping]]] = ...) -> None: ...

class ListPartyToParticipantRequest(_message.Message):
    __slots__ = ("base_query", "filter_party", "filter_participant")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_party: str
    filter_participant: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_party: _Optional[str] = ..., filter_participant: _Optional[str] = ...) -> None: ...

class ListPartyToParticipantResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.PartyToParticipant
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.PartyToParticipant, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListPartyToParticipantResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListPartyToParticipantResponse.Result, _Mapping]]] = ...) -> None: ...

class ListAuthorityOfRequest(_message.Message):
    __slots__ = ("base_query", "filter_party")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTY_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_party: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_party: _Optional[str] = ...) -> None: ...

class ListAuthorityOfResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.AuthorityOf
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.AuthorityOf, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListAuthorityOfResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListAuthorityOfResponse.Result, _Mapping]]] = ...) -> None: ...

class ListDomainParametersStateRequest(_message.Message):
    __slots__ = ("base_query", "filter_domain")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ...) -> None: ...

class ListDomainParametersStateResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _domain_parameters_pb2.DynamicDomainParameters
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_domain_parameters_pb2.DynamicDomainParameters, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListDomainParametersStateResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListDomainParametersStateResponse.Result, _Mapping]]] = ...) -> None: ...

class ListMediatorDomainStateRequest(_message.Message):
    __slots__ = ("base_query", "filter_domain")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ...) -> None: ...

class ListMediatorDomainStateResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.MediatorDomainState
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.MediatorDomainState, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListMediatorDomainStateResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListMediatorDomainStateResponse.Result, _Mapping]]] = ...) -> None: ...

class ListSequencerDomainStateRequest(_message.Message):
    __slots__ = ("base_query", "filter_domain")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ...) -> None: ...

class ListSequencerDomainStateResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.SequencerDomainState
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.SequencerDomainState, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListSequencerDomainStateResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListSequencerDomainStateResponse.Result, _Mapping]]] = ...) -> None: ...

class ListPurgeTopologyTransactionRequest(_message.Message):
    __slots__ = ("base_query", "filter_domain")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ...) -> None: ...

class ListPurgeTopologyTransactionResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.PurgeTopologyTransaction
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.PurgeTopologyTransaction, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListPurgeTopologyTransactionResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListPurgeTopologyTransactionResponse.Result, _Mapping]]] = ...) -> None: ...

class ListAvailableStoresRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAvailableStoresResponse(_message.Message):
    __slots__ = ("store_ids",)
    STORE_IDS_FIELD_NUMBER: _ClassVar[int]
    store_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAllRequest(_message.Message):
    __slots__ = ("base_query", "exclude_mappings", "filter_namespace")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    exclude_mappings: _containers.RepeatedScalarFieldContainer[str]
    filter_namespace: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., exclude_mappings: _Optional[_Iterable[str]] = ..., filter_namespace: _Optional[str] = ...) -> None: ...

class ExportTopologySnapshotRequest(_message.Message):
    __slots__ = ("base_query", "exclude_mappings", "filter_namespace")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    exclude_mappings: _containers.RepeatedScalarFieldContainer[str]
    filter_namespace: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., exclude_mappings: _Optional[_Iterable[str]] = ..., filter_namespace: _Optional[str] = ...) -> None: ...

class ListAllResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _topology_ext_pb2.TopologyTransactions
    def __init__(self, result: _Optional[_Union[_topology_ext_pb2.TopologyTransactions, _Mapping]] = ...) -> None: ...

class ExportTopologySnapshotResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: bytes
    def __init__(self, result: _Optional[bytes] = ...) -> None: ...

class GenesisStateRequest(_message.Message):
    __slots__ = ("filter_domain_store", "timestamp")
    FILTER_DOMAIN_STORE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    filter_domain_store: Store
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, filter_domain_store: _Optional[_Union[Store, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GenesisStateResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...
