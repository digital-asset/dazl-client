# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v2 import topology_pb2 as _topology_pb2
from ....protocol.v2 import domain_params_pb2 as _domain_params_pb2
from ....protocol.v0 import topology_ext_pb2 as _topology_ext_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTrafficStateRequest(_message.Message):
    __slots__ = ["base_query", "filter_member"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_MEMBER_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_member: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_member: _Optional[str] = ...) -> None: ...

class ListTrafficStateResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.TrafficControlStateX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.TrafficControlStateX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListTrafficStateResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListTrafficStateResult.Result, _Mapping]]] = ...) -> None: ...

class BaseQuery(_message.Message):
    __slots__ = ["filter_store", "proposals", "operation", "filter_operation", "snapshot", "head_state", "range", "filter_signed_key", "protocol_version"]
    class TimeRange(_message.Message):
        __slots__ = ["until"]
        FROM_FIELD_NUMBER: _ClassVar[int]
        UNTIL_FIELD_NUMBER: _ClassVar[int]
        until: _timestamp_pb2.Timestamp
        def __init__(self, until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...
    FILTER_STORE_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    FILTER_OPERATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    HEAD_STATE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    FILTER_SIGNED_KEY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    filter_store: str
    proposals: bool
    operation: _topology_pb2.TopologyChangeOpX
    filter_operation: bool
    snapshot: _timestamp_pb2.Timestamp
    head_state: _empty_pb2.Empty
    range: BaseQuery.TimeRange
    filter_signed_key: str
    protocol_version: _wrappers_pb2.StringValue
    def __init__(self, filter_store: _Optional[str] = ..., proposals: bool = ..., operation: _Optional[_Union[_topology_pb2.TopologyChangeOpX, str]] = ..., filter_operation: bool = ..., snapshot: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., head_state: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., range: _Optional[_Union[BaseQuery.TimeRange, _Mapping]] = ..., filter_signed_key: _Optional[str] = ..., protocol_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class BaseResult(_message.Message):
    __slots__ = ["store", "sequenced", "valid_from", "valid_until", "operation", "transaction_hash", "serial", "signed_by_fingerprints"]
    STORE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCED_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FINGERPRINTS_FIELD_NUMBER: _ClassVar[int]
    store: str
    sequenced: _timestamp_pb2.Timestamp
    valid_from: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    operation: _topology_pb2.TopologyChangeOpX
    transaction_hash: bytes
    serial: int
    signed_by_fingerprints: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store: _Optional[str] = ..., sequenced: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., operation: _Optional[_Union[_topology_pb2.TopologyChangeOpX, str]] = ..., transaction_hash: _Optional[bytes] = ..., serial: _Optional[int] = ..., signed_by_fingerprints: _Optional[_Iterable[str]] = ...) -> None: ...

class ListNamespaceDelegationRequest(_message.Message):
    __slots__ = ["base_query", "filter_namespace", "filter_target_key_fingerprint"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    FILTER_TARGET_KEY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_namespace: str
    filter_target_key_fingerprint: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_namespace: _Optional[str] = ..., filter_target_key_fingerprint: _Optional[str] = ...) -> None: ...

class ListNamespaceDelegationResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.NamespaceDelegationX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.NamespaceDelegationX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListNamespaceDelegationResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListNamespaceDelegationResult.Result, _Mapping]]] = ...) -> None: ...

class ListUnionspaceDefinitionRequest(_message.Message):
    __slots__ = ["base_query", "filter_namespace"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_namespace: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_namespace: _Optional[str] = ...) -> None: ...

class ListUnionspaceDefinitionResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.UnionspaceDefinitionX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.UnionspaceDefinitionX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListUnionspaceDefinitionResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListUnionspaceDefinitionResult.Result, _Mapping]]] = ...) -> None: ...

class ListIdentifierDelegationRequest(_message.Message):
    __slots__ = ["base_query", "filter_uid", "filter_target_key_fingerprint"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    FILTER_TARGET_KEY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    filter_target_key_fingerprint: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ..., filter_target_key_fingerprint: _Optional[str] = ...) -> None: ...

class ListIdentifierDelegationResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.IdentifierDelegationX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.IdentifierDelegationX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListIdentifierDelegationResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListIdentifierDelegationResult.Result, _Mapping]]] = ...) -> None: ...

class ListOwnerToKeyMappingRequest(_message.Message):
    __slots__ = ["base_query", "filter_key_owner_type", "filter_key_owner_uid"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_KEY_OWNER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_KEY_OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_key_owner_type: str
    filter_key_owner_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_key_owner_type: _Optional[str] = ..., filter_key_owner_uid: _Optional[str] = ...) -> None: ...

class ListOwnerToKeyMappingResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.OwnerToKeyMappingX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.OwnerToKeyMappingX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListOwnerToKeyMappingResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListOwnerToKeyMappingResult.Result, _Mapping]]] = ...) -> None: ...

class ListDomainTrustCertificateRequest(_message.Message):
    __slots__ = ["base_query", "filter_uid"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListDomainTrustCertificateResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.DomainTrustCertificateX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.DomainTrustCertificateX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListDomainTrustCertificateResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListDomainTrustCertificateResult.Result, _Mapping]]] = ...) -> None: ...

class ListParticipantDomainPermissionRequest(_message.Message):
    __slots__ = ["base_query", "filter_uid"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListParticipantDomainPermissionResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.ParticipantDomainPermissionX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.ParticipantDomainPermissionX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListParticipantDomainPermissionResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListParticipantDomainPermissionResult.Result, _Mapping]]] = ...) -> None: ...

class ListPartyHostingLimitsRequest(_message.Message):
    __slots__ = ["base_query", "filter_uid"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListPartyHostingLimitsResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.PartyHostingLimitsX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.PartyHostingLimitsX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListPartyHostingLimitsResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListPartyHostingLimitsResult.Result, _Mapping]]] = ...) -> None: ...

class ListVettedPackagesRequest(_message.Message):
    __slots__ = ["base_query", "filter_participant"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_participant: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_participant: _Optional[str] = ...) -> None: ...

class ListVettedPackagesResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.VettedPackagesX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.VettedPackagesX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListVettedPackagesResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListVettedPackagesResult.Result, _Mapping]]] = ...) -> None: ...

class ListPartyToParticipantRequest(_message.Message):
    __slots__ = ["base_query", "filter_party", "filter_participant"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_party: str
    filter_participant: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_party: _Optional[str] = ..., filter_participant: _Optional[str] = ...) -> None: ...

class ListPartyToParticipantResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.PartyToParticipantX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.PartyToParticipantX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListPartyToParticipantResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListPartyToParticipantResult.Result, _Mapping]]] = ...) -> None: ...

class ListAuthorityOfRequest(_message.Message):
    __slots__ = ["base_query", "filter_party"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTY_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_party: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_party: _Optional[str] = ...) -> None: ...

class ListAuthorityOfResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.AuthorityOfX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.AuthorityOfX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListAuthorityOfResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListAuthorityOfResult.Result, _Mapping]]] = ...) -> None: ...

class ListDomainParametersStateRequest(_message.Message):
    __slots__ = ["base_query", "filter_domain"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ...) -> None: ...

class ListDomainParametersStateResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _domain_params_pb2.DynamicDomainParametersX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_domain_params_pb2.DynamicDomainParametersX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListDomainParametersStateResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListDomainParametersStateResult.Result, _Mapping]]] = ...) -> None: ...

class ListMediatorDomainStateRequest(_message.Message):
    __slots__ = ["base_query", "filter_domain"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ...) -> None: ...

class ListMediatorDomainStateResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.MediatorDomainStateX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.MediatorDomainStateX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListMediatorDomainStateResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListMediatorDomainStateResult.Result, _Mapping]]] = ...) -> None: ...

class ListSequencerDomainStateRequest(_message.Message):
    __slots__ = ["base_query", "filter_domain"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ...) -> None: ...

class ListSequencerDomainStateResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.SequencerDomainStateX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.SequencerDomainStateX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListSequencerDomainStateResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListSequencerDomainStateResult.Result, _Mapping]]] = ...) -> None: ...

class ListPurgeTopologyTransactionXRequest(_message.Message):
    __slots__ = ["base_query", "filter_domain"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ...) -> None: ...

class ListPurgeTopologyTransactionXResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.PurgeTopologyTransactionX
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.PurgeTopologyTransactionX, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListPurgeTopologyTransactionXResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListPurgeTopologyTransactionXResult.Result, _Mapping]]] = ...) -> None: ...

class ListAvailableStoresRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ListAvailableStoresResult(_message.Message):
    __slots__ = ["store_ids"]
    STORE_IDS_FIELD_NUMBER: _ClassVar[int]
    store_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAllRequest(_message.Message):
    __slots__ = ["base_query"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ...) -> None: ...

class ListAllResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _topology_ext_pb2.TopologyTransactions
    def __init__(self, result: _Optional[_Union[_topology_ext_pb2.TopologyTransactions, _Mapping]] = ...) -> None: ...
