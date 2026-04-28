# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import event_pb2 as _event_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetContractRequest(_message.Message):
    __slots__ = ("contract_id", "querying_parties")
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    QUERYING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    querying_parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contract_id: _Optional[str] = ..., querying_parties: _Optional[_Iterable[str]] = ...) -> None: ...

class GetContractResponse(_message.Message):
    __slots__ = ("created_event",)
    CREATED_EVENT_FIELD_NUMBER: _ClassVar[int]
    created_event: _event_pb2.CreatedEvent
    def __init__(self, created_event: _Optional[_Union[_event_pb2.CreatedEvent, _Mapping]] = ...) -> None: ...
