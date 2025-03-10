# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReassignmentCommand(_message.Message):
    __slots__ = ("workflow_id", "application_id", "command_id", "submitter", "unassign_command", "assign_command", "submission_id")
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    UNASSIGN_COMMAND_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_COMMAND_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    workflow_id: str
    application_id: str
    command_id: str
    submitter: str
    unassign_command: UnassignCommand
    assign_command: AssignCommand
    submission_id: str
    def __init__(self, workflow_id: _Optional[str] = ..., application_id: _Optional[str] = ..., command_id: _Optional[str] = ..., submitter: _Optional[str] = ..., unassign_command: _Optional[_Union[UnassignCommand, _Mapping]] = ..., assign_command: _Optional[_Union[AssignCommand, _Mapping]] = ..., submission_id: _Optional[str] = ...) -> None: ...

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
