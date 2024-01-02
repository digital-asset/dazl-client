# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from ..v0 import sequencing_pb2 as _sequencing_pb2
from ..v1 import common_pb2 as _common_pb2
from ...time.v0 import time_proof_pb2 as _time_proof_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferOutView(_message.Message):
    __slots__ = ["salt", "submitter", "contract_id", "template_id", "target_domain", "target_time_proof", "target_protocol_version", "submitting_participant", "application_id", "submission_id", "workflow_id", "command_id", "transfer_counter"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_TIME_PROOF_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_COUNTER_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    submitter: str
    contract_id: str
    template_id: str
    target_domain: str
    target_time_proof: _time_proof_pb2.TimeProof
    target_protocol_version: int
    submitting_participant: str
    application_id: str
    submission_id: str
    workflow_id: str
    command_id: str
    transfer_counter: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., submitter: _Optional[str] = ..., contract_id: _Optional[str] = ..., template_id: _Optional[str] = ..., target_domain: _Optional[str] = ..., target_time_proof: _Optional[_Union[_time_proof_pb2.TimeProof, _Mapping]] = ..., target_protocol_version: _Optional[int] = ..., submitting_participant: _Optional[str] = ..., application_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., command_id: _Optional[str] = ..., transfer_counter: _Optional[int] = ...) -> None: ...

class TransferInView(_message.Message):
    __slots__ = ["salt", "submitter", "contract", "transfer_out_result_event", "creating_transaction_id", "source_protocol_version", "submitting_participant", "application_id", "submission_id", "workflow_id", "command_id", "transfer_counter"]
    SALT_FIELD_NUMBER: _ClassVar[int]
    SUBMITTER_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OUT_RESULT_EVENT_FIELD_NUMBER: _ClassVar[int]
    CREATING_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUBMITTING_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_COUNTER_FIELD_NUMBER: _ClassVar[int]
    salt: _crypto_pb2.Salt
    submitter: str
    contract: _common_pb2.SerializableContract
    transfer_out_result_event: _sequencing_pb2.SignedContent
    creating_transaction_id: bytes
    source_protocol_version: int
    submitting_participant: str
    application_id: str
    submission_id: str
    workflow_id: str
    command_id: str
    transfer_counter: int
    def __init__(self, salt: _Optional[_Union[_crypto_pb2.Salt, _Mapping]] = ..., submitter: _Optional[str] = ..., contract: _Optional[_Union[_common_pb2.SerializableContract, _Mapping]] = ..., transfer_out_result_event: _Optional[_Union[_sequencing_pb2.SignedContent, _Mapping]] = ..., creating_transaction_id: _Optional[bytes] = ..., source_protocol_version: _Optional[int] = ..., submitting_participant: _Optional[str] = ..., application_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., workflow_id: _Optional[str] = ..., command_id: _Optional[str] = ..., transfer_counter: _Optional[int] = ...) -> None: ...
