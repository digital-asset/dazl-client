# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendRequest(_message.Message):
    __slots__ = ("tag", "payload")
    TAG_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    tag: str
    payload: bytes
    def __init__(self, tag: _Optional[str] = ..., payload: _Optional[bytes] = ...) -> None: ...

class SendResponse(_message.Message):
    __slots__ = ("rejection_reason",)
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    rejection_reason: str
    def __init__(self, rejection_reason: _Optional[str] = ...) -> None: ...

class ReadOrderedRequest(_message.Message):
    __slots__ = ("start_height",)
    START_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    start_height: int
    def __init__(self, start_height: _Optional[int] = ...) -> None: ...

class ReadOrderedResponse(_message.Message):
    __slots__ = ("height", "block")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    height: int
    block: _containers.RepeatedCompositeFieldContainer[Ordered]
    def __init__(self, height: _Optional[int] = ..., block: _Optional[_Iterable[_Union[Ordered, _Mapping]]] = ...) -> None: ...

class Ordered(_message.Message):
    __slots__ = ("tag", "payload")
    TAG_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    tag: str
    payload: bytes
    def __init__(self, tag: _Optional[str] = ..., payload: _Optional[bytes] = ...) -> None: ...
