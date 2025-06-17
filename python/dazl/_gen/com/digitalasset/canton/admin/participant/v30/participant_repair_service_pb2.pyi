# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import synchronizer_connectivity_pb2 as _synchronizer_connectivity_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContractIdImportMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTRACT_ID_IMPORT_MODE_UNSPECIFIED: _ClassVar[ContractIdImportMode]
    CONTRACT_ID_IMPORT_MODE_ACCEPT: _ClassVar[ContractIdImportMode]
    CONTRACT_ID_IMPORT_MODE_VALIDATION: _ClassVar[ContractIdImportMode]
    CONTRACT_ID_IMPORT_MODE_RECOMPUTATION: _ClassVar[ContractIdImportMode]
CONTRACT_ID_IMPORT_MODE_UNSPECIFIED: ContractIdImportMode
CONTRACT_ID_IMPORT_MODE_ACCEPT: ContractIdImportMode
CONTRACT_ID_IMPORT_MODE_VALIDATION: ContractIdImportMode
CONTRACT_ID_IMPORT_MODE_RECOMPUTATION: ContractIdImportMode

class PurgeContractsRequest(_message.Message):
    __slots__ = ("synchronizer_alias", "contract_ids", "ignore_already_purged")
    SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ALREADY_PURGED_FIELD_NUMBER: _ClassVar[int]
    synchronizer_alias: str
    contract_ids: _containers.RepeatedScalarFieldContainer[str]
    ignore_already_purged: bool
    def __init__(self, synchronizer_alias: _Optional[str] = ..., contract_ids: _Optional[_Iterable[str]] = ..., ignore_already_purged: bool = ...) -> None: ...

class PurgeContractsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChangeAssignationRequest(_message.Message):
    __slots__ = ("source_synchronizer_alias", "target_synchronizer_alias", "skip_inactive", "contracts")
    class Contract(_message.Message):
        __slots__ = ("id", "reassignment_counter_override")
        ID_FIELD_NUMBER: _ClassVar[int]
        REASSIGNMENT_COUNTER_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        id: str
        reassignment_counter_override: int
        def __init__(self, id: _Optional[str] = ..., reassignment_counter_override: _Optional[int] = ...) -> None: ...
    SOURCE_SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    SKIP_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    source_synchronizer_alias: str
    target_synchronizer_alias: str
    skip_inactive: bool
    contracts: _containers.RepeatedCompositeFieldContainer[ChangeAssignationRequest.Contract]
    def __init__(self, source_synchronizer_alias: _Optional[str] = ..., target_synchronizer_alias: _Optional[str] = ..., skip_inactive: bool = ..., contracts: _Optional[_Iterable[_Union[ChangeAssignationRequest.Contract, _Mapping]]] = ...) -> None: ...

class ChangeAssignationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MigrateSynchronizerRequest(_message.Message):
    __slots__ = ("source_synchronizer_alias", "target_synchronizer_connection_config", "force")
    SOURCE_SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SYNCHRONIZER_CONNECTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    source_synchronizer_alias: str
    target_synchronizer_connection_config: _synchronizer_connectivity_pb2.SynchronizerConnectionConfig
    force: bool
    def __init__(self, source_synchronizer_alias: _Optional[str] = ..., target_synchronizer_connection_config: _Optional[_Union[_synchronizer_connectivity_pb2.SynchronizerConnectionConfig, _Mapping]] = ..., force: bool = ...) -> None: ...

class MigrateSynchronizerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportAcsOldRequest(_message.Message):
    __slots__ = ("parties", "filter_synchronizer_id", "timestamp", "contract_synchronizer_renames", "force", "parties_offboarding")
    class TargetSynchronizer(_message.Message):
        __slots__ = ("synchronizer_id", "protocol_version")
        SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
        PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        synchronizer_id: str
        protocol_version: int
        def __init__(self, synchronizer_id: _Optional[str] = ..., protocol_version: _Optional[int] = ...) -> None: ...
    class ContractSynchronizerRenamesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExportAcsOldRequest.TargetSynchronizer
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ExportAcsOldRequest.TargetSynchronizer, _Mapping]] = ...) -> None: ...
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    FILTER_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SYNCHRONIZER_RENAMES_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    PARTIES_OFFBOARDING_FIELD_NUMBER: _ClassVar[int]
    parties: _containers.RepeatedScalarFieldContainer[str]
    filter_synchronizer_id: str
    timestamp: _timestamp_pb2.Timestamp
    contract_synchronizer_renames: _containers.MessageMap[str, ExportAcsOldRequest.TargetSynchronizer]
    force: bool
    parties_offboarding: bool
    def __init__(self, parties: _Optional[_Iterable[str]] = ..., filter_synchronizer_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., contract_synchronizer_renames: _Optional[_Mapping[str, ExportAcsOldRequest.TargetSynchronizer]] = ..., force: bool = ..., parties_offboarding: bool = ...) -> None: ...

