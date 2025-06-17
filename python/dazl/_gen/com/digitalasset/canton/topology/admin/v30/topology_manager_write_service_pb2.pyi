# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import topology_pb2 as _topology_pb2
from . import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForceFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORCE_FLAG_UNSPECIFIED: _ClassVar[ForceFlag]
    FORCE_FLAG_ALIEN_MEMBER: _ClassVar[ForceFlag]
    FORCE_FLAG_LEDGER_TIME_RECORD_TIME_TOLERANCE_INCREASE: _ClassVar[ForceFlag]
    FORCE_FLAG_ALLOW_UNVET_PACKAGE: _ClassVar[ForceFlag]
    FORCE_FLAG_ALLOW_UNKNOWN_PACKAGE: _ClassVar[ForceFlag]
    FORCE_FLAG_ALLOW_UNVETTED_DEPENDENCIES: _ClassVar[ForceFlag]
    FORCE_FLAG_DISABLE_PARTY_WITH_ACTIVE_CONTRACTS: _ClassVar[ForceFlag]
    FORCE_FLAG_ALLOW_UNVALIDATED_SIGNING_KEYS: _ClassVar[ForceFlag]
    FORCE_FLAG_ALLOW_UNVET_PACKAGE_WITH_ACTIVE_CONTRACTS: _ClassVar[ForceFlag]
    FORCE_FLAG_PREPARATION_TIME_RECORD_TIME_TOLERANCE_INCREASE: _ClassVar[ForceFlag]
    FORCE_FLAG_ALLOW_INSUFFICIENT_PARTICIPANT_PERMISSION_FOR_SIGNATORY_PARTY: _ClassVar[ForceFlag]
    FORCE_FLAG_ALLOW_INSUFFICIENT_SIGNATORY_ASSIGNING_PARTICIPANTS_FOR_PARTY: _ClassVar[ForceFlag]
FORCE_FLAG_UNSPECIFIED: ForceFlag
FORCE_FLAG_ALIEN_MEMBER: ForceFlag
FORCE_FLAG_LEDGER_TIME_RECORD_TIME_TOLERANCE_INCREASE: ForceFlag
FORCE_FLAG_ALLOW_UNVET_PACKAGE: ForceFlag
FORCE_FLAG_ALLOW_UNKNOWN_PACKAGE: ForceFlag
FORCE_FLAG_ALLOW_UNVETTED_DEPENDENCIES: ForceFlag
FORCE_FLAG_DISABLE_PARTY_WITH_ACTIVE_CONTRACTS: ForceFlag
FORCE_FLAG_ALLOW_UNVALIDATED_SIGNING_KEYS: ForceFlag
FORCE_FLAG_ALLOW_UNVET_PACKAGE_WITH_ACTIVE_CONTRACTS: ForceFlag
FORCE_FLAG_PREPARATION_TIME_RECORD_TIME_TOLERANCE_INCREASE: ForceFlag
FORCE_FLAG_ALLOW_INSUFFICIENT_PARTICIPANT_PERMISSION_FOR_SIGNATORY_PARTY: ForceFlag
FORCE_FLAG_ALLOW_INSUFFICIENT_SIGNATORY_ASSIGNING_PARTICIPANTS_FOR_PARTY: ForceFlag

class GenerateTransactionsRequest(_message.Message):
    __slots__ = ("proposals",)
    class Proposal(_message.Message):
        __slots__ = ("operation", "serial", "mapping", "store")
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        MAPPING_FIELD_NUMBER: _ClassVar[int]
        STORE_FIELD_NUMBER: _ClassVar[int]
        operation: _topology_pb2.Enums.TopologyChangeOp
        serial: int
        mapping: _topology_pb2.TopologyMapping
        store: _common_pb2.StoreId
        def __init__(self, operation: _Optional[_Union[_topology_pb2.Enums.TopologyChangeOp, str]] = ..., serial: _Optional[int] = ..., mapping: _Optional[_Union[_topology_pb2.TopologyMapping, _Mapping]] = ..., store: _Optional[_Union[_common_pb2.StoreId, _Mapping]] = ...) -> None: ...
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    proposals: _containers.RepeatedCompositeFieldContainer[GenerateTransactionsRequest.Proposal]
    def __init__(self, proposals: _Optional[_Iterable[_Union[GenerateTransactionsRequest.Proposal, _Mapping]]] = ...) -> None: ...

class GenerateTransactionsResponse(_message.Message):
    __slots__ = ("generated_transactions",)
    class GeneratedTransaction(_message.Message):
        __slots__ = ("serialized_transaction", "transaction_hash")
        SERIALIZED_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
        serialized_transaction: bytes
        transaction_hash: bytes
        def __init__(self, serialized_transaction: _Optional[bytes] = ..., transaction_hash: _Optional[bytes] = ...) -> None: ...
    GENERATED_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    generated_transactions: _containers.RepeatedCompositeFieldContainer[GenerateTransactionsResponse.GeneratedTransaction]
    def __init__(self, generated_transactions: _Optional[_Iterable[_Union[GenerateTransactionsResponse.GeneratedTransaction, _Mapping]]] = ...) -> None: ...

