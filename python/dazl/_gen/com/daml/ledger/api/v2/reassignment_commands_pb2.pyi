# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReassignmentCommands(_message.Message):
    __slots__ = ("workflow_id", "user_id", "command_id", "submitter", "submission_id", "commands")
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    workflow_id: str
    user_id: str
    command_id: str
    submitter: str
    submission_id: str
    commands: _containers.RepeatedCompositeFieldContainer[ReassignmentCommand]
    def __init__(self, workflow_id: _Optional[str] = ..., user_id: _Optional[str] = ..., command_id: _Optional[str] = ..., submitter: _Optional[str] = ..., submission_id: _Optional[str] = ..., commands: _Optional[_Iterable[_Union[ReassignmentCommand, _Mapping]]] = ...) -> None: ...

class ReassignmentCommand(_message.Message):
    __slots__ = ("unassign_command", "assign_command")
    UNASSIGN_COMMAND_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_COMMAND_FIELD_NUMBER: _ClassVar[int]
    unassign_command: UnassignCommand
    assign_command: AssignCommand
    def __init__(self, unassign_command: _Optional[_Union[UnassignCommand, _Mapping]] = ..., assign_command: _Optional[_Union[AssignCommand, _Mapping]] = ...) -> None: ...

class UnassignCommand(_message.Message):
    __slots__ = ("contract_id", "source", "target")
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    source: str
    target: str
    def __init__(self, contract_id: _Optional[str] = ..., source: _Optional[str] = ..., target: _Optional[str] = ...) -> None: ...

class AssignCommand(_message.Message):
    __slots__ = ("unassign_id", "source", "target")
    UNASSIGN_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    unassign_id: str
    source: str
    target: str
    def __init__(self, unassign_id: _Optional[str] = ..., source: _Optional[str] = ..., target: _Optional[str] = ...) -> None: ...
