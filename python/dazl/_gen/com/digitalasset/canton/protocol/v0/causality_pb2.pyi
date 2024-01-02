# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import participant_transfer_pb2 as _participant_transfer_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CausalityMessage(_message.Message):
    __slots__ = ["target_domain_id", "transfer_id", "clock"]
    TARGET_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    target_domain_id: str
    transfer_id: _participant_transfer_pb2.TransferId
    clock: VectorClock
    def __init__(self, target_domain_id: _Optional[str] = ..., transfer_id: _Optional[_Union[_participant_transfer_pb2.TransferId, _Mapping]] = ..., clock: _Optional[_Union[VectorClock, _Mapping]] = ...) -> None: ...

class VectorClock(_message.Message):
    __slots__ = ["origin_domain_id", "local_ts", "party_id", "clock"]
    class ClockEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _timestamp_pb2.Timestamp
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ORIGIN_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_TS_FIELD_NUMBER: _ClassVar[int]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    origin_domain_id: str
    local_ts: _timestamp_pb2.Timestamp
    party_id: str
    clock: _containers.MessageMap[str, _timestamp_pb2.Timestamp]
    def __init__(self, origin_domain_id: _Optional[str] = ..., local_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., party_id: _Optional[str] = ..., clock: _Optional[_Mapping[str, _timestamp_pb2.Timestamp]] = ...) -> None: ...

class CausalityUpdate(_message.Message):
    __slots__ = ["informeeStakeholders", "ts", "domain_id", "request_counter", "transactionUpdate", "transferOutUpdate", "transferInUpdate"]
    INFORMEESTAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_COUNTER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONUPDATE_FIELD_NUMBER: _ClassVar[int]
    TRANSFEROUTUPDATE_FIELD_NUMBER: _ClassVar[int]
    TRANSFERINUPDATE_FIELD_NUMBER: _ClassVar[int]
    informeeStakeholders: _containers.RepeatedScalarFieldContainer[str]
    ts: _timestamp_pb2.Timestamp
    domain_id: str
    request_counter: int
    transactionUpdate: TransactionUpdate
    transferOutUpdate: TransferOutUpdate
    transferInUpdate: TransferInUpdate
    def __init__(self, informeeStakeholders: _Optional[_Iterable[str]] = ..., ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., domain_id: _Optional[str] = ..., request_counter: _Optional[int] = ..., transactionUpdate: _Optional[_Union[TransactionUpdate, _Mapping]] = ..., transferOutUpdate: _Optional[_Union[TransferOutUpdate, _Mapping]] = ..., transferInUpdate: _Optional[_Union[TransferInUpdate, _Mapping]] = ...) -> None: ...

class TransactionUpdate(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class TransferOutUpdate(_message.Message):
    __slots__ = ["transfer_id"]
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: _participant_transfer_pb2.TransferId
    def __init__(self, transfer_id: _Optional[_Union[_participant_transfer_pb2.TransferId, _Mapping]] = ...) -> None: ...

class TransferInUpdate(_message.Message):
    __slots__ = ["transfer_id"]
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: _participant_transfer_pb2.TransferId
    def __init__(self, transfer_id: _Optional[_Union[_participant_transfer_pb2.TransferId, _Mapping]] = ...) -> None: ...
