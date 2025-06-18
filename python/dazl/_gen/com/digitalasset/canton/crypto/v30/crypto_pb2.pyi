# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HashAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HASH_ALGORITHM_UNSPECIFIED: _ClassVar[HashAlgorithm]
    HASH_ALGORITHM_SHA256: _ClassVar[HashAlgorithm]

class HmacAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HMAC_ALGORITHM_UNSPECIFIED: _ClassVar[HmacAlgorithm]
    HMAC_ALGORITHM_HMAC_SHA256: _ClassVar[HmacAlgorithm]

class SignatureFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_FORMAT_UNSPECIFIED: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_RAW: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_DER: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_CONCAT: _ClassVar[SignatureFormat]
    SIGNATURE_FORMAT_SYMBOLIC: _ClassVar[SignatureFormat]

class EncryptionKeySpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCRYPTION_KEY_SPEC_UNSPECIFIED: _ClassVar[EncryptionKeySpec]
    ENCRYPTION_KEY_SPEC_EC_P256: _ClassVar[EncryptionKeySpec]
    ENCRYPTION_KEY_SPEC_RSA_2048: _ClassVar[EncryptionKeySpec]

class SigningKeySpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNING_KEY_SPEC_UNSPECIFIED: _ClassVar[SigningKeySpec]
    SIGNING_KEY_SPEC_EC_CURVE25519: _ClassVar[SigningKeySpec]
    SIGNING_KEY_SPEC_EC_P256: _ClassVar[SigningKeySpec]
    SIGNING_KEY_SPEC_EC_P384: _ClassVar[SigningKeySpec]
    SIGNING_KEY_SPEC_EC_SECP256K1: _ClassVar[SigningKeySpec]

class KeyPurpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_PURPOSE_UNSPECIFIED: _ClassVar[KeyPurpose]
    KEY_PURPOSE_SIGNING: _ClassVar[KeyPurpose]
    KEY_PURPOSE_ENCRYPTION: _ClassVar[KeyPurpose]

class SigningKeyUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNING_KEY_USAGE_UNSPECIFIED: _ClassVar[SigningKeyUsage]
    SIGNING_KEY_USAGE_NAMESPACE: _ClassVar[SigningKeyUsage]
    SIGNING_KEY_USAGE_IDENTITY_DELEGATION: _ClassVar[SigningKeyUsage]
    SIGNING_KEY_USAGE_SEQUENCER_AUTHENTICATION: _ClassVar[SigningKeyUsage]
    SIGNING_KEY_USAGE_PROTOCOL: _ClassVar[SigningKeyUsage]
    SIGNING_KEY_USAGE_PROOF_OF_OWNERSHIP: _ClassVar[SigningKeyUsage]

class SigningAlgorithmSpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNING_ALGORITHM_SPEC_UNSPECIFIED: _ClassVar[SigningAlgorithmSpec]
    SIGNING_ALGORITHM_SPEC_ED25519: _ClassVar[SigningAlgorithmSpec]
    SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256: _ClassVar[SigningAlgorithmSpec]
    SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384: _ClassVar[SigningAlgorithmSpec]

class SigningKeyScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNING_KEY_SCHEME_UNSPECIFIED: _ClassVar[SigningKeyScheme]
    SIGNING_KEY_SCHEME_ED25519: _ClassVar[SigningKeyScheme]
    SIGNING_KEY_SCHEME_EC_DSA_P256: _ClassVar[SigningKeyScheme]
    SIGNING_KEY_SCHEME_EC_DSA_P384: _ClassVar[SigningKeyScheme]

class EncryptionAlgorithmSpec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCRYPTION_ALGORITHM_SPEC_UNSPECIFIED: _ClassVar[EncryptionAlgorithmSpec]
    ENCRYPTION_ALGORITHM_SPEC_ECIES_HKDF_HMAC_SHA256_AES128GCM: _ClassVar[EncryptionAlgorithmSpec]
    ENCRYPTION_ALGORITHM_SPEC_ECIES_HKDF_HMAC_SHA256_AES128CBC: _ClassVar[EncryptionAlgorithmSpec]
    ENCRYPTION_ALGORITHM_SPEC_RSA_OAEP_SHA256: _ClassVar[EncryptionAlgorithmSpec]

class EncryptionKeyScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCRYPTION_KEY_SCHEME_UNSPECIFIED: _ClassVar[EncryptionKeyScheme]
    ENCRYPTION_KEY_SCHEME_ECIES_P256_HKDF_HMAC_SHA256_AES128GCM: _ClassVar[EncryptionKeyScheme]
    ENCRYPTION_KEY_SCHEME_ECIES_P256_HMAC_SHA256A_ES128CBC: _ClassVar[EncryptionKeyScheme]
    ENCRYPTION_KEY_SCHEME_RSA2048_OAEP_SHA256: _ClassVar[EncryptionKeyScheme]

class SymmetricKeyScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYMMETRIC_KEY_SCHEME_UNSPECIFIED: _ClassVar[SymmetricKeyScheme]
    SYMMETRIC_KEY_SCHEME_AES128GCM: _ClassVar[SymmetricKeyScheme]

class CryptoKeyFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CRYPTO_KEY_FORMAT_UNSPECIFIED: _ClassVar[CryptoKeyFormat]
    CRYPTO_KEY_FORMAT_DER: _ClassVar[CryptoKeyFormat]
    CRYPTO_KEY_FORMAT_RAW: _ClassVar[CryptoKeyFormat]
    CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO: _ClassVar[CryptoKeyFormat]
    CRYPTO_KEY_FORMAT_DER_PKCS8_PRIVATE_KEY_INFO: _ClassVar[CryptoKeyFormat]
    CRYPTO_KEY_FORMAT_SYMBOLIC: _ClassVar[CryptoKeyFormat]

class PbkdfScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PBKDF_SCHEME_UNSPECIFIED: _ClassVar[PbkdfScheme]
    PBKDF_SCHEME_ARGON2ID_MODE1: _ClassVar[PbkdfScheme]
HASH_ALGORITHM_UNSPECIFIED: HashAlgorithm
HASH_ALGORITHM_SHA256: HashAlgorithm
HMAC_ALGORITHM_UNSPECIFIED: HmacAlgorithm
HMAC_ALGORITHM_HMAC_SHA256: HmacAlgorithm
SIGNATURE_FORMAT_UNSPECIFIED: SignatureFormat
SIGNATURE_FORMAT_RAW: SignatureFormat
SIGNATURE_FORMAT_DER: SignatureFormat
SIGNATURE_FORMAT_CONCAT: SignatureFormat
SIGNATURE_FORMAT_SYMBOLIC: SignatureFormat
ENCRYPTION_KEY_SPEC_UNSPECIFIED: EncryptionKeySpec
ENCRYPTION_KEY_SPEC_EC_P256: EncryptionKeySpec
ENCRYPTION_KEY_SPEC_RSA_2048: EncryptionKeySpec
SIGNING_KEY_SPEC_UNSPECIFIED: SigningKeySpec
SIGNING_KEY_SPEC_EC_CURVE25519: SigningKeySpec
SIGNING_KEY_SPEC_EC_P256: SigningKeySpec
SIGNING_KEY_SPEC_EC_P384: SigningKeySpec
SIGNING_KEY_SPEC_EC_SECP256K1: SigningKeySpec
KEY_PURPOSE_UNSPECIFIED: KeyPurpose
KEY_PURPOSE_SIGNING: KeyPurpose
KEY_PURPOSE_ENCRYPTION: KeyPurpose
SIGNING_KEY_USAGE_UNSPECIFIED: SigningKeyUsage
SIGNING_KEY_USAGE_NAMESPACE: SigningKeyUsage
SIGNING_KEY_USAGE_IDENTITY_DELEGATION: SigningKeyUsage
SIGNING_KEY_USAGE_SEQUENCER_AUTHENTICATION: SigningKeyUsage
SIGNING_KEY_USAGE_PROTOCOL: SigningKeyUsage
SIGNING_KEY_USAGE_PROOF_OF_OWNERSHIP: SigningKeyUsage
SIGNING_ALGORITHM_SPEC_UNSPECIFIED: SigningAlgorithmSpec
SIGNING_ALGORITHM_SPEC_ED25519: SigningAlgorithmSpec
SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256: SigningAlgorithmSpec
SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384: SigningAlgorithmSpec
SIGNING_KEY_SCHEME_UNSPECIFIED: SigningKeyScheme
SIGNING_KEY_SCHEME_ED25519: SigningKeyScheme
SIGNING_KEY_SCHEME_EC_DSA_P256: SigningKeyScheme
SIGNING_KEY_SCHEME_EC_DSA_P384: SigningKeyScheme
ENCRYPTION_ALGORITHM_SPEC_UNSPECIFIED: EncryptionAlgorithmSpec
ENCRYPTION_ALGORITHM_SPEC_ECIES_HKDF_HMAC_SHA256_AES128GCM: EncryptionAlgorithmSpec
ENCRYPTION_ALGORITHM_SPEC_ECIES_HKDF_HMAC_SHA256_AES128CBC: EncryptionAlgorithmSpec
ENCRYPTION_ALGORITHM_SPEC_RSA_OAEP_SHA256: EncryptionAlgorithmSpec
ENCRYPTION_KEY_SCHEME_UNSPECIFIED: EncryptionKeyScheme
ENCRYPTION_KEY_SCHEME_ECIES_P256_HKDF_HMAC_SHA256_AES128GCM: EncryptionKeyScheme
ENCRYPTION_KEY_SCHEME_ECIES_P256_HMAC_SHA256A_ES128CBC: EncryptionKeyScheme
ENCRYPTION_KEY_SCHEME_RSA2048_OAEP_SHA256: EncryptionKeyScheme
SYMMETRIC_KEY_SCHEME_UNSPECIFIED: SymmetricKeyScheme
SYMMETRIC_KEY_SCHEME_AES128GCM: SymmetricKeyScheme
CRYPTO_KEY_FORMAT_UNSPECIFIED: CryptoKeyFormat
CRYPTO_KEY_FORMAT_DER: CryptoKeyFormat
CRYPTO_KEY_FORMAT_RAW: CryptoKeyFormat
CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO: CryptoKeyFormat
CRYPTO_KEY_FORMAT_DER_PKCS8_PRIVATE_KEY_INFO: CryptoKeyFormat
CRYPTO_KEY_FORMAT_SYMBOLIC: CryptoKeyFormat
PBKDF_SCHEME_UNSPECIFIED: PbkdfScheme
PBKDF_SCHEME_ARGON2ID_MODE1: PbkdfScheme

