# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message
from google.protobuf.timestamp_pb2 import Timestamp

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "ContractMetadata",
]


class ContractMetadata(_Message):
    @property
    def created_at(self) -> Timestamp: ...
    contract_key_hash: _builtins.bytes
    driver_metadata: _builtins.bytes
    def __init__(self, *, created_at: _typing.Optional[Timestamp] = ..., contract_key_hash: _typing.Optional[_builtins.bytes] = ..., driver_metadata: _typing.Optional[_builtins.bytes] = ...): ...
    def HasField(self, field_name: _L["created_at", "contract_key_hash", "driver_metadata"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["created_at", "contract_key_hash", "driver_metadata"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
