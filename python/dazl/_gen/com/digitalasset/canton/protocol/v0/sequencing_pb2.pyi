# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from ...v0 import trace_context_pb2 as _trace_context_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SequencedEvent(_message.Message):
    __slots__ = ["counter", "timestamp", "domain_id", "message_id", "batch", "deliver_error_reason"]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    DELIVER_ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    counter: int
    timestamp: _timestamp_pb2.Timestamp
    domain_id: str
    message_id: _wrappers_pb2.StringValue
    batch: CompressedBatch
    deliver_error_reason: DeliverErrorReason
    def __init__(self, counter: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., domain_id: _Optional[str] = ..., message_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., batch: _Optional[_Union[CompressedBatch, _Mapping]] = ..., deliver_error_reason: _Optional[_Union[DeliverErrorReason, _Mapping]] = ...) -> None: ...

class PossiblyIgnoredSequencedEvent(_message.Message):
    __slots__ = ["counter", "timestamp", "trace_context", "is_ignored", "underlying"]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_IGNORED_FIELD_NUMBER: _ClassVar[int]
    UNDERLYING_FIELD_NUMBER: _ClassVar[int]
    counter: int
    timestamp: _timestamp_pb2.Timestamp
    trace_context: _trace_context_pb2.TraceContext
    is_ignored: bool
    underlying: SignedContent
    def __init__(self, counter: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ..., is_ignored: bool = ..., underlying: _Optional[_Union[SignedContent, _Mapping]] = ...) -> None: ...

class RecipientsTree(_message.Message):
    __slots__ = ["recipients", "children"]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    recipients: _containers.RepeatedScalarFieldContainer[str]
    children: _containers.RepeatedCompositeFieldContainer[RecipientsTree]
    def __init__(self, recipients: _Optional[_Iterable[str]] = ..., children: _Optional[_Iterable[_Union[RecipientsTree, _Mapping]]] = ...) -> None: ...

class Recipients(_message.Message):
    __slots__ = ["recipients_tree"]
    RECIPIENTS_TREE_FIELD_NUMBER: _ClassVar[int]
    recipients_tree: _containers.RepeatedCompositeFieldContainer[RecipientsTree]
    def __init__(self, recipients_tree: _Optional[_Iterable[_Union[RecipientsTree, _Mapping]]] = ...) -> None: ...

class Envelope(_message.Message):
    __slots__ = ["content", "recipients"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    recipients: Recipients
    def __init__(self, content: _Optional[bytes] = ..., recipients: _Optional[_Union[Recipients, _Mapping]] = ...) -> None: ...

class CompressedBatch(_message.Message):
    __slots__ = ["algorithm", "compressed_batch"]
    class CompressionAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []  # type: ignore
        None_: _ClassVar[CompressedBatch.CompressionAlgorithm]
        Gzip: _ClassVar[CompressedBatch.CompressionAlgorithm]
    None_: CompressedBatch.CompressionAlgorithm
    Gzip: CompressedBatch.CompressionAlgorithm
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_BATCH_FIELD_NUMBER: _ClassVar[int]
    algorithm: CompressedBatch.CompressionAlgorithm
    compressed_batch: bytes
    def __init__(self, algorithm: _Optional[_Union[CompressedBatch.CompressionAlgorithm, str]] = ..., compressed_batch: _Optional[bytes] = ...) -> None: ...

class Batch(_message.Message):
    __slots__ = ["envelopes"]
    ENVELOPES_FIELD_NUMBER: _ClassVar[int]
    envelopes: _containers.RepeatedCompositeFieldContainer[Envelope]
    def __init__(self, envelopes: _Optional[_Iterable[_Union[Envelope, _Mapping]]] = ...) -> None: ...

class SignedContent(_message.Message):
    __slots__ = ["content", "signatures", "timestamp_of_signing_key"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_OF_SIGNING_KEY_FIELD_NUMBER: _ClassVar[int]
    content: _wrappers_pb2.BytesValue
    signatures: _crypto_pb2.Signature
    timestamp_of_signing_key: _timestamp_pb2.Timestamp
    def __init__(self, content: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., signatures: _Optional[_Union[_crypto_pb2.Signature, _Mapping]] = ..., timestamp_of_signing_key: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeliverErrorReason(_message.Message):
    __slots__ = ["batch_invalid", "batch_refused"]
    BATCH_INVALID_FIELD_NUMBER: _ClassVar[int]
    BATCH_REFUSED_FIELD_NUMBER: _ClassVar[int]
    batch_invalid: str
    batch_refused: str
    def __init__(self, batch_invalid: _Optional[str] = ..., batch_refused: _Optional[str] = ...) -> None: ...

class ServiceAgreement(_message.Message):
    __slots__ = ["id", "legal_text"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEGAL_TEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    legal_text: str
    def __init__(self, id: _Optional[str] = ..., legal_text: _Optional[str] = ...) -> None: ...

class StaticDomainParameters(_message.Message):
    __slots__ = ["reconciliation_interval", "max_rate_per_participant", "max_inbound_message_size", "unique_contract_keys", "required_signing_key_schemes", "required_encryption_key_schemes", "required_symmetric_key_schemes", "required_hash_algorithms", "required_crypto_key_formats", "protocol_version"]
    RECONCILIATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MAX_RATE_PER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    MAX_INBOUND_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CONTRACT_KEYS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SIGNING_KEY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENCRYPTION_KEY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SYMMETRIC_KEY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_HASH_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CRYPTO_KEY_FORMATS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    reconciliation_interval: _duration_pb2.Duration
    max_rate_per_participant: int
    max_inbound_message_size: int
    unique_contract_keys: bool
    required_signing_key_schemes: _containers.RepeatedScalarFieldContainer[_crypto_pb2.SigningKeyScheme]
    required_encryption_key_schemes: _containers.RepeatedScalarFieldContainer[_crypto_pb2.EncryptionKeyScheme]
    required_symmetric_key_schemes: _containers.RepeatedScalarFieldContainer[_crypto_pb2.SymmetricKeyScheme]
    required_hash_algorithms: _containers.RepeatedScalarFieldContainer[_crypto_pb2.HashAlgorithm]
    required_crypto_key_formats: _containers.RepeatedScalarFieldContainer[_crypto_pb2.CryptoKeyFormat]
    protocol_version: str
    def __init__(self, reconciliation_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_rate_per_participant: _Optional[int] = ..., max_inbound_message_size: _Optional[int] = ..., unique_contract_keys: bool = ..., required_signing_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.SigningKeyScheme, str]]] = ..., required_encryption_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.EncryptionKeyScheme, str]]] = ..., required_symmetric_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.SymmetricKeyScheme, str]]] = ..., required_hash_algorithms: _Optional[_Iterable[_Union[_crypto_pb2.HashAlgorithm, str]]] = ..., required_crypto_key_formats: _Optional[_Iterable[_Union[_crypto_pb2.CryptoKeyFormat, str]]] = ..., protocol_version: _Optional[str] = ...) -> None: ...

