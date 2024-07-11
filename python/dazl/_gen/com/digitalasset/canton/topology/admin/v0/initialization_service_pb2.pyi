# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InitIdRequest(_message.Message):
    __slots__ = ["identifier", "fingerprint", "instance"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    fingerprint: str
    instance: str
    def __init__(self, identifier: _Optional[str] = ..., fingerprint: _Optional[str] = ..., instance: _Optional[str] = ...) -> None: ...

class InitIdResponse(_message.Message):
    __slots__ = ["unique_identifier", "instance"]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    unique_identifier: str
    instance: str
    def __init__(self, unique_identifier: _Optional[str] = ..., instance: _Optional[str] = ...) -> None: ...

class GetIdResponse(_message.Message):
    __slots__ = ["initialized", "unique_identifier", "instance"]
    INITIALIZED_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    initialized: bool
    unique_identifier: str
    instance: str
    def __init__(self, initialized: bool = ..., unique_identifier: _Optional[str] = ..., instance: _Optional[str] = ...) -> None: ...
