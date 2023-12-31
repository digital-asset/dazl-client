# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from . import common_pb2 as _common_pb2
from . import merkle_pb2 as _merkle_pb2
from . import sequencing_pb2 as _sequencing_pb2
from ...time.v0 import time_proof_pb2 as _time_proof_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferId(_message.Message):
    __slots__ = ["origin_domain", "timestamp"]
    ORIGIN_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    origin_domain: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, origin_domain: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TransferOutMediatorMessage(_message.Message):
    __slots__ = ["tree"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: TransferViewTree
    def __init__(self, tree: _Optional[_Union[TransferViewTree, _Mapping]] = ...) -> None: ...

class TransferInMediatorMessage(_message.Message):
    __slots__ = ["tree"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: TransferViewTree
    def __init__(self, tree: _Optional[_Union[TransferViewTree, _Mapping]] = ...) -> None: ...

class TransferViewTree(_message.Message):
    __slots__ = ["common_data", "participant_data"]
    COMMON_DATA_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_DATA_FIELD_NUMBER: _ClassVar[int]
    common_data: _merkle_pb2.BlindableNode
    participant_data: _merkle_pb2.BlindableNode
    def __init__(self, common_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ..., participant_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ...) -> None: ...

class TransferOutCommonData(_message.Message):
    __slots__ = ["salt", "origin_domain", "stakeholders", "admin_parties", "uuid", "origin_mediator"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_PARTIES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    origin_domain: str
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    admin_parties: _containers.RepeatedScalarFieldContainer[str]
    uuid: str
    origin_mediator: str
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., origin_domain: _Optional[str] = ..., stakeholders: _Optional[_Iterable[str]] = ..., admin_parties: _Optional[_Iterable[str]] = ..., uuid: _Optional[str] = ..., origin_mediator: _Optional[str] = ...) -> None: ...

class TransferOutView(_message.Message):
    __slots__ = ["salt", "submitter", "contract_id", "target_domain", "target_time_proof"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIME_PROOF_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    submitter: str
    contract_id: str
    target_domain: str
    target_time_proof: _time_proof_pb2.TimeProof
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., submitter: _Optional[str] = ..., contract_id: _Optional[str] = ..., target_domain: _Optional[str] = ..., target_time_proof: _Optional[_Union[_time_proof_pb2.TimeProof, _Mapping]] = ...) -> None: ...

class TransferInCommonData(_message.Message):
    __slots__ = ["salt", "target_domain", "stakeholders", "uuid", "target_mediator"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    TARGET_MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    target_domain: str
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    uuid: str
    target_mediator: str
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., target_domain: _Optional[str] = ..., stakeholders: _Optional[_Iterable[str]] = ..., uuid: _Optional[str] = ..., target_mediator: _Optional[str] = ...) -> None: ...

class TransferInView(_message.Message):
    __slots__ = ["salt", "submitter", "contract", "transfer_out_result_event", "creating_transaction_id"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OUT_RESULT_EVENT_FIELD_NUMBER: _ClassVar[int]
    CREATING_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    submitter: str
    contract: _common_pb2.SerializableContract
    transfer_out_result_event: _sequencing_pb2.SignedContent
    creating_transaction_id: bytes
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., submitter: _Optional[str] = ..., contract: _Optional[_Union[_common_pb2.SerializableContract, _Mapping]] = ..., transfer_out_result_event: _Optional[_Union[_sequencing_pb2.SignedContent, _Mapping]] = ..., creating_transaction_id: _Optional[bytes] = ...) -> None: ...
