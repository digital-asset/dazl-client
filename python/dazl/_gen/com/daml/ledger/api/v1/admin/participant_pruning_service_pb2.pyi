# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

from google.protobuf.message import Message as _Message

__all__ = [
    "PruneRequest",
    "PruneResponse",
]


class PruneRequest(_Message):
    prune_up_to: str
    submission_id: str
    def __init__(self, *, prune_up_to: _typing.Optional[str] = ..., submission_id: _typing.Optional[str] = ...): ...
    def HasField(self, field_name: _typing.Literal["prune_up_to", "submission_id"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["prune_up_to", "submission_id"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class PruneResponse(_Message):
    def __init__(self): ...
    def HasField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def ClearField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
