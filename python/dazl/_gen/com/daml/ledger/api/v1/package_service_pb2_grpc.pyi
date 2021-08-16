# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off

import typing as _typing

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
    @_typing.overload
    def __new__(cls, channel: __Channel) -> _PackageServiceStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: __AsyncChannel) -> _PackageServiceStub_Async: ...
    def ListPackages(self, __1: ListPackagesRequest) -> _typing.Union[ListPackagesResponse, _typing.Awaitable[ListPackagesResponse]]: ...
    def GetPackage(self, __1: GetPackageRequest) -> _typing.Union[GetPackageRequest, _typing.Awaitable[GetPackageResponse]]: ...
    def GetPackageStatus(self, __1: GetPackageStatusRequest) -> _typing.Union[GetPackageStatusResponse, _typing.Awaitable[GetPackageStatusResponse]]: ...

class _PackageServiceStub(PackageServiceStub):
    def ListPackages(self, __1: ListPackagesRequest) -> ListPackagesResponse: ...
    def GetPackage(self, __1: GetPackageRequest) -> GetPackageResponse: ...
    def GetPackageStatus(self, __1: GetPackageStatusRequest) -> GetPackageStatusResponse: ...

class _PackageServiceStub_Async(PackageServiceStub):
    def ListPackages(self, __1: ListPackagesRequest) -> _typing.Awaitable[ListPackagesResponse]: ...
    def GetPackage(self, __1: GetPackageRequest) -> _typing.Awaitable[GetPackageResponse]: ...
    def GetPackageStatus(self, __1: GetPackageStatusRequest) -> _typing.Awaitable[GetPackageStatusResponse]: ...
