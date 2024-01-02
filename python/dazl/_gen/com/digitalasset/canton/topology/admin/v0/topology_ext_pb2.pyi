# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TopologyTransactions(_message.Message):
    __slots__ = ["items"]
    class Item(_message.Message):
        __slots__ = ["sequenced", "valid_from", "valid_until", "transaction"]
        SEQUENCED_FIELD_NUMBER: _ClassVar[int]
        VALID_FROM_FIELD_NUMBER: _ClassVar[int]
        VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_FIELD_NUMBER: _ClassVar[int]
        sequenced: _timestamp_pb2.Timestamp
        valid_from: _timestamp_pb2.Timestamp
        valid_until: _timestamp_pb2.Timestamp
        transaction: bytes
        def __init__(self, sequenced: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., transaction: _Optional[bytes] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TopologyTransactions.Item]
    def __init__(self, items: _Optional[_Iterable[_Union[TopologyTransactions.Item, _Mapping]]] = ...) -> None: ...
