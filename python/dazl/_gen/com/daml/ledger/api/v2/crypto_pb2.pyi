# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SigningKeySpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNING_KEY_SPEC_UNSPECIFIED: _ClassVar[SigningKeySpec]
    SIGNING_KEY_SPEC_EC_CURVE25519: _ClassVar[SigningKeySpec]
    SIGNING_KEY_SPEC_EC_P256: _ClassVar[SigningKeySpec]
    SIGNING_KEY_SPEC_EC_P384: _ClassVar[SigningKeySpec]
    SIGNING_KEY_SPEC_EC_SECP256K1: _ClassVar[SigningKeySpec]

class CryptoKeyFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CRYPTO_KEY_FORMAT_UNSPECIFIED: _ClassVar[CryptoKeyFormat]
    CRYPTO_KEY_FORMAT_DER: _ClassVar[CryptoKeyFormat]
    CRYPTO_KEY_FORMAT_RAW: _ClassVar[CryptoKeyFormat]
    CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO: _ClassVar[CryptoKeyFormat]

class SigningAlgorithmSpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNING_ALGORITHM_SPEC_UNSPECIFIED: _ClassVar[SigningAlgorithmSpec]
    SIGNING_ALGORITHM_SPEC_ED25519: _ClassVar[SigningAlgorithmSpec]
    SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256: _ClassVar[SigningAlgorithmSpec]
    SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384: _ClassVar[SigningAlgorithmSpec]

class SignatureFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_FORMAT_UNSPECIFIED: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_RAW: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_DER: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_CONCAT: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_SYMBOLIC: _ClassVar[SignatureFormat]
SIGNING_KEY_SPEC_UNSPECIFIED: SigningKeySpec
SIGNING_KEY_SPEC_EC_CURVE25519: SigningKeySpec
SIGNING_KEY_SPEC_EC_P256: SigningKeySpec
SIGNING_KEY_SPEC_EC_P384: SigningKeySpec
SIGNING_KEY_SPEC_EC_SECP256K1: SigningKeySpec
CRYPTO_KEY_FORMAT_UNSPECIFIED: CryptoKeyFormat
CRYPTO_KEY_FORMAT_DER: CryptoKeyFormat
CRYPTO_KEY_FORMAT_RAW: CryptoKeyFormat
CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO: CryptoKeyFormat
SIGNING_ALGORITHM_SPEC_UNSPECIFIED: SigningAlgorithmSpec
SIGNING_ALGORITHM_SPEC_ED25519: SigningAlgorithmSpec
SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256: SigningAlgorithmSpec
SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384: SigningAlgorithmSpec
SIGNATURE_FORMAT_UNSPECIFIED: SignatureFormat
SIGNATURE_FORMAT_RAW: SignatureFormat
SIGNATURE_FORMAT_DER: SignatureFormat
SIGNATURE_FORMAT_CONCAT: SignatureFormat
SIGNATURE_FORMAT_SYMBOLIC: SignatureFormat

class SigningPublicKey(_message.Message):
    __slots__ = ("format", "key_data", "key_spec")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    KEY_SPEC_FIELD_NUMBER: _ClassVar[int]
    format: CryptoKeyFormat
    key_data: bytes
    key_spec: SigningKeySpec
    def __init__(self, format: _Optional[_Union[CryptoKeyFormat, str]] = ..., key_data: _Optional[bytes] = ..., key_spec: _Optional[_Union[SigningKeySpec, str]] = ...) -> None: ...

class Signature(_message.Message):
    __slots__ = ("format", "signature", "signed_by", "signing_algorithm_spec")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    SIGNING_ALGORITHM_SPEC_FIELD_NUMBER: _ClassVar[int]
    format: SignatureFormat
    signature: bytes
    signed_by: str
    signing_algorithm_spec: SigningAlgorithmSpec
    def __init__(self, format: _Optional[_Union[SignatureFormat, str]] = ..., signature: _Optional[bytes] = ..., signed_by: _Optional[str] = ..., signing_algorithm_spec: _Optional[_Union[SigningAlgorithmSpec, str]] = ...) -> None: ...
