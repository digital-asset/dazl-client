# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LedgerOffset(_message.Message):
    __slots__ = ["absolute", "boundary"]
    class LedgerBoundary(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []  # type: ignore
        LEDGER_BEGIN: _ClassVar[LedgerOffset.LedgerBoundary]
        LEDGER_END: _ClassVar[LedgerOffset.LedgerBoundary]
    LEDGER_BEGIN: LedgerOffset.LedgerBoundary
    LEDGER_END: LedgerOffset.LedgerBoundary
    ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
    BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    absolute: str
    boundary: LedgerOffset.LedgerBoundary
    def __init__(self, absolute: _Optional[str] = ..., boundary: _Optional[_Union[LedgerOffset.LedgerBoundary, str]] = ...) -> None: ...
