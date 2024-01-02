# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContractMetadata(_message.Message):
    __slots__ = ["created_at", "contract_key_hash", "driver_metadata"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_KEY_HASH_FIELD_NUMBER: _ClassVar[int]
    DRIVER_METADATA_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    contract_key_hash: bytes
    driver_metadata: bytes
    def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., contract_key_hash: _Optional[bytes] = ..., driver_metadata: _Optional[bytes] = ...) -> None: ...
