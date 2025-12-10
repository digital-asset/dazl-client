# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContractAuthenticationData(_message.Message):
    __slots__ = ("contract_salt", "creating_transaction_id", "relative_argument_suffixes")
    CONTRACT_SALT_FIELD_NUMBER: _ClassVar[int]
    CREATING_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_ARGUMENT_SUFFIXES_FIELD_NUMBER: _ClassVar[int]
    contract_salt: bytes
    creating_transaction_id: bytes
    relative_argument_suffixes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, contract_salt: _Optional[bytes] = ..., creating_transaction_id: _Optional[bytes] = ..., relative_argument_suffixes: _Optional[_Iterable[bytes]] = ...) -> None: ...
