# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
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
    __slots__ = ("begin_exclusive", "end_inclusive", "update_format", "descending_order")
    BEGIN_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    END_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DESCENDING_ORDER_FIELD_NUMBER: _ClassVar[int]
    begin_exclusive: int
    end_inclusive: int
    update_format: _transaction_filter_pb2.UpdateFormat
    descending_order: bool
    def __init__(self, begin_exclusive: _Optional[int] = ..., end_inclusive: _Optional[int] = ..., update_format: _Optional[_Union[_transaction_filter_pb2.UpdateFormat, _Mapping]] = ..., descending_order: bool = ...) -> None: ...

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

class GetUpdatesPageRequest(_message.Message):
    __slots__ = ("begin_offset_exclusive", "end_offset_inclusive", "max_page_size", "update_format", "descending_order", "page_token")
    BEGIN_OFFSET_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    MAX_PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DESCENDING_ORDER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    begin_offset_exclusive: int
    end_offset_inclusive: int
    max_page_size: int
    update_format: _transaction_filter_pb2.UpdateFormat
    descending_order: bool
    page_token: bytes
    def __init__(self, begin_offset_exclusive: _Optional[int] = ..., end_offset_inclusive: _Optional[int] = ..., max_page_size: _Optional[int] = ..., update_format: _Optional[_Union[_transaction_filter_pb2.UpdateFormat, _Mapping]] = ..., descending_order: bool = ..., page_token: _Optional[bytes] = ...) -> None: ...

class GetUpdatesPageResponse(_message.Message):
    __slots__ = ("updates", "lowest_page_offset_exclusive", "highest_page_offset_inclusive", "next_page_token")
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    LOWEST_PAGE_OFFSET_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_PAGE_OFFSET_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[GetUpdateResponse]
    lowest_page_offset_exclusive: int
    highest_page_offset_inclusive: int
    next_page_token: bytes
    def __init__(self, updates: _Optional[_Iterable[_Union[GetUpdateResponse, _Mapping]]] = ..., lowest_page_offset_exclusive: _Optional[int] = ..., highest_page_offset_inclusive: _Optional[int] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...
