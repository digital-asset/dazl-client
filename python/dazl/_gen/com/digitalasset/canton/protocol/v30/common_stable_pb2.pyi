# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GlobalKey(_message.Message):
    __slots__ = ("template_id", "key", "package_name")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    template_id: bytes
    key: bytes
    package_name: str
    def __init__(self, template_id: _Optional[bytes] = ..., key: _Optional[bytes] = ..., package_name: _Optional[str] = ...) -> None: ...

class AggregationRule(_message.Message):
    __slots__ = ("eligible_members", "threshold")
    ELIGIBLE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    eligible_members: _containers.RepeatedScalarFieldContainer[str]
    threshold: int
    def __init__(self, eligible_members: _Optional[_Iterable[str]] = ..., threshold: _Optional[int] = ...) -> None: ...

class Stakeholders(_message.Message):
    __slots__ = ("all", "signatories")
    ALL_FIELD_NUMBER: _ClassVar[int]
    SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    all: _containers.RepeatedScalarFieldContainer[str]
    signatories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, all: _Optional[_Iterable[str]] = ..., signatories: _Optional[_Iterable[str]] = ...) -> None: ...
