# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ....protocol.v30 import participant_transaction_pb2 as _participant_transaction_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompletionInfo(_message.Message):
    __slots__ = ("act_as", "user_id", "command_id", "opt_deduplication_period", "submission_id")
    ACT_AS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    OPT_DEDUPLICATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    act_as: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    command_id: str
    opt_deduplication_period: _participant_transaction_pb2.DeduplicationPeriod
    submission_id: str
    def __init__(self, act_as: _Optional[_Iterable[str]] = ..., user_id: _Optional[str] = ..., command_id: _Optional[str] = ..., opt_deduplication_period: _Optional[_Union[_participant_transaction_pb2.DeduplicationPeriod, _Mapping]] = ..., submission_id: _Optional[str] = ...) -> None: ...

class CommandRejected(_message.Message):
    __slots__ = ()
    class GrpcRejectionReasonTemplate(_message.Message):
        __slots__ = ("status",)
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: bytes
        def __init__(self, status: _Optional[bytes] = ...) -> None: ...
    def __init__(self) -> None: ...

class SubmissionTrackingData(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: TransactionSubmissionTrackingData
    def __init__(self, transaction: _Optional[_Union[TransactionSubmissionTrackingData, _Mapping]] = ...) -> None: ...

class TransactionSubmissionTrackingData(_message.Message):
    __slots__ = ("completion_info", "rejection_cause", "synchronizer_id")
    class RejectionCause(_message.Message):
        __slots__ = ("timeout", "rejection_reason_template")
        TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        REJECTION_REASON_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        timeout: _empty_pb2.Empty
        rejection_reason_template: CommandRejected.GrpcRejectionReasonTemplate
        def __init__(self, timeout: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., rejection_reason_template: _Optional[_Union[CommandRejected.GrpcRejectionReasonTemplate, _Mapping]] = ...) -> None: ...
    COMPLETION_INFO_FIELD_NUMBER: _ClassVar[int]
    REJECTION_CAUSE_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    completion_info: CompletionInfo
    rejection_cause: TransactionSubmissionTrackingData.RejectionCause
    synchronizer_id: str
    def __init__(self, completion_info: _Optional[_Union[CompletionInfo, _Mapping]] = ..., rejection_cause: _Optional[_Union[TransactionSubmissionTrackingData.RejectionCause, _Mapping]] = ..., synchronizer_id: _Optional[str] = ...) -> None: ...
