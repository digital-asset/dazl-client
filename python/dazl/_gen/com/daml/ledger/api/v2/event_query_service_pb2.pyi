# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import event_pb2 as _event_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEventsByContractIdRequest(_message.Message):
    __slots__ = ("contract_id", "requesting_parties")
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contract_id: _Optional[str] = ..., requesting_parties: _Optional[_Iterable[str]] = ...) -> None: ...

class GetEventsByContractIdResponse(_message.Message):
    __slots__ = ("created", "archived")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    created: Created
    archived: Archived
    def __init__(self, created: _Optional[_Union[Created, _Mapping]] = ..., archived: _Optional[_Union[Archived, _Mapping]] = ...) -> None: ...

class Created(_message.Message):
    __slots__ = ("created_event", "domain_id")
    CREATED_EVENT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    created_event: _event_pb2.CreatedEvent
    domain_id: str
    def __init__(self, created_event: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ..., domain_id: _Optional[str] = ...) -> None: ...

class Archived(_message.Message):
    __slots__ = ("archived_event", "domain_id")
    ARCHIVED_EVENT_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    archived_event: _event_pb2.ArchivedEvent
    domain_id: str
    def __init__(self, archived_event: _Optional[_Union[_event_pb2.ArchivedEvent, _Mapping]] = ..., domain_id: _Optional[str] = ...) -> None: ...
