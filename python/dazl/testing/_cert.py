# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
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
    subject_alternative_name: "Optional[Collection[str]]" = None,
    serial_number: int = 0,
    validity_end_in_seconds: int = 10 * 365 * 24 * 60 * 60,
) -> "Certificate":
    from OpenSSL import crypto

    # can look at generated file using openssl:
    # openssl x509 -inform pem -in selfsigned.crt -noout -text
    # create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)
    # create a self-signed cert
    cert = crypto.X509()
    cert.set_version(2)
    subject = cert.get_subject()
    subject.C = country_name
    subject.ST = state_or_province_name
    subject.L = locality_name
    subject.O = organization_name
    subject.OU = organization_unit_name
    subject.CN = common_name
    subject.emailAddress = email_address
    cert.set_serial_number(serial_number)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(validity_end_in_seconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    if subject_alternative_name:
        if isinstance(subject_alternative_name, str):
            subject_alternative_name = (subject_alternative_name,)
        cert.add_extensions(
            [
                crypto.X509Extension(
                    b"subjectAltName",
                    False,
                    ",".join(f"DNS:{san}" for san in subject_alternative_name).encode("ascii"),
                )
            ]
        )

    cert.sign(k, "sha512")
    return Certificate(
        public_cert=crypto.dump_certificate(crypto.FILETYPE_PEM, cert),
        private_key=crypto.dump_privatekey(crypto.FILETYPE_PEM, k),
    )
