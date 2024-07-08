# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PruneRequest(_message.Message):
    __slots__ = ["prune_up_to", "submission_id", "prune_all_divulged_contracts"]
    PRUNE_UP_TO_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    PRUNE_ALL_DIVULGED_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    prune_up_to: str
    submission_id: str
    prune_all_divulged_contracts: bool
    def __init__(self, prune_up_to: _Optional[str] = ..., submission_id: _Optional[str] = ..., prune_all_divulged_contracts: bool = ...) -> None: ...

class PruneResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...
