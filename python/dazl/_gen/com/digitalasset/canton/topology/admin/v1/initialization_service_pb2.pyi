# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ....protocol.v0 import topology_ext_pb2 as _topology_ext_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitIdRequest(_message.Message):
    __slots__ = ["unique_identifier"]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    unique_identifier: str
    def __init__(self, unique_identifier: _Optional[str] = ...) -> None: ...

class InitIdResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class GetIdResponse(_message.Message):
    __slots__ = ["initialized", "unique_identifier"]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    initialized: bool
    unique_identifier: str
    def __init__(self, initialized: bool = ..., unique_identifier: _Optional[str] = ...) -> None: ...

class GetOnboardingTransactionsRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class GetOnboardingTransactionsResponse(_message.Message):
    __slots__ = ["transactions"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _topology_ext_pb2.TopologyTransactions
    def __init__(self, transactions: _Optional[_Union[_topology_ext_pb2.TopologyTransactions, _Mapping]] = ...) -> None: ...
