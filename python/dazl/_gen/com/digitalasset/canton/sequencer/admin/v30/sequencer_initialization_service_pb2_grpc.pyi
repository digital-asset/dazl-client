# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, typing as _typing

import grpc as _grpc
from grpc import aio as _grpc_aio

from .sequencer_initialization_service_pb2 import InitializeSequencerFromGenesisStateRequest, InitializeSequencerFromGenesisStateResponse, InitializeSequencerFromOnboardingStateRequest, InitializeSequencerFromOnboardingStateResponse

__all__ = [
    "SequencerInitializationServiceStub",
]


# noinspection PyPep8Naming,DuplicatedCode
class SequencerInitializationServiceStub:
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc.Channel) -> _SequencerInitializationServiceBlockingStub: ...  # type: ignore
    @classmethod  # type: ignore
    @_typing.overload
    def __new__(cls, channel: _grpc_aio.Channel) -> _SequencerInitializationServiceAsyncStub: ...  # type: ignore
    def InitializeSequencerFromGenesisState(self, __1: _typing.Iterable[InitializeSequencerFromGenesisStateRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[InitializeSequencerFromGenesisStateResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, InitializeSequencerFromGenesisStateResponse]]: ...
    def InitializeSequencerFromOnboardingState(self, __1: _typing.Iterable[InitializeSequencerFromOnboardingStateRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _typing.Union[InitializeSequencerFromOnboardingStateResponse, _grpc_aio.UnaryUnaryCall[_typing.Any, InitializeSequencerFromOnboardingStateResponse]]: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerInitializationServiceBlockingStub(SequencerInitializationServiceStub):
    def InitializeSequencerFromGenesisState(self, __1: _typing.Iterable[InitializeSequencerFromGenesisStateRequest], timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> InitializeSequencerFromGenesisStateResponse: ...
    def InitializeSequencerFromOnboardingState(self, __1: _typing.Iterable[InitializeSequencerFromOnboardingStateRequest], timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_typing.Tuple[_typing.Tuple[str, _typing.Union[str, bytes]], ...]] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> InitializeSequencerFromOnboardingStateResponse: ...

# noinspection PyPep8Naming,DuplicatedCode
class _SequencerInitializationServiceAsyncStub(SequencerInitializationServiceStub):
    def InitializeSequencerFromGenesisState(self, __1: _typing.Iterable[InitializeSequencerFromGenesisStateRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, InitializeSequencerFromGenesisStateResponse]: ...  # type: ignore
    def InitializeSequencerFromOnboardingState(self, __1: _typing.Iterable[InitializeSequencerFromOnboardingStateRequest], *, timeout: _typing.Optional[float] = ..., metadata: _typing.Optional[_grpc_aio.Metadata] = ..., credentials: _typing.Optional[_grpc.CallCredentials] = ..., wait_for_ready: _typing.Optional[bool] = ..., compression: _typing.Optional[_grpc.Compression] = ...) -> _grpc_aio.UnaryUnaryCall[_typing.Any, InitializeSequencerFromOnboardingStateResponse]: ...  # type: ignore
