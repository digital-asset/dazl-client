# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LookupContractDomain(_message.Message):
    __slots__ = []  # type: ignore
    class Request(_message.Message):
        __slots__ = ["contract_id"]
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        contract_id: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, contract_id: _Optional[_Iterable[str]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["results"]
        class ResultsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        RESULTS_FIELD_NUMBER: _ClassVar[int]
        results: _containers.ScalarMap[str, str]
        def __init__(self, results: _Optional[_Mapping[str, str]] = ...) -> None: ...
    def __init__(self) -> None: ...

class LookupTransactionDomain(_message.Message):
    __slots__ = []  # type: ignore
    class Request(_message.Message):
        __slots__ = ["transaction_id"]
        TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        transaction_id: str
        def __init__(self, transaction_id: _Optional[str] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["domain_id"]
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        domain_id: str
        def __init__(self, domain_id: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class LookupOffsetByTime(_message.Message):
    __slots__ = []  # type: ignore
    class Request(_message.Message):
        __slots__ = ["timestamp"]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["offset"]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: str
        def __init__(self, offset: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class LookupOffsetByIndex(_message.Message):
    __slots__ = []  # type: ignore
    class Request(_message.Message):
        __slots__ = ["index"]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        index: int
        def __init__(self, index: _Optional[int] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["offset"]
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: str
        def __init__(self, offset: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
