# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.message import Message as _Message

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "ExperimentalFeatures",
    "ExperimentalSelfServiceErrorCodes",
]


class ExperimentalFeatures(_Message):
    @property
    def self_service_error_codes(self) -> ExperimentalSelfServiceErrorCodes: ...
    def __init__(self, *, self_service_error_codes: _typing.Optional[ExperimentalSelfServiceErrorCodes] = ...): ...
    def HasField(self, field_name: _L["self_service_error_codes"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["self_service_error_codes"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExperimentalSelfServiceErrorCodes(_Message):
    def __init__(self): ...
    def HasField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def ClearField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
