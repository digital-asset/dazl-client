# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import package_reference_pb2 as _package_reference_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
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

class PackageMetadataFilter(_message.Message):
    __slots__ = ("package_ids", "package_name_prefixes")
    PACKAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    package_ids: _containers.RepeatedScalarFieldContainer[str]
    package_name_prefixes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, package_ids: _Optional[_Iterable[str]] = ..., package_name_prefixes: _Optional[_Iterable[str]] = ...) -> None: ...

class TopologyStateFilter(_message.Message):
    __slots__ = ("participant_ids", "synchronizer_ids")
    PARTICIPANT_IDS_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_IDS_FIELD_NUMBER: _ClassVar[int]
    participant_ids: _containers.RepeatedScalarFieldContainer[str]
    synchronizer_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, participant_ids: _Optional[_Iterable[str]] = ..., synchronizer_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListVettedPackagesRequest(_message.Message):
    __slots__ = ("package_metadata_filter", "topology_state_filter", "page_token", "page_size")
    PACKAGE_METADATA_FILTER_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_STATE_FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    package_metadata_filter: PackageMetadataFilter
    topology_state_filter: TopologyStateFilter
    page_token: str
    page_size: int
    def __init__(self, package_metadata_filter: _Optional[_Union[PackageMetadataFilter, _Mapping]] = ..., topology_state_filter: _Optional[_Union[TopologyStateFilter, _Mapping]] = ..., page_token: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListVettedPackagesResponse(_message.Message):
    __slots__ = ("vetted_packages", "next_page_token")
    VETTED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    vetted_packages: _containers.RepeatedCompositeFieldContainer[_package_reference_pb2.VettedPackages]
    next_page_token: str
    def __init__(self, vetted_packages: _Optional[_Iterable[_Union[_package_reference_pb2.VettedPackages, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
