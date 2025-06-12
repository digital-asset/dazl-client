# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...crypto.v0 import crypto_pb2 as _crypto_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StaticDomainParameters(_message.Message):
    __slots__ = ("unique_contract_keys", "required_signing_key_schemes", "required_encryption_key_schemes", "required_symmetric_key_schemes", "required_hash_algorithms", "required_crypto_key_formats", "protocol_version")
    UNIQUE_CONTRACT_KEYS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SIGNING_KEY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_ENCRYPTION_KEY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SYMMETRIC_KEY_SCHEMES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_HASH_ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CRYPTO_KEY_FORMATS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    unique_contract_keys: bool
    required_signing_key_schemes: _containers.RepeatedScalarFieldContainer[_crypto_pb2.SigningKeyScheme]
    required_encryption_key_schemes: _containers.RepeatedScalarFieldContainer[_crypto_pb2.EncryptionKeyScheme]
    required_symmetric_key_schemes: _containers.RepeatedScalarFieldContainer[_crypto_pb2.SymmetricKeyScheme]
    required_hash_algorithms: _containers.RepeatedScalarFieldContainer[_crypto_pb2.HashAlgorithm]
    required_crypto_key_formats: _containers.RepeatedScalarFieldContainer[_crypto_pb2.CryptoKeyFormat]
    protocol_version: int
    def __init__(self, unique_contract_keys: bool = ..., required_signing_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.SigningKeyScheme, str]]] = ..., required_encryption_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.EncryptionKeyScheme, str]]] = ..., required_symmetric_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.SymmetricKeyScheme, str]]] = ..., required_hash_algorithms: _Optional[_Iterable[_Union[_crypto_pb2.HashAlgorithm, str]]] = ..., required_crypto_key_formats: _Optional[_Iterable[_Union[_crypto_pb2.CryptoKeyFormat, str]]] = ..., protocol_version: _Optional[int] = ...) -> None: ...

class DynamicDomainParameters(_message.Message):
    __slots__ = ("participant_response_timeout", "mediator_reaction_timeout", "transfer_exclusivity_timeout", "topology_change_delay", "ledger_time_record_time_tolerance", "reconciliation_interval", "mediator_deduplication_timeout", "max_rate_per_participant", "max_request_size")
    PARTICIPANT_RESPONSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_REACTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_EXCLUSIVITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TOPOLOGY_CHANGE_DELAY_FIELD_NUMBER: _ClassVar[int]
    LEDGER_TIME_RECORD_TIME_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    RECONCILIATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_DEDUPLICATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_RATE_PER_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUEST_SIZE_FIELD_NUMBER: _ClassVar[int]
    participant_response_timeout: _duration_pb2.Duration
    mediator_reaction_timeout: _duration_pb2.Duration
    transfer_exclusivity_timeout: _duration_pb2.Duration
    topology_change_delay: _duration_pb2.Duration
    ledger_time_record_time_tolerance: _duration_pb2.Duration
    reconciliation_interval: _duration_pb2.Duration
    mediator_deduplication_timeout: _duration_pb2.Duration
    max_rate_per_participant: int
    max_request_size: int
    def __init__(self, participant_response_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., mediator_reaction_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., transfer_exclusivity_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., topology_change_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ledger_time_record_time_tolerance: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., reconciliation_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., mediator_deduplication_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_rate_per_participant: _Optional[int] = ..., max_request_size: _Optional[int] = ...) -> None: ...
