# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from os import PathLike, fspath
import sys
from typing import TYPE_CHECKING, Optional, TypedDict

from .log import LoggerArgs

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

if TYPE_CHECKING:
    # We refer to the Config class in a docstring and
    # without this import, Sphinx can't resolve the reference
    # noinspection PyUnresolvedReferences
    from . import Config


__all__ = ["SSLConfig", "SSLConfigArgs", "_SSLConfigArgs"]


class SSLConfigArgs(TypedDict, total=False):
    ca: Optional[bytes]
    ca_file: Optional[PathLike]
    cert: Optional[bytes]
    cert_file: Optional[PathLike]
    cert_key: Optional[bytes]
    cert_key_file: Optional[PathLike]


class _SSLConfigArgs(SSLConfigArgs, LoggerArgs, total=False):
    pass


class SSLConfig:
    """
    Configuration parameters that affect SSL connections.

    See :meth:`Config.create` for a more detailed description of these parameters.
    """

    def __init__(self, **kwargs: Unpack[_SSLConfigArgs]):
        self._ca = kwargs.get("ca", None)
        self._cert = kwargs.get("cert", None)
        self._cert_key = kwargs.get("cert_key", None)

        if ca_file := kwargs.get("ca_file", None):
            if self._ca:
                raise ValueError("ca and ca_file cannot both be specified at the same time")
            with open(fspath(ca_file), "rb") as f:
                self._ca = f.read()

        if cert_file := kwargs.get("cert_file", None):
            if self._cert:
                raise ValueError("cert and cert_file cannot both be specified at the same time")
            with open(fspath(cert_file), "rb") as f:
                self._cert = f.read()

        if cert_key_file := kwargs.get("cert_key_file", None):
            if self._cert_key:
                raise ValueError(
                    "cert_key and cert_key_file cannot both be specified at the same time"
                )
            with open(fspath(cert_key_file), "rb") as f:
                self._cert_key = f.read()

    def __bool__(self):
        """
        True if SSL settings are supplied; otherwise False if no SSL settings of any kind were
        supplied.
        """
        return bool(self._ca or self._cert or self._cert_key)

    @property
    def ca(self) -> Optional[bytes]:
        """
        Server certificate authority file.
        """
        return self._ca

    @property
    def cert(self) -> Optional[bytes]:
        """
        Client certificate file.
        """
        return self._cert

    @property
    def cert_key(self) -> Optional[bytes]:
        """
        Client certificate and key file.
        """
        return self._cert_key
