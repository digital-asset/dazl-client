# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import daml_lf_1_pb2 as _daml_lf_1_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HashFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    SHA256: _ClassVar[HashFunction]
SHA256: HashFunction

class ArchivePayload(_message.Message):
    __slots__ = ["minor", "daml_lf_1"]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    DAML_LF_1_FIELD_NUMBER: _ClassVar[int]
    minor: str
    daml_lf_1: _daml_lf_1_pb2.Package
    def __init__(self, minor: _Optional[str] = ..., daml_lf_1: _Optional[_Union[_daml_lf_1_pb2.Package, _Mapping]] = ...) -> None: ...

class Archive(_message.Message):
    __slots__ = ["hash_function", "payload", "hash"]
    HASH_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash_function: HashFunction
    payload: bytes
    hash: str
    def __init__(self, hash_function: _Optional[_Union[HashFunction, str]] = ..., payload: _Optional[bytes] = ..., hash: _Optional[str] = ...) -> None: ...
