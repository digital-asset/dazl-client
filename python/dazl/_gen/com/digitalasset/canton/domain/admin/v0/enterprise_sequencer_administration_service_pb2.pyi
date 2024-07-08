# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import sequencer_initialization_snapshot_pb2 as _sequencer_initialization_snapshot_pb2
from ....pruning.admin.v0 import pruning_pb2 as _pruning_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EthereumAccount(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class LedgerIdentity(_message.Message):
    __slots__ = ["ethereum_account"]
    class AuthorizeRequest(_message.Message):
        __slots__ = ["identify"]
        IDENTIFY_FIELD_NUMBER: _ClassVar[int]
        identify: LedgerIdentity
        def __init__(self, identify: _Optional[_Union[LedgerIdentity, _Mapping]] = ...) -> None: ...
    class AuthorizeResponse(_message.Message):
        __slots__ = ["success", "failure"]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        success: LedgerIdentity.Success
        failure: LedgerIdentity.Failure
        def __init__(self, success: _Optional[_Union[LedgerIdentity.Success, _Mapping]] = ..., failure: _Optional[_Union[LedgerIdentity.Failure, _Mapping]] = ...) -> None: ...
    class Success(_message.Message):
        __slots__ = []  # type: ignore
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ["reason"]
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    ETHEREUM_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ethereum_account: EthereumAccount
    def __init__(self, ethereum_account: _Optional[_Union[EthereumAccount, _Mapping]] = ...) -> None: ...

class Pruning(_message.Message):
    __slots__ = []  # type: ignore
    class Request(_message.Message):
        __slots__ = ["timestamp"]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["details"]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        details: str
        def __init__(self, details: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class Snapshot(_message.Message):
    __slots__ = []  # type: ignore
    class Request(_message.Message):
        __slots__ = ["timestamp"]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["success", "failure", "versionedSuccess"]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        VERSIONEDSUCCESS_FIELD_NUMBER: _ClassVar[int]
        success: Snapshot.Success
        failure: Snapshot.Failure
        versionedSuccess: Snapshot.VersionedSuccess
        def __init__(self, success: _Optional[_Union[Snapshot.Success, _Mapping]] = ..., failure: _Optional[_Union[Snapshot.Failure, _Mapping]] = ..., versionedSuccess: _Optional[_Union[Snapshot.VersionedSuccess, _Mapping]] = ...) -> None: ...
    class Success(_message.Message):
        __slots__ = ["state"]
        STATE_FIELD_NUMBER: _ClassVar[int]
        state: _sequencer_initialization_snapshot_pb2.SequencerSnapshot
        def __init__(self, state: _Optional[_Union[_sequencer_initialization_snapshot_pb2.SequencerSnapshot, _Mapping]] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ["reason"]
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    class VersionedSuccess(_message.Message):
        __slots__ = ["snapshot"]
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        snapshot: bytes
        def __init__(self, snapshot: _Optional[bytes] = ...) -> None: ...
    def __init__(self) -> None: ...

class DisableMemberRequest(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: str
    def __init__(self, member: _Optional[str] = ...) -> None: ...
