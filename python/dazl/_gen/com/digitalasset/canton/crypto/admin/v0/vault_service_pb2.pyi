# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from ...v0 import crypto_pb2 as _crypto_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateCertificateRequest(_message.Message):
    __slots__ = ["unique_identifier", "certificate_key", "additional_subject", "subject_alternative_names"]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_KEY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ALTERNATIVE_NAMES_FIELD_NUMBER: _ClassVar[int]
    unique_identifier: str
    certificate_key: str
    additional_subject: str
    subject_alternative_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, unique_identifier: _Optional[str] = ..., certificate_key: _Optional[str] = ..., additional_subject: _Optional[str] = ..., subject_alternative_names: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateCertificateResponse(_message.Message):
    __slots__ = ["x509_cert"]
    X509_CERT_FIELD_NUMBER: _ClassVar[int]
    x509_cert: str
    def __init__(self, x509_cert: _Optional[str] = ...) -> None: ...

class ListCertificateRequest(_message.Message):
    __slots__ = ["filterUid"]
    FILTERUID_FIELD_NUMBER: _ClassVar[int]
    filterUid: str
    def __init__(self, filterUid: _Optional[str] = ...) -> None: ...

class ListCertificateResponse(_message.Message):
    __slots__ = ["results"]
    class Result(_message.Message):
        __slots__ = ["x509_cert"]
        X509_CERT_FIELD_NUMBER: _ClassVar[int]
        x509_cert: str
        def __init__(self, x509_cert: _Optional[str] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ListCertificateResponse.Result]
    def __init__(self, results: _Optional[_Iterable[_Union[ListCertificateResponse.Result, _Mapping]]] = ...) -> None: ...

class ImportCertificateRequest(_message.Message):
    __slots__ = ["x509_cert"]
    X509_CERT_FIELD_NUMBER: _ClassVar[int]
    x509_cert: str
    def __init__(self, x509_cert: _Optional[str] = ...) -> None: ...

class ImportCertificateResponse(_message.Message):
    __slots__ = ["certificate_id"]
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    def __init__(self, certificate_id: _Optional[str] = ...) -> None: ...

