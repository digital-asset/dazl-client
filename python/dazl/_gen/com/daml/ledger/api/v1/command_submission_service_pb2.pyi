# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import commands_pb2 as _commands_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmitRequest(_message.Message):
    __slots__ = ["commands"]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _commands_pb2.Commands
    def __init__(self, commands: _Optional[_Union[_commands_pb2.Commands, _Mapping]] = ...) -> None: ...
