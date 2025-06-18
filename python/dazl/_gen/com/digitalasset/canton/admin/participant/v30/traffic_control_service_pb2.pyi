# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrafficControlStateRequest(_message.Message):
    __slots__ = ("synchronizer_id",)
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    def __init__(self, synchronizer_id: _Optional[str] = ...) -> None: ...

class TrafficControlStateResponse(_message.Message):
    __slots__ = ("traffic_state",)
    TRAFFIC_STATE_FIELD_NUMBER: _ClassVar[int]
    traffic_state: TrafficState
    def __init__(self, traffic_state: _Optional[_Union[TrafficState, _Mapping]] = ...) -> None: ...

class TrafficState(_message.Message):
    __slots__ = ("extra_traffic_purchased", "extra_traffic_consumed", "base_traffic_remainder", "last_consumed_cost", "timestamp", "serial")
    EXTRA_TRAFFIC_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    EXTRA_TRAFFIC_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    BASE_TRAFFIC_REMAINDER_FIELD_NUMBER: _ClassVar[int]
    LAST_CONSUMED_COST_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    extra_traffic_purchased: int
    extra_traffic_consumed: int
    base_traffic_remainder: int
    last_consumed_cost: int
    timestamp: int
    serial: int
    def __init__(self, extra_traffic_purchased: _Optional[int] = ..., extra_traffic_consumed: _Optional[int] = ..., base_traffic_remainder: _Optional[int] = ..., last_consumed_cost: _Optional[int] = ..., timestamp: _Optional[int] = ..., serial: _Optional[int] = ...) -> None: ...
