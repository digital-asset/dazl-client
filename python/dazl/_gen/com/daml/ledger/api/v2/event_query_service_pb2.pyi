# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import event_pb2 as _event_pb2
from . import transaction_filter_pb2 as _transaction_filter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEventsByContractIdRequest(_message.Message):
    __slots__ = ("contract_id", "requesting_parties", "event_format")
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    EVENT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    event_format: _transaction_filter_pb2.EventFormat
    def __init__(self, contract_id: _Optional[str] = ..., requesting_parties: _Optional[_Iterable[str]] = ..., event_format: _Optional[_Union[_transaction_filter_pb2.EventFormat, _Mapping]] = ...) -> None: ...

class GetEventsByContractIdResponse(_message.Message):
    __slots__ = ("created", "archived")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    created: Created
    archived: Archived
    def __init__(self, created: _Optional[_Union[Created, _Mapping]] = ..., archived: _Optional[_Union[Archived, _Mapping]] = ...) -> None: ...

class Created(_message.Message):
    __slots__ = ("created_event", "synchronizer_id")
    CREATED_EVENT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    created_event: _event_pb2.CreatedEvent
    synchronizer_id: str
    def __init__(self, created_event: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...

class Archived(_message.Message):
    __slots__ = ("archived_event", "synchronizer_id")
    ARCHIVED_EVENT_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    archived_event: _event_pb2.ArchivedEvent
    synchronizer_id: str
    def __init__(self, archived_event: _Optional[_Union[_event_pb2.ArchivedEvent, _Mapping]] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...
