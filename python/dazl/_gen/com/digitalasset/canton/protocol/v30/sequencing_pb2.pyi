# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from ...v30 import trace_context_pb2 as _trace_context_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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
    underlying: bytes
    def __init__(self, counter: _Optional[int] = ..., timestamp: _Optional[int] = ..., trace_context: _Optional[_Union[_trace_context_pb2.TraceContext, _Mapping]] = ..., is_ignored: _Optional[bool] = ..., underlying: _Optional[bytes] = ...) -> None: ...

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

class SequencingSubmissionCost(_message.Message):
    __slots__ = ("cost",)
    COST_FIELD_NUMBER: _ClassVar[int]
    cost: int
    def __init__(self, cost: _Optional[int] = ...) -> None: ...

class StaticSynchronizerParameters(_message.Message):
    __slots__ = ("required_signing_specs", "required_encryption_specs", "required_symmetric_key_schemes", "required_hash_algorithms", "required_crypto_key_formats", "required_signature_formats", "protocol_version", "serial", "enable_transparency_checks", "topology_change_delay")
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
    def __init__(self, required_signing_specs: _Optional[_Union[_crypto_pb2.RequiredSigningSpecs, _Mapping]] = ..., required_encryption_specs: _Optional[_Union[_crypto_pb2.RequiredEncryptionSpecs, _Mapping]] = ..., required_symmetric_key_schemes: _Optional[_Iterable[_Union[_crypto_pb2.SymmetricKeyScheme, str]]] = ..., required_hash_algorithms: _Optional[_Iterable[_Union[_crypto_pb2.HashAlgorithm, str]]] = ..., required_crypto_key_formats: _Optional[_Iterable[_Union[_crypto_pb2.CryptoKeyFormat, str]]] = ..., required_signature_formats: _Optional[_Iterable[_Union[_crypto_pb2.SignatureFormat, str]]] = ..., protocol_version: _Optional[int] = ..., serial: _Optional[int] = ..., enable_transparency_checks: _Optional[bool] = ..., topology_change_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class CompressedBatch(_message.Message):
    __slots__ = ()
    class CompressionAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPRESSION_ALGORITHM_UNSPECIFIED: _ClassVar[CompressedBatch.CompressionAlgorithm]
        COMPRESSION_ALGORITHM_GZIP: _ClassVar[CompressedBatch.CompressionAlgorithm]
    COMPRESSION_ALGORITHM_UNSPECIFIED: CompressedBatch.CompressionAlgorithm
    COMPRESSION_ALGORITHM_GZIP: CompressedBatch.CompressionAlgorithm
    def __init__(self) -> None: ...
