# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

from .vault_service_pb2 import DeleteKeyPairRequest, DeleteKeyPairResponse, ExportKeyPairRequest, ExportKeyPairResponse, GenerateCertificateRequest, GenerateCertificateResponse, GenerateEncryptionKeyRequest, GenerateEncryptionKeyResponse, GenerateSigningKeyRequest, GenerateSigningKeyResponse, GetWrapperKeyIdRequest, GetWrapperKeyIdResponse, ImportCertificateRequest, ImportCertificateResponse, ImportKeyPairRequest, ImportKeyPairResponse, ImportPublicKeyRequest, ImportPublicKeyResponse, ListCertificateRequest, ListCertificateResponse, ListKeysFilters, ListMyKeysRequest, ListMyKeysResponse, ListPublicKeysRequest, ListPublicKeysResponse, PrivateKeyMetadata, RegisterKmsEncryptionKeyRequest, RegisterKmsEncryptionKeyResponse, RegisterKmsSigningKeyRequest, RegisterKmsSigningKeyResponse, RotateWrapperKeyRequest, RotateWrapperKeyResponse
from .vault_service_pb2_grpc import VaultServiceStub

__all__ = [
    "DeleteKeyPairRequest",
    "DeleteKeyPairResponse",
    "ExportKeyPairRequest",
    "ExportKeyPairResponse",
    "GenerateCertificateRequest",
    "GenerateCertificateResponse",
    "GenerateEncryptionKeyRequest",
    "GenerateEncryptionKeyResponse",
    "GenerateSigningKeyRequest",
    "GenerateSigningKeyResponse",
    "GetWrapperKeyIdRequest",
    "GetWrapperKeyIdResponse",
    "ImportCertificateRequest",
    "ImportCertificateResponse",
    "ImportKeyPairRequest",
    "ImportKeyPairResponse",
    "ImportPublicKeyRequest",
    "ImportPublicKeyResponse",
    "ListCertificateRequest",
    "ListCertificateResponse",
    "ListKeysFilters",
    "ListMyKeysRequest",
    "ListMyKeysResponse",
    "ListPublicKeysRequest",
    "ListPublicKeysResponse",
    "PrivateKeyMetadata",
    "RegisterKmsEncryptionKeyRequest",
    "RegisterKmsEncryptionKeyResponse",
    "RegisterKmsSigningKeyRequest",
    "RegisterKmsSigningKeyResponse",
    "RotateWrapperKeyRequest",
    "RotateWrapperKeyResponse",
    "VaultServiceStub",
]
