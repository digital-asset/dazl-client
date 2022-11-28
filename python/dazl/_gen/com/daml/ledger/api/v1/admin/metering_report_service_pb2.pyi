# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message
from google.protobuf.struct_pb2 import Struct
from google.protobuf.timestamp_pb2 import Timestamp

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "GetMeteringReportRequest",
    "GetMeteringReportResponse",
]


class GetMeteringReportRequest(_Message):
    @property
    def to(self) -> Timestamp: ...
    application_id: _builtins.str
    def __init__(self, *, to: _typing.Optional[Timestamp] = ..., application_id: _typing.Optional[_builtins.str] = ...): ...
    def HasField(self, field_name: _L["from", "to", "application_id"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["from", "to", "application_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetMeteringReportResponse(_Message):
    @property
    def request(self) -> GetMeteringReportRequest: ...
    @property
    def report_generation_time(self) -> Timestamp: ...
    @property
    def metering_report_json(self) -> Struct: ...
    def __init__(self, *, request: _typing.Optional[GetMeteringReportRequest] = ..., report_generation_time: _typing.Optional[Timestamp] = ..., metering_report_json: _typing.Optional[Struct] = ...): ...
    def HasField(self, field_name: _L["request", "report_generation_time", "metering_report_json"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["request", "report_generation_time", "metering_report_json"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
