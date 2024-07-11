# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from . import ledger_sync_event_pb2 as _ledger_sync_event_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmissionTrackingData(_message.Message):
    __slots__ = ["transaction"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: TransactionSubmissionTrackingData
    def __init__(self, transaction: _Optional[_Union[TransactionSubmissionTrackingData, _Mapping]] = ...) -> None: ...

class TransactionSubmissionTrackingData(_message.Message):
    __slots__ = ["completion_info", "rejection_cause", "domain_id"]
    class RejectionCause(_message.Message):
        __slots__ = ["timeout", "rejection_reason_template"]
        TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        REJECTION_REASON_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        timeout: _empty_pb2.Empty
        rejection_reason_template: _ledger_sync_event_pb2.CommandRejected.GrpcRejectionReasonTemplate
        def __init__(self, timeout: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., rejection_reason_template: _Optional[_Union[_ledger_sync_event_pb2.CommandRejected.GrpcRejectionReasonTemplate, _Mapping]] = ...) -> None: ...
    COMPLETION_INFO_FIELD_NUMBER: _ClassVar[int]
    REJECTION_CAUSE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    completion_info: _ledger_sync_event_pb2.CompletionInfo
    rejection_cause: TransactionSubmissionTrackingData.RejectionCause
    domain_id: _wrappers_pb2.StringValue
    def __init__(self, completion_info: _Optional[_Union[_ledger_sync_event_pb2.CompletionInfo, _Mapping]] = ..., rejection_cause: _Optional[_Union[TransactionSubmissionTrackingData.RejectionCause, _Mapping]] = ..., domain_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
