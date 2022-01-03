# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from logging import Logger
from os import PathLike, fspath
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    # We refer to the Config class in a docstring and
    # without this import, Sphinx can't resolve the reference
    # noinspection PyUnresolvedReferences
    from . import Config


class SSLConfig:
    """
    Configuration parameters that affect SSL connections.

    See :meth:`Config.create` for a more detailed description of these parameters.
    """

    def __init__(
        self,
        ca: "Optional[bytes]" = None,
        ca_file: "Optional[PathLike]" = None,
        cert: "Optional[bytes]" = None,
        cert_file: "Optional[PathLike]" = None,
        cert_key: "Optional[bytes]" = None,
        cert_key_file: "Optional[PathLike]" = None,
        logger: Optional[Logger] = None,
    ):
        self._ca: Optional[bytes]
        self._cert: Optional[bytes]
        self._cert_key: Optional[bytes]

        if ca_file:
            if ca:
                raise ValueError("ca and ca_file cannot both be specified at the same time")
            with open(fspath(ca_file), "rb") as f:
                self._ca = f.read()
        else:
            self._ca = ca

        if cert_file:
            if cert:
                raise ValueError("cert and cert_file cannot both be specified at the same time")
            with open(fspath(cert_file), "rb") as f:
                self._cert = f.read()
        else:
            self._cert = cert

        if cert_key_file:
            if cert_key:
                raise ValueError(
                    "cert_key and cert_key_file cannot both be specified at the same time"
                )
            with open(fspath(cert_key_file), "rb") as f:
                self._cert_key = f.read()
        else:
            self._cert_key = cert_key

    def __bool__(self):
        """
        True if SSL settings are supplied; otherwise False if no SSL settings of any kind were
        supplied.
        """
        return bool(self._ca or self._cert or self._cert_key)

    @property
    def ca(self) -> "Optional[bytes]":
        """
        Server certificate authority file.
        """
        return self._ca

    @property
    def cert(self) -> "Optional[bytes]":
        """
        Client certificate file.
        """
        return self._cert

    @property
    def cert_key(self) -> "Optional[bytes]":
        """
        Client certificate and key file.
        """
        return self._cert_key
