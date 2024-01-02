# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v2 import topology_pb2 as _topology_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizeRequest(_message.Message):
    __slots__ = ["proposal", "transaction_hash", "must_fully_authorize", "force_change", "signed_by"]
    class Proposal(_message.Message):
        __slots__ = ["change", "serial", "mapping"]
        CHANGE_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        MAPPING_FIELD_NUMBER: _ClassVar[int]
        change: _topology_pb2.TopologyChangeOpX
        serial: int
        mapping: _topology_pb2.TopologyMappingX
        def __init__(self, change: _Optional[_Union[_topology_pb2.TopologyChangeOpX, str]] = ..., serial: _Optional[int] = ..., mapping: _Optional[_Union[_topology_pb2.TopologyMappingX, _Mapping]] = ...) -> None: ...
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    MUST_FULLY_AUTHORIZE_FIELD_NUMBER: _ClassVar[int]
    FORCE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    proposal: AuthorizeRequest.Proposal
    transaction_hash: str
    must_fully_authorize: bool
    force_change: bool
    signed_by: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, proposal: _Optional[_Union[AuthorizeRequest.Proposal, _Mapping]] = ..., transaction_hash: _Optional[str] = ..., must_fully_authorize: bool = ..., force_change: bool = ..., signed_by: _Optional[_Iterable[str]] = ...) -> None: ...

class AuthorizeResponse(_message.Message):
    __slots__ = ["transaction"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: _topology_pb2.SignedTopologyTransactionX
    def __init__(self, transaction: _Optional[_Union[_topology_pb2.SignedTopologyTransactionX, _Mapping]] = ...) -> None: ...

class AddTransactionsRequest(_message.Message):
    __slots__ = ["transactions", "force_change"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    FORCE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[_topology_pb2.SignedTopologyTransactionX]
    force_change: bool
    def __init__(self, transactions: _Optional[_Iterable[_Union[_topology_pb2.SignedTopologyTransactionX, _Mapping]]] = ..., force_change: bool = ...) -> None: ...

class AddTransactionsResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...
