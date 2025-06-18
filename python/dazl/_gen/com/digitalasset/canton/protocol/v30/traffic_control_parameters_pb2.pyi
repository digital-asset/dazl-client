# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrafficControlParameters(_message.Message):
    __slots__ = ("max_base_traffic_amount", "max_base_traffic_accumulation_duration", "read_vs_write_scaling_factor", "set_balance_request_submission_window_size", "enforce_rate_limiting", "base_event_cost")
    MAX_BASE_TRAFFIC_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_BASE_TRAFFIC_ACCUMULATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    READ_VS_WRITE_SCALING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    SET_BALANCE_REQUEST_SUBMISSION_WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_RATE_LIMITING_FIELD_NUMBER: _ClassVar[int]
    BASE_EVENT_COST_FIELD_NUMBER: _ClassVar[int]
    max_base_traffic_amount: int
    max_base_traffic_accumulation_duration: _duration_pb2.Duration
    read_vs_write_scaling_factor: int
    set_balance_request_submission_window_size: _duration_pb2.Duration
    enforce_rate_limiting: bool
    base_event_cost: int
    def __init__(self, max_base_traffic_amount: _Optional[int] = ..., max_base_traffic_accumulation_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., read_vs_write_scaling_factor: _Optional[int] = ..., set_balance_request_submission_window_size: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., enforce_rate_limiting: bool = ..., base_event_cost: _Optional[int] = ...) -> None: ...

class TrafficReceipt(_message.Message):
    __slots__ = ("consumed_cost", "extra_traffic_consumed", "base_traffic_remainder")
    CONSUMED_COST_FIELD_NUMBER: _ClassVar[int]
    EXTRA_TRAFFIC_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    BASE_TRAFFIC_REMAINDER_FIELD_NUMBER: _ClassVar[int]
    consumed_cost: int
    extra_traffic_consumed: int
    base_traffic_remainder: int
    def __init__(self, consumed_cost: _Optional[int] = ..., extra_traffic_consumed: _Optional[int] = ..., base_traffic_remainder: _Optional[int] = ...) -> None: ...

class TrafficConsumed(_message.Message):
    __slots__ = ("member", "extra_traffic_consumed", "base_traffic_remainder", "last_consumed_cost", "sequencing_timestamp")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_TRAFFIC_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    BASE_TRAFFIC_REMAINDER_FIELD_NUMBER: _ClassVar[int]
    LAST_CONSUMED_COST_FIELD_NUMBER: _ClassVar[int]
    SEQUENCING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    member: str
    extra_traffic_consumed: int
    base_traffic_remainder: int
    last_consumed_cost: int
    sequencing_timestamp: int
    def __init__(self, member: _Optional[str] = ..., extra_traffic_consumed: _Optional[int] = ..., base_traffic_remainder: _Optional[int] = ..., last_consumed_cost: _Optional[int] = ..., sequencing_timestamp: _Optional[int] = ...) -> None: ...

class TrafficPurchased(_message.Message):
    __slots__ = ("member", "serial", "extra_traffic_purchased", "sequencing_timestamp")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    EXTRA_TRAFFIC_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    SEQUENCING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    member: str
    serial: int
    extra_traffic_purchased: int
    sequencing_timestamp: int
    def __init__(self, member: _Optional[str] = ..., serial: _Optional[int] = ..., extra_traffic_purchased: _Optional[int] = ..., sequencing_timestamp: _Optional[int] = ...) -> None: ...

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

class SetTrafficPurchasedMessage(_message.Message):
    __slots__ = ("member", "serial", "total_traffic_purchased", "synchronizer_id")
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRAFFIC_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    member: str
    serial: int
    total_traffic_purchased: int
    synchronizer_id: str
    def __init__(self, member: _Optional[str] = ..., serial: _Optional[int] = ..., total_traffic_purchased: _Optional[int] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...
