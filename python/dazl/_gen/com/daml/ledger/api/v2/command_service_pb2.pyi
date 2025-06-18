# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import commands_pb2 as _commands_pb2
from . import reassignment_pb2 as _reassignment_pb2
from . import reassignment_commands_pb2 as _reassignment_commands_pb2
from . import transaction_pb2 as _transaction_pb2
from . import transaction_filter_pb2 as _transaction_filter_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmitAndWaitRequest(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _commands_pb2.Commands
    def __init__(self, commands: _Optional[_Union[_commands_pb2.Commands, _Mapping]] = ...) -> None: ...

class SubmitAndWaitForTransactionRequest(_message.Message):
    __slots__ = ("commands", "transaction_format")
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FORMAT_FIELD_NUMBER: _ClassVar[int]
    commands: _commands_pb2.Commands
    transaction_format: _transaction_filter_pb2.TransactionFormat
    def __init__(self, commands: _Optional[_Union[_commands_pb2.Commands, _Mapping]] = ..., transaction_format: _Optional[_Union[_transaction_filter_pb2.TransactionFormat, _Mapping]] = ...) -> None: ...

class SubmitAndWaitResponse(_message.Message):
    __slots__ = ("update_id", "completion_offset")
    UPDATE_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_OFFSET_FIELD_NUMBER: _ClassVar[int]
    update_id: str
    completion_offset: int
    def __init__(self, update_id: _Optional[str] = ..., completion_offset: _Optional[int] = ...) -> None: ...

class SubmitAndWaitForTransactionResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.Transaction
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]] = ...) -> None: ...

class SubmitAndWaitForTransactionTreeResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.TransactionTree
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.TransactionTree, _Mapping]] = ...) -> None: ...

class SubmitAndWaitForReassignmentRequest(_message.Message):
    __slots__ = ("reassignment_commands", "event_format")
    REASSIGNMENT_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    EVENT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    reassignment_commands: _reassignment_commands_pb2.ReassignmentCommands
    event_format: _transaction_filter_pb2.EventFormat
    def __init__(self, reassignment_commands: _Optional[_Union[_reassignment_commands_pb2.ReassignmentCommands, _Mapping]] = ..., event_format: _Optional[_Union[_transaction_filter_pb2.EventFormat, _Mapping]] = ...) -> None: ...

class SubmitAndWaitForReassignmentResponse(_message.Message):
    __slots__ = ("reassignment",)
    REASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    reassignment: _reassignment_pb2.Reassignment
    def __init__(self, reassignment: _Optional[_Union[_reassignment_pb2.Reassignment, _Mapping]] = ...) -> None: ...