class ImportPublicKeyRequest(_message.Message):
    __slots__ = ["public_key", "name"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    name: str
    def __init__(self, public_key: _Optional[bytes] = ..., name: _Optional[str] = ...) -> None: ...

class ImportPublicKeyResponse(_message.Message):
    __slots__ = ["fingerprint"]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    fingerprint: str
    def __init__(self, fingerprint: _Optional[str] = ...) -> None: ...

class ListKeysRequest(_message.Message):
    __slots__ = ["filter_fingerprint", "filter_name", "filter_purpose"]
    FILTER_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_PURPOSE_FIELD_NUMBER: _ClassVar[int]
    filter_fingerprint: str
    filter_name: str
    filter_purpose: _containers.RepeatedScalarFieldContainer[_crypto_pb2.KeyPurpose]
    def __init__(self, filter_fingerprint: _Optional[str] = ..., filter_name: _Optional[str] = ..., filter_purpose: _Optional[_Iterable[_Union[_crypto_pb2.KeyPurpose, str]]] = ...) -> None: ...

class PrivateKeyMetadata(_message.Message):
    __slots__ = ["public_key_with_name", "wrapper_key_id"]
    PUBLIC_KEY_WITH_NAME_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    public_key_with_name: _crypto_pb2.PublicKeyWithName
    wrapper_key_id: str
    def __init__(self, public_key_with_name: _Optional[_Union[_crypto_pb2.PublicKeyWithName, _Mapping]] = ..., wrapper_key_id: _Optional[str] = ...) -> None: ...

class ListMyKeysResponse(_message.Message):
    __slots__ = ["private_keys_metadata"]
    PRIVATE_KEYS_METADATA_FIELD_NUMBER: _ClassVar[int]
    private_keys_metadata: _containers.RepeatedCompositeFieldContainer[PrivateKeyMetadata]
    def __init__(self, private_keys_metadata: _Optional[_Iterable[_Union[PrivateKeyMetadata, _Mapping]]] = ...) -> None: ...

class ListKeysResponse(_message.Message):
    __slots__ = ["public_keys"]
    PUBLIC_KEYS_FIELD_NUMBER: _ClassVar[int]
    public_keys: _containers.RepeatedCompositeFieldContainer[_crypto_pb2.PublicKeyWithName]
    def __init__(self, public_keys: _Optional[_Iterable[_Union[_crypto_pb2.PublicKeyWithName, _Mapping]]] = ...) -> None: ...

class GenerateSigningKeyRequest(_message.Message):
    __slots__ = ["key_scheme", "name"]
    KEY_SCHEME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    key_scheme: _crypto_pb2.SigningKeyScheme
    name: str
    def __init__(self, key_scheme: _Optional[_Union[_crypto_pb2.SigningKeyScheme, str]] = ..., name: _Optional[str] = ...) -> None: ...

class GenerateSigningKeyResponse(_message.Message):
    __slots__ = ["public_key"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: _crypto_pb2.SigningPublicKey
    def __init__(self, public_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ...) -> None: ...

class GenerateEncryptionKeyRequest(_message.Message):
    __slots__ = ["key_scheme", "name"]
    KEY_SCHEME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    key_scheme: _crypto_pb2.EncryptionKeyScheme
    name: str
    def __init__(self, key_scheme: _Optional[_Union[_crypto_pb2.EncryptionKeyScheme, str]] = ..., name: _Optional[str] = ...) -> None: ...

class GenerateEncryptionKeyResponse(_message.Message):
    __slots__ = ["public_key"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: _crypto_pb2.EncryptionPublicKey
    def __init__(self, public_key: _Optional[_Union[_crypto_pb2.EncryptionPublicKey, _Mapping]] = ...) -> None: ...

class RegisterKmsSigningKeyRequest(_message.Message):
    __slots__ = ["kms_key_id", "name"]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    kms_key_id: str
    name: str
    def __init__(self, kms_key_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RegisterKmsSigningKeyResponse(_message.Message):
    __slots__ = ["public_key"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: _crypto_pb2.SigningPublicKey
    def __init__(self, public_key: _Optional[_Union[_crypto_pb2.SigningPublicKey, _Mapping]] = ...) -> None: ...

class RegisterKmsEncryptionKeyRequest(_message.Message):
    __slots__ = ["kms_key_id", "name"]
    KMS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    kms_key_id: str
    name: str
    def __init__(self, kms_key_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RegisterKmsEncryptionKeyResponse(_message.Message):
    __slots__ = ["public_key"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    public_key: _crypto_pb2.EncryptionPublicKey
    def __init__(self, public_key: _Optional[_Union[_crypto_pb2.EncryptionPublicKey, _Mapping]] = ...) -> None: ...

class RotateWrapperKeyRequest(_message.Message):
    __slots__ = ["new_wrapper_key_id"]
    NEW_WRAPPER_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    new_wrapper_key_id: str
    def __init__(self, new_wrapper_key_id: _Optional[str] = ...) -> None: ...

class GetWrapperKeyIdRequest(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class GetWrapperKeyIdResponse(_message.Message):
    __slots__ = ["wrapper_key_id"]
    WRAPPER_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    wrapper_key_id: str
    def __init__(self, wrapper_key_id: _Optional[str] = ...) -> None: ...

class ExportKeyPairRequest(_message.Message):
    __slots__ = ["fingerprint", "protocol_version"]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    fingerprint: str
    protocol_version: int
    def __init__(self, fingerprint: _Optional[str] = ..., protocol_version: _Optional[int] = ...) -> None: ...

class ExportKeyPairResponse(_message.Message):
    __slots__ = ["key_pair"]
    KEY_PAIR_FIELD_NUMBER: _ClassVar[int]
    key_pair: bytes
    def __init__(self, key_pair: _Optional[bytes] = ...) -> None: ...

class ImportKeyPairRequest(_message.Message):
    __slots__ = ["key_pair", "name"]
    KEY_PAIR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    key_pair: bytes
    name: str
    def __init__(self, key_pair: _Optional[bytes] = ..., name: _Optional[str] = ...) -> None: ...

class ImportKeyPairResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...

class DeleteKeyPairRequest(_message.Message):
    __slots__ = ["fingerprint"]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    fingerprint: str
    def __init__(self, fingerprint: _Optional[str] = ...) -> None: ...

class DeleteKeyPairResponse(_message.Message):
    __slots__ = []  # type: ignore
    def __init__(self) -> None: ...