class DynamicDomainParameters(_message.Message):
    __slots__ = ["participant_response_timeout", "mediator_reaction_timeout", "transfer_exclusivity_timeout", "topology_change_delay", "ledger_time_record_time_tolerance"]
    PARTICIPANT_RESPONSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REACTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_EXCLUSIVITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_CHANGE_DELAY_FIELD_NUMBER: _ClassVar[int]
    LEDGER_TIME_RECORD_TIME_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    participant_response_timeout: _duration_pb2.Duration
    mediator_reaction_timeout: _duration_pb2.Duration
    transfer_exclusivity_timeout: _duration_pb2.Duration
    topology_change_delay: _duration_pb2.Duration
    ledger_time_record_time_tolerance: _duration_pb2.Duration
    def __init__(self, participant_response_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., mediator_reaction_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., transfer_exclusivity_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., topology_change_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ledger_time_record_time_tolerance: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class Handshake(_message.Message):
    __slots__ = []  # type: ignore
    class Request(_message.Message):
        __slots__ = ["client_protocol_versions", "minimum_protocol_version"]
        CLIENT_PROTOCOL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        client_protocol_versions: _containers.RepeatedScalarFieldContainer[str]
        minimum_protocol_version: _wrappers_pb2.StringValue
        def __init__(self, client_protocol_versions: _Optional[_Iterable[str]] = ..., minimum_protocol_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    class Response(_message.Message):
        __slots__ = ["server_protocol_version", "success", "failure"]
        SERVER_PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        FAILURE_FIELD_NUMBER: _ClassVar[int]
        server_protocol_version: str
        success: Handshake.Success
        failure: Handshake.Failure
        def __init__(self, server_protocol_version: _Optional[str] = ..., success: _Optional[_Union[Handshake.Success, _Mapping]] = ..., failure: _Optional[_Union[Handshake.Failure, _Mapping]] = ...) -> None: ...
    class Success(_message.Message):
        __slots__ = []  # type: ignore
        def __init__(self) -> None: ...
    class Failure(_message.Message):
        __slots__ = ["reason"]
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class SubmissionRequest(_message.Message):
    __slots__ = ["sender", "message_id", "is_request", "batch", "max_sequencing_time", "timestamp_of_signing_key"]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_SEQUENCING_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_OF_SIGNING_KEY_FIELD_NUMBER: _ClassVar[int]
    sender: str
    message_id: str
    is_request: bool
    batch: CompressedBatch
    max_sequencing_time: _timestamp_pb2.Timestamp
    timestamp_of_signing_key: _timestamp_pb2.Timestamp
    def __init__(self, sender: _Optional[str] = ..., message_id: _Optional[str] = ..., is_request: bool = ..., batch: _Optional[_Union[CompressedBatch, _Mapping]] = ..., max_sequencing_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timestamp_of_signing_key: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AggregationRule(_message.Message):
    __slots__ = ["eligible_members", "threshold"]
    ELIGIBLE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    eligible_members: _containers.RepeatedScalarFieldContainer[str]
    threshold: int
    def __init__(self, eligible_members: _Optional[_Iterable[str]] = ..., threshold: _Optional[int] = ...) -> None: ...
