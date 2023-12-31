# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import ledger_offset_pb2 as _ledger_offset_pb2
from . import transaction_filter_pb2 as _transaction_filter_pb2
from . import transaction_pb2 as _transaction_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTransactionsRequest(_message.Message):
    __slots__ = ["ledger_id", "begin", "end", "filter", "verbose"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    begin: _ledger_offset_pb2.LedgerOffset
    end: _ledger_offset_pb2.LedgerOffset
    filter: _transaction_filter_pb2.TransactionFilter
    verbose: bool
    def __init__(self, ledger_id: _Optional[str] = ..., begin: _Optional[_Union[_ledger_offset_pb2.LedgerOffset, _Mapping]] = ..., end: _Optional[_Union[_ledger_offset_pb2.LedgerOffset, _Mapping]] = ..., filter: _Optional[_Union[_transaction_filter_pb2.TransactionFilter, _Mapping]] = ..., verbose: bool = ...) -> None: ...

class GetTransactionsResponse(_message.Message):
    __slots__ = ["transactions"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_transaction_pb2.Transaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[_transaction_pb2.Transaction, _Mapping]]] = ...) -> None: ...

class GetTransactionTreesResponse(_message.Message):
    __slots__ = ["transactions"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_transaction_pb2.TransactionTree]
    def __init__(self, transactions: _Optional[_Iterable[_Union[_transaction_pb2.TransactionTree, _Mapping]]] = ...) -> None: ...

class GetTransactionByEventIdRequest(_message.Message):
    __slots__ = ["ledger_id", "event_id", "requesting_parties"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    event_id: str
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ledger_id: _Optional[str] = ..., event_id: _Optional[str] = ..., requesting_parties: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTransactionByIdRequest(_message.Message):
    __slots__ = ["ledger_id", "transaction_id", "requesting_parties"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_PARTIES_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    transaction_id: str
    requesting_parties: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ledger_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., requesting_parties: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTransactionResponse(_message.Message):
    __slots__ = ["transaction"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.TransactionTree
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.TransactionTree, _Mapping]] = ...) -> None: ...

class GetFlatTransactionResponse(_message.Message):
    __slots__ = ["transaction"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _transaction_pb2.Transaction
    def __init__(self, transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]] = ...) -> None: ...

class GetLedgerEndRequest(_message.Message):
    __slots__ = ["ledger_id"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    def __init__(self, ledger_id: _Optional[str] = ...) -> None: ...

class GetLedgerEndResponse(_message.Message):
    __slots__ = ["offset"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: _ledger_offset_pb2.LedgerOffset
    def __init__(self, offset: _Optional[_Union[_ledger_offset_pb2.LedgerOffset, _Mapping]] = ...) -> None: ...

class GetLatestPrunedOffsetsRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class GetLatestPrunedOffsetsResponse(_message.Message):
    __slots__ = ["participant_pruned_up_to_inclusive", "all_divulged_contracts_pruned_up_to_inclusive"]
    PARTICIPANT_PRUNED_UP_TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    ALL_DIVULGED_CONTRACTS_PRUNED_UP_TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    participant_pruned_up_to_inclusive: _ledger_offset_pb2.LedgerOffset
    all_divulged_contracts_pruned_up_to_inclusive: _ledger_offset_pb2.LedgerOffset
    def __init__(self, participant_pruned_up_to_inclusive: _Optional[_Union[_ledger_offset_pb2.LedgerOffset, _Mapping]] = ..., all_divulged_contracts_pruned_up_to_inclusive: _Optional[_Union[_ledger_offset_pb2.LedgerOffset, _Mapping]] = ...) -> None: ...
