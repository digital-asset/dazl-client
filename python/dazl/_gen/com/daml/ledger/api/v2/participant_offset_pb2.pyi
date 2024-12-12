# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParticipantOffset(_message.Message):
    __slots__ = ("absolute", "boundary")
    class ParticipantBoundary(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTICIPANT_BOUNDARY_BEGIN: _ClassVar[ParticipantOffset.ParticipantBoundary]
        PARTICIPANT_BOUNDARY_END: _ClassVar[ParticipantOffset.ParticipantBoundary]
    PARTICIPANT_BOUNDARY_BEGIN: ParticipantOffset.ParticipantBoundary
    PARTICIPANT_BOUNDARY_END: ParticipantOffset.ParticipantBoundary
    ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    absolute: str
    boundary: ParticipantOffset.ParticipantBoundary
    def __init__(self, absolute: _Optional[str] = ..., boundary: _Optional[_Union[ParticipantOffset.ParticipantBoundary, str]] = ...) -> None: ...
