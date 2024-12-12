# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
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
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferId(_message.Message):
    __slots__ = ("source_domain", "timestamp")
    SOURCE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    source_domain: str
    timestamp: int
    def __init__(self, source_domain: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class TransferOutCommonData(_message.Message):
    __slots__ = ("salt", "source_domain", "stakeholders", "admin_parties", "uuid", "source_mediator_group", "submitter_metadata")
    SALT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_PARTIES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_METADATA_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    source_domain: str
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    admin_parties: _containers.RepeatedScalarFieldContainer[str]
    uuid: str
    source_mediator_group: int
    submitter_metadata: TransferSubmitterMetadata
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., source_domain: _Optional[str] = ..., stakeholders: _Optional[_Iterable[str]] = ..., admin_parties: _Optional[_Iterable[str]] = ..., uuid: _Optional[str] = ..., source_mediator_group: _Optional[int] = ..., submitter_metadata: _Optional[_Union[TransferSubmitterMetadata, _Mapping]] = ...) -> None: ...

class TransferViewTree(_message.Message):
    __slots__ = ("common_data", "participant_data")
    COMMON_DATA_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_DATA_FIELD_NUMBER: _ClassVar[int]
    common_data: bytes
    participant_data: _merkle_pb2.BlindableNode
    def __init__(self, common_data: _Optional[bytes] = ..., participant_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ...) -> None: ...

class TransferInMediatorMessage(_message.Message):
    __slots__ = ("tree", "submitting_participant_signature")
    TREE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    tree: TransferViewTree
    submitting_participant_signature: _crypto_pb2.Signature
    def __init__(self, tree: _Optional[_Union[TransferViewTree, _Mapping]] = ..., submitting_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class TransferOutMediatorMessage(_message.Message):
    __slots__ = ("tree", "submitting_participant_signature")
    TREE_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    tree: TransferViewTree
    submitting_participant_signature: _crypto_pb2.Signature
    def __init__(self, tree: _Optional[_Union[TransferViewTree, _Mapping]] = ..., submitting_participant_signature: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ...) -> None: ...

class TransferInCommonData(_message.Message):
    __slots__ = ("salt", "target_domain", "stakeholders", "uuid", "target_mediator_group", "submitter_metadata")
    SALT_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    TARGET_MEDIATOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_METADATA_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    target_domain: str
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    uuid: str
    target_mediator_group: int
    submitter_metadata: TransferSubmitterMetadata
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., target_domain: _Optional[str] = ..., stakeholders: _Optional[_Iterable[str]] = ..., uuid: _Optional[str] = ..., target_mediator_group: _Optional[int] = ..., submitter_metadata: _Optional[_Union[TransferSubmitterMetadata, _Mapping]] = ...) -> None: ...

class TransferSubmitterMetadata(_message.Message):
    __slots__ = ("submitter", "submitting_participant_uid", "command_id", "submission_id", "application_id", "workflow_id")
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_UID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    submitter: str
    submitting_participant_uid: str
    command_id: str
    submission_id: str
    application_id: str
    workflow_id: str
    def __init__(self, submitter: _Optional[str] = ..., submitting_participant_uid: _Optional[str] = ..., command_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., application_id: _Optional[str] = ..., workflow_id: _Optional[str] = ...) -> None: ...

class TransferOutView(_message.Message):
    __slots__ = ("salt", "target_domain", "target_time_proof", "target_protocol_version", "transfer_counter", "creating_transaction_id", "contract")
    SALT_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIME_PROOF_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_COUNTER_FIELD_NUMBER: _ClassVar[int]
    CREATING_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    target_domain: str
    target_time_proof: _time_proof_pb2.TimeProof
    target_protocol_version: int
    transfer_counter: int
    creating_transaction_id: bytes
    contract: _common_stable_pb2.SerializableContract
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., target_domain: _Optional[str] = ..., target_time_proof: _Optional[_Union[_time_proof_pb2.TimeProof, _Mapping]] = ..., target_protocol_version: _Optional[int] = ..., transfer_counter: _Optional[int] = ..., creating_transaction_id: _Optional[bytes] = ..., contract: _Optional[_Union[_common_stable_pb2.SerializableContract, _Mapping]] = ...) -> None: ...

class TransferInView(_message.Message):
    __slots__ = ("salt", "contract", "transfer_out_result_event", "creating_transaction_id", "source_protocol_version", "transfer_counter")
    SALT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OUT_RESULT_EVENT_FIELD_NUMBER: _ClassVar[int]
    CREATING_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_COUNTER_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    contract: _common_stable_pb2.SerializableContract
    transfer_out_result_event: bytes
    creating_transaction_id: bytes
    source_protocol_version: int
    transfer_counter: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., contract: _Optional[_Union[_common_stable_pb2.SerializableContract, _Mapping]] = ..., transfer_out_result_event: _Optional[bytes] = ..., creating_transaction_id: _Optional[bytes] = ..., source_protocol_version: _Optional[int] = ..., transfer_counter: _Optional[int] = ...) -> None: ...
