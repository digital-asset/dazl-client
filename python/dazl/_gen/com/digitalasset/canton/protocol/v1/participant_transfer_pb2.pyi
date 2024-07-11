# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from ..v0 import sequencing_pb2 as _sequencing_pb2
from . import common_pb2 as _common_pb2
from . import merkle_pb2 as _merkle_pb2
from ...time.v0 import time_proof_pb2 as _time_proof_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferOutCommonData(_message.Message):
    __slots__ = ["salt", "source_domain", "stakeholders", "admin_parties", "uuid", "source_mediator", "source_protocol_version"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_PARTIES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    source_domain: str
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    admin_parties: _containers.RepeatedScalarFieldContainer[str]
    uuid: str
    source_mediator: str
    source_protocol_version: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., source_domain: _Optional[str] = ..., stakeholders: _Optional[_Iterable[str]] = ..., admin_parties: _Optional[_Iterable[str]] = ..., uuid: _Optional[str] = ..., source_mediator: _Optional[str] = ..., source_protocol_version: _Optional[int] = ...) -> None: ...

class TransferViewTree(_message.Message):
    __slots__ = ["common_data", "participant_data"]
    COMMON_DATA_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_DATA_FIELD_NUMBER: _ClassVar[int]
    common_data: _merkle_pb2.BlindableNode
    participant_data: _merkle_pb2.BlindableNode
    def __init__(self, common_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ..., participant_data: _Optional[_Union[_merkle_pb2.BlindableNode, _Mapping]] = ...) -> None: ...

class TransferInMediatorMessage(_message.Message):
    __slots__ = ["tree"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: TransferViewTree
    def __init__(self, tree: _Optional[_Union[TransferViewTree, _Mapping]] = ...) -> None: ...

class TransferOutMediatorMessage(_message.Message):
    __slots__ = ["tree"]
    TREE_FIELD_NUMBER: _ClassVar[int]
    tree: TransferViewTree
    def __init__(self, tree: _Optional[_Union[TransferViewTree, _Mapping]] = ...) -> None: ...

class TransferOutView(_message.Message):
    __slots__ = ["salt", "submitter", "contract_id", "target_domain", "target_time_proof", "target_protocol_version"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIME_PROOF_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    submitter: str
    contract_id: str
    target_domain: str
    target_time_proof: _time_proof_pb2.TimeProof
    target_protocol_version: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., submitter: _Optional[str] = ..., contract_id: _Optional[str] = ..., target_domain: _Optional[str] = ..., target_time_proof: _Optional[_Union[_time_proof_pb2.TimeProof, _Mapping]] = ..., target_protocol_version: _Optional[int] = ...) -> None: ...

class TransferInCommonData(_message.Message):
    __slots__ = ["salt", "target_domain", "stakeholders", "uuid", "target_mediator", "target_protocol_version"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    STAKEHOLDERS_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    TARGET_MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    target_domain: str
    stakeholders: _containers.RepeatedScalarFieldContainer[str]
    uuid: str
    target_mediator: str
    target_protocol_version: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., target_domain: _Optional[str] = ..., stakeholders: _Optional[_Iterable[str]] = ..., uuid: _Optional[str] = ..., target_mediator: _Optional[str] = ..., target_protocol_version: _Optional[int] = ...) -> None: ...

class TransferInView(_message.Message):
    __slots__ = ["salt", "submitter", "contract", "transfer_out_result_event", "creating_transaction_id", "source_protocol_version"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OUT_RESULT_EVENT_FIELD_NUMBER: _ClassVar[int]
    CREATING_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    submitter: str
    contract: _common_pb2.SerializableContract
    transfer_out_result_event: _sequencing_pb2.SignedContent
    creating_transaction_id: bytes
    source_protocol_version: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., submitter: _Optional[str] = ..., contract: _Optional[_Union[_common_pb2.SerializableContract, _Mapping]] = ..., transfer_out_result_event: _Optional[_Union[_sequencing_pb2.SignedContent, _Mapping]] = ..., creating_transaction_id: _Optional[bytes] = ..., source_protocol_version: _Optional[int] = ...) -> None: ...
