# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import commands_pb2 as _commands_pb2
from . import reassignment_commands_pb2 as _reassignment_commands_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmitRequest(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _commands_pb2.Commands
    def __init__(self, commands: _Optional[_Union[_commands_pb2.Commands, _Mapping]] = ...) -> None: ...

class SubmitResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubmitReassignmentRequest(_message.Message):
    __slots__ = ("reassignment_commands",)
    REASSIGNMENT_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    reassignment_commands: _reassignment_commands_pb2.ReassignmentCommands
    def __init__(self, reassignment_commands: _Optional[_Union[_reassignment_commands_pb2.ReassignmentCommands, _Mapping]] = ...) -> None: ...

class SubmitReassignmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
