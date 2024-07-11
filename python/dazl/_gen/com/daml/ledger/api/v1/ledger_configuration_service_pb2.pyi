# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetLedgerConfigurationRequest(_message.Message):
    __slots__ = ["ledger_id"]
    LEDGER_ID_FIELD_NUMBER: _ClassVar[int]
    ledger_id: str
    def __init__(self, ledger_id: _Optional[str] = ...) -> None: ...

class GetLedgerConfigurationResponse(_message.Message):
    __slots__ = ["ledger_configuration"]
    LEDGER_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    ledger_configuration: LedgerConfiguration
    def __init__(self, ledger_configuration: _Optional[_Union[LedgerConfiguration, _Mapping]] = ...) -> None: ...

class LedgerConfiguration(_message.Message):
    __slots__ = ["max_deduplication_duration"]
    MAX_DEDUPLICATION_DURATION_FIELD_NUMBER: _ClassVar[int]
    max_deduplication_duration: _duration_pb2.Duration
    def __init__(self, max_deduplication_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
