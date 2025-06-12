# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PACKAGE_STATUS_UNSPECIFIED: _ClassVar[PackageStatus]
    PACKAGE_STATUS_REGISTERED: _ClassVar[PackageStatus]

class HashFunction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HASH_FUNCTION_SHA256: _ClassVar[HashFunction]
PACKAGE_STATUS_UNSPECIFIED: PackageStatus
PACKAGE_STATUS_REGISTERED: PackageStatus
HASH_FUNCTION_SHA256: HashFunction

class ListPackagesResponse(_message.Message):
    __slots__ = ("package_ids",)
    PACKAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    package_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, package_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetPackageResponse(_message.Message):
    __slots__ = ("hash_function", "archive_payload", "hash")
    HASH_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash_function: HashFunction
    archive_payload: bytes
    hash: str
    def __init__(self, hash_function: _Optional[_Union[HashFunction, str]] = ..., archive_payload: _Optional[bytes] = ..., hash: _Optional[str] = ...) -> None: ...

class GetPackageStatusResponse(_message.Message):
    __slots__ = ("package_status",)
    PACKAGE_STATUS_FIELD_NUMBER: _ClassVar[int]
    package_status: PackageStatus
    def __init__(self, package_status: _Optional[_Union[PackageStatus, str]] = ...) -> None: ...

class ListPackagesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPackageRequest(_message.Message):
    __slots__ = ("package_id",)
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    def __init__(self, package_id: _Optional[str] = ...) -> None: ...

class GetPackageStatusRequest(_message.Message):
    __slots__ = ("package_id",)
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    def __init__(self, package_id: _Optional[str] = ...) -> None: ...
