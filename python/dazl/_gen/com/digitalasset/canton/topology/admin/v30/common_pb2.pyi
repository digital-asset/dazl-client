# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TopologyTransactions(_message.Message):
    __slots__ = ("items",)
    class Item(_message.Message):
        __slots__ = ("sequenced", "valid_from", "valid_until", "transaction", "rejection_reason")
        SEQUENCED_FIELD_NUMBER: _ClassVar[int]
        VALID_FROM_FIELD_NUMBER: _ClassVar[int]
        VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_FIELD_NUMBER: _ClassVar[int]
        REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
        sequenced: _timestamp_pb2.Timestamp
        valid_from: _timestamp_pb2.Timestamp
        valid_until: _timestamp_pb2.Timestamp
        transaction: bytes
        rejection_reason: str
        def __init__(self, sequenced: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., transaction: _Optional[bytes] = ..., rejection_reason: _Optional[str] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TopologyTransactions.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[TopologyTransactions.Item, _Mapping]]] = ...) -> None: ...

class StoreId(_message.Message):
    __slots__ = ("authorized", "synchronizer", "temporary")
    class Authorized(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Synchronizer(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Temporary(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    authorized: StoreId.Authorized
    synchronizer: StoreId.Synchronizer
    temporary: StoreId.Temporary
    def __init__(self, authorized: _Optional[_Union[StoreId.Authorized, _Mapping]] = ..., synchronizer: _Optional[_Union[StoreId.Synchronizer, _Mapping]] = ..., temporary: _Optional[_Union[StoreId.Temporary, _Mapping]] = ...) -> None: ...
