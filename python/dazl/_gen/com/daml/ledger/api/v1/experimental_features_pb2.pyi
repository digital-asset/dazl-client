# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

import builtins as _builtins, sys, typing as _typing

from google.protobuf.descriptor import EnumDescriptor
from google.protobuf.message import Message as _Message

if sys.version_info >= (3, 8):
    from typing import Literal as _L
else:
    from typing_extensions import Literal as _L

__all__ = [
    "ExperimentalFeatures",
    "ExperimentalSelfServiceErrorCodes",
    "ExperimentalStaticTime",
    "CommandDeduplicationFeatures",
    "ExperimentalOptionalLedgerId",
    "CommandDeduplicationPeriodSupport",
    "ExperimentalContractIds",
    "ExperimentalCommitterEventLog",
    "ExperimentalExplicitDisclosure",
    "ExperimentalUserAndPartyLocalMetadataExtensions",
]

class CommandDeduplicationType:
    DESCRIPTOR: _typing.ClassVar[EnumDescriptor] = ...
    ASYNC_ONLY: _typing.ClassVar[_L[0]] = ...
    ASYNC_AND_CONCURRENT_SYNC: _typing.ClassVar[_L[1]] = ...
ASYNC_ONLY = _L[0]
ASYNC_AND_CONCURRENT_SYNC = _L[1]


class ExperimentalFeatures(_Message):
    @property
    def self_service_error_codes(self) -> ExperimentalSelfServiceErrorCodes: ...
    @property
    def static_time(self) -> ExperimentalStaticTime: ...
    @property
    def command_deduplication(self) -> CommandDeduplicationFeatures: ...
    @property
    def optional_ledger_id(self) -> ExperimentalOptionalLedgerId: ...
    @property
    def contract_ids(self) -> ExperimentalContractIds: ...
    @property
    def committer_event_log(self) -> ExperimentalCommitterEventLog: ...
    @property
    def explicit_disclosure(self) -> ExperimentalExplicitDisclosure: ...
    @property
    def user_and_party_local_metadata_extensions(self) -> ExperimentalUserAndPartyLocalMetadataExtensions: ...
    def __init__(self, *, self_service_error_codes: _typing.Optional[ExperimentalSelfServiceErrorCodes] = ..., static_time: _typing.Optional[ExperimentalStaticTime] = ..., command_deduplication: _typing.Optional[CommandDeduplicationFeatures] = ..., optional_ledger_id: _typing.Optional[ExperimentalOptionalLedgerId] = ..., contract_ids: _typing.Optional[ExperimentalContractIds] = ..., committer_event_log: _typing.Optional[ExperimentalCommitterEventLog] = ..., explicit_disclosure: _typing.Optional[ExperimentalExplicitDisclosure] = ..., user_and_party_local_metadata_extensions: _typing.Optional[ExperimentalUserAndPartyLocalMetadataExtensions] = ...): ...
    def HasField(self, field_name: _L["self_service_error_codes", "static_time", "command_deduplication", "optional_ledger_id", "contract_ids", "committer_event_log", "explicit_disclosure", "user_and_party_local_metadata_extensions"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["self_service_error_codes", "static_time", "command_deduplication", "optional_ledger_id", "contract_ids", "committer_event_log", "explicit_disclosure", "user_and_party_local_metadata_extensions"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExperimentalSelfServiceErrorCodes(_Message):
    def __init__(self): ...
    def HasField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def ClearField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExperimentalStaticTime(_Message):
    supported: _builtins.bool
    def __init__(self, *, supported: _typing.Optional[_builtins.bool] = ...): ...
    def HasField(self, field_name: _L["supported"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["supported"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class CommandDeduplicationFeatures(_Message):
    @property
    def deduplication_period_support(self) -> CommandDeduplicationPeriodSupport: ...
    @property
    def deduplication_type(self) -> _L[0, 1]: ...
    max_deduplication_duration_enforced: _builtins.bool
    def __init__(self, *, deduplication_period_support: _typing.Optional[CommandDeduplicationPeriodSupport] = ..., deduplication_type: _typing.Optional[_L['ASYNC_ONLY', 0, 'ASYNC_AND_CONCURRENT_SYNC', 1]] = ..., max_deduplication_duration_enforced: _typing.Optional[_builtins.bool] = ...): ...
    def HasField(self, field_name: _L["deduplication_period_support", "deduplication_type", "max_deduplication_duration_enforced"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["deduplication_period_support", "deduplication_type", "max_deduplication_duration_enforced"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExperimentalOptionalLedgerId(_Message):
    def __init__(self): ...
    def HasField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def ClearField(self, field_name: _typing.NoReturn) -> _typing.NoReturn: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class CommandDeduplicationPeriodSupport(_Message):
    @property
    def offset_support(self) -> _L[0, 1, 2]: ...
    @property
    def duration_support(self) -> _L[0, 1]: ...
    def __init__(self, *, offset_support: _typing.Optional[_L['OFFSET_NOT_SUPPORTED', 0, 'OFFSET_NATIVE_SUPPORT', 1, 'OFFSET_CONVERT_TO_DURATION', 2]] = ..., duration_support: _typing.Optional[_L['DURATION_NATIVE_SUPPORT', 0, 'DURATION_CONVERT_TO_OFFSET', 1]] = ...): ...
    def HasField(self, field_name: _L["offset_support", "duration_support"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["offset_support", "duration_support"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExperimentalContractIds(_Message):
    @property
    def v1(self) -> _L[0, 1]: ...
    def __init__(self, *, v1: _typing.Optional[_L['SUFFIXED', 0, 'NON_SUFFIXED', 1]] = ...): ...
    def HasField(self, field_name: _L["v1"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["v1"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExperimentalCommitterEventLog(_Message):
    @property
    def event_log_type(self) -> _L[0, 1]: ...
    def __init__(self, *, event_log_type: _typing.Optional[_L['CENTRALIZED', 0, 'DISTRIBUTED', 1]] = ...): ...
    def HasField(self, field_name: _L["event_log_type"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["event_log_type"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExperimentalExplicitDisclosure(_Message):
    supported: _builtins.bool
    def __init__(self, *, supported: _typing.Optional[_builtins.bool] = ...): ...
    def HasField(self, field_name: _L["supported"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["supported"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...

class ExperimentalUserAndPartyLocalMetadataExtensions(_Message):
    supported: _builtins.bool
    def __init__(self, *, supported: _typing.Optional[_builtins.bool] = ...): ...
    def HasField(self, field_name: _L["supported"]) -> _builtins.bool: ...
    def ClearField(self, field_name: _L["supported"]) -> None: ...
    def WhichOneof(self, oneof_group: _typing.NoReturn) -> _typing.NoReturn: ...
