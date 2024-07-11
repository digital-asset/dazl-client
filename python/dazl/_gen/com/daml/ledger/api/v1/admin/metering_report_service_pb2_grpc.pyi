# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .metering_report_service_pb2 import GetMeteringReportRequest, GetMeteringReportResponse

__all__ = [
    "MeteringReportServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class MeteringReportServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _MeteringReportServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _MeteringReportServiceAsyncStub: ...  # type: ignore
    def GetMeteringReport(self, __1: GetMeteringReportRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[GetMeteringReportResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, GetMeteringReportResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _MeteringReportServiceBlockingStub(MeteringReportServiceStub):
    def GetMeteringReport(self, __1: GetMeteringReportRequest, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> GetMeteringReportResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _MeteringReportServiceAsyncStub(MeteringReportServiceStub):
    def GetMeteringReport(self, __1: GetMeteringReportRequest, *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, GetMeteringReportResponse]: ...  # type: ignore
