# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

import typing as _typing

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
    @_typing.overload
    def __new__(cls, channel: __Channel) -> _PackageManagementServiceStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __AsyncChannel) -> _PackageManagementServiceStub_Async: ...
    def ListKnownPackages(self, __1: ListKnownPackagesRequest) -> _typing.Union[ListKnownPackagesResponse, _typing.Awaitable[ListKnownPackagesResponse]]: ...
    def UploadDarFile(self, __1: UploadDarFileRequest) -> _typing.Union[UploadDarFileResponse, _typing.Awaitable[UploadDarFileResponse]]: ...

class _PackageManagementServiceStub(PackageManagementServiceStub):
    def ListKnownPackages(self, __1: ListKnownPackagesRequest) -> ListKnownPackagesResponse: ...
    def UploadDarFile(self, __1: UploadDarFileRequest) -> UploadDarFileResponse: ...

class _PackageManagementServiceStub_Async(PackageManagementServiceStub):
    def ListKnownPackages(self, __1: ListKnownPackagesRequest) -> _typing.Awaitable[ListKnownPackagesResponse]: ...
    def UploadDarFile(self, __1: UploadDarFileRequest) -> _typing.Awaitable[UploadDarFileResponse]: ...
