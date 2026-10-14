# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ..v30 import common_stable_pb2 as _common_stable_pb2
from ..v30 import sequencing_pb2 as _sequencing_pb2
from ..v32 import sequencing_pb2 as _sequencing_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmissionRequest(_message.Message):
    __slots__ = ("sender", "message_id", "batch", "max_sequencing_time", "aggregation_rule", "submission_cost")
    SENDER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_SEQUENCING_TIME_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_RULE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_COST_FIELD_NUMBER: _ClassVar[int]
    sender: str
    message_id: str
    batch: _sequencing_pb2_1.CompressedBatch
    max_sequencing_time: int
    aggregation_rule: _common_stable_pb2.AggregationRule
    submission_cost: _sequencing_pb2.SequencingSubmissionCost
    def __init__(self, sender: _Optional[str] = ..., message_id: _Optional[str] = ..., batch: _Optional[_Union[_sequencing_pb2_1.CompressedBatch, _Mapping]] = ..., max_sequencing_time: _Optional[int] = ..., aggregation_rule: _Optional[_Union[_common_stable_pb2.AggregationRule, _Mapping]] = ..., submission_cost: _Optional[_Union[_sequencing_pb2.SequencingSubmissionCost, _Mapping]] = ...) -> None: ...
