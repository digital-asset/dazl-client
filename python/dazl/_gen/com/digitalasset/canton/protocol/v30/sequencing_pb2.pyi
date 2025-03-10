# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from . import common_stable_pb2 as _common_stable_pb2
from . import traffic_control_parameters_pb2 as _traffic_control_parameters_pb2
from ...v30 import trace_context_pb2 as _trace_context_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PossiblyIgnoredSequencedEvent(_message.Message):
    __slots__ = ("counter", "timestamp", "trace_context", "is_ignored", "underlying")
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_IGNORED_FIELD_NUMBER: _ClassVar[int]
    UNDERLYING_FIELD_NUMBER: _ClassVar[int]
    counter: int
    timestamp: int
    trace_context: _trace_context_pb2.TraceContext
    is_ignored: bool
    underlying: _wrappers_pb2.BytesValue
    def __init__(self, counter: _Optional[int] = ..., timestamp: _Optional[int] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ..., is_ignored: bool = ..., underlying: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class RecipientsTree(_message.Message):
    __slots__ = ("recipients", "children")
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    recipients: _containers.RepeatedScalarFieldContainer[str]
    children: _containers.RepeatedCompositeFieldContainer[RecipientsTree]
    def __init__(self, recipients: _Optional[_Iterable[str]] = ..., children: _Optional[_Iterable[_Union[RecipientsTree, _Mapping]]] = ...) -> None: ...

class Recipients(_message.Message):
    __slots__ = ("recipients_tree",)
    RECIPIENTS_TREE_FIELD_NUMBER: _ClassVar[int]
    recipients_tree: _containers.RepeatedCompositeFieldContainer[RecipientsTree]
    def __init__(self, recipients_tree: _Optional[_Iterable[_Union[RecipientsTree, _Mapping]]] = ...) -> None: ...

class ServiceAgreement(_message.Message):
    __slots__ = ("id", "legal_text")
    ID_FIELD_NUMBER: _ClassVar[int]
    LEGAL_TEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    legal_text: str
    def __init__(self, id: _Optional[str] = ..., legal_text: _Optional[str] = ...) -> None: ...

class Handshake(_message.Message):
    __slots__ = ()
    class Request(_message.Message):
        __slots__ = ("client_protocol_versions", "minimum_protocol_version")
        CLIENT_PROTOCOL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        client_protocol_versions: _containers.RepeatedScalarFieldContainer[str]
        minimum_protocol_version: _wrappers_pb2.StringValue
        def __init__(self, client_protocol_versions: _Optional[_Iterable[str]] = ..., minimum_protocol_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ("server_protocol_version", "success", "failure")
        SERVER_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        server_protocol_version: str
        success: Handshake.Success
        failure: Handshake.Failure
        def __init__(self, server_protocol_version: _Optional[str] = ..., success: _Optional[_Union[Handshake.Success, _Mapping]] = ..., failure: _Optional[_Union[Handshake.Failure, _Mapping]] = ...) -> None: ...
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class SequencingSubmissionCost(_message.Message):
    __slots__ = ("cost",)
    COST_FIELD_NUMBER: _ClassVar[int]
    cost: int
    def __init__(self, cost: _Optional[int] = ...) -> None: ...

class SinglePartySignatures(_message.Message):
    __slots__ = ("party", "signatures")
    PARTY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    party: str
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    def __init__(self, party: _Optional[str] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...

class PartySignatures(_message.Message):
    __slots__ = ("signatures",)
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    signatures: _containers.RepeatedCompositeFieldContainer[SinglePartySignatures]
    def __init__(self, signatures: _Optional[_Iterable[_Union[SinglePartySignatures, _Mapping]]] = ...) -> None: ...

class StaticDomainParameters(_message.Message):
    __slots__ = ("required_signing_key_schemes", "required_encryption_specs", "required_symmetric_key_schemes", "required_hash_algorithms", "required_crypto_key_formats", "protocol_version")
    REQUIRED_SIGNING_KEY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENCRYPTION_SPECS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SYMMETRIC_KEY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_HASH_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CRYPTO_KEY_FORMATS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    required_signing_key_schemes: _containers.RepeatedScalarFieldContainer[_crypto_pb2.SigningKeyScheme]
    required_encryption_specs: _crypto_pb2.RequiredEncryptionSpecs
    required_symmetric_key_schemes: _containers.RepeatedScalarFieldContainer[_crypto_pb2.SymmetricKeyScheme]
    required_hash_algorithms: _containers.RepeatedScalarFieldContainer[_crypto_pb2.HashAlgorithm]
    required_crypto_key_formats: _containers.RepeatedScalarFieldContainer[_crypto_pb2.CryptoKeyFormat]
    protocol_version: int
    def __init__(self, required_signing_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.SigningKeyScheme, str]]] = ..., required_encryption_specs: _Optional[_Union[_crypto_pb2.RequiredEncryptionSpecs, _Mapping]] = ..., required_symmetric_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.SymmetricKeyScheme, str]]] = ..., required_hash_algorithms: _Optional[_Iterable[_Union[_crypto_pb2.HashAlgorithm, str]]] = ..., required_crypto_key_formats: _Optional[_Iterable[_Union[_crypto_pb2.CryptoKeyFormat, str]]] = ..., protocol_version: _Optional[int] = ...) -> None: ...

