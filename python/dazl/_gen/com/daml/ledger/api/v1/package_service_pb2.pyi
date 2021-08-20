# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import typing as _typing

from google.protobuf.descriptor import EnumDescriptor
from google.protobuf.internal.containers import RepeatedScalarFieldContainer
from google.protobuf.message import Message as _Message

from .trace_context_pb2 import TraceContext

__all__ = [
    "ListPackagesRequest",
    "ListPackagesResponse",
    "GetPackageRequest",
    "GetPackageResponse",
    "GetPackageStatusRequest",
    "GetPackageStatusResponse",
]

class PackageStatus:
    DESCRIPTOR: _typing.ClassVar[EnumDescriptor] = ...
    UNKNOWN: _typing.ClassVar[_typing.Literal[0]] = ...
    REGISTERED: _typing.ClassVar[_typing.Literal[1]] = ...
UNKNOWN = _typing.Literal[0]
REGISTERED = _typing.Literal[1]

class HashFunction:
    DESCRIPTOR: _typing.ClassVar[EnumDescriptor] = ...
    SHA256: _typing.ClassVar[_typing.Literal[0]] = ...
SHA256 = _typing.Literal[0]


class ListPackagesRequest(_Message):
    ledger_id: str
    @property
    def trace_context(self) -> TraceContext: ...
    def __init__(self, *, ledger_id: _typing.Optional[str] = ..., trace_context: _typing.Optional[TraceContext] = ...): ...
    def HasField(self, field_name: _typing.Literal["ledger_id", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["ledger_id", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ListPackagesResponse(_Message):
    @property
    def package_ids(self) -> RepeatedScalarFieldContainer[str]: ...
    def __init__(self, *, package_ids: _typing.Optional[_typing.Iterable[str]] = ...): ...
    def HasField(self, field_name: _typing.Literal["package_ids"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["package_ids"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPackageRequest(_Message):
    ledger_id: str
    package_id: str
    @property
    def trace_context(self) -> TraceContext: ...
    def __init__(self, *, ledger_id: _typing.Optional[str] = ..., package_id: _typing.Optional[str] = ..., trace_context: _typing.Optional[TraceContext] = ...): ...
    def HasField(self, field_name: _typing.Literal["ledger_id", "package_id", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["ledger_id", "package_id", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPackageResponse(_Message):
    hash_function: _typing.Literal[0]
    archive_payload: bytes
    hash: str
    def __init__(self, *, hash_function: _typing.Optional[_typing.Literal['SHA256', 0]] = ..., archive_payload: _typing.Optional[bytes] = ..., hash: _typing.Optional[str] = ...): ...
    def HasField(self, field_name: _typing.Literal["hash_function", "archive_payload", "hash"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["hash_function", "archive_payload", "hash"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPackageStatusRequest(_Message):
    ledger_id: str
    package_id: str
    @property
    def trace_context(self) -> TraceContext: ...
    def __init__(self, *, ledger_id: _typing.Optional[str] = ..., package_id: _typing.Optional[str] = ..., trace_context: _typing.Optional[TraceContext] = ...): ...
    def HasField(self, field_name: _typing.Literal["ledger_id", "package_id", "trace_context"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["ledger_id", "package_id", "trace_context"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class GetPackageStatusResponse(_Message):
    package_status: _typing.Literal[0, 1]
    def __init__(self, *, package_status: _typing.Optional[_typing.Literal['UNKNOWN', 0, 'REGISTERED', 1]] = ...): ...
    def HasField(self, field_name: _typing.Literal["package_status"]) -> bool: ...
    def ClearField(self, field_name: _typing.Literal["package_status"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
