# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import topology_pb2 as _topology_pb2
from . import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitIdRequest(_message.Message):
    __slots__ = ("identifier", "namespace", "namespace_delegations")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_DELEGATIONS_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    namespace: str
    namespace_delegations: _containers.RepeatedCompositeFieldContainer[_topology_pb2.SignedTopologyTransaction]
    def __init__(self, identifier: _Optional[str] = ..., namespace: _Optional[str] = ..., namespace_delegations: _Optional[_Iterable[_Union[_topology_pb2.SignedTopologyTransaction, _Mapping]]] = ...) -> None: ...

class InitIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetIdResponse(_message.Message):
    __slots__ = ("initialized", "unique_identifier")
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    initialized: bool
    unique_identifier: str
    def __init__(self, initialized: bool = ..., unique_identifier: _Optional[str] = ...) -> None: ...

class GetOnboardingTransactionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetOnboardingTransactionsResponse(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _common_pb2.TopologyTransactions
    def __init__(self, transactions: _Optional[_Union[_common_pb2.TopologyTransactions, _Mapping]] = ...) -> None: ...

class GetIdRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CurrentTimeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CurrentTimeResponse(_message.Message):
    __slots__ = ("current_time",)
    CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
    current_time: int
    def __init__(self, current_time: _Optional[int] = ...) -> None: ...