class AuthorizeRequest(_message.Message):
    __slots__ = ("proposal", "transaction_hash", "must_fully_authorize", "force_changes", "signed_by", "store", "wait_to_become_effective")
    class Proposal(_message.Message):
        __slots__ = ("change", "serial", "mapping")
        CHANGE_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        MAPPING_FIELD_NUMBER: _ClassVar[int]
        change: _topology_pb2.Enums.TopologyChangeOp
        serial: int
        mapping: _topology_pb2.TopologyMapping
        def __init__(self, change: _Optional[_Union[_topology_pb2.Enums.TopologyChangeOp, str]] = ..., serial: _Optional[int] = ..., mapping: _Optional[_Union[_topology_pb2.TopologyMapping, _Mapping]] = ...) -> None: ...
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    MUST_FULLY_AUTHORIZE_FIELD_NUMBER: _ClassVar[int]
    FORCE_CHANGES_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    WAIT_TO_BECOME_EFFECTIVE_FIELD_NUMBER: _ClassVar[int]
    proposal: AuthorizeRequest.Proposal
    transaction_hash: str
    must_fully_authorize: bool
    force_changes: _containers.RepeatedScalarFieldContainer[ForceFlag]
    signed_by: _containers.RepeatedScalarFieldContainer[str]
    store: _common_pb2.StoreId
    wait_to_become_effective: _duration_pb2.Duration
    def __init__(self, proposal: _Optional[_Union[AuthorizeRequest.Proposal, _Mapping]] = ..., transaction_hash: _Optional[str] = ..., must_fully_authorize: bool = ..., force_changes: _Optional[_Iterable[_Union[ForceFlag, str]]] = ..., signed_by: _Optional[_Iterable[str]] = ..., store: _Optional[_Union[_common_pb2.StoreId, _Mapping]] = ..., wait_to_become_effective: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class AuthorizeResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _topology_pb2.SignedTopologyTransaction
    def __init__(self, transaction: _Optional[_Union[_topology_pb2.SignedTopologyTransaction, _Mapping]] = ...) -> None: ...

class AddTransactionsRequest(_message.Message):
    __slots__ = ("transactions", "force_changes", "store", "wait_to_become_effective")
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    FORCE_CHANGES_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    WAIT_TO_BECOME_EFFECTIVE_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_topology_pb2.SignedTopologyTransaction]
    force_changes: _containers.RepeatedScalarFieldContainer[ForceFlag]
    store: _common_pb2.StoreId
    wait_to_become_effective: _duration_pb2.Duration
    def __init__(self, transactions: _Optional[_Iterable[_Union[_topology_pb2.SignedTopologyTransaction, _Mapping]]] = ..., force_changes: _Optional[_Iterable[_Union[ForceFlag, str]]] = ..., store: _Optional[_Union[_common_pb2.StoreId, _Mapping]] = ..., wait_to_become_effective: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class AddTransactionsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ImportTopologySnapshotRequest(_message.Message):
    __slots__ = ("topology_snapshot", "store", "wait_to_become_effective")
    TOPOLOGY_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    WAIT_TO_BECOME_EFFECTIVE_FIELD_NUMBER: _ClassVar[int]
    topology_snapshot: bytes
    store: _common_pb2.StoreId
    wait_to_become_effective: _duration_pb2.Duration
    def __init__(self, topology_snapshot: _Optional[bytes] = ..., store: _Optional[_Union[_common_pb2.StoreId, _Mapping]] = ..., wait_to_become_effective: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ImportTopologySnapshotResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SignTransactionsRequest(_message.Message):
    __slots__ = ("transactions", "signed_by", "store", "force_flags")
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_topology_pb2.SignedTopologyTransaction]
    signed_by: _containers.RepeatedScalarFieldContainer[str]
    store: _common_pb2.StoreId
    force_flags: _containers.RepeatedScalarFieldContainer[ForceFlag]
    def __init__(self, transactions: _Optional[_Iterable[_Union[_topology_pb2.SignedTopologyTransaction, _Mapping]]] = ..., signed_by: _Optional[_Iterable[str]] = ..., store: _Optional[_Union[_common_pb2.StoreId, _Mapping]] = ..., force_flags: _Optional[_Iterable[_Union[ForceFlag, str]]] = ...) -> None: ...

class SignTransactionsResponse(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_topology_pb2.SignedTopologyTransaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[_topology_pb2.SignedTopologyTransaction, _Mapping]]] = ...) -> None: ...

class CreateTemporaryTopologyStoreRequest(_message.Message):
    __slots__ = ("name", "protocol_version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    protocol_version: int
    def __init__(self, name: _Optional[str] = ..., protocol_version: _Optional[int] = ...) -> None: ...

class CreateTemporaryTopologyStoreResponse(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: _common_pb2.StoreId.Temporary
    def __init__(self, store_id: _Optional[_Union[_common_pb2.StoreId.Temporary, _Mapping]] = ...) -> None: ...

class DropTemporaryTopologyStoreRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: _common_pb2.StoreId.Temporary
    def __init__(self, store_id: _Optional[_Union[_common_pb2.StoreId.Temporary, _Mapping]] = ...) -> None: ...

class DropTemporaryTopologyStoreResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