class Hmac(_message.Message):
    __slots__ = ("algorithm", "hmac")
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    HMAC_FIELD_NUMBER: _ClassVar[int]
    algorithm: HmacAlgorithm
    hmac: bytes
    def __init__(self, algorithm: _Optional[_Union[HmacAlgorithm, str]] = ..., hmac: _Optional[bytes] = ...) -> None: ...

class Salt(_message.Message):
    __slots__ = ("hmac", "salt")
    HMAC_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    hmac: HmacAlgorithm
    salt: bytes
    def __init__(self, hmac: _Optional[_Union[HmacAlgorithm, str]] = ..., salt: _Optional[bytes] = ...) -> None: ...

class Signature(_message.Message):
    __slots__ = ("format", "signature", "signed_by", "signing_algorithm_spec", "signature_delegation")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    SIGNING_ALGORITHM_SPEC_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_DELEGATION_FIELD_NUMBER: _ClassVar[int]
    format: SignatureFormat
    signature: bytes
    signed_by: str
    signing_algorithm_spec: SigningAlgorithmSpec
    signature_delegation: SignatureDelegation
    def __init__(self, format: _Optional[_Union[SignatureFormat, str]] = ..., signature: _Optional[bytes] = ..., signed_by: _Optional[str] = ..., signing_algorithm_spec: _Optional[_Union[SigningAlgorithmSpec, str]] = ..., signature_delegation: _Optional[_Union[SignatureDelegation, _Mapping]] = ...) -> None: ...

class SignatureDelegation(_message.Message):
    __slots__ = ("session_key", "session_key_spec", "validity_period_from_inclusive", "validity_period_duration_seconds", "format", "signature", "signing_algorithm_spec")
    SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_SPEC_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_PERIOD_FROM_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_PERIOD_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNING_ALGORITHM_SPEC_FIELD_NUMBER: _ClassVar[int]
    session_key: bytes
    session_key_spec: SigningKeySpec
    validity_period_from_inclusive: int
    validity_period_duration_seconds: int
    format: SignatureFormat
    signature: bytes
    signing_algorithm_spec: SigningAlgorithmSpec
    def __init__(self, session_key: _Optional[bytes] = ..., session_key_spec: _Optional[_Union[SigningKeySpec, str]] = ..., validity_period_from_inclusive: _Optional[int] = ..., validity_period_duration_seconds: _Optional[int] = ..., format: _Optional[_Union[SignatureFormat, str]] = ..., signature: _Optional[bytes] = ..., signing_algorithm_spec: _Optional[_Union[SigningAlgorithmSpec, str]] = ...) -> None: ...

