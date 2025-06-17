# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from .. import value_pb2 as _value_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GlobalKey(_message.Message):
    __slots__ = ("template_id", "package_name", "key", "hash")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    template_id: _value_pb2.Identifier
    package_name: str
    key: _value_pb2.Value
    hash: bytes
    def __init__(self, template_id: _Optional[_Union[_value_pb2.Identifier, _Mapping]] = ..., package_name: _Optional[str] = ..., key: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., hash: _Optional[bytes] = ...) -> None: ...
