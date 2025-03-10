# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentalFeatures(_message.Message):
    __slots__ = ("static_time", "command_inspection_service", "interactive_submission_service")
    STATIC_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_INSPECTION_SERVICE_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVE_SUBMISSION_SERVICE_FIELD_NUMBER: _ClassVar[int]
    static_time: ExperimentalStaticTime
    command_inspection_service: ExperimentalCommandInspectionService
    interactive_submission_service: ExperimentalInteractiveSubmissionService
    def __init__(self, static_time: _Optional[_Union[ExperimentalStaticTime, _Mapping]] = ..., command_inspection_service: _Optional[_Union[ExperimentalCommandInspectionService, _Mapping]] = ..., interactive_submission_service: _Optional[_Union[ExperimentalInteractiveSubmissionService, _Mapping]] = ...) -> None: ...

class ExperimentalStaticTime(_message.Message):
    __slots__ = ("supported",)
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...

class ExperimentalCommandInspectionService(_message.Message):
    __slots__ = ("supported",)
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...

class ExperimentalInteractiveSubmissionService(_message.Message):
    __slots__ = ("supported",)
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...