class ExportAcsOldResponse(_message.Message):
    __slots__ = ("chunk",)
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class ImportAcsOldRequest(_message.Message):
    __slots__ = ("acs_snapshot", "workflow_id_prefix", "allow_contract_id_suffix_recomputation")
    ACS_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CONTRACT_ID_SUFFIX_RECOMPUTATION_FIELD_NUMBER: _ClassVar[int]
    acs_snapshot: bytes
    workflow_id_prefix: str
    allow_contract_id_suffix_recomputation: bool
    def __init__(self, acs_snapshot: _Optional[bytes] = ..., workflow_id_prefix: _Optional[str] = ..., allow_contract_id_suffix_recomputation: bool = ...) -> None: ...

class ImportAcsOldResponse(_message.Message):
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

class ImportAcsRequest(_message.Message):
    __slots__ = ("acs_snapshot", "workflow_id_prefix", "contract_id_suffix_recomputation_mode")
    ACS_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_SUFFIX_RECOMPUTATION_MODE_FIELD_NUMBER: _ClassVar[int]
    acs_snapshot: bytes
    workflow_id_prefix: str
    contract_id_suffix_recomputation_mode: ContractIdImportMode
    def __init__(self, acs_snapshot: _Optional[bytes] = ..., workflow_id_prefix: _Optional[str] = ..., contract_id_suffix_recomputation_mode: _Optional[_Union[ContractIdImportMode, str]] = ...) -> None: ...

class ImportAcsResponse(_message.Message):
    __slots__ = ("contract_id_mappings",)
    class ContractIdMappingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONTRACT_ID_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    contract_id_mappings: _containers.ScalarMap[str, str]
    def __init__(self, contract_id_mappings: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PurgeDeactivatedSynchronizerRequest(_message.Message):
    __slots__ = ("synchronizer_alias",)
    SYNCHRONIZER_ALIAS_FIELD_NUMBER: _ClassVar[int]
    synchronizer_alias: str
    def __init__(self, synchronizer_alias: _Optional[str] = ...) -> None: ...

class PurgeDeactivatedSynchronizerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IgnoreEventsRequest(_message.Message):
    __slots__ = ("synchronizer_id", "from_inclusive", "to_inclusive", "force")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    from_inclusive: int
    to_inclusive: int
    force: bool
    def __init__(self, synchronizer_id: _Optional[str] = ..., from_inclusive: _Optional[int] = ..., to_inclusive: _Optional[int] = ..., force: bool = ...) -> None: ...

class IgnoreEventsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnignoreEventsRequest(_message.Message):
    __slots__ = ("synchronizer_id", "from_inclusive", "to_inclusive", "force")
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    TO_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    synchronizer_id: str
    from_inclusive: int
    to_inclusive: int
    force: bool
    def __init__(self, synchronizer_id: _Optional[str] = ..., from_inclusive: _Optional[int] = ..., to_inclusive: _Optional[int] = ..., force: bool = ...) -> None: ...

class UnignoreEventsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RollbackUnassignmentRequest(_message.Message):
    __slots__ = ("unassign_id", "source_synchronizer_id", "target_synchronizer_id")
    UNASSIGN_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    unassign_id: str
    source_synchronizer_id: str
    target_synchronizer_id: str
    def __init__(self, unassign_id: _Optional[str] = ..., source_synchronizer_id: _Optional[str] = ..., target_synchronizer_id: _Optional[str] = ...) -> None: ...

class RollbackUnassignmentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
