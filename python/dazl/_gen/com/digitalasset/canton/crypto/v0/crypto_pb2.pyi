# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HashAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingHashAlgorithm: _ClassVar[HashAlgorithm]
    Sha256: _ClassVar[HashAlgorithm]

class HmacAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingHmacAlgorithm: _ClassVar[HmacAlgorithm]
    HmacSha256: _ClassVar[HmacAlgorithm]

class SignatureFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingSignatureFormat: _ClassVar[SignatureFormat]
    RawSignatureFormat: _ClassVar[SignatureFormat]

class KeyPurpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    UnknownKeyPurpose: _ClassVar[KeyPurpose]
    SigningKeyPurpose: _ClassVar[KeyPurpose]
    EncryptionKeyPurpose: _ClassVar[KeyPurpose]

class SigningKeyScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingSigningKeyScheme: _ClassVar[SigningKeyScheme]
    Ed25519: _ClassVar[SigningKeyScheme]
    EcDsaP256: _ClassVar[SigningKeyScheme]
    EcDsaP384: _ClassVar[SigningKeyScheme]
    Sm2: _ClassVar[SigningKeyScheme]

class EncryptionKeyScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingEncryptionKeyScheme: _ClassVar[EncryptionKeyScheme]
    EciesP256HkdfHmacSha256Aes128Gcm: _ClassVar[EncryptionKeyScheme]
    EciesP256HmacSha256Aes128Cbc: _ClassVar[EncryptionKeyScheme]
    Rsa2048OaepSha256: _ClassVar[EncryptionKeyScheme]

class SymmetricKeyScheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingSymmetricKeyScheme: _ClassVar[SymmetricKeyScheme]
    Aes128Gcm: _ClassVar[SymmetricKeyScheme]

class CryptoKeyFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []  # type: ignore
    MissingCryptoKeyFormat: _ClassVar[CryptoKeyFormat]
    Tink: _ClassVar[CryptoKeyFormat]
    Der: _ClassVar[CryptoKeyFormat]
    Raw: _ClassVar[CryptoKeyFormat]
    Symbolic: _ClassVar[CryptoKeyFormat]
MissingHashAlgorithm: HashAlgorithm
Sha256: HashAlgorithm
MissingHmacAlgorithm: HmacAlgorithm
HmacSha256: HmacAlgorithm
MissingSignatureFormat: SignatureFormat
RawSignatureFormat: SignatureFormat
UnknownKeyPurpose: KeyPurpose
SigningKeyPurpose: KeyPurpose
EncryptionKeyPurpose: KeyPurpose
MissingSigningKeyScheme: SigningKeyScheme
Ed25519: SigningKeyScheme
EcDsaP256: SigningKeyScheme
EcDsaP384: SigningKeyScheme
Sm2: SigningKeyScheme
MissingEncryptionKeyScheme: EncryptionKeyScheme
EciesP256HkdfHmacSha256Aes128Gcm: EncryptionKeyScheme
EciesP256HmacSha256Aes128Cbc: EncryptionKeyScheme
Rsa2048OaepSha256: EncryptionKeyScheme
MissingSymmetricKeyScheme: SymmetricKeyScheme
Aes128Gcm: SymmetricKeyScheme
MissingCryptoKeyFormat: CryptoKeyFormat
Tink: CryptoKeyFormat
Der: CryptoKeyFormat
Raw: CryptoKeyFormat
Symbolic: CryptoKeyFormat

class Hmac(_message.Message):
    __slots__ = ["algorithm", "hmac"]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    HMAC_FIELD_NUMBER: _ClassVar[int]
    algorithm: HmacAlgorithm
    hmac: bytes
    def __init__(self, algorithm: _Optional[_Union[HmacAlgorithm, str]] = ..., hmac: _Optional[bytes] = ...) -> None: ...

class Salt(_message.Message):
    __slots__ = ["hmac", "salt"]
    HMAC_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    hmac: HmacAlgorithm
    salt: bytes
    def __init__(self, hmac: _Optional[_Union[HmacAlgorithm, str]] = ..., salt: _Optional[bytes] = ...) -> None: ...

class Signature(_message.Message):
    __slots__ = ["format", "signature", "signed_by"]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    format: SignatureFormat
    signature: bytes
    signed_by: str
    def __init__(self, format: _Optional[_Union[SignatureFormat, str]] = ..., signature: _Optional[bytes] = ..., signed_by: _Optional[str] = ...) -> None: ...