class Envelope(_message.Message):
    __slots__ = ("content", "recipients", "signatures")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    recipients: Recipients
    signatures: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.Signature]
    def __init__(self, content: _Optional[bytes] = ..., recipients: _Optional[_Union[Recipients, _Mapping]] = ..., signatures: _Optional[_Iterable[_Union[_crypto_pb2.Signature, _Mapping]]] = ...) -> None: ...

class Batch(_message.Message):
    __slots__ = ("envelopes",)
    ENVELOPES_FIELD_NUMBER: _ClassVar[int]
    envelopes: _containers.RepeatedCompositeFieldContainer[Envelope]
    def __init__(self, envelopes: _Optional[_Iterable[_Union[Envelope, _Mapping]]] = ...) -> None: ...

class CompressedBatch(_message.Message):
    __slots__ = ("algorithm", "compressed_batch")
    class CompressionAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPRESSION_ALGORITHM_UNSPECIFIED: _ClassVar[CompressedBatch.CompressionAlgorithm]
        COMPRESSION_ALGORITHM_GZIP: _ClassVar[CompressedBatch.CompressionAlgorithm]
    COMPRESSION_ALGORITHM_UNSPECIFIED: CompressedBatch.CompressionAlgorithm
    COMPRESSION_ALGORITHM_GZIP: CompressedBatch.CompressionAlgorithm
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_BATCH_FIELD_NUMBER: _ClassVar[int]
    algorithm: CompressedBatch.CompressionAlgorithm
    compressed_batch: bytes
    def __init__(self, algorithm: _Optional[_Union[CompressedBatch.CompressionAlgorithm, str]] = ..., compressed_batch: _Optional[bytes] = ...) -> None: ...

class SequencedEvent(_message.Message):
    __slots__ = ("counter", "timestamp", "domain_id", "message_id", "batch", "deliver_error_reason", "topology_timestamp", "traffic_receipt")
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    DELIVER_ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_RECEIPT_FIELD_NUMBER: _ClassVar[int]
    counter: int
    timestamp: int
    domain_id: str
    message_id: _wrappers_pb2.StringValue
    batch: CompressedBatch
    deliver_error_reason: _status_pb2.Status
    topology_timestamp: _wrappers_pb2.Int64Value
    traffic_receipt: _traffic_control_parameters_pb2.TrafficReceipt
    def __init__(self, counter: _Optional[int] = ..., timestamp: _Optional[int] = ..., domain_id: _Optional[str] = ..., message_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., batch: _Optional[_Union[CompressedBatch, _Mapping]] = ..., deliver_error_reason: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., topology_timestamp: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., traffic_receipt: _Optional[_Union[_traffic_control_parameters_pb2.TrafficReceipt, _Mapping]] = ...) -> None: ...

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
    topology_timestamp: _wrappers_pb2.Int64Value
    aggregation_rule: _common_stable_pb2.AggregationRule
    submission_cost: SequencingSubmissionCost
    def __init__(self, sender: _Optional[str] = ..., message_id: _Optional[str] = ..., batch: _Optional[_Union[CompressedBatch, _Mapping]] = ..., max_sequencing_time: _Optional[int] = ..., topology_timestamp: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., aggregation_rule: _Optional[_Union[_common_stable_pb2.AggregationRule, _Mapping]] = ..., submission_cost: _Optional[_Union[SequencingSubmissionCost, _Mapping]] = ...) -> None: ...
