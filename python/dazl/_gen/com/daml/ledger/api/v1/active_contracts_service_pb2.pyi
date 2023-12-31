# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import event_pb2 as _event_pb2
from . import transaction_filter_pb2 as _transaction_filter_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetActiveContractsRequest(_message.Message):
    __slots__ = ["ledger_id", "filter", "verbose", "active_at_offset"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_AT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    filter: _transaction_filter_pb2.TransactionFilter
    verbose: bool
    active_at_offset: str
    def __init__(self, ledger_id: _Optional[str] = ..., filter: _Optional[_Union[_transaction_filter_pb2.TransactionFilter, _Mapping]] = ..., verbose: bool = ..., active_at_offset: _Optional[str] = ...) -> None: ...

class GetActiveContractsResponse(_message.Message):
    __slots__ = ["offset", "workflow_id", "active_contracts"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    offset: str
    workflow_id: str
    active_contracts: _containers.RepeatedCompositeFieldContainer[_event_pb2.CreatedEvent]
    def __init__(self, offset: _Optional[str] = ..., workflow_id: _Optional[str] = ..., active_contracts: _Optional[_Iterable[_Union[_event_pb2.CreatedEvent, _Mapping]]] = ...) -> None: ...