class PublicKey(_message.Message):
    __slots__ = ["signing_public_key", "encryption_public_key"]
    SIGNING_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    signing_public_key: SigningPublicKey
    encryption_public_key: EncryptionPublicKey
    def __init__(self, signing_public_key: _Optional[_Union[SigningPublicKey, _Mapping]] = ..., encryption_public_key: _Optional[_Union[EncryptionPublicKey, _Mapping]] = ...) -> None: ...

class PublicKeyWithName(_message.Message):
    __slots__ = ["public_key", "name"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    public_key: PublicKey
    name: str
    def __init__(self, public_key: _Optional[_Union[PublicKey, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class PrivateKey(_message.Message):
    __slots__ = ["signing_private_key", "encryption_private_key"]
    SIGNING_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    signing_private_key: SigningPrivateKey
    encryption_private_key: EncryptionPrivateKey
    def __init__(self, signing_private_key: _Optional[_Union[SigningPrivateKey, _Mapping]] = ..., encryption_private_key: _Optional[_Union[EncryptionPrivateKey, _Mapping]] = ...) -> None: ...

class SigningPublicKey(_message.Message):
    __slots__ = ["id", "format", "public_key", "scheme"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    id: str
    format: CryptoKeyFormat
    public_key: bytes
    scheme: SigningKeyScheme
    def __init__(self, id: _Optional[str] = ..., format: _Optional[_Union[CryptoKeyFormat, str]] = ..., public_key: _Optional[bytes] = ..., scheme: _Optional[_Union[SigningKeyScheme, str]] = ...) -> None: ...

class SigningPrivateKey(_message.Message):
    __slots__ = ["id", "format", "private_key", "scheme"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    id: str
    format: CryptoKeyFormat
    private_key: bytes
    scheme: SigningKeyScheme
    def __init__(self, id: _Optional[str] = ..., format: _Optional[_Union[CryptoKeyFormat, str]] = ..., private_key: _Optional[bytes] = ..., scheme: _Optional[_Union[SigningKeyScheme, str]] = ...) -> None: ...

class SigningKeyPair(_message.Message):
    __slots__ = ["public_key", "private_key"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: SigningPublicKey
    private_key: SigningPrivateKey
    def __init__(self, public_key: _Optional[_Union[SigningPublicKey, _Mapping]] = ..., private_key: _Optional[_Union[SigningPrivateKey, _Mapping]] = ...) -> None: ...

class EncryptionPublicKey(_message.Message):
    __slots__ = ["id", "format", "public_key", "scheme"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    id: str
    format: CryptoKeyFormat
    public_key: bytes
    scheme: EncryptionKeyScheme
    def __init__(self, id: _Optional[str] = ..., format: _Optional[_Union[CryptoKeyFormat, str]] = ..., public_key: _Optional[bytes] = ..., scheme: _Optional[_Union[EncryptionKeyScheme, str]] = ...) -> None: ...

class EncryptionPrivateKey(_message.Message):
    __slots__ = ["id", "format", "private_key", "scheme"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    id: str
    format: CryptoKeyFormat
    private_key: bytes
    scheme: EncryptionKeyScheme
    def __init__(self, id: _Optional[str] = ..., format: _Optional[_Union[CryptoKeyFormat, str]] = ..., private_key: _Optional[bytes] = ..., scheme: _Optional[_Union[EncryptionKeyScheme, str]] = ...) -> None: ...

class EncryptionKeyPair(_message.Message):
    __slots__ = ["public_key", "private_key"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: EncryptionPublicKey
    private_key: EncryptionPrivateKey
    def __init__(self, public_key: _Optional[_Union[EncryptionPublicKey, _Mapping]] = ..., private_key: _Optional[_Union[EncryptionPrivateKey, _Mapping]] = ...) -> None: ...

class CryptoKeyPair(_message.Message):
    __slots__ = ["signing_key_pair", "encryption_key_pair"]
    SIGNING_KEY_PAIR_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_PAIR_FIELD_NUMBER: _ClassVar[int]
    signing_key_pair: SigningKeyPair
    encryption_key_pair: EncryptionKeyPair
    def __init__(self, signing_key_pair: _Optional[_Union[SigningKeyPair, _Mapping]] = ..., encryption_key_pair: _Optional[_Union[EncryptionKeyPair, _Mapping]] = ...) -> None: ...

class SymmetricKey(_message.Message):
    __slots__ = ["format", "key", "scheme"]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    format: CryptoKeyFormat
    key: bytes
    scheme: SymmetricKeyScheme
    def __init__(self, format: _Optional[_Union[CryptoKeyFormat, str]] = ..., key: _Optional[bytes] = ..., scheme: _Optional[_Union[SymmetricKeyScheme, str]] = ...) -> None: ...
