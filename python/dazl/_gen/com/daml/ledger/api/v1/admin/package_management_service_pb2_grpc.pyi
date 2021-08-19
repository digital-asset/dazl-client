# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .package_management_service_pb2 import ListKnownPackagesRequest, ListKnownPackagesResponse, UploadDarFileRequest, UploadDarFileResponse

__all__ = [
    "PackageManagementServiceStub",
]

_T = _typing.TypeVar('_T')


# noinspection PyAbstractClass
class _Async(_grpc_aio.UnaryUnaryCall, _typing.Awaitable[_T]):
    pass

# noinspection PyAbstractClass
class _AsyncStream(_grpc_aio.UnaryStreamCall, _typing.AsyncIterator[_T]):
    pass


# noinspection PyPep8Naming,DuplicatedCode
class PackageManagementServiceStub:
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _PackageManagementServiceBlockingStub: ...
    @classmethod
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _PackageManagementServiceAsyncStub: ...
    def ListKnownPackages(self, __1: ListKnownPackagesRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[ListKnownPackagesResponse, _Async[ListKnownPackagesResponse]]: ...
    def UploadDarFile(self, __1: UploadDarFileRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[UploadDarFileResponse, _Async[UploadDarFileResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PackageManagementServiceBlockingStub(PackageManagementServiceStub):
    def ListKnownPackages(self, __1: ListKnownPackagesRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> ListKnownPackagesResponse: ...
    def UploadDarFile(self, __1: UploadDarFileRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> UploadDarFileResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _PackageManagementServiceAsyncStub(PackageManagementServiceStub):
    def ListKnownPackages(self, __1: ListKnownPackagesRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _Async[ListKnownPackagesResponse]: ...
    def UploadDarFile(self, __1: UploadDarFileRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _Async[UploadDarFileResponse]: ...
