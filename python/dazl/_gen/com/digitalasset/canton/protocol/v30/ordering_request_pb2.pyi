# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrderingRequest(_message.Message):
    __slots__ = ("sequencer_uid", "content")
    SEQUENCER_UID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    sequencer_uid: str
    content: bytes
    def __init__(self, sequencer_uid: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...
