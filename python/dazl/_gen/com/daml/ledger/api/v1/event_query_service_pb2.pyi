# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import event_pb2 as _event_pb2
from . import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEventsByContractIdRequest(_message.Message):
    __slots__ = ["contract_id", "requesting_parties"]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contract_id: _Optional[str] = ..., requesting_parties: _Optional[_Iterable[str]] = ...) -> None: ...

class GetEventsByContractIdResponse(_message.Message):
    __slots__ = ["create_event", "archive_event"]
    CREATE_EVENT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_EVENT_FIELD_NUMBER: _ClassVar[int]
    create_event: _event_pb2.CreatedEvent
    archive_event: _event_pb2.ArchivedEvent
    def __init__(self, create_event: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ..., archive_event: _Optional[_Union[_event_pb2.ArchivedEvent, _Mapping]] = ...) -> None: ...

class GetEventsByContractKeyRequest(_message.Message):
    __slots__ = ["contract_key", "template_id", "requesting_parties", "continuation_token"]
    CONTRACT_KEY_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    contract_key: _value_pb2.Value
    template_id: _value_pb2.Identifier
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    continuation_token: str
    def __init__(self, contract_key: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., requesting_parties: _Optional[_Iterable[str]] = ..., continuation_token: _Optional[str] = ...) -> None: ...

class GetEventsByContractKeyResponse(_message.Message):
    __slots__ = ["create_event", "archive_event", "continuation_token"]
    CREATE_EVENT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_EVENT_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    create_event: _event_pb2.CreatedEvent
    archive_event: _event_pb2.ArchivedEvent
    continuation_token: str
    def __init__(self, create_event: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ..., archive_event: _Optional[_Union[_event_pb2.ArchivedEvent, _Mapping]] = ..., continuation_token: _Optional[str] = ...) -> None: ...