class PublicKey(_message.Message):
    __slots__ = ("signing_public_key", "encryption_public_key")
    SIGNING_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    signing_public_key: SigningPublicKey
    encryption_public_key: EncryptionPublicKey
    def __init__(self, signing_public_key: _Optional[_Union[SigningPublicKey, _Mapping]] = ..., encryption_public_key: _Optional[_Union[EncryptionPublicKey, _Mapping]] = ...) -> None: ...

class PublicKeyWithName(_message.Message):
    __slots__ = ("public_key", "name")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    public_key: PublicKey
    name: str
    def __init__(self, public_key: _Optional[_Union[PublicKey, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class PrivateKey(_message.Message):
    __slots__ = ("signing_private_key", "encryption_private_key")
    SIGNING_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    signing_private_key: SigningPrivateKey
    encryption_private_key: EncryptionPrivateKey
    def __init__(self, signing_private_key: _Optional[_Union[SigningPrivateKey, _Mapping]] = ..., encryption_private_key: _Optional[_Union[EncryptionPrivateKey, _Mapping]] = ...) -> None: ...

class SigningPublicKey(_message.Message):
    __slots__ = ("format", "public_key", "scheme", "usage", "key_spec")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_SPEC_FIELD_NUMBER: _ClassVar[int]
    format: CryptoKeyFormat
    public_key: bytes
    scheme: SigningKeyScheme
    usage: _containers.RepeatedScalarFieldContainer[SigningKeyUsage]
    key_spec: SigningKeySpec
    def __init__(self, format: _Optional[_Union[CryptoKeyFormat, str]] = ..., public_key: _Optional[bytes] = ..., scheme: _Optional[_Union[SigningKeyScheme, str]] = ..., usage: _Optional[_Iterable[_Union[SigningKeyUsage, str]]] = ..., key_spec: _Optional[_Union[SigningKeySpec, str]] = ...) -> None: ...

class SigningPrivateKey(_message.Message):
    __slots__ = ("id", "format", "private_key", "scheme", "usage", "key_spec")
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_SPEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    format: CryptoKeyFormat
    private_key: bytes
    scheme: SigningKeyScheme
    usage: _containers.RepeatedScalarFieldContainer[SigningKeyUsage]
    key_spec: SigningKeySpec
    def __init__(self, id: _Optional[str] = ..., format: _Optional[_Union[CryptoKeyFormat, str]] = ..., private_key: _Optional[bytes] = ..., scheme: _Optional[_Union[SigningKeyScheme, str]] = ..., usage: _Optional[_Iterable[_Union[SigningKeyUsage, str]]] = ..., key_spec: _Optional[_Union[SigningKeySpec, str]] = ...) -> None: ...

class SigningKeyPair(_message.Message):
    __slots__ = ("public_key", "private_key")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: SigningPublicKey
    private_key: SigningPrivateKey
    def __init__(self, public_key: _Optional[_Union[SigningPublicKey, _Mapping]] = ..., private_key: _Optional[_Union[SigningPrivateKey, _Mapping]] = ...) -> None: ...

class RequiredSigningSpecs(_message.Message):
    __slots__ = ("algorithms", "keys")
    ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    algorithms: _containers.RepeatedScalarFieldContainer[SigningAlgorithmSpec]
    keys: _containers.RepeatedScalarFieldContainer[SigningKeySpec]
    def __init__(self, algorithms: _Optional[_Iterable[_Union[SigningAlgorithmSpec, str]]] = ..., keys: _Optional[_Iterable[_Union[SigningKeySpec, str]]] = ...) -> None: ...

class EncryptionPublicKey(_message.Message):
    __slots__ = ("format", "public_key", "scheme", "key_spec")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    KEY_SPEC_FIELD_NUMBER: _ClassVar[int]
    format: CryptoKeyFormat
    public_key: bytes
    scheme: EncryptionKeyScheme
    key_spec: EncryptionKeySpec
    def __init__(self, format: _Optional[_Union[CryptoKeyFormat, str]] = ..., public_key: _Optional[bytes] = ..., scheme: _Optional[_Union[EncryptionKeyScheme, str]] = ..., key_spec: _Optional[_Union[EncryptionKeySpec, str]] = ...) -> None: ...

class EncryptionPrivateKey(_message.Message):
    __slots__ = ("id", "format", "private_key", "scheme", "key_spec")
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    KEY_SPEC_FIELD_NUMBER: _ClassVar[int]
    id: str
    format: CryptoKeyFormat
    private_key: bytes
    scheme: EncryptionKeyScheme
    key_spec: EncryptionKeySpec
    def __init__(self, id: _Optional[str] = ..., format: _Optional[_Union[CryptoKeyFormat, str]] = ..., private_key: _Optional[bytes] = ..., scheme: _Optional[_Union[EncryptionKeyScheme, str]] = ..., key_spec: _Optional[_Union[EncryptionKeySpec, str]] = ...) -> None: ...

class EncryptionKeyPair(_message.Message):
    __slots__ = ("public_key", "private_key")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: EncryptionPublicKey
    private_key: EncryptionPrivateKey
    def __init__(self, public_key: _Optional[_Union[EncryptionPublicKey, _Mapping]] = ..., private_key: _Optional[_Union[EncryptionPrivateKey, _Mapping]] = ...) -> None: ...

class RequiredEncryptionSpecs(_message.Message):
    __slots__ = ("algorithms", "keys")
    ALGORITHMS_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    algorithms: _containers.RepeatedScalarFieldContainer[EncryptionAlgorithmSpec]
    keys: _containers.RepeatedScalarFieldContainer[EncryptionKeySpec]
    def __init__(self, algorithms: _Optional[_Iterable[_Union[EncryptionAlgorithmSpec, str]]] = ..., keys: _Optional[_Iterable[_Union[EncryptionKeySpec, str]]] = ...) -> None: ...

class CryptoKeyPair(_message.Message):
    __slots__ = ("signing_key_pair", "encryption_key_pair")
    SIGNING_KEY_PAIR_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_PAIR_FIELD_NUMBER: _ClassVar[int]
    signing_key_pair: SigningKeyPair
    encryption_key_pair: EncryptionKeyPair
    def __init__(self, signing_key_pair: _Optional[_Union[SigningKeyPair, _Mapping]] = ..., encryption_key_pair: _Optional[_Union[EncryptionKeyPair, _Mapping]] = ...) -> None: ...

class SymmetricKey(_message.Message):
    __slots__ = ("format", "key", "scheme")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    format: CryptoKeyFormat
    key: bytes
    scheme: SymmetricKeyScheme
    def __init__(self, format: _Optional[_Union[CryptoKeyFormat, str]] = ..., key: _Optional[bytes] = ..., scheme: _Optional[_Union[SymmetricKeyScheme, str]] = ...) -> None: ...

class PasswordBasedEncrypted(_message.Message):
    __slots__ = ("ciphertext", "symmetric_key_scheme", "pbkdf_scheme", "salt")
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    SYMMETRIC_KEY_SCHEME_FIELD_NUMBER: _ClassVar[int]
    PBKDF_SCHEME_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    ciphertext: bytes
    symmetric_key_scheme: SymmetricKeyScheme
    pbkdf_scheme: PbkdfScheme
    salt: bytes
    def __init__(self, ciphertext: _Optional[bytes] = ..., symmetric_key_scheme: _Optional[_Union[SymmetricKeyScheme, str]] = ..., pbkdf_scheme: _Optional[_Union[PbkdfScheme, str]] = ..., salt: _Optional[bytes] = ...) -> None: ...

class AsymmetricEncrypted(_message.Message):
    __slots__ = ("ciphertext", "encryption_algorithm_spec", "fingerprint")
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ALGORITHM_SPEC_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    ciphertext: bytes
    encryption_algorithm_spec: EncryptionAlgorithmSpec
    fingerprint: str
    def __init__(self, ciphertext: _Optional[bytes] = ..., encryption_algorithm_spec: _Optional[_Union[EncryptionAlgorithmSpec, str]] = ..., fingerprint: _Optional[str] = ...) -> None: ...
