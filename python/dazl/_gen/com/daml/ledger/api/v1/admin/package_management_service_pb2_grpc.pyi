# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

from typing import (
    AsyncIterable as __AsyncStream,
    Awaitable as __Awaitable,
    Iterable as __Stream,
    Union as __Union,
    overload,
)

from grpc import Channel as __Channel
from grpc.aio import Channel as __AsyncChannel

from .package_management_service_pb2 import (
    ListKnownPackagesRequest,
    ListKnownPackagesResponse,
    UploadDarFileRequest,
    UploadDarFileResponse,
)

__all__ = [
    "PackageManagementServiceStub",
]

class PackageManagementServiceStub:
    @classmethod
    @overload
    def __new__(cls, channel: __Channel) -> _PackageManagementServiceStub: ...
    @classmethod
    @overload
    def __new__(cls, channel: __AsyncChannel) -> _PackageManagementServiceStub_Async: ...
    def ListKnownPackages(self, __1: ListKnownPackagesRequest) -> __Union[ListKnownPackagesResponse, __Awaitable[ListKnownPackagesResponse]]: ...
    def UploadDarFile(self, __1: UploadDarFileRequest) -> __Union[UploadDarFileResponse, __Awaitable[UploadDarFileResponse]]: ...

class _PackageManagementServiceStub(PackageManagementServiceStub):
    def ListKnownPackages(self, __1: ListKnownPackagesRequest) -> ListKnownPackagesResponse: ...
    def UploadDarFile(self, __1: UploadDarFileRequest) -> UploadDarFileResponse: ...

class _PackageManagementServiceStub_Async(PackageManagementServiceStub):
    def ListKnownPackages(self, __1: ListKnownPackagesRequest) -> __Awaitable[ListKnownPackagesResponse]: ...
    def UploadDarFile(self, __1: UploadDarFileRequest) -> __Awaitable[UploadDarFileResponse]: ...
