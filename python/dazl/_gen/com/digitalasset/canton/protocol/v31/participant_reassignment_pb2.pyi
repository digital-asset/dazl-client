# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from ..v30 import participant_reassignment_pb2 as _participant_reassignment_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnassignmentView(_message.Message):
    __slots__ = ("salt", "target_physical_synchronizer_id", "target_timestamp", "contracts")
    SALT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    target_physical_synchronizer_id: str
    target_timestamp: int
    contracts: _containers.RepeatedCompositeFieldContainer[ActiveContract]
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., target_physical_synchronizer_id: _Optional[str] = ..., target_timestamp: _Optional[int] = ..., contracts: _Optional[_Iterable[_Union[ActiveContract, _Mapping]]] = ...) -> None: ...

class UnassignmentData(_message.Message):
    __slots__ = ("submitter_metadata", "contracts", "reassigning_participant_uids", "source_physical_synchronizer_id", "target_physical_synchronizer_id", "target_timestamp", "unassignment_ts")
    SUBMITTER_METADATA_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    REASSIGNING_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNMENT_TS_FIELD_NUMBER: _ClassVar[int]
    submitter_metadata: _participant_reassignment_pb2.ReassignmentSubmitterMetadata
    contracts: _containers.RepeatedCompositeFieldContainer[ActiveContract]
    reassigning_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    source_physical_synchronizer_id: str
    target_physical_synchronizer_id: str
    target_timestamp: _timestamp_pb2.Timestamp
    unassignment_ts: _timestamp_pb2.Timestamp
    def __init__(self, submitter_metadata: _Optional[_Union[_participant_reassignment_pb2.ReassignmentSubmitterMetadata, _Mapping]] = ..., contracts: _Optional[_Iterable[_Union[ActiveContract, _Mapping]]] = ..., reassigning_participant_uids: _Optional[_Iterable[str]] = ..., source_physical_synchronizer_id: _Optional[str] = ..., target_physical_synchronizer_id: _Optional[str] = ..., target_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., unassignment_ts: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AssignmentView(_message.Message):
    __slots__ = ("salt", "contracts", "reassignment_id")
    SALT_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    contracts: _containers.RepeatedCompositeFieldContainer[ActiveContract]
    reassignment_id: _participant_reassignment_pb2.ReassignmentId
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., contracts: _Optional[_Iterable[_Union[ActiveContract, _Mapping]]] = ..., reassignment_id: _Optional[_Union[_participant_reassignment_pb2.ReassignmentId, _Mapping]] = ...) -> None: ...

class ActiveContract(_message.Message):
    __slots__ = ("contract", "source_validation_package_id", "target_validation_package_id", "reassignment_counter")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VALIDATION_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_VALIDATION_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    contract: bytes
    source_validation_package_id: str
    target_validation_package_id: str
    reassignment_counter: int
    def __init__(self, contract: _Optional[bytes] = ..., source_validation_package_id: _Optional[str] = ..., target_validation_package_id: _Optional[str] = ..., reassignment_counter: _Optional[int] = ...) -> None: ...
