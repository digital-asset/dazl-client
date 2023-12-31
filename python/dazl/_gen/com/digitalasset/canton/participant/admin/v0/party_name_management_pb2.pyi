# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPartyDisplayNameRequest(_message.Message):
    __slots__ = ["party_id", "display_name"]
    PARTY_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    party_id: str
    display_name: str
    def __init__(self, party_id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class SetPartyDisplayNameResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...
