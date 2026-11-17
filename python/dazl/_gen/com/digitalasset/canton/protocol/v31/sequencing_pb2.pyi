# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
import datetime

from ...crypto.v30 import crypto_pb2 as _crypto_pb2
from google.protobuf import duration_pb2 as _duration_pb2
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
