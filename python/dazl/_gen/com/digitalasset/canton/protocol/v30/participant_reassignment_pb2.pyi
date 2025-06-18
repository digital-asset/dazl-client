# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from . import common_stable_pb2 as _common_stable_pb2
from . import merkle_pb2 as _merkle_pb2
from ...time.v30 import time_proof_pb2 as _time_proof_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReassignmentId(_message.Message):
    __slots__ = ("source_synchronizer_id", "timestamp")
    SOURCE_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    source_synchronizer_id: str
    timestamp: int
    def __init__(self, source_synchronizer_id: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class UnassignmentCommonData(_message.Message):
    __slots__ = ("salt", "source_synchronizer_id", "stakeholders", "reassigning_participant_uids", "uuid", "source_mediator_group", "submitter_metadata")
    SALT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    REASSIGNING_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_METADATA_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    source_synchronizer_id: str
    stakeholders: _common_stable_pb2.Stakeholders
    reassigning_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    uuid: str
    source_mediator_group: int
    submitter_metadata: ReassignmentSubmitterMetadata
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., source_synchronizer_id: _Optional[str] = ..., stakeholders: _Optional[_Union[_common_stable_pb2.Stakeholders, _Mapping]] = ..., reassigning_participant_uids: _Optional[_Iterable[str]] = ..., uuid: _Optional[str] = ..., source_mediator_group: _Optional[int] = ..., submitter_metadata: _Optional[_Union[ReassignmentSubmitterMetadata, _Mapping]] = ...) -> None: ...

class ReassignmentViewTree(_message.Message):
    __slots__ = ("common_data", "participant_data")
    COMMON_DATA_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_DATA_FIELD_NUMBER: _ClassVar[int]
    common_data: bytes
    participant_data: _merkle_pb2.BlindableNode
    def __init__(self, common_data: _Optional[bytes] = ..., participant_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ...) -> None: ...

class AssignmentMediatorMessage(_message.Message):
    __slots__ = ("tree", "submitting_participant_signature")
    TREE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    tree: ReassignmentViewTree
    submitting_participant_signature: _crypto_pb2.Signature
    def __init__(self, tree: _Optional[_Union[ReassignmentViewTree, _Mapping]] = ..., submitting_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class UnassignmentMediatorMessage(_message.Message):
    __slots__ = ("tree", "submitting_participant_signature")
    TREE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    tree: ReassignmentViewTree
    submitting_participant_signature: _crypto_pb2.Signature
    def __init__(self, tree: _Optional[_Union[ReassignmentViewTree, _Mapping]] = ..., submitting_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class AssignmentCommonData(_message.Message):
    __slots__ = ("salt", "target_synchronizer_id", "stakeholders", "uuid", "target_mediator_group", "submitter_metadata", "reassigning_participant_uids")
    SALT_FIELD_NUMBER: _ClassVar[int]
    TARGET_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    TARGET_MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_METADATA_FIELD_NUMBER: _ClassVar[int]
    REASSIGNING_PARTICIPANT_UIDS_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    target_synchronizer_id: str
    stakeholders: _common_stable_pb2.Stakeholders
    uuid: str
    target_mediator_group: int
    submitter_metadata: ReassignmentSubmitterMetadata
    reassigning_participant_uids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., target_synchronizer_id: _Optional[str] = ..., stakeholders: _Optional[_Union[_common_stable_pb2.Stakeholders, _Mapping]] = ..., uuid: _Optional[str] = ..., target_mediator_group: _Optional[int] = ..., submitter_metadata: _Optional[_Union[ReassignmentSubmitterMetadata, _Mapping]] = ..., reassigning_participant_uids: _Optional[_Iterable[str]] = ...) -> None: ...

class ReassignmentSubmitterMetadata(_message.Message):
    __slots__ = ("submitter", "submitting_participant_uid", "command_id", "submission_id", "user_id", "workflow_id")
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    submitter: str
    submitting_participant_uid: str
    command_id: str
    submission_id: str
    user_id: str
    workflow_id: str
    def __init__(self, submitter: _Optional[str] = ..., submitting_participant_uid: _Optional[str] = ..., command_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., user_id: _Optional[str] = ..., workflow_id: _Optional[str] = ...) -> None: ...

class UnassignmentView(_message.Message):
    __slots__ = ("salt", "target_synchronizer_id", "target_time_proof", "target_protocol_version", "reassignment_counter", "contract")
    SALT_FIELD_NUMBER: _ClassVar[int]
    TARGET_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIME_PROOF_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    target_synchronizer_id: str
    target_time_proof: _time_proof_pb2.TimeProof
    target_protocol_version: int
    reassignment_counter: int
    contract: _common_stable_pb2.SerializableContract
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., target_synchronizer_id: _Optional[str] = ..., target_time_proof: _Optional[_Union[_time_proof_pb2.TimeProof, _Mapping]] = ..., target_protocol_version: _Optional[int] = ..., reassignment_counter: _Optional[int] = ..., contract: _Optional[_Union[_common_stable_pb2.SerializableContract, _Mapping]] = ...) -> None: ...

class AssignmentView(_message.Message):
    __slots__ = ("salt", "contract", "unassignment_result_event", "reassignment_counter")
    SALT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNMENT_RESULT_EVENT_FIELD_NUMBER: _ClassVar[int]
    REASSIGNMENT_COUNTER_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    contract: _common_stable_pb2.SerializableContract
    unassignment_result_event: bytes
    reassignment_counter: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., contract: _Optional[_Union[_common_stable_pb2.SerializableContract, _Mapping]] = ..., unassignment_result_event: _Optional[bytes] = ..., reassignment_counter: _Optional[int] = ...) -> None: ...
