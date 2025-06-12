# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from ..v0 import sequencing_pb2 as _sequencing_pb2
from . import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferInView(_message.Message):
    __slots__ = ("salt", "submitter", "contract", "transfer_out_result_event", "creating_transaction_id", "source_protocol_version")
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
