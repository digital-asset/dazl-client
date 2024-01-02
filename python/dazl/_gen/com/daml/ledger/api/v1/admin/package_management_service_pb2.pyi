# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListKnownPackagesRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ListKnownPackagesResponse(_message.Message):
    __slots__ = ["package_details"]
    PACKAGE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    package_details: _containers.RepeatedCompositeFieldContainer[PackageDetails]
    def __init__(self, package_details: _Optional[_Iterable[_Union[PackageDetails, _Mapping]]] = ...) -> None: ...

class PackageDetails(_message.Message):
    __slots__ = ["package_id", "package_size", "known_since", "source_description"]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    KNOWN_SINCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    package_id: str
    package_size: int
    known_since: _timestamp_pb2.Timestamp
    source_description: str
    def __init__(self, package_id: _Optional[str] = ..., package_size: _Optional[int] = ..., known_since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source_description: _Optional[str] = ...) -> None: ...

class UploadDarFileRequest(_message.Message):
    __slots__ = ["dar_file", "submission_id"]
    DAR_FILE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    dar_file: bytes
    submission_id: str
    def __init__(self, dar_file: _Optional[bytes] = ..., submission_id: _Optional[str] = ...) -> None: ...

class UploadDarFileResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...
