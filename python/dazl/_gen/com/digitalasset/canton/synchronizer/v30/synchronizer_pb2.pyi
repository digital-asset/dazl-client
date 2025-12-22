# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SynchronizerPredecessor(_message.Message):
    __slots__ = ("predecessor_physical_id", "upgrade_time")
    PREDECESSOR_PHYSICAL_ID_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_TIME_FIELD_NUMBER: _ClassVar[int]
    predecessor_physical_id: str
    upgrade_time: _timestamp_pb2.Timestamp
    def __init__(self, predecessor_physical_id: _Optional[str] = ..., upgrade_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
