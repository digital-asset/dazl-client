# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from ..v30 import common_stable_pb2 as _common_stable_pb2
from ..v30 import sequencing_pb2 as _sequencing_pb2
from ..v30 import traffic_control_parameters_pb2 as _traffic_control_parameters_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompressedBatch(_message.Message):
    __slots__ = ("compressed_recipients", "compressed_envelopes")
    class DecompressedRecipients(_message.Message):
        __slots__ = ("recipients",)
        RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
        recipients: _containers.RepeatedCompositeFieldContainer[_sequencing_pb2.Recipients]
        def __init__(self, recipients: _Optional[_Iterable[_Union[_sequencing_pb2.Recipients, _Mapping]]] = ...) -> None: ...
    COMPRESSED_RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_ENVELOPES_FIELD_NUMBER: _ClassVar[int]
    compressed_recipients: bytes
    compressed_envelopes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, compressed_recipients: _Optional[bytes] = ..., compressed_envelopes: _Optional[_Iterable[bytes]] = ...) -> None: ...

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

class SynchronizerLimits(_message.Message):
    __slots__ = ("transaction_protocol_limits",)
    TRANSACTION_PROTOCOL_LIMITS_FIELD_NUMBER: _ClassVar[int]
    transaction_protocol_limits: TransactionProtocolLimits
    def __init__(self, transaction_protocol_limits: _Optional[_Union[TransactionProtocolLimits, _Mapping]] = ...) -> None: ...

class TransactionProtocolLimits(_message.Message):
    __slots__ = ("max_act_as", "max_envelopes", "max_recipients_per_batch", "max_recipients_trees", "max_recipients_per_recipients_tree_level", "max_children_per_recipients_tree_level", "max_recipients_per_envelope", "max_recipients_tree_depth", "max_transaction_root_views", "max_transaction_sub_views", "max_transaction_tree_depth")
    MAX_ACT_AS_FIELD_NUMBER: _ClassVar[int]
    MAX_ENVELOPES_FIELD_NUMBER: _ClassVar[int]
    MAX_RECIPIENTS_PER_BATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_RECIPIENTS_TREES_FIELD_NUMBER: _ClassVar[int]
    MAX_RECIPIENTS_PER_RECIPIENTS_TREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_CHILDREN_PER_RECIPIENTS_TREE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_RECIPIENTS_PER_ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    MAX_RECIPIENTS_TREE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    MAX_TRANSACTION_ROOT_VIEWS_FIELD_NUMBER: _ClassVar[int]
    MAX_TRANSACTION_SUB_VIEWS_FIELD_NUMBER: _ClassVar[int]
    MAX_TRANSACTION_TREE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    max_act_as: int
    max_envelopes: int
    max_recipients_per_batch: int
    max_recipients_trees: int
    max_recipients_per_recipients_tree_level: int
    max_children_per_recipients_tree_level: int
    max_recipients_per_envelope: int
    max_recipients_tree_depth: int
    max_transaction_root_views: int
    max_transaction_sub_views: int
    max_transaction_tree_depth: int
    def __init__(self, max_act_as: _Optional[int] = ..., max_envelopes: _Optional[int] = ..., max_recipients_per_batch: _Optional[int] = ..., max_recipients_trees: _Optional[int] = ..., max_recipients_per_recipients_tree_level: _Optional[int] = ..., max_children_per_recipients_tree_level: _Optional[int] = ..., max_recipients_per_envelope: _Optional[int] = ..., max_recipients_tree_depth: _Optional[int] = ..., max_transaction_root_views: _Optional[int] = ..., max_transaction_sub_views: _Optional[int] = ..., max_transaction_tree_depth: _Optional[int] = ...) -> None: ...

class StaticSynchronizerParameters(_message.Message):
    __slots__ = ("required_signing_specs", "required_encryption_specs", "required_symmetric_key_schemes", "required_hash_algorithms", "required_crypto_key_formats", "required_signature_formats", "protocol_version", "serial", "enable_transparency_checks", "topology_change_delay", "synchronizer_limits")
    REQUIRED_SIGNING_SPECS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENCRYPTION_SPECS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SYMMETRIC_KEY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_HASH_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CRYPTO_KEY_FORMATS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SIGNATURE_FORMATS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TRANSPARENCY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_CHANGE_DELAY_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONIZER_LIMITS_FIELD_NUMBER: _ClassVar[int]
    required_signing_specs: _crypto_pb2.RequiredSigningSpecs
    required_encryption_specs: _crypto_pb2.RequiredEncryptionSpecs
    required_symmetric_key_schemes: _containers.RepeatedScalarFieldContainer[_crypto_pb2.SymmetricKeyScheme]
    required_hash_algorithms: _containers.RepeatedScalarFieldContainer[_crypto_pb2.HashAlgorithm]
    required_crypto_key_formats: _containers.RepeatedScalarFieldContainer[_crypto_pb2.CryptoKeyFormat]
    required_signature_formats: _containers.RepeatedScalarFieldContainer[_crypto_pb2.SignatureFormat]
    protocol_version: int
    serial: int
    enable_transparency_checks: bool
    topology_change_delay: _duration_pb2.Duration
    synchronizer_limits: SynchronizerLimits
    def __init__(self, required_signing_specs: _Optional[_Union[_crypto_pb2.RequiredSigningSpecs, _Mapping]] = ..., required_encryption_specs: _Optional[_Union[_crypto_pb2.RequiredEncryptionSpecs, _Mapping]] = ..., required_symmetric_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.SymmetricKeyScheme, str]]] = ..., required_hash_algorithms: _Optional[_Iterable[_Union[_crypto_pb2.HashAlgorithm, str]]] = ..., required_crypto_key_formats: _Optional[_Iterable[_Union[_crypto_pb2.CryptoKeyFormat, str]]] = ..., required_signature_formats: _Optional[_Iterable[_Union[_crypto_pb2.SignatureFormat, str]]] = ..., protocol_version: _Optional[int] = ..., serial: _Optional[int] = ..., enable_transparency_checks: _Optional[bool] = ..., topology_change_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., synchronizer_limits: _Optional[_Union[SynchronizerLimits, _Mapping]] = ...) -> None: ...
