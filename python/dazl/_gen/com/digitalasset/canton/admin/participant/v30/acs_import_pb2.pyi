# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContractImportMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTRACT_IMPORT_MODE_UNSPECIFIED: _ClassVar[ContractImportMode]
    CONTRACT_IMPORT_MODE_ACCEPT: _ClassVar[ContractImportMode]
    CONTRACT_IMPORT_MODE_VALIDATION: _ClassVar[ContractImportMode]
    CONTRACT_IMPORT_MODE_RECOMPUTATION: _ClassVar[ContractImportMode]
CONTRACT_IMPORT_MODE_UNSPECIFIED: ContractImportMode
CONTRACT_IMPORT_MODE_ACCEPT: ContractImportMode
CONTRACT_IMPORT_MODE_VALIDATION: ContractImportMode
CONTRACT_IMPORT_MODE_RECOMPUTATION: ContractImportMode

class RepresentativePackageIdOverride(_message.Message):
    __slots__ = ("contract_override", "package_id_override", "package_name_override")
    class ContractOverrideEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PackageIdOverrideEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PackageNameOverrideEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONTRACT_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    contract_override: _containers.ScalarMap[str, str]
    package_id_override: _containers.ScalarMap[str, str]
    package_name_override: _containers.ScalarMap[str, str]
    def __init__(self, contract_override: _Optional[_Mapping[str, str]] = ..., package_id_override: _Optional[_Mapping[str, str]] = ..., package_name_override: _Optional[_Mapping[str, str]] = ...) -> None: ...
