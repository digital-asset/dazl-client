# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetResourceLimitsRequest(_message.Message):
    __slots__ = ("new_limits",)
    NEW_LIMITS_FIELD_NUMBER: _ClassVar[int]
    new_limits: ResourceLimits
    def __init__(self, new_limits: _Optional[_Union[ResourceLimits, _Mapping]] = ...) -> None: ...

class SetResourceLimitsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetResourceLimitsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetResourceLimitsResponse(_message.Message):
    __slots__ = ("current_limits",)
    CURRENT_LIMITS_FIELD_NUMBER: _ClassVar[int]
    current_limits: ResourceLimits
    def __init__(self, current_limits: _Optional[_Union[ResourceLimits, _Mapping]] = ...) -> None: ...

class ResourceLimits(_message.Message):
    __slots__ = ("max_inflight_validation_requests", "max_submission_rate", "max_submission_burst_factor")
    MAX_INFLIGHT_VALIDATION_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    MAX_SUBMISSION_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_SUBMISSION_BURST_FACTOR_FIELD_NUMBER: _ClassVar[int]
    max_inflight_validation_requests: int
    max_submission_rate: int
    max_submission_burst_factor: float
    def __init__(self, max_inflight_validation_requests: _Optional[int] = ..., max_submission_rate: _Optional[int] = ..., max_submission_burst_factor: _Optional[float] = ...) -> None: ...
