# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....crypto.v0 import crypto_pb2 as _crypto_pb2
from ....protocol.v0 import sequencing_pb2 as _sequencing_pb2
from ....protocol.v0 import topology_pb2 as _topology_pb2
from ....protocol.v1 import sequencing_pb2 as _sequencing_pb2_1
from ....protocol.v0 import topology_ext_pb2 as _topology_ext_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListNamespaceDelegationRequest(_message.Message):
    __slots__ = ["base_query", "filter_namespace"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_namespace: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_namespace: _Optional[str] = ...) -> None: ...

class ListNamespaceDelegationResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item", "target_key_fingerprint"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        TARGET_KEY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.NamespaceDelegation
        target_key_fingerprint: str
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.NamespaceDelegation, _Mapping]] = ..., target_key_fingerprint: _Optional[str] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListNamespaceDelegationResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListNamespaceDelegationResult.Result, _Mapping]]] = ...) -> None: ...

class ListIdentifierDelegationRequest(_message.Message):
    __slots__ = ["base_query", "filter_uid"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListIdentifierDelegationResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item", "target_key_fingerprint"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        TARGET_KEY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.IdentifierDelegation
        target_key_fingerprint: str
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.IdentifierDelegation, _Mapping]] = ..., target_key_fingerprint: _Optional[str] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListIdentifierDelegationResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListIdentifierDelegationResult.Result, _Mapping]]] = ...) -> None: ...

class BaseQuery(_message.Message):
    __slots__ = ["filter_store", "use_state_store", "operation", "filter_operation", "snapshot", "head_state", "range", "filter_signed_key", "protocol_version"]
    class TimeRange(_message.Message):
        __slots__ = ["until"]
        FROM_FIELD_NUMBER: _ClassVar[int]
        UNTIL_FIELD_NUMBER: _ClassVar[int]
        until: _timestamp_pb2.Timestamp
        def __init__(self, until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...
    FILTER_STORE_FIELD_NUMBER: _ClassVar[int]
    USE_STATE_STORE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    FILTER_OPERATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    HEAD_STATE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    FILTER_SIGNED_KEY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    filter_store: str
    use_state_store: bool
    operation: _topology_pb2.TopologyChangeOp
    filter_operation: bool
    snapshot: _timestamp_pb2.Timestamp
    head_state: _empty_pb2.Empty
    range: BaseQuery.TimeRange
    filter_signed_key: str
    protocol_version: _wrappers_pb2.StringValue
    def __init__(self, filter_store: _Optional[str] = ..., use_state_store: bool = ..., operation: _Optional[_Union[_topology_pb2.TopologyChangeOp, str]] = ..., filter_operation: bool = ..., snapshot: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., head_state: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., range: _Optional[_Union[BaseQuery.TimeRange, _Mapping]] = ..., filter_signed_key: _Optional[str] = ..., protocol_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class BaseResult(_message.Message):
    __slots__ = ["store", "sequenced", "valid_from", "valid_until", "operation", "serialized", "signed_by_fingerprint"]
    STORE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCED_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    store: str
    sequenced: _timestamp_pb2.Timestamp
    valid_from: _timestamp_pb2.Timestamp
    valid_until: _timestamp_pb2.Timestamp
    operation: _topology_pb2.TopologyChangeOp
    serialized: bytes
    signed_by_fingerprint: str
    def __init__(self, store: _Optional[str] = ..., sequenced: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., operation: _Optional[_Union[_topology_pb2.TopologyChangeOp, str]] = ..., serialized: _Optional[bytes] = ..., signed_by_fingerprint: _Optional[str] = ...) -> None: ...

class ListPartyToParticipantResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.PartyToParticipant
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.PartyToParticipant, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListPartyToParticipantResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListPartyToParticipantResult.Result, _Mapping]]] = ...) -> None: ...

