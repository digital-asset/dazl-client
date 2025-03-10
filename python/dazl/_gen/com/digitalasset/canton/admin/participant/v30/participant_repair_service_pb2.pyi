# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import domain_connectivity_pb2 as _domain_connectivity_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PurgeContractsRequest(_message.Message):
    __slots__ = ("domain", "contract_ids", "ignore_already_purged")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ALREADY_PURGED_FIELD_NUMBER: _ClassVar[int]
    domain: str
    contract_ids: _containers.RepeatedScalarFieldContainer[str]
    ignore_already_purged: bool
    def __init__(self, domain: _Optional[str] = ..., contract_ids: _Optional[_Iterable[str]] = ..., ignore_already_purged: bool = ...) -> None: ...

class PurgeContractsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MigrateDomainRequest(_message.Message):
    __slots__ = ("source_alias", "target_domain_connection_config", "force")
    SOURCE_ALIAS_FIELD_NUMBER: _ClassVar[int]
    TARGET_DOMAIN_CONNECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    source_alias: str
    target_domain_connection_config: _domain_connectivity_pb2.DomainConnectionConfig
    force: bool
    def __init__(self, source_alias: _Optional[str] = ..., target_domain_connection_config: _Optional[_Union[_domain_connectivity_pb2.DomainConnectionConfig, _Mapping]] = ..., force: bool = ...) -> None: ...

class MigrateDomainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportAcsRequest(_message.Message):
    __slots__ = ("parties", "filter_domain_id", "timestamp", "contract_domain_renames", "force", "parties_offboarding")
    class TargetDomain(_message.Message):
        __slots__ = ("domain_id", "protocol_version")
        DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        domain_id: str
        protocol_version: int
        def __init__(self, domain_id: _Optional[str] = ..., protocol_version: _Optional[int] = ...) -> None: ...
    class ContractDomainRenamesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExportAcsRequest.TargetDomain
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ExportAcsRequest.TargetDomain, _Mapping]] = ...) -> None: ...
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    FILTER_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_DOMAIN_RENAMES_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    PARTIES_OFFBOARDING_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    filter_domain_id: str
    timestamp: _timestamp_pb2.Timestamp
    contract_domain_renames: _containers.MessageMap[str, ExportAcsRequest.TargetDomain]
    force: bool
    parties_offboarding: bool
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., filter_domain_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., contract_domain_renames: _Optional[_Mapping[str, ExportAcsRequest.TargetDomain]] = ..., force: bool = ..., parties_offboarding: bool = ...) -> None: ...

class ExportAcsResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class ImportAcsRequest(_message.Message):
    __slots__ = ("acs_snapshot", "workflow_id_prefix", "allow_contract_id_suffix_recomputation")
    ACS_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CONTRACT_ID_SUFFIX_RECOMPUTATION_FIELD_NUMBER: _ClassVar[int]
    acs_snapshot: bytes
    workflow_id_prefix: str
    allow_contract_id_suffix_recomputation: bool
    def __init__(self, acs_snapshot: _Optional[bytes] = ..., workflow_id_prefix: _Optional[str] = ..., allow_contract_id_suffix_recomputation: bool = ...) -> None: ...

class ImportAcsResponse(_message.Message):
    __slots__ = ("contract_id_mapping",)
    class ContractIdMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONTRACT_ID_MAPPING_FIELD_NUMBER: _ClassVar[int]
    contract_id_mapping: _containers.ScalarMap[str, str]
    def __init__(self, contract_id_mapping: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PurgeDeactivatedDomainRequest(_message.Message):
    __slots__ = ("domain_alias",)
    DOMAIN_ALIAS_FIELD_NUMBER: _ClassVar[int]
    domain_alias: str
    def __init__(self, domain_alias: _Optional[str] = ...) -> None: ...

class PurgeDeactivatedDomainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IgnoreEventsRequest(_message.Message):
    __slots__ = ("domain_id", "from_inclusive", "to_inclusive", "force")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    from_inclusive: int
    to_inclusive: int
    force: bool
    def __init__(self, domain_id: _Optional[str] = ..., from_inclusive: _Optional[int] = ..., to_inclusive: _Optional[int] = ..., force: bool = ...) -> None: ...

class IgnoreEventsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnignoreEventsRequest(_message.Message):
    __slots__ = ("domain_id", "from_inclusive", "to_inclusive", "force")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    from_inclusive: int
    to_inclusive: int
    force: bool
    def __init__(self, domain_id: _Optional[str] = ..., from_inclusive: _Optional[int] = ..., to_inclusive: _Optional[int] = ..., force: bool = ...) -> None: ...

class UnignoreEventsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
