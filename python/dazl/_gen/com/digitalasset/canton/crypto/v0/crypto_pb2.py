# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: com/digitalasset/canton/crypto/v0/crypto.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'com/digitalasset/canton/crypto/v0/crypto.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.com/digitalasset/canton/crypto/v0/crypto.proto\x12!com.digitalasset.canton.crypto.v0\"j\n\x04Hmac\x12N\n\talgorithm\x18\x01 \x01(\x0e\x32\x30.com.digitalasset.canton.crypto.v0.HmacAlgorithmR\talgorithm\x12\x12\n\x04hmac\x18\x02 \x01(\x0cR\x04hmac\"o\n\x04Salt\x12\x46\n\x04hmac\x18\x01 \x01(\x0e\x32\x30.com.digitalasset.canton.crypto.v0.HmacAlgorithmH\x00R\x04hmac\x12\x12\n\x04salt\x18\x02 \x01(\x0cR\x04saltB\x0b\n\talgorithm\"\x92\x01\n\tSignature\x12J\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x32.com.digitalasset.canton.crypto.v0.SignatureFormatR\x06\x66ormat\x12\x1c\n\tsignature\x18\x02 \x01(\x0cR\tsignature\x12\x1b\n\tsigned_by\x18\x03 \x01(\tR\x08signedBy\"\xe5\x01\n\tPublicKey\x12\x63\n\x12signing_public_key\x18\x01 \x01(\x0b\x32\x33.com.digitalasset.canton.crypto.v0.SigningPublicKeyH\x00R\x10signingPublicKey\x12l\n\x15\x65ncryption_public_key\x18\x02 \x01(\x0b\x32\x36.com.digitalasset.canton.crypto.v0.EncryptionPublicKeyH\x00R\x13\x65ncryptionPublicKeyB\x05\n\x03key\"t\n\x11PublicKeyWithName\x12K\n\npublic_key\x18\x01 \x01(\x0b\x32,.com.digitalasset.canton.crypto.v0.PublicKeyR\tpublicKey\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\xec\x01\n\nPrivateKey\x12\x66\n\x13signing_private_key\x18\x01 \x01(\x0b\x32\x34.com.digitalasset.canton.crypto.v0.SigningPrivateKeyH\x00R\x11signingPrivateKey\x12o\n\x16\x65ncryption_private_key\x18\x02 \x01(\x0b\x32\x37.com.digitalasset.canton.crypto.v0.EncryptionPrivateKeyH\x00R\x14\x65ncryptionPrivateKeyB\x05\n\x03key\"\xda\x01\n\x10SigningPublicKey\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12J\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x32.com.digitalasset.canton.crypto.v0.CryptoKeyFormatR\x06\x66ormat\x12\x1d\n\npublic_key\x18\x03 \x01(\x0cR\tpublicKey\x12K\n\x06scheme\x18\x04 \x01(\x0e\x32\x33.com.digitalasset.canton.crypto.v0.SigningKeySchemeR\x06scheme\"\xdd\x01\n\x11SigningPrivateKey\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12J\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x32.com.digitalasset.canton.crypto.v0.CryptoKeyFormatR\x06\x66ormat\x12\x1f\n\x0bprivate_key\x18\x03 \x01(\x0cR\nprivateKey\x12K\n\x06scheme\x18\x04 \x01(\x0e\x32\x33.com.digitalasset.canton.crypto.v0.SigningKeySchemeR\x06scheme\"\xbb\x01\n\x0eSigningKeyPair\x12R\n\npublic_key\x18\x01 \x01(\x0b\x32\x33.com.digitalasset.canton.crypto.v0.SigningPublicKeyR\tpublicKey\x12U\n\x0bprivate_key\x18\x02 \x01(\x0b\x32\x34.com.digitalasset.canton.crypto.v0.SigningPrivateKeyR\nprivateKey\"\xe0\x01\n\x13\x45ncryptionPublicKey\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12J\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x32.com.digitalasset.canton.crypto.v0.CryptoKeyFormatR\x06\x66ormat\x12\x1d\n\npublic_key\x18\x03 \x01(\x0cR\tpublicKey\x12N\n\x06scheme\x18\x04 \x01(\x0e\x32\x36.com.digitalasset.canton.crypto.v0.EncryptionKeySchemeR\x06scheme\"\xe3\x01\n\x14\x45ncryptionPrivateKey\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12J\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x32.com.digitalasset.canton.crypto.v0.CryptoKeyFormatR\x06\x66ormat\x12\x1f\n\x0bprivate_key\x18\x03 \x01(\x0cR\nprivateKey\x12N\n\x06scheme\x18\x04 \x01(\x0e\x32\x36.com.digitalasset.canton.crypto.v0.EncryptionKeySchemeR\x06scheme\"\xc4\x01\n\x11\x45ncryptionKeyPair\x12U\n\npublic_key\x18\x01 \x01(\x0b\x32\x36.com.digitalasset.canton.crypto.v0.EncryptionPublicKeyR\tpublicKey\x12X\n\x0bprivate_key\x18\x02 \x01(\x0b\x32\x37.com.digitalasset.canton.crypto.v0.EncryptionPrivateKeyR\nprivateKey\"\xde\x01\n\rCryptoKeyPair\x12]\n\x10signing_key_pair\x18\x01 \x01(\x0b\x32\x31.com.digitalasset.canton.crypto.v0.SigningKeyPairH\x00R\x0esigningKeyPair\x12\x66\n\x13\x65ncryption_key_pair\x18\x02 \x01(\x0b\x32\x34.com.digitalasset.canton.crypto.v0.EncryptionKeyPairH\x00R\x11\x65ncryptionKeyPairB\x06\n\x04pair\"\xbb\x01\n\x0cSymmetricKey\x12J\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x32.com.digitalasset.canton.crypto.v0.CryptoKeyFormatR\x06\x66ormat\x12\x10\n\x03key\x18\x02 \x01(\x0cR\x03key\x12M\n\x06scheme\x18\x03 \x01(\x0e\x32\x35.com.digitalasset.canton.crypto.v0.SymmetricKeySchemeR\x06scheme*5\n\rHashAlgorithm\x12\x18\n\x14MissingHashAlgorithm\x10\x00\x12\n\n\x06Sha256\x10\x01*9\n\rHmacAlgorithm\x12\x18\n\x14MissingHmacAlgorithm\x10\x00\x12\x0e\n\nHmacSha256\x10\x01*E\n\x0fSignatureFormat\x12\x1a\n\x16MissingSignatureFormat\x10\x00\x12\x16\n\x12RawSignatureFormat\x10\x01*T\n\nKeyPurpose\x12\x15\n\x11UnknownKeyPurpose\x10\x00\x12\x15\n\x11SigningKeyPurpose\x10\x01\x12\x18\n\x14\x45ncryptionKeyPurpose\x10\x02*c\n\x10SigningKeyScheme\x12\x1b\n\x17MissingSigningKeyScheme\x10\x00\x12\x0b\n\x07\x45\x64\x32\x35\x35\x31\x39\x10\x01\x12\r\n\tEcDsaP256\x10\x02\x12\r\n\tEcDsaP384\x10\x03\x12\x07\n\x03Sm2\x10\x04*\x94\x01\n\x13\x45ncryptionKeyScheme\x12\x1e\n\x1aMissingEncryptionKeyScheme\x10\x00\x12$\n EciesP256HkdfHmacSha256Aes128Gcm\x10\x01\x12 \n\x1c\x45\x63iesP256HmacSha256Aes128Cbc\x10\x02\x12\x15\n\x11Rsa2048OaepSha256\x10\x03*B\n\x12SymmetricKeyScheme\x12\x1d\n\x19MissingSymmetricKeyScheme\x10\x00\x12\r\n\tAes128Gcm\x10\x01*X\n\x0f\x43ryptoKeyFormat\x12\x1a\n\x16MissingCryptoKeyFormat\x10\x00\x12\x08\n\x04Tink\x10\x01\x12\x07\n\x03\x44\x65r\x10\x02\x12\x07\n\x03Raw\x10\x03\x12\r\n\x08Symbolic\x10\x90NBRZPgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.digitalasset.canton.crypto.v0.crypto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZPgithub.com/digital-asset/dazl-client/v8/go/api/com/digitalasset/canton/crypto/v0'
  _globals['_HASHALGORITHM']._serialized_start=2750
  _globals['_HASHALGORITHM']._serialized_end=2803
  _globals['_HMACALGORITHM']._serialized_start=2805
  _globals['_HMACALGORITHM']._serialized_end=2862
  _globals['_SIGNATUREFORMAT']._serialized_start=2864
  _globals['_SIGNATUREFORMAT']._serialized_end=2933
  _globals['_KEYPURPOSE']._serialized_start=2935
  _globals['_KEYPURPOSE']._serialized_end=3019
  _globals['_SIGNINGKEYSCHEME']._serialized_start=3021
  _globals['_SIGNINGKEYSCHEME']._serialized_end=3120
  _globals['_ENCRYPTIONKEYSCHEME']._serialized_start=3123
  _globals['_ENCRYPTIONKEYSCHEME']._serialized_end=3271
  _globals['_SYMMETRICKEYSCHEME']._serialized_start=3273
  _globals['_SYMMETRICKEYSCHEME']._serialized_end=3339
  _globals['_CRYPTOKEYFORMAT']._serialized_start=3341
  _globals['_CRYPTOKEYFORMAT']._serialized_end=3429
  _globals['_HMAC']._serialized_start=85
  _globals['_HMAC']._serialized_end=191
  _globals['_SALT']._serialized_start=193
  _globals['_SALT']._serialized_end=304
  _globals['_SIGNATURE']._serialized_start=307
  _globals['_SIGNATURE']._serialized_end=453
  _globals['_PUBLICKEY']._serialized_start=456
  _globals['_PUBLICKEY']._serialized_end=685
  _globals['_PUBLICKEYWITHNAME']._serialized_start=687
  _globals['_PUBLICKEYWITHNAME']._serialized_end=803
  _globals['_PRIVATEKEY']._serialized_start=806
  _globals['_PRIVATEKEY']._serialized_end=1042
  _globals['_SIGNINGPUBLICKEY']._serialized_start=1045
  _globals['_SIGNINGPUBLICKEY']._serialized_end=1263
  _globals['_SIGNINGPRIVATEKEY']._serialized_start=1266
  _globals['_SIGNINGPRIVATEKEY']._serialized_end=1487
  _globals['_SIGNINGKEYPAIR']._serialized_start=1490
  _globals['_SIGNINGKEYPAIR']._serialized_end=1677
  _globals['_ENCRYPTIONPUBLICKEY']._serialized_start=1680
  _globals['_ENCRYPTIONPUBLICKEY']._serialized_end=1904
  _globals['_ENCRYPTIONPRIVATEKEY']._serialized_start=1907
  _globals['_ENCRYPTIONPRIVATEKEY']._serialized_end=2134
  _globals['_ENCRYPTIONKEYPAIR']._serialized_start=2137
  _globals['_ENCRYPTIONKEYPAIR']._serialized_end=2333
  _globals['_CRYPTOKEYPAIR']._serialized_start=2336
  _globals['_CRYPTOKEYPAIR']._serialized_end=2558
  _globals['_SYMMETRICKEY']._serialized_start=2561
  _globals['_SYMMETRICKEY']._serialized_end=2748
# @@protoc_insertion_point(module_scope)
