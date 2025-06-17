# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
import builtins
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListPackagesRequest(_message.Message):
    __slots__ = ("limit", "filter_name")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
    limit: int
    filter_name: str
    def __init__(self, limit: _Optional[int] = ..., filter_name: _Optional[str] = ...) -> None: ...

class PackageDescription(_message.Message):
    __slots__ = ("package_id", "name", "version", "uploaded_at", "size")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPLOADED_AT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    name: str
    version: str
    uploaded_at: _timestamp_pb2.Timestamp
    size: int
    def __init__(self, package_id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., uploaded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., size: _Optional[int] = ...) -> None: ...

class ListPackagesResponse(_message.Message):
    __slots__ = ("package_descriptions",)
    PACKAGE_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    package_descriptions: _containers.RepeatedCompositeFieldContainer[PackageDescription]
    def __init__(self, package_descriptions: _Optional[_Iterable[_Union[PackageDescription, _Mapping]]] = ...) -> None: ...

class GetPackageContentsRequest(_message.Message):
    __slots__ = ("package_id",)
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    def __init__(self, package_id: _Optional[str] = ...) -> None: ...

class ModuleDescription(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetPackageContentsResponse(_message.Message):
    __slots__ = ("description", "modules", "is_utility_package", "language_version")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    IS_UTILITY_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    description: PackageDescription
    modules: _containers.RepeatedCompositeFieldContainer[ModuleDescription]
    is_utility_package: bool
    language_version: str
    def __init__(self, description: _Optional[_Union[PackageDescription, _Mapping]] = ..., modules: _Optional[_Iterable[_Union[ModuleDescription, _Mapping]]] = ..., is_utility_package: bool = ..., language_version: _Optional[str] = ...) -> None: ...

class GetPackageReferencesRequest(_message.Message):
    __slots__ = ("package_id",)
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    def __init__(self, package_id: _Optional[str] = ...) -> None: ...

class GetPackageReferencesResponse(_message.Message):
    __slots__ = ("dars",)
    DARS_FIELD_NUMBER: _ClassVar[int]
    dars: _containers.RepeatedCompositeFieldContainer[DarDescription]
    def __init__(self, dars: _Optional[_Iterable[_Union[DarDescription, _Mapping]]] = ...) -> None: ...

class RemovePackageRequest(_message.Message):
    __slots__ = ("package_id", "force")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    force: bool
    def __init__(self, package_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class RemovePackageResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: _empty_pb2.Empty
    def __init__(self, success: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...

class ValidateDarRequest(_message.Message):
    __slots__ = ("data", "filename")
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    filename: str
    def __init__(self, data: _Optional[bytes] = ..., filename: _Optional[str] = ...) -> None: ...

class ValidateDarResponse(_message.Message):
    __slots__ = ("main_package_id",)
    MAIN_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    main_package_id: str
    def __init__(self, main_package_id: _Optional[str] = ...) -> None: ...

class UploadDarRequest(_message.Message):
    __slots__ = ("dars", "vet_all_packages", "synchronize_vetting")
    class UploadDarData(_message.Message):
        __slots__ = ("bytes", "description", "expected_main_package_id")
        BYTES_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_MAIN_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
        bytes: builtins.bytes
        description: str
        expected_main_package_id: str
        def __init__(self, bytes: _Optional[builtins.bytes] = ..., description: _Optional[str] = ..., expected_main_package_id: _Optional[str] = ...) -> None: ...
    DARS_FIELD_NUMBER: _ClassVar[int]
    VET_ALL_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZE_VETTING_FIELD_NUMBER: _ClassVar[int]
    dars: _containers.RepeatedCompositeFieldContainer[UploadDarRequest.UploadDarData]
    vet_all_packages: bool
    synchronize_vetting: bool
    def __init__(self, dars: _Optional[_Iterable[_Union[UploadDarRequest.UploadDarData, _Mapping]]] = ..., vet_all_packages: bool = ..., synchronize_vetting: bool = ...) -> None: ...

class UploadDarResponse(_message.Message):
    __slots__ = ("dar_ids",)
    DAR_IDS_FIELD_NUMBER: _ClassVar[int]
    dar_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dar_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class RemoveDarRequest(_message.Message):
    __slots__ = ("main_package_id",)
    MAIN_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    main_package_id: str
    def __init__(self, main_package_id: _Optional[str] = ...) -> None: ...

class RemoveDarResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDarRequest(_message.Message):
    __slots__ = ("main_package_id",)
    MAIN_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    main_package_id: str
    def __init__(self, main_package_id: _Optional[str] = ...) -> None: ...

class DarDescription(_message.Message):
    __slots__ = ("main", "name", "version", "description")
    MAIN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    main: str
    name: str
    version: str
    description: str
    def __init__(self, main: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GetDarResponse(_message.Message):
    __slots__ = ("payload", "data")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    data: DarDescription
    def __init__(self, payload: _Optional[bytes] = ..., data: _Optional[_Union[DarDescription, _Mapping]] = ...) -> None: ...

class ListDarsRequest(_message.Message):
    __slots__ = ("limit", "filter_name")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
    limit: int
    filter_name: str
    def __init__(self, limit: _Optional[int] = ..., filter_name: _Optional[str] = ...) -> None: ...

class ListDarsResponse(_message.Message):
    __slots__ = ("dars",)
    DARS_FIELD_NUMBER: _ClassVar[int]
    dars: _containers.RepeatedCompositeFieldContainer[DarDescription]
    def __init__(self, dars: _Optional[_Iterable[_Union[DarDescription, _Mapping]]] = ...) -> None: ...

class GetDarContentsRequest(_message.Message):
    __slots__ = ("main_package_id",)
    MAIN_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    main_package_id: str
    def __init__(self, main_package_id: _Optional[str] = ...) -> None: ...

class GetDarContentsResponse(_message.Message):
    __slots__ = ("description", "packages")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    description: DarDescription
    packages: _containers.RepeatedCompositeFieldContainer[PackageDescription]
    def __init__(self, description: _Optional[_Union[DarDescription, _Mapping]] = ..., packages: _Optional[_Iterable[_Union[PackageDescription, _Mapping]]] = ...) -> None: ...

class VetDarRequest(_message.Message):
    __slots__ = ("main_package_id", "synchronize")
    MAIN_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZE_FIELD_NUMBER: _ClassVar[int]
    main_package_id: str
    synchronize: bool
    def __init__(self, main_package_id: _Optional[str] = ..., synchronize: bool = ...) -> None: ...

class VetDarResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnvetDarRequest(_message.Message):
    __slots__ = ("main_package_id",)
    MAIN_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    main_package_id: str
    def __init__(self, main_package_id: _Optional[str] = ...) -> None: ...

class UnvetDarResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
