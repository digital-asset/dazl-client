# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTimeRequest(_message.Message):
    __slots__ = ["ledger_id"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    def __init__(self, ledger_id: _Optional[str] = ...) -> None: ...

class GetTimeResponse(_message.Message):
    __slots__ = ["current_time"]
    CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
    current_time: _timestamp_pb2.Timestamp
    def __init__(self, current_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SetTimeRequest(_message.Message):
    __slots__ = ["ledger_id", "current_time", "new_time"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
    NEW_TIME_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    current_time: _timestamp_pb2.Timestamp
    new_time: _timestamp_pb2.Timestamp
    def __init__(self, ledger_id: _Optional[str] = ..., current_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., new_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
