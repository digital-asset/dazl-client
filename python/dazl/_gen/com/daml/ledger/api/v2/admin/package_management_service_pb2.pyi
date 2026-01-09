# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from .. import package_reference_pb2 as _package_reference_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateVettedPackagesForceFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPDATE_VETTED_PACKAGES_FORCE_FLAG_UNSPECIFIED: _ClassVar[UpdateVettedPackagesForceFlag]
    UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_VET_INCOMPATIBLE_UPGRADES: _ClassVar[UpdateVettedPackagesForceFlag]
    UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_UNVETTED_DEPENDENCIES: _ClassVar[UpdateVettedPackagesForceFlag]
UPDATE_VETTED_PACKAGES_FORCE_FLAG_UNSPECIFIED: UpdateVettedPackagesForceFlag
UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_VET_INCOMPATIBLE_UPGRADES: UpdateVettedPackagesForceFlag
UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_UNVETTED_DEPENDENCIES: UpdateVettedPackagesForceFlag

class ListKnownPackagesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListKnownPackagesResponse(_message.Message):
    __slots__ = ("package_details",)
    PACKAGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    package_details: _containers.RepeatedCompositeFieldContainer[PackageDetails]
    def __init__(self, package_details: _Optional[_Iterable[_Union[PackageDetails, _Mapping]]] = ...) -> None: ...

class PackageDetails(_message.Message):
    __slots__ = ("package_id", "package_size", "known_since", "name", "version")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    KNOWN_SINCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    package_size: int
    known_since: _timestamp_pb2.Timestamp
    name: str
    version: str
    def __init__(self, package_id: _Optional[str] = ..., package_size: _Optional[int] = ..., known_since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class UploadDarFileRequest(_message.Message):
    __slots__ = ("dar_file", "submission_id", "vetting_change", "synchronizer_id")
    class VettingChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VETTING_CHANGE_UNSPECIFIED: _ClassVar[UploadDarFileRequest.VettingChange]
        VETTING_CHANGE_VET_ALL_PACKAGES: _ClassVar[UploadDarFileRequest.VettingChange]
        VETTING_CHANGE_DONT_VET_ANY_PACKAGES: _ClassVar[UploadDarFileRequest.VettingChange]
    VETTING_CHANGE_UNSPECIFIED: UploadDarFileRequest.VettingChange
    VETTING_CHANGE_VET_ALL_PACKAGES: UploadDarFileRequest.VettingChange
    VETTING_CHANGE_DONT_VET_ANY_PACKAGES: UploadDarFileRequest.VettingChange
    DAR_FILE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    VETTING_CHANGE_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    dar_file: bytes
    submission_id: str
    vetting_change: UploadDarFileRequest.VettingChange
    synchronizer_id: str
    def __init__(self, dar_file: _Optional[bytes] = ..., submission_id: _Optional[str] = ..., vetting_change: _Optional[_Union[UploadDarFileRequest.VettingChange, str]] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...

class UploadDarFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ValidateDarFileRequest(_message.Message):
    __slots__ = ("dar_file", "submission_id", "synchronizer_id")
    DAR_FILE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    dar_file: bytes
    submission_id: str
    synchronizer_id: str
    def __init__(self, dar_file: _Optional[bytes] = ..., submission_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...

class ValidateDarFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VettedPackagesChange(_message.Message):
    __slots__ = ("vet", "unvet")
    class Unvet(_message.Message):
        __slots__ = ("packages",)
        PACKAGES_FIELD_NUMBER: _ClassVar[int]
        packages: _containers.RepeatedCompositeFieldContainer[VettedPackagesRef]
        def __init__(self, packages: _Optional[_Iterable[_Union[VettedPackagesRef, _Mapping]]] = ...) -> None: ...
    class Vet(_message.Message):
        __slots__ = ("packages", "new_valid_from_inclusive", "new_valid_until_exclusive")
        PACKAGES_FIELD_NUMBER: _ClassVar[int]
        NEW_VALID_FROM_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        NEW_VALID_UNTIL_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        packages: _containers.RepeatedCompositeFieldContainer[VettedPackagesRef]
        new_valid_from_inclusive: _timestamp_pb2.Timestamp
        new_valid_until_exclusive: _timestamp_pb2.Timestamp
        def __init__(self, packages: _Optional[_Iterable[_Union[VettedPackagesRef, _Mapping]]] = ..., new_valid_from_inclusive: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., new_valid_until_exclusive: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    VET_FIELD_NUMBER: _ClassVar[int]
    UNVET_FIELD_NUMBER: _ClassVar[int]
    vet: VettedPackagesChange.Vet
    unvet: VettedPackagesChange.Unvet
    def __init__(self, vet: _Optional[_Union[VettedPackagesChange.Vet, _Mapping]] = ..., unvet: _Optional[_Union[VettedPackagesChange.Unvet, _Mapping]] = ...) -> None: ...

class VettedPackagesRef(_message.Message):
    __slots__ = ("package_id", "package_name", "package_version")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    package_name: str
    package_version: str
    def __init__(self, package_id: _Optional[str] = ..., package_name: _Optional[str] = ..., package_version: _Optional[str] = ...) -> None: ...

class UpdateVettedPackagesRequest(_message.Message):
    __slots__ = ("changes", "dry_run", "synchronizer_id", "expected_topology_serial", "update_vetted_packages_force_flags")
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VETTED_PACKAGES_FORCE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[VettedPackagesChange]
    dry_run: bool
    synchronizer_id: str
    expected_topology_serial: _package_reference_pb2.PriorTopologySerial
    update_vetted_packages_force_flags: _containers.RepeatedScalarFieldContainer[UpdateVettedPackagesForceFlag]
    def __init__(self, changes: _Optional[_Iterable[_Union[VettedPackagesChange, _Mapping]]] = ..., dry_run: bool = ..., synchronizer_id: _Optional[str] = ..., expected_topology_serial: _Optional[_Union[_package_reference_pb2.PriorTopologySerial, _Mapping]] = ..., update_vetted_packages_force_flags: _Optional[_Iterable[_Union[UpdateVettedPackagesForceFlag, str]]] = ...) -> None: ...

class UpdateVettedPackagesResponse(_message.Message):
    __slots__ = ("past_vetted_packages", "new_vetted_packages")
    PAST_VETTED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    NEW_VETTED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    past_vetted_packages: _package_reference_pb2.VettedPackages
    new_vetted_packages: _package_reference_pb2.VettedPackages
    def __init__(self, past_vetted_packages: _Optional[_Union[_package_reference_pb2.VettedPackages, _Mapping]] = ..., new_vetted_packages: _Optional[_Union[_package_reference_pb2.VettedPackages, _Mapping]] = ...) -> None: ...
