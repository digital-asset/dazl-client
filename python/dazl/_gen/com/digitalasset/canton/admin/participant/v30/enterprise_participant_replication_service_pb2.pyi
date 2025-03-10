# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPassive(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Response(_message.Message):
        __slots__ = ("became_passive",)
        BECAME_PASSIVE_FIELD_NUMBER: _ClassVar[int]
        became_passive: bool
        def __init__(self, became_passive: bool = ...) -> None: ...
    def __init__(self) -> None: ...
