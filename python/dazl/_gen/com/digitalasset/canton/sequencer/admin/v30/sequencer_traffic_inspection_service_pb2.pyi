# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTrafficSummariesRequest(_message.Message):
    __slots__ = ("sequencing_timestamps",)
    SEQUENCING_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    sequencing_timestamps: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, sequencing_timestamps: _Optional[_Iterable[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class GetTrafficSummariesResponse(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: _containers.RepeatedCompositeFieldContainer[TrafficSummary]
    def __init__(self, summary: _Optional[_Iterable[_Union[TrafficSummary, _Mapping]]] = ...) -> None: ...

class TrafficSummary(_message.Message):
    __slots__ = ("sequencing_time", "total_traffic_cost", "envelopes")
    SEQUENCING_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRAFFIC_COST_FIELD_NUMBER: _ClassVar[int]
    ENVELOPES_FIELD_NUMBER: _ClassVar[int]
    sequencing_time: _timestamp_pb2.Timestamp
    total_traffic_cost: int
    envelopes: _containers.RepeatedCompositeFieldContainer[EnvelopeTrafficSummary]
    def __init__(self, sequencing_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_traffic_cost: _Optional[int] = ..., envelopes: _Optional[_Iterable[_Union[EnvelopeTrafficSummary, _Mapping]]] = ...) -> None: ...

class EnvelopeTrafficSummary(_message.Message):
    __slots__ = ("envelope_traffic_cost", "view_hashes")
    ENVELOPE_TRAFFIC_COST_FIELD_NUMBER: _ClassVar[int]
    VIEW_HASHES_FIELD_NUMBER: _ClassVar[int]
    envelope_traffic_cost: int
    view_hashes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, envelope_traffic_cost: _Optional[int] = ..., view_hashes: _Optional[_Iterable[bytes]] = ...) -> None: ...
