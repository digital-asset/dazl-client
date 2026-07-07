# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import datetime
from typing import Collection, Optional


class Certificate:
    def __init__(self, public_cert: bytes, private_key: bytes):
        self.public_cert = public_cert
        self.private_key = private_key


def cert_gen(
    email_address: str = "emailAddress",
    common_name: str = "commonName",
    country_name: str = "NT",
    locality_name: str = "localityName",
    state_or_province_name: str = "stateOrProvinceName",
    organization_name: str = "organizationName",
    organization_unit_name: str = "organizationUnitName",
    subject_alternative_name: Optional[Collection[str]] = None,
    serial_number: int = 0,
    validity_end_in_seconds: int = 10 * 365 * 24 * 60 * 60,
) -> Certificate:
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.x509.oid import NameOID

    # 1. Generate a private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # 2. Set up certificate details
    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.EMAIL_ADDRESS, email_address),
            x509.NameAttribute(NameOID.COUNTRY_NAME, country_name),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state_or_province_name),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization_name),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, organization_unit_name),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        ]
    )

    # 3. Build the certificate
    cert_builder = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
        # Valid for 365 days
        .not_valid_after(
            datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(seconds=validity_end_in_seconds)
        )
    )

    if subject_alternative_name:
        cert_builder = cert_builder.add_extension(
            x509.SubjectAlternativeName([x509.DNSName("localhost")]),
            critical=False,
        )

    cert = cert_builder.sign(private_key, hashes.SHA256())

    return Certificate(
        public_cert=cert.public_bytes(serialization.Encoding.PEM),
        private_key=private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ),
    )
