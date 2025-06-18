# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import synchronizer_parameters_pb2 as _synchronizer_parameters_pb2
from ....protocol.v30 import topology_pb2 as _topology_pb2
from . import common_pb2 as _common_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaseQuery(_message.Message):
    __slots__ = ("store", "proposals", "operation", "snapshot", "head_state", "range", "filter_signed_key", "protocol_version")
    class TimeRange(_message.Message):
        __slots__ = ("until",)
        FROM_FIELD_NUMBER: _ClassVar[int]
        UNTIL_FIELD_NUMBER: _ClassVar[int]
        until: _timestamp_pb2.Timestamp
        def __init__(self, until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...
    STORE_FIELD_NUMBER: _ClassVar[int]
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    HEAD_STATE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    FILTER_SIGNED_KEY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    store: _common_pb2.StoreId
    proposals: bool
    operation: _topology_pb2.Enums.TopologyChangeOp
    snapshot: _timestamp_pb2.Timestamp
    head_state: _empty_pb2.Empty
    range: BaseQuery.TimeRange
    filter_signed_key: str
    protocol_version: int
    def __init__(self, store: _Optional[_Union[_common_pb2.StoreId, _Mapping]] = ..., proposals: bool = ..., operation: _Optional[_Union[_topology_pb2.Enums.TopologyChangeOp, str]] = ..., snapshot: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., head_state: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., range: _Optional[_Union[BaseQuery.TimeRange, _Mapping]] = ..., filter_signed_key: _Optional[str] = ..., protocol_version: _Optional[int] = ...) -> None: ...

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
    store: _common_pb2.StoreId
    sequenced: _timestamp_pb2.Timestamp
    valid_from: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    operation: _topology_pb2.Enums.TopologyChangeOp
    transaction_hash: bytes
    serial: int
    signed_by_fingerprints: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store: _Optional[_Union[_common_pb2.StoreId, _Mapping]] = ..., sequenced: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., operation: _Optional[_Union[_topology_pb2.Enums.TopologyChangeOp, str]] = ..., transaction_hash: _Optional[bytes] = ..., serial: _Optional[int] = ..., signed_by_fingerprints: _Optional[_Iterable[str]] = ...) -> None: ...

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

class ListSynchronizerTrustCertificateRequest(_message.Message):
    __slots__ = ("base_query", "filter_uid")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListSynchronizerTrustCertificateResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.SynchronizerTrustCertificate
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.SynchronizerTrustCertificate, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListSynchronizerTrustCertificateResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListSynchronizerTrustCertificateResponse.Result, _Mapping]]] = ...) -> None: ...

class ListParticipantSynchronizerPermissionRequest(_message.Message):
    __slots__ = ("base_query", "filter_uid")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListParticipantSynchronizerPermissionResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.ParticipantSynchronizerPermission
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.ParticipantSynchronizerPermission, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListParticipantSynchronizerPermissionResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListParticipantSynchronizerPermissionResponse.Result, _Mapping]]] = ...) -> None: ...

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

class ListSynchronizerParametersStateRequest(_message.Message):
    __slots__ = ("base_query", "filter_synchronizer_id")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_synchronizer_id: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_synchronizer_id: _Optional[str] = ...) -> None: ...

class ListSynchronizerParametersStateResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _synchronizer_parameters_pb2.DynamicSynchronizerParameters
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_synchronizer_parameters_pb2.DynamicSynchronizerParameters, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListSynchronizerParametersStateResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListSynchronizerParametersStateResponse.Result, _Mapping]]] = ...) -> None: ...

class ListMediatorSynchronizerStateRequest(_message.Message):
    __slots__ = ("base_query", "filter_synchronizer_id")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_synchronizer_id: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_synchronizer_id: _Optional[str] = ...) -> None: ...

class ListMediatorSynchronizerStateResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.MediatorSynchronizerState
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.MediatorSynchronizerState, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListMediatorSynchronizerStateResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListMediatorSynchronizerStateResponse.Result, _Mapping]]] = ...) -> None: ...

class ListSequencerSynchronizerStateRequest(_message.Message):
    __slots__ = ("base_query", "filter_synchronizer_id")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_synchronizer_id: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_synchronizer_id: _Optional[str] = ...) -> None: ...

class ListSequencerSynchronizerStateResponse(_message.Message):
    __slots__ = ("results",)
    class Result(_message.Message):
        __slots__ = ("context", "item")
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.SequencerSynchronizerState
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.SequencerSynchronizerState, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListSequencerSynchronizerStateResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListSequencerSynchronizerStateResponse.Result, _Mapping]]] = ...) -> None: ...

class ListPurgeTopologyTransactionRequest(_message.Message):
    __slots__ = ("base_query", "filter_synchronizer_id")
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_synchronizer_id: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_synchronizer_id: _Optional[str] = ...) -> None: ...

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
    store_ids: _containers.RepeatedCompositeFieldContainer[_common_pb2.StoreId]
    def __init__(self, store_ids: _Optional[_Iterable[_Union[_common_pb2.StoreId, _Mapping]]] = ...) -> None: ...

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
    result: _common_pb2.TopologyTransactions
    def __init__(self, result: _Optional[_Union[_common_pb2.TopologyTransactions, _Mapping]] = ...) -> None: ...

class ExportTopologySnapshotResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class GenesisStateRequest(_message.Message):
    __slots__ = ("synchronizer_store", "timestamp")
    SYNCHRONIZER_STORE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    synchronizer_store: _common_pb2.StoreId
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, synchronizer_store: _Optional[_Union[_common_pb2.StoreId, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GenesisStateResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...
