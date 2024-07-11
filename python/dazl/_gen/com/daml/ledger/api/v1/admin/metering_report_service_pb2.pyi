# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMeteringReportRequest(_message.Message):
    __slots__ = ["to", "application_id"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    application_id: str
    def __init__(self, to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., application_id: _Optional[str] = ..., **kwargs) -> None: ...

class GetMeteringReportResponse(_message.Message):
    __slots__ = ["request", "report_generation_time", "metering_report_json"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    REPORT_GENERATION_TIME_FIELD_NUMBER: _ClassVar[int]
    METERING_REPORT_JSON_FIELD_NUMBER: _ClassVar[int]
    request: GetMeteringReportRequest
    report_generation_time: _timestamp_pb2.Timestamp
    metering_report_json: _struct_pb2.Struct
    def __init__(self, request: _Optional[_Union[GetMeteringReportRequest, _Mapping]] = ..., report_generation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metering_report_json: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
