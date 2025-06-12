# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListPackageContentsRequest(_message.Message):
    __slots__ = ("package_id",)
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    def __init__(self, package_id: _Optional[str] = ...) -> None: ...

class ListPackageContentsResponse(_message.Message):
    __slots__ = ("modules",)
    MODULES_FIELD_NUMBER: _ClassVar[int]
    modules: _containers.RepeatedCompositeFieldContainer[ModuleDescription]
    def __init__(self, modules: _Optional[_Iterable[_Union[ModuleDescription, _Mapping]]] = ...) -> None: ...

class ListDarContentsRequest(_message.Message):
    __slots__ = ("dar_id",)
    DAR_ID_FIELD_NUMBER: _ClassVar[int]
    dar_id: str
    def __init__(self, dar_id: _Optional[str] = ...) -> None: ...

class ListDarContentsResponse(_message.Message):
    __slots__ = ("description", "main", "packages", "dependencies")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MAIN_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    description: str
    main: str
    packages: _containers.RepeatedScalarFieldContainer[str]
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, description: _Optional[str] = ..., main: _Optional[str] = ..., packages: _Optional[_Iterable[str]] = ..., dependencies: _Optional[_Iterable[str]] = ...) -> None: ...

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

class VetDarRequest(_message.Message):
    __slots__ = ("dar_hash", "synchronize")
    DAR_HASH_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZE_FIELD_NUMBER: _ClassVar[int]
    dar_hash: str
    synchronize: bool
    def __init__(self, dar_hash: _Optional[str] = ..., synchronize: bool = ...) -> None: ...

class VetDarResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnvetDarRequest(_message.Message):
    __slots__ = ("dar_hash", "synchronize")
    DAR_HASH_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZE_FIELD_NUMBER: _ClassVar[int]
    dar_hash: str
    synchronize: bool
    def __init__(self, dar_hash: _Optional[str] = ..., synchronize: bool = ...) -> None: ...

class UnvetDarResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveDarRequest(_message.Message):
    __slots__ = ("dar_hash",)
    DAR_HASH_FIELD_NUMBER: _ClassVar[int]
    dar_hash: str
    def __init__(self, dar_hash: _Optional[str] = ...) -> None: ...

class RemoveDarResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: _empty_pb2.Empty
    def __init__(self, success: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...

class ModuleDescription(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPackagesRequest(_message.Message):
    __slots__ = ("limit",)
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class ListPackagesResponse(_message.Message):
    __slots__ = ("package_descriptions",)
    PACKAGE_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    package_descriptions: _containers.RepeatedCompositeFieldContainer[PackageDescription]
    def __init__(self, package_descriptions: _Optional[_Iterable[_Union[PackageDescription, _Mapping]]] = ...) -> None: ...

class ListDarsRequest(_message.Message):
    __slots__ = ("limit",)
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    def __init__(self, limit: _Optional[int] = ...) -> None: ...

class ListDarsResponse(_message.Message):
    __slots__ = ("dars",)
    DARS_FIELD_NUMBER: _ClassVar[int]
    dars: _containers.RepeatedCompositeFieldContainer[DarDescription]
    def __init__(self, dars: _Optional[_Iterable[_Union[DarDescription, _Mapping]]] = ...) -> None: ...

class DarDescription(_message.Message):
    __slots__ = ("hash", "name")
    HASH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    hash: str
    name: str
    def __init__(self, hash: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UploadDarRequest(_message.Message):
    __slots__ = ("data", "filename", "vet_all_packages", "synchronize_vetting")
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    VET_ALL_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZE_VETTING_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    filename: str
    vet_all_packages: bool
    synchronize_vetting: bool
    def __init__(self, data: _Optional[bytes] = ..., filename: _Optional[str] = ..., vet_all_packages: bool = ..., synchronize_vetting: bool = ...) -> None: ...

class UploadDarResponse(_message.Message):
    __slots__ = ("success", "failure")
    class Success(_message.Message):
        __slots__ = ("hash",)
        HASH_FIELD_NUMBER: _ClassVar[int]
        hash: str
        def __init__(self, hash: _Optional[str] = ...) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: UploadDarResponse.Success
    failure: UploadDarResponse.Failure
    def __init__(self, success: _Optional[_Union[UploadDarResponse.Success, _Mapping]] = ..., failure: _Optional[_Union[UploadDarResponse.Failure, _Mapping]] = ...) -> None: ...

class ValidateDarRequest(_message.Message):
    __slots__ = ("data", "filename")
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    filename: str
    def __init__(self, data: _Optional[bytes] = ..., filename: _Optional[str] = ...) -> None: ...

class ValidateDarResponse(_message.Message):
    __slots__ = ("hash",)
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class GetDarRequest(_message.Message):
    __slots__ = ("hash",)
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class GetDarResponse(_message.Message):
    __slots__ = ("data", "name")
    DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    name: str
    def __init__(self, data: _Optional[bytes] = ..., name: _Optional[str] = ...) -> None: ...

class PackageDescription(_message.Message):
    __slots__ = ("package_id", "source_description")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    source_description: str
    def __init__(self, package_id: _Optional[str] = ..., source_description: _Optional[str] = ...) -> None: ...
