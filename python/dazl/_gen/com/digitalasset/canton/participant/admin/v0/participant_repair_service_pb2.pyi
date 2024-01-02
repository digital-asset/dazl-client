# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import domain_connectivity_pb2 as _domain_connectivity_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PurgeContractsRequest(_message.Message):
    __slots__ = ["domain", "contract_ids", "ignore_already_purged"]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ALREADY_PURGED_FIELD_NUMBER: _ClassVar[int]
    domain: str
    contract_ids: _containers.RepeatedScalarFieldContainer[str]
    ignore_already_purged: bool
    def __init__(self, domain: _Optional[str] = ..., contract_ids: _Optional[_Iterable[str]] = ..., ignore_already_purged: bool = ...) -> None: ...

class PurgeContractsResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class DownloadRequest(_message.Message):
    __slots__ = ["parties", "filter_domain_id", "timestamp", "protocol_version", "chunkSize", "gzip_format", "contract_domain_renames"]
    class ContractDomainRenamesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    CHUNKSIZE_FIELD_NUMBER: _ClassVar[int]
    GZIP_FORMAT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_DOMAIN_RENAMES_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    filter_domain_id: str
    timestamp: _timestamp_pb2.Timestamp
    protocol_version: str
    chunkSize: _wrappers_pb2.UInt32Value
    gzip_format: bool
    contract_domain_renames: _containers.ScalarMap[str, str]
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., filter_domain_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., protocol_version: _Optional[str] = ..., chunkSize: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., gzip_format: bool = ..., contract_domain_renames: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AcsSnapshotChunk(_message.Message):
    __slots__ = ["chunk"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class UploadRequest(_message.Message):
    __slots__ = ["acs_snapshot", "gzip_format"]
    ACS_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    GZIP_FORMAT_FIELD_NUMBER: _ClassVar[int]
    acs_snapshot: bytes
    gzip_format: bool
    def __init__(self, acs_snapshot: _Optional[bytes] = ..., gzip_format: bool = ...) -> None: ...

class UploadResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class MigrateDomainRequest(_message.Message):
    __slots__ = ["source_alias", "target_domain_connection_config"]
    SOURCE_ALIAS_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_CONNECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    source_alias: str
    target_domain_connection_config: _domain_connectivity_pb2.DomainConnectionConfig
    def __init__(self, source_alias: _Optional[str] = ..., target_domain_connection_config: _Optional[_Union[_domain_connectivity_pb2.DomainConnectionConfig, _Mapping]] = ...) -> None: ...

class MigrateDomainResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...
