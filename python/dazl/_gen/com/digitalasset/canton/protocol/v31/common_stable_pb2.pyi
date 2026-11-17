# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GlobalKey(_message.Message):
    __slots__ = ("template_id", "key", "package_name", "hash")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    template_id: bytes
    key: bytes
    package_name: str
    hash: bytes
    def __init__(self, template_id: _Optional[bytes] = ..., key: _Optional[bytes] = ..., package_name: _Optional[str] = ..., hash: _Optional[bytes] = ...) -> None: ...
