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

from .package_service_pb2 import (
    GetPackageRequest,
    GetPackageResponse,
    GetPackageStatusRequest,
    GetPackageStatusResponse,
    ListPackagesRequest,
    ListPackagesResponse,
)

__all__ = [
    "PackageServiceStub"
]

# noinspection PyPep8Naming
class PackageServiceStub:
    @classmethod
    @overload
    def __new__(cls, channel: __Channel) -> _PackageServiceStub: ...
    @classmethod
    @overload
    def __new__(cls, channel: __AsyncChannel) -> _PackageServiceStub_Async: ...
    def ListPackages(self, __1: ListPackagesRequest) -> __Union[ListPackagesResponse, __Awaitable[ListPackagesResponse]]: ...
    def GetPackage(self, __1: GetPackageRequest) -> __Union[GetPackageRequest, __Awaitable[GetPackageResponse]]: ...
    def GetPackageStatus(self, __1: GetPackageStatusRequest) -> __Union[GetPackageStatusResponse, __Awaitable[GetPackageStatusResponse]]: ...

class _PackageServiceStub(PackageServiceStub):
    def ListPackages(self, __1: ListPackagesRequest) -> ListPackagesResponse: ...
    def GetPackage(self, __1: GetPackageRequest) -> GetPackageResponse: ...
    def GetPackageStatus(self, __1: GetPackageStatusRequest) -> GetPackageStatusResponse: ...

class _PackageServiceStub_Async(PackageServiceStub):
    def ListPackages(self, __1: ListPackagesRequest) -> __Awaitable[ListPackagesResponse]: ...
    def GetPackage(self, __1: GetPackageRequest) -> __Awaitable[GetPackageResponse]: ...
    def GetPackageStatus(self, __1: GetPackageStatusRequest) -> __Awaitable[GetPackageStatusResponse]: ...
