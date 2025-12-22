# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackageReference(_message.Message):
    __slots__ = ("package_id", "package_name", "package_version")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    package_name: str
    package_version: str
    def __init__(self, package_id: _Optional[str] = ..., package_name: _Optional[str] = ..., package_version: _Optional[str] = ...) -> None: ...

class VettedPackage(_message.Message):
    __slots__ = ("package_id", "valid_from_inclusive", "valid_until_exclusive", "package_name", "package_version")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    valid_from_inclusive: _timestamp_pb2.Timestamp
    valid_until_exclusive: _timestamp_pb2.Timestamp
    package_name: str
    package_version: str
    def __init__(self, package_id: _Optional[str] = ..., valid_from_inclusive: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., valid_until_exclusive: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., package_name: _Optional[str] = ..., package_version: _Optional[str] = ...) -> None: ...

class VettedPackages(_message.Message):
    __slots__ = ("packages", "participant_id", "synchronizer_id", "topology_serial")
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_SERIAL_FIELD_NUMBER: _ClassVar[int]
    packages: _containers.RepeatedCompositeFieldContainer[VettedPackage]
    participant_id: str
    synchronizer_id: str
    topology_serial: int
    def __init__(self, packages: _Optional[_Iterable[_Union[VettedPackage, _Mapping]]] = ..., participant_id: _Optional[str] = ..., synchronizer_id: _Optional[str] = ..., topology_serial: _Optional[int] = ...) -> None: ...

class PriorTopologySerial(_message.Message):
    __slots__ = ("prior", "no_prior")
    PRIOR_FIELD_NUMBER: _ClassVar[int]
    NO_PRIOR_FIELD_NUMBER: _ClassVar[int]
    prior: int
    no_prior: _empty_pb2.Empty
    def __init__(self, prior: _Optional[int] = ..., no_prior: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...
