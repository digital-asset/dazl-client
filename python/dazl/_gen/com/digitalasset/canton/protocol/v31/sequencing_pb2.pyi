# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from ..v30 import common_stable_pb2 as _common_stable_pb2
from ..v30 import sequencing_pb2 as _sequencing_pb2
from ..v30 import traffic_control_parameters_pb2 as _traffic_control_parameters_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvelopeWithoutRecipients(_message.Message):
    __slots__ = ("content", "signatures")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    def __init__(self, content: _Optional[bytes] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...

class CompressedBatch(_message.Message):
    __slots__ = ("algorithm", "compressed_recipients", "compressed_envelopes")
    class DecompressedRecipients(_message.Message):
        __slots__ = ("recipients",)
        RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
        recipients: _containers.RepeatedCompositeFieldContainer[_sequencing_pb2.Recipients]
        def __init__(self, recipients: _Optional[_Iterable[_Union[_sequencing_pb2.Recipients, _Mapping]]] = ...) -> None: ...
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_ENVELOPES_FIELD_NUMBER: _ClassVar[int]
    algorithm: _sequencing_pb2.CompressedBatch.CompressionAlgorithm
    compressed_recipients: bytes
    compressed_envelopes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, algorithm: _Optional[_Union[_sequencing_pb2.CompressedBatch.CompressionAlgorithm, str]] = ..., compressed_recipients: _Optional[bytes] = ..., compressed_envelopes: _Optional[_Iterable[bytes]] = ...) -> None: ...

class SequencedEvent(_message.Message):
    __slots__ = ("previous_timestamp", "timestamp", "physical_synchronizer_id", "message_id", "batch", "deliver_error_reason", "topology_timestamp", "traffic_receipt")
    PREVIOUS_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_SYNCHRONIZER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    DELIVER_ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_RECEIPT_FIELD_NUMBER: _ClassVar[int]
    previous_timestamp: int
    timestamp: int
    physical_synchronizer_id: str
    message_id: str
    batch: CompressedBatch
    deliver_error_reason: _status_pb2.Status
    topology_timestamp: int
    traffic_receipt: _traffic_control_parameters_pb2.TrafficReceipt
    def __init__(self, previous_timestamp: _Optional[int] = ..., timestamp: _Optional[int] = ..., physical_synchronizer_id: _Optional[str] = ..., message_id: _Optional[str] = ..., batch: _Optional[_Union[CompressedBatch, _Mapping]] = ..., deliver_error_reason: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., topology_timestamp: _Optional[int] = ..., traffic_receipt: _Optional[_Union[_traffic_control_parameters_pb2.TrafficReceipt, _Mapping]] = ...) -> None: ...

class SubmissionRequest(_message.Message):
    __slots__ = ("sender", "message_id", "batch", "max_sequencing_time", "topology_timestamp", "aggregation_rule", "submission_cost")
    SENDER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_SEQUENCING_TIME_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_RULE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_COST_FIELD_NUMBER: _ClassVar[int]
    sender: str
    message_id: str
    batch: CompressedBatch
    max_sequencing_time: int
    topology_timestamp: int
    aggregation_rule: _common_stable_pb2.AggregationRule
    submission_cost: _sequencing_pb2.SequencingSubmissionCost
    def __init__(self, sender: _Optional[str] = ..., message_id: _Optional[str] = ..., batch: _Optional[_Union[CompressedBatch, _Mapping]] = ..., max_sequencing_time: _Optional[int] = ..., topology_timestamp: _Optional[int] = ..., aggregation_rule: _Optional[_Union[_common_stable_pb2.AggregationRule, _Mapping]] = ..., submission_cost: _Optional[_Union[_sequencing_pb2.SequencingSubmissionCost, _Mapping]] = ...) -> None: ...