class ListPartyToParticipantRequest(_message.Message):
    __slots__ = ["base_query", "filter_party", "filter_participant", "filter_request_side", "filter_permission"]
    class FilterRequestSide(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _topology_pb2.RequestSide
        def __init__(self, value: _Optional[_Union[_topology_pb2.RequestSide, str]] = ...) -> None: ...
    class FilterPermission(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _topology_pb2.ParticipantPermission
        def __init__(self, value: _Optional[_Union[_topology_pb2.ParticipantPermission, str]] = ...) -> None: ...
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTY_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    FILTER_REQUEST_SIDE_FIELD_NUMBER: _ClassVar[int]
    FILTER_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_party: str
    filter_participant: str
    filter_request_side: ListPartyToParticipantRequest.FilterRequestSide
    filter_permission: ListPartyToParticipantRequest.FilterPermission
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_party: _Optional[str] = ..., filter_participant: _Optional[str] = ..., filter_request_side: _Optional[_Union[ListPartyToParticipantRequest.FilterRequestSide, _Mapping]] = ..., filter_permission: _Optional[_Union[ListPartyToParticipantRequest.FilterPermission, _Mapping]] = ...) -> None: ...

class ListOwnerToKeyMappingRequest(_message.Message):
    __slots__ = ["base_query", "filter_key_owner_type", "filter_key_owner_uid", "filter_key_purpose"]
    class FilterKeyPurpose(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _crypto_pb2.KeyPurpose
        def __init__(self, value: _Optional[_Union[_crypto_pb2.KeyPurpose, str]] = ...) -> None: ...
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_KEY_OWNER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_KEY_OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    FILTER_KEY_PURPOSE_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_key_owner_type: str
    filter_key_owner_uid: str
    filter_key_purpose: ListOwnerToKeyMappingRequest.FilterKeyPurpose
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_key_owner_type: _Optional[str] = ..., filter_key_owner_uid: _Optional[str] = ..., filter_key_purpose: _Optional[_Union[ListOwnerToKeyMappingRequest.FilterKeyPurpose, _Mapping]] = ...) -> None: ...

class ListOwnerToKeyMappingResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item", "key_fingerprint"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        KEY_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.OwnerToKeyMapping
        key_fingerprint: str
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.OwnerToKeyMapping, _Mapping]] = ..., key_fingerprint: _Optional[str] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListOwnerToKeyMappingResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListOwnerToKeyMappingResult.Result, _Mapping]]] = ...) -> None: ...

class ListSignedLegalIdentityClaimRequest(_message.Message):
    __slots__ = ["base_query", "filter_uid"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_UID_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_uid: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_uid: _Optional[str] = ...) -> None: ...

class ListSignedLegalIdentityClaimResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.SignedLegalIdentityClaim
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.SignedLegalIdentityClaim, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListSignedLegalIdentityClaimResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListSignedLegalIdentityClaimResult.Result, _Mapping]]] = ...) -> None: ...

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
        item: _topology_pb2.VettedPackages
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.VettedPackages, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListVettedPackagesResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListVettedPackagesResult.Result, _Mapping]]] = ...) -> None: ...

class ListDomainParametersChangesRequest(_message.Message):
    __slots__ = ["base_query"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ...) -> None: ...

class ListDomainParametersChangesResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "v0", "v1"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        V0_FIELD_NUMBER: _ClassVar[int]
        V1_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        v0: _sequencing_pb2.DynamicDomainParameters
        v1: _sequencing_pb2_1.DynamicDomainParameters
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., v0: _Optional[_Union[_sequencing_pb2.DynamicDomainParameters, _Mapping]] = ..., v1: _Optional[_Union[_sequencing_pb2_1.DynamicDomainParameters, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListDomainParametersChangesResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListDomainParametersChangesResult.Result, _Mapping]]] = ...) -> None: ...

class ListAvailableStoresRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ListAvailableStoresResult(_message.Message):
    __slots__ = ["store_ids"]
    STORE_IDS_FIELD_NUMBER: _ClassVar[int]
    store_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, store_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListParticipantDomainStateRequest(_message.Message):
    __slots__ = ["base_query", "filter_domain", "filter_participant"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILTER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    filter_participant: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ..., filter_participant: _Optional[str] = ...) -> None: ...

class ListParticipantDomainStateResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.ParticipantState
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.ParticipantState, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListParticipantDomainStateResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListParticipantDomainStateResult.Result, _Mapping]]] = ...) -> None: ...

class ListMediatorDomainStateRequest(_message.Message):
    __slots__ = ["base_query", "filter_domain", "filter_mediator"]
    BASE_QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FILTER_MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    base_query: BaseQuery
    filter_domain: str
    filter_mediator: str
    def __init__(self, base_query: _Optional[_Union[BaseQuery, _Mapping]] = ..., filter_domain: _Optional[str] = ..., filter_mediator: _Optional[str] = ...) -> None: ...

class ListMediatorDomainStateResult(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["context", "item"]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        context: BaseResult
        item: _topology_pb2.MediatorDomainState
        def __init__(self, context: _Optional[_Union[BaseResult, _Mapping]] = ..., item: _Optional[_Union[_topology_pb2.MediatorDomainState, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListMediatorDomainStateResult.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListMediatorDomainStateResult.Result, _Mapping]]] = ...) -> None: ...

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
