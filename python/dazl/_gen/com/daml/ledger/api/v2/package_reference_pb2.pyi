# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PackageReference(_message.Message):
    __slots__ = ("package_id", "package_name", "package_version")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    package_name: str
    package_version: str
    def __init__(self, package_id: _Optional[str] = ..., package_name: _Optional[str] = ..., package_version: _Optional[str] = ...) -> None: ...
