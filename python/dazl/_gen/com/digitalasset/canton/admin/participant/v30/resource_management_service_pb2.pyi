# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceLimits(_message.Message):
    __slots__ = ("max_inflight_validation_requests", "max_submission_rate", "max_submission_burst_factor")
    MAX_INFLIGHT_VALIDATION_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    MAX_SUBMISSION_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_SUBMISSION_BURST_FACTOR_FIELD_NUMBER: _ClassVar[int]
    max_inflight_validation_requests: int
    max_submission_rate: int
    max_submission_burst_factor: float
    def __init__(self, max_inflight_validation_requests: _Optional[int] = ..., max_submission_rate: _Optional[int] = ..., max_submission_burst_factor: _Optional[float] = ...) -> None: ...
