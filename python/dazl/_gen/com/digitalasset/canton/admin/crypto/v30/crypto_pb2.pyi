# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HmacAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HMAC_ALGORITHM_UNSPECIFIED: _ClassVar[HmacAlgorithm]
    HMAC_ALGORITHM_HMAC_SHA256: _ClassVar[HmacAlgorithm]
HMAC_ALGORITHM_UNSPECIFIED: HmacAlgorithm
HMAC_ALGORITHM_HMAC_SHA256: HmacAlgorithm

class Salt(_message.Message):
    __slots__ = ("hmac", "salt")
    HMAC_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    hmac: HmacAlgorithm
    salt: bytes
    def __init__(self, hmac: _Optional[_Union[HmacAlgorithm, str]] = ..., salt: _Optional[bytes] = ...) -> None: ...
