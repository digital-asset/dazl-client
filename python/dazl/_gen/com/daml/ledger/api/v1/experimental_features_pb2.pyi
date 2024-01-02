# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommandDeduplicationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    ASYNC_ONLY: _ClassVar[CommandDeduplicationType]
    ASYNC_AND_CONCURRENT_SYNC: _ClassVar[CommandDeduplicationType]
ASYNC_ONLY: CommandDeduplicationType
ASYNC_AND_CONCURRENT_SYNC: CommandDeduplicationType

class ExperimentalFeatures(_message.Message):
    __slots__ = ["self_service_error_codes", "static_time", "command_deduplication", "optional_ledger_id", "contract_ids", "committer_event_log", "explicit_disclosure", "user_and_party_local_metadata_extensions", "acs_active_at_offset"]
    SELF_SERVICE_ERROR_CODES_FIELD_NUMBER: _ClassVar[int]
    STATIC_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_DEDUPLICATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDS_FIELD_NUMBER: _ClassVar[int]
    COMMITTER_EVENT_LOG_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_DISCLOSURE_FIELD_NUMBER: _ClassVar[int]
    USER_AND_PARTY_LOCAL_METADATA_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    ACS_ACTIVE_AT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    self_service_error_codes: ExperimentalSelfServiceErrorCodes
    static_time: ExperimentalStaticTime
    command_deduplication: CommandDeduplicationFeatures
    optional_ledger_id: ExperimentalOptionalLedgerId
    contract_ids: ExperimentalContractIds
    committer_event_log: ExperimentalCommitterEventLog
    explicit_disclosure: ExperimentalExplicitDisclosure
    user_and_party_local_metadata_extensions: ExperimentalUserAndPartyLocalMetadataExtensions
    acs_active_at_offset: AcsActiveAtOffsetFeature
    def __init__(self, self_service_error_codes: _Optional[_Union[ExperimentalSelfServiceErrorCodes, _Mapping]] = ..., static_time: _Optional[_Union[ExperimentalStaticTime, _Mapping]] = ..., command_deduplication: _Optional[_Union[CommandDeduplicationFeatures, _Mapping]] = ..., optional_ledger_id: _Optional[_Union[ExperimentalOptionalLedgerId, _Mapping]] = ..., contract_ids: _Optional[_Union[ExperimentalContractIds, _Mapping]] = ..., committer_event_log: _Optional[_Union[ExperimentalCommitterEventLog, _Mapping]] = ..., explicit_disclosure: _Optional[_Union[ExperimentalExplicitDisclosure, _Mapping]] = ..., user_and_party_local_metadata_extensions: _Optional[_Union[ExperimentalUserAndPartyLocalMetadataExtensions, _Mapping]] = ..., acs_active_at_offset: _Optional[_Union[AcsActiveAtOffsetFeature, _Mapping]] = ...) -> None: ...

class ExperimentalSelfServiceErrorCodes(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class ExperimentalStaticTime(_message.Message):
    __slots__ = ["supported"]
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...

class CommandDeduplicationFeatures(_message.Message):
    __slots__ = ["deduplication_period_support", "deduplication_type", "max_deduplication_duration_enforced"]
    DEDUPLICATION_PERIOD_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_DEDUPLICATION_DURATION_ENFORCED_FIELD_NUMBER: _ClassVar[int]
    deduplication_period_support: CommandDeduplicationPeriodSupport
    deduplication_type: CommandDeduplicationType
    max_deduplication_duration_enforced: bool
    def __init__(self, deduplication_period_support: _Optional[_Union[CommandDeduplicationPeriodSupport, _Mapping]] = ..., deduplication_type: _Optional[_Union[CommandDeduplicationType, str]] = ..., max_deduplication_duration_enforced: bool = ...) -> None: ...

class ExperimentalOptionalLedgerId(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class CommandDeduplicationPeriodSupport(_message.Message):
    __slots__ = ["offset_support", "duration_support"]
    class OffsetSupport(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []  # type: ignore
        OFFSET_NOT_SUPPORTED: _ClassVar[CommandDeduplicationPeriodSupport.OffsetSupport]
        OFFSET_NATIVE_SUPPORT: _ClassVar[CommandDeduplicationPeriodSupport.OffsetSupport]
        OFFSET_CONVERT_TO_DURATION: _ClassVar[CommandDeduplicationPeriodSupport.OffsetSupport]
    OFFSET_NOT_SUPPORTED: CommandDeduplicationPeriodSupport.OffsetSupport
    OFFSET_NATIVE_SUPPORT: CommandDeduplicationPeriodSupport.OffsetSupport
    OFFSET_CONVERT_TO_DURATION: CommandDeduplicationPeriodSupport.OffsetSupport
    class DurationSupport(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []  # type: ignore
        DURATION_NATIVE_SUPPORT: _ClassVar[CommandDeduplicationPeriodSupport.DurationSupport]
        DURATION_CONVERT_TO_OFFSET: _ClassVar[CommandDeduplicationPeriodSupport.DurationSupport]
    DURATION_NATIVE_SUPPORT: CommandDeduplicationPeriodSupport.DurationSupport
    DURATION_CONVERT_TO_OFFSET: CommandDeduplicationPeriodSupport.DurationSupport
    OFFSET_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    DURATION_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    offset_support: CommandDeduplicationPeriodSupport.OffsetSupport
    duration_support: CommandDeduplicationPeriodSupport.DurationSupport
    def __init__(self, offset_support: _Optional[_Union[CommandDeduplicationPeriodSupport.OffsetSupport, str]] = ..., duration_support: _Optional[_Union[CommandDeduplicationPeriodSupport.DurationSupport, str]] = ...) -> None: ...

class ExperimentalContractIds(_message.Message):
    __slots__ = ["v1"]
    class ContractIdV1Support(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []  # type: ignore
        SUFFIXED: _ClassVar[ExperimentalContractIds.ContractIdV1Support]
        NON_SUFFIXED: _ClassVar[ExperimentalContractIds.ContractIdV1Support]
    SUFFIXED: ExperimentalContractIds.ContractIdV1Support
    NON_SUFFIXED: ExperimentalContractIds.ContractIdV1Support
    V1_FIELD_NUMBER: _ClassVar[int]
    v1: ExperimentalContractIds.ContractIdV1Support
    def __init__(self, v1: _Optional[_Union[ExperimentalContractIds.ContractIdV1Support, str]] = ...) -> None: ...

class ExperimentalCommitterEventLog(_message.Message):
    __slots__ = ["event_log_type"]
    class CommitterEventLogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []  # type: ignore
        CENTRALIZED: _ClassVar[ExperimentalCommitterEventLog.CommitterEventLogType]
        DISTRIBUTED: _ClassVar[ExperimentalCommitterEventLog.CommitterEventLogType]
    CENTRALIZED: ExperimentalCommitterEventLog.CommitterEventLogType
    DISTRIBUTED: ExperimentalCommitterEventLog.CommitterEventLogType
    EVENT_LOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    event_log_type: ExperimentalCommitterEventLog.CommitterEventLogType
    def __init__(self, event_log_type: _Optional[_Union[ExperimentalCommitterEventLog.CommitterEventLogType, str]] = ...) -> None: ...

class ExperimentalExplicitDisclosure(_message.Message):
    __slots__ = ["supported"]
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...

class ExperimentalUserAndPartyLocalMetadataExtensions(_message.Message):
    __slots__ = ["supported"]
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...

class AcsActiveAtOffsetFeature(_message.Message):
    __slots__ = ["supported"]
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...
