# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TraceContext(_message.Message):
    __slots__ = ["traceparent", "tracestate"]
    TRACEPARENT_FIELD_NUMBER: _ClassVar[int]
    TRACESTATE_FIELD_NUMBER: _ClassVar[int]
    traceparent: _wrappers_pb2.StringValue
    tracestate: _wrappers_pb2.StringValue
    def __init__(self, traceparent: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., tracestate: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
