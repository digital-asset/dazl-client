# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from .. import commands_pb2 as _commands_pb2
from .. import completion_pb2 as _completion_pb2
from .. import value_pb2 as _value_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMAND_STATE_UNSPECIFIED: _ClassVar[CommandState]
    COMMAND_STATE_PENDING: _ClassVar[CommandState]
    COMMAND_STATE_SUCCEEDED: _ClassVar[CommandState]
    COMMAND_STATE_FAILED: _ClassVar[CommandState]
COMMAND_STATE_UNSPECIFIED: CommandState
COMMAND_STATE_PENDING: CommandState
COMMAND_STATE_SUCCEEDED: CommandState
COMMAND_STATE_FAILED: CommandState

class GetCommandStatusRequest(_message.Message):
    __slots__ = ("command_id_prefix", "state", "limit")
    COMMAND_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    command_id_prefix: str
    state: CommandState
    limit: int
    def __init__(self, command_id_prefix: _Optional[str] = ..., state: _Optional[_Union[CommandState, str]] = ..., limit: _Optional[int] = ...) -> None: ...

class GetCommandStatusResponse(_message.Message):
    __slots__ = ("command_status",)
    COMMAND_STATUS_FIELD_NUMBER: _ClassVar[int]
    command_status: _containers.RepeatedCompositeFieldContainer[CommandStatus]
    def __init__(self, command_status: _Optional[_Iterable[_Union[CommandStatus, _Mapping]]] = ...) -> None: ...

class CommandStatus(_message.Message):
    __slots__ = ("started", "completed", "completion", "state", "commands", "request_statistics", "updates")
    STARTED_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    started: _timestamp_pb2.Timestamp
    completed: _timestamp_pb2.Timestamp
    completion: _completion_pb2.Completion
    state: CommandState
    commands: _containers.RepeatedCompositeFieldContainer[_commands_pb2.Command]
    request_statistics: RequestStatistics
    updates: CommandUpdates
    def __init__(self, started: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completion: _Optional[_Union[_completion_pb2.Completion, _Mapping]] = ..., state: _Optional[_Union[CommandState, str]] = ..., commands: _Optional[_Iterable[_Union[_commands_pb2.Command, _Mapping]]] = ..., request_statistics: _Optional[_Union[RequestStatistics, _Mapping]] = ..., updates: _Optional[_Union[CommandUpdates, _Mapping]] = ...) -> None: ...

class RequestStatistics(_message.Message):
    __slots__ = ("envelopes", "request_size", "recipients")
    ENVELOPES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SIZE_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    envelopes: int
    request_size: int
    recipients: int
    def __init__(self, envelopes: _Optional[int] = ..., request_size: _Optional[int] = ..., recipients: _Optional[int] = ...) -> None: ...

class CommandUpdates(_message.Message):
    __slots__ = ("created", "archived", "exercised", "fetched", "looked_up_by_key")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    EXERCISED_FIELD_NUMBER: _ClassVar[int]
    FETCHED_FIELD_NUMBER: _ClassVar[int]
    LOOKED_UP_BY_KEY_FIELD_NUMBER: _ClassVar[int]
    created: _containers.RepeatedCompositeFieldContainer[Contract]
    archived: _containers.RepeatedCompositeFieldContainer[Contract]
    exercised: int
    fetched: int
    looked_up_by_key: int
    def __init__(self, created: _Optional[_Iterable[_Union[Contract, _Mapping]]] = ..., archived: _Optional[_Iterable[_Union[Contract, _Mapping]]] = ..., exercised: _Optional[int] = ..., fetched: _Optional[int] = ..., looked_up_by_key: _Optional[int] = ...) -> None: ...

class Contract(_message.Message):
    __slots__ = ("template_id", "contract_id", "contract_key")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_KEY_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    contract_id: str
    contract_key: _value_pb2.Value
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., contract_id: _Optional[str] = ..., contract_key: _Optional[_Union[_value_pb2.Value, _Mapping]] = ...) -> None: ...
