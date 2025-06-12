# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import offset_checkpoint_pb2 as _offset_checkpoint_pb2
from . import reassignment_pb2 as _reassignment_pb2
from . import transaction_pb2 as _transaction_pb2
from . import transaction_filter_pb2 as _transaction_filter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUpdatesRequest(_message.Message):
    __slots__ = ("begin_exclusive", "end_inclusive", "filter", "verbose")
    BEGIN_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    END_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    begin_exclusive: int
    end_inclusive: int
    filter: _transaction_filter_pb2.TransactionFilter
    verbose: bool
    def __init__(self, begin_exclusive: _Optional[int] = ..., end_inclusive: _Optional[int] = ..., filter: _Optional[_Union[_transaction_filter_pb2.TransactionFilter, _Mapping]] = ..., verbose: bool = ...) -> None: ...

class GetUpdatesResponse(_message.Message):
    __slots__ = ("transaction", "reassignment", "offset_checkpoint")
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.Transaction
    reassignment: _reassignment_pb2.Reassignment
    offset_checkpoint: _offset_checkpoint_pb2.OffsetCheckpoint
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]] = ..., reassignment: _Optional[_Union[_reassignment_pb2.Reassignment, _Mapping]] = ..., offset_checkpoint: _Optional[_Union[_offset_checkpoint_pb2.OffsetCheckpoint, _Mapping]] = ...) -> None: ...

class GetUpdateTreesResponse(_message.Message):
    __slots__ = ("transaction_tree", "reassignment", "offset_checkpoint")
    TRANSACTION_TREE_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    transaction_tree: _transaction_pb2.TransactionTree
    reassignment: _reassignment_pb2.Reassignment
    offset_checkpoint: _offset_checkpoint_pb2.OffsetCheckpoint
    def __init__(self, transaction_tree: _Optional[_Union[_transaction_pb2.TransactionTree, _Mapping]] = ..., reassignment: _Optional[_Union[_reassignment_pb2.Reassignment, _Mapping]] = ..., offset_checkpoint: _Optional[_Union[_offset_checkpoint_pb2.OffsetCheckpoint, _Mapping]] = ...) -> None: ...

class GetTransactionByEventIdRequest(_message.Message):
    __slots__ = ("event_id", "requesting_parties")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, event_id: _Optional[str] = ..., requesting_parties: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTransactionByIdRequest(_message.Message):
    __slots__ = ("update_id", "requesting_parties")
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, update_id: _Optional[str] = ..., requesting_parties: _Optional[_Iterable[str]] = ...) -> None: ...

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
