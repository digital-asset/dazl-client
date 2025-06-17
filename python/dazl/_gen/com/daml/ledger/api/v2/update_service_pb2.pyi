# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import offset_checkpoint_pb2 as _offset_checkpoint_pb2
from . import reassignment_pb2 as _reassignment_pb2
from . import topology_transaction_pb2 as _topology_transaction_pb2
from . import transaction_pb2 as _transaction_pb2
from . import transaction_filter_pb2 as _transaction_filter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUpdatesRequest(_message.Message):
    __slots__ = ("begin_exclusive", "end_inclusive", "filter", "verbose", "update_format")
    BEGIN_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    END_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    begin_exclusive: int
    end_inclusive: int
    filter: _transaction_filter_pb2.TransactionFilter
    verbose: bool
    update_format: _transaction_filter_pb2.UpdateFormat
    def __init__(self, begin_exclusive: _Optional[int] = ..., end_inclusive: _Optional[int] = ..., filter: _Optional[_Union[_transaction_filter_pb2.TransactionFilter, _Mapping]] = ..., verbose: bool = ..., update_format: _Optional[_Union[_transaction_filter_pb2.UpdateFormat, _Mapping]] = ...) -> None: ...

class GetUpdatesResponse(_message.Message):
    __slots__ = ("transaction", "reassignment", "offset_checkpoint", "topology_transaction")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.Transaction
    reassignment: _reassignment_pb2.Reassignment
    offset_checkpoint: _offset_checkpoint_pb2.OffsetCheckpoint
    topology_transaction: _topology_transaction_pb2.TopologyTransaction
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]] = ..., reassignment: _Optional[_Union[_reassignment_pb2.Reassignment, _Mapping]] = ..., offset_checkpoint: _Optional[_Union[_offset_checkpoint_pb2.OffsetCheckpoint, _Mapping]] = ..., topology_transaction: _Optional[_Union[_topology_transaction_pb2.TopologyTransaction, _Mapping]] = ...) -> None: ...

class GetUpdateTreesResponse(_message.Message):
    __slots__ = ("transaction_tree", "reassignment", "offset_checkpoint")
    TRANSACTION_TREE_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    transaction_tree: _transaction_pb2.TransactionTree
    reassignment: _reassignment_pb2.Reassignment
    offset_checkpoint: _offset_checkpoint_pb2.OffsetCheckpoint
    def __init__(self, transaction_tree: _Optional[_Union[_transaction_pb2.TransactionTree, _Mapping]] = ..., reassignment: _Optional[_Union[_reassignment_pb2.Reassignment, _Mapping]] = ..., offset_checkpoint: _Optional[_Union[_offset_checkpoint_pb2.OffsetCheckpoint, _Mapping]] = ...) -> None: ...

class GetTransactionByOffsetRequest(_message.Message):
    __slots__ = ("offset", "requesting_parties", "transaction_format")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FORMAT_FIELD_NUMBER: _ClassVar[int]
    offset: int
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    transaction_format: _transaction_filter_pb2.TransactionFormat
    def __init__(self, offset: _Optional[int] = ..., requesting_parties: _Optional[_Iterable[str]] = ..., transaction_format: _Optional[_Union[_transaction_filter_pb2.TransactionFormat, _Mapping]] = ...) -> None: ...

class GetTransactionByIdRequest(_message.Message):
    __slots__ = ("update_id", "requesting_parties", "transaction_format")
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FORMAT_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    transaction_format: _transaction_filter_pb2.TransactionFormat
    def __init__(self, update_id: _Optional[str] = ..., requesting_parties: _Optional[_Iterable[str]] = ..., transaction_format: _Optional[_Union[_transaction_filter_pb2.TransactionFormat, _Mapping]] = ...) -> None: ...

class GetTransactionTreeResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.TransactionTree
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.TransactionTree, _Mapping]] = ...) -> None: ...

class GetTransactionResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.Transaction
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]] = ...) -> None: ...

class GetUpdateByOffsetRequest(_message.Message):
    __slots__ = ("offset", "update_format")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    offset: int
    update_format: _transaction_filter_pb2.UpdateFormat
    def __init__(self, offset: _Optional[int] = ..., update_format: _Optional[_Union[_transaction_filter_pb2.UpdateFormat, _Mapping]] = ...) -> None: ...

class GetUpdateByIdRequest(_message.Message):
    __slots__ = ("update_id", "update_format")
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    update_format: _transaction_filter_pb2.UpdateFormat
    def __init__(self, update_id: _Optional[str] = ..., update_format: _Optional[_Union[_transaction_filter_pb2.UpdateFormat, _Mapping]] = ...) -> None: ...

class GetUpdateResponse(_message.Message):
    __slots__ = ("transaction", "reassignment", "topology_transaction")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.Transaction
    reassignment: _reassignment_pb2.Reassignment
    topology_transaction: _topology_transaction_pb2.TopologyTransaction
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]] = ..., reassignment: _Optional[_Union[_reassignment_pb2.Reassignment, _Mapping]] = ..., topology_transaction: _Optional[_Union[_topology_transaction_pb2.TopologyTransaction, _Mapping]] = ...) -> None: ...
