# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
:mod:`dazl.ledger.config` — connection configuration
====================================================

This module contains configuration objects for a :class:`Connection`.

Normally you don't need to construct these objects directly; instead, simply call
:meth:`dazl.connect`, which contains the same options exposed by the :meth:`Config.create` function,
which in turn includes the options exposed by the subobjects of :class:`Config`.

Generally you should not modify a :class:`Config` object (or subobjects) that have already been
passed to a :class:`Connection`. There are some exceptions to this rule, though; for example, when
using tokens, you can simply assign ``Config.access.token`` to a new value.

Configuration options are broken up into three subobjects:

* :ref:`Access configuration <access-configuration>`: settings commonly found in Daml JWT tokens
  (party settings, ledger ID, application name)
* :ref:`SSL/TLS configuration <ssl-tls-configuration>`: settings for configuring TLS connections
* :ref:`URL Configuration <url-configuration>`: settings that determine the location of gRPC Ledger
  API or HTTP JSON API implementation

.. autoclass:: Config
    :members:

.. _access-configuration:

Access configuration
--------------------

The :class:`AccessConfig` protocol specifies how ``dazl`` identifies itself to a ledger. There are
two built-in mechanisms for this: **property-based access**, which is traditionally used with
ledgers that do NOT require authorization/authentication (typical in a local development scenario,
for example coding against a local sandbox), and **token-based access**, which is required for
ledgers that DO require authorization/authentication (typical in a production scenario and/or hosted
ledgers).

In **property-based access** (:class:`PropertyBasedAccessConfig`), the behavior differs depending on
whether you are connecting over the gRPC Ledger API or the HTTP JSON API:

* For the *gRPC Ledger API*, ``read_as`` and ``act_as`` are used as-is. ``ledger_id`` is
  defaulted to the value requested from the ledger (but only if not initially specified).
  The ``admin`` property is ignored and unused.
* For the *HTTP JSON API*, ``read_as``, ``act_as``, ``admin``, ``ledger_id``, and
  ``application_name`` are all used to generate an unsigned JWT locally. ``ledger_id`` MUST be
  supplied.

In **token-based access** (:class:`TokenBasedAccessConfig`), the value of the token completely
determines the parties that can be used, the ledger ID to connect to, and the name of the
application. ``AccessConfig.token`` can be overwritten at any time, and that value will be used for
all subsequent calls to the ledger. If your ledger requires authorization/authentication using
tokens, you _must_ use token-based access.

Although ``dazl`` does not currently refresh tokens automatically, you can update the token yourself
at any time:

.. code-block:: python

    async def main():
        async with dazl.connect(token=MY_INITIAL_TOKEN) as conn:
            task1 = asyncio.create_task(do_ledger_stuff(conn))
            task2 = asyncio.create_task(refresh_token(conn))

            await task1
            task2.cancel()

    async def do_ledger_stuff(conn):
        # use the connection normally to make ledger calls
        ...

    async def refresh(conn):
        while True:
            # sleep for one hour
            await asyncio.sleep(3600)
            conn.config.access.token = NEW_REFRESHED_TOKEN

Deeper support for token refreshing may be added in a future release.

.. autoclass:: AccessConfig()
    :members:

.. autofunction:: create_access

.. autoclass:: PropertyBasedAccessConfig()
    :members:

.. autoclass:: TokenBasedAccessConfig()
    :members:

.. _ssl-tls-configuration:

SSL/TLS configuration
---------------------

.. autoclass:: SSLConfig
    :members:

.. _url-configuration:

URL configuration
-----------------

The :class:`URLConfig` protocol specifies the ledger implementation that ``dazl`` connects to
(either gRPC Ledger API or HTTP JSON API).

.. autofunction:: create_url

.. autoclass:: URLConfig()
    :members:

"""

from __future__ import annotations

import itertools
import logging
from logging import Logger
import sys
from typing import Optional

from ...damlast.lookup import MultiPackageLookup
from .access import (
    AccessConfig,
    AccessConfigArgs,
    PropertyBasedAccessConfig,
    TokenBasedAccessConfig,
    _AccessConfigArgs,
    create_access,
)
from .argv import configure_parser
from .log import LoggerArgs
from .ssl import SSLConfig, SSLConfigArgs, _SSLConfigArgs
from .url import URLConfig, URLConfigArgs, _URLConfigArgs, create_url

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = [
    "Config",
    "ConfigArgs",
    "AccessConfig",
    "SSLConfig",
    "URLConfig",
    "TokenBasedAccessConfig",
    "PropertyBasedAccessConfig",
    "create_access",
    "create_url",
    "configure_parser",
]

# an incrementing counter that helps keep loggers for individual config connections unique
# (see https://mail.python.org/pipermail//python-ideas/2016-August/041871.html); this is safe to
# do even in multithreaded environments because ultimately we're reusing the GIL as our lock
id_generator = itertools.count()


class ConfigArgs(AccessConfigArgs, SSLConfigArgs, URLConfigArgs, LoggerArgs, total=False):
    logger_name: Optional[str]
    log_level: Optional[str]
    lookup: Optional[MultiPackageLookup]


# PyCharm thinks ``from .url import ...`` clashes with variables named ``url``
# (same with ``ssl`` and ``access``).
# noinspection PyShadowingNames
class Config:
    """
    Stores configuration for a :class:`Connection`.
    """

    @classmethod
    def create(cls, **kwargs: Unpack[ConfigArgs]) -> Config:
        """
        Create a :class:`Config` object from the supplied parameters.

        The remote can be configured either by supplying a URL or by supplying a host (and optional
        port and scheme). If none of ``url``, ``host``, ``port``, or ``scheme`` are supplied, then
        environment variables are consulted; if no environment variables are specified either, then
        default values are used.

        The remote can be configured either by supplying a URL or by supplying a host (and optional
        port and scheme). If none of ``url``, ``host``, ``port``, or ``scheme`` are supplied, then
        environment variables are consulted; if no environment variables are specified either, then
        default values are used.

        When the URL scheme is ``http`` or ``https``, dazl will first attempt to connect assuming
        the HTTP JSON API; if this fails, gRPC Ledger API is attempted.

        If ``oauth_token`` is supplied and non-empty, then *token-based access* is used to connect
        to the ledger.

        If other fields are specified, then *property-based access* is used. At least one of
        ``read_as``, ``act_as``, or ``admin`` must be supplied. For the HTTP JSON API,
        ``ledger_id`` MUST be supplied.

        If _no_ fields are specified, this is an error unless environment variables supply an
        alternate source of configuration.

        +-------------------+----------------------+-----------------------------------------------+
        | function argument | environment variable | default value                                 |
        +===================+======================+===============================================+
        | ``url``           | DAML_LEDGER_URL      | localhost:6865                                |
        +-------------------+----------------------+-----------------------------------------------+
        | ``host``          | DAML_LEDGER_HOST     | localhost                                     |
        +-------------------+----------------------+-----------------------------------------------+
        | ``port``          | DAML_LEDGER_PORT     | 6865, unless ``scheme`` is specified:         |
        |                   |                      | * 80 for ``http``                             |
        |                   |                      | * 443 for ``https``                           |
        |                   |                      | * 6865 for ``grpc``                           |
        +-------------------+----------------------+-----------------------------------------------+
        | ``scheme``        | DAML_LEDGER_SCHEME   | | ``https`` for port 443 or 8443              |
        |                   |                      | | ``http`` for port 80, 7575 or 8080          |
        |                   |                      | | ``grpc`` for port 6865                      |
        |                   |                      | | ``https`` for all other ports               |
        +-------------------+----------------------+-----------------------------------------------+

        **HTTP(s) proxies (gRPC Ledger API only)**

        When connecting to the gRPC Ledger API, note that
        `gRPC environment variables
        <https://grpc.github.io/grpc/cpp/md_doc_environment_variables.html>`_
        are always also respected; you can set ``https_proxy``/`http_proxy`` (note the lowercase
        environment variable name). dazl, by default, will _also_ disable usage of a proxy server
        for a ``localhost`` host or a ``127.0.0.1`` host; this can be overridden by passing a value
        of ``use_http_proxy`` to ``True``.

        :param url:
            The URL to connect to. Can be used as an alternative to supplying ``host``, ``port``,
            and ``scheme`` as individual values. Can alternatively be supplied via the environment
            variable ``DAML_LEDGER_URL``.
        :param host:
            The host to connect to. Can be used as an alternative to supplying ``url`` as a combined
            value. Can alternatively be supplied via the environment variable ``DAML_LEDGER_HOST``.
        :param port:
            The port to connect to. Can be used as an alternative to supplying ``url`` as a combined
            value. Can alternatively be supplied via the environment variable ``DAML_LEDGER_PORT``.
        :param scheme:
            The scheme to connect to. Can be used as an alternative to supplying ``url`` as a
            combined value. Can alternatively be supplied via the environment variable
            ``DAML_LEDGER_SCHEME``.
        :param connect_timeout:
            Length of time to wait before giving up connecting to the remote and declaring an error.
            The default value is 30 seconds.
        :param retry_timeout:
            Length of time to wait while attempting to retry retryable errors before giving up and
            declaring an error. The default value is 30 seconds.
        :param use_http_proxy:
            ``True`` to use an HTTP(S) proxy server if configured; ``False`` to avoid using any
            configured server. If unspecified and the host is ``localhost``, the proxy server is
            avoided; otherwise the proxy server is used.
        :param ca:
            A certificate authority to use to validate the server's certificate. If not supplied,
            the operating system's default trust store is used. Cannot be specified with
            ``ca_file``.
        :param ca_file:
            A file containing the certificate authority to use to validate the server's certificate.
            If not supplied, the operating system's default trust store is used. Cannot be specified
            with ``ca``.
        :param cert:
            A client-side certificate to be used when connecting to a server that requires mutual
            TLS. Cannot be specified with ``cert_file``.
        :param cert_file:
            A file containing the client-side certificate to be used when connecting to a server
            that requires mutual TLS. Cannot be specified with ``cert``.
        :param cert_key:
            A client-side private key to be used when connecting to a server that requires mutual
            TLS. Cannot be specified with ``cert_key_file``.
        :param cert_key_file:
            A client-side private key to be used when connecting to a server that requires mutual
            TLS. Cannot be specified with ``cert_key``.
        :param read_as:
            A party or set of parties on whose behalf (in addition to all parties listed in
            ``act_as``) contracts can be retrieved. Cannot be specified if ``oauth_token`` or
            ``oauth_token_file`` is specified.
        :param act_as:
            A party or set of parties on whose behalf commands should be executed. Parties here are
            also implicitly granted ``read_as`` access as well. Cannot be specified if
            ``oauth_token`` or ``oauth_token_file`` is specified.
        :param admin:
            HTTP JSON API only: allow admin endpoints to be used. This flag is ignored when
            connecting to gRPC Ledger API implementations. Cannot be specified if ``oauth_token`` or
            ``oauth_token_file`` is specified.
        :param ledger_id:
            The ledger ID to connect to. For the HTTP JSON API, this value is required. For the gRPC
            Ledger API, if this value is _not_ supplied, its value will be retrieved from the
            server. Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is specified.
        :param application_name:
            A string that identifies this application. This is used for tracing purposes on the
            server-side. Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is
            specified.
        :param oauth_token:
            The OAuth bearer token to be used on all requests. If specified, no other access
            parameters can be specified.
        :param oauth_token_file:
            A file that contains the OAuth bearer token to be used on all requests. If specified, no
            other access parameters can be specified.
        :param logger:
            The logger to use for connections created from this configuration. If not supplied, a
            logger will be created.
        :param logger_name:
            The name of the logger. Only used if ``logger`` is not provided.
        :param log_level:
            The logging level for the logger. The default is ``warn``. Only used if ``logger`` is
            not provided.
        :param lookup:
            An alternate symbol table to use to store package information. You should not normally
            need to set this value.
        """
        logger = kwargs.get("logger", None)
        logger_name = kwargs.get("logger_name", None)
        log_level = kwargs.get("log_level")
        if logger is None:
            if not logger_name:
                logger_name = f"dazl.conn.{next(id_generator)}"
            logger = logging.getLogger(logger_name)
            if log_level is not None:
                logger.setLevel(log_level)

        lookup = kwargs.get("lookup", None)

        url_config_args = _URLConfigArgs()
        if "url" in kwargs:
            url_config_args["url"] = kwargs["url"]
        if "host" in kwargs:
            url_config_args["host"] = kwargs["host"]
        if "port" in kwargs:
            url_config_args["port"] = kwargs["port"]
        if "scheme" in kwargs:
            url_config_args["scheme"] = kwargs["scheme"]
        if "connect_timeout" in kwargs:
            url_config_args["connect_timeout"] = kwargs["connect_timeout"]
        if "retry_timeout" in kwargs:
            url_config_args["retry_timeout"] = kwargs["retry_timeout"]
        if "use_http_proxy" in kwargs:
            url_config_args["use_http_proxy"] = kwargs["use_http_proxy"]
        if logger is not None:
            url_config_args["logger"] = logger

        url_config = create_url(**url_config_args)

        access_config_args = _AccessConfigArgs()
        if "read_as" in kwargs:
            access_config_args["read_as"] = kwargs["read_as"]
        if "act_as" in kwargs:
            access_config_args["act_as"] = kwargs["act_as"]
        if "admin" in kwargs:
            access_config_args["admin"] = kwargs["admin"]
        if "ledger_id" in kwargs:
            access_config_args["ledger_id"] = kwargs["ledger_id"]
        if "application_name" in kwargs:
            access_config_args["application_name"] = kwargs["application_name"]
        if "oauth_token" in kwargs:
            access_config_args["oauth_token"] = kwargs["oauth_token"]
        if "oauth_token_file" in kwargs:
            access_config_args["oauth_token_file"] = kwargs["oauth_token_file"]
        if logger is not None:
            access_config_args["logger"] = logger

        access_config = create_access(**access_config_args)

        ssl_config_args = _SSLConfigArgs()
        if "ca" in kwargs:
            ssl_config_args["ca"] = kwargs["ca"]
        if "ca_file" in kwargs:
            ssl_config_args["ca_file"] = kwargs["ca_file"]
        if "cert" in kwargs:
            ssl_config_args["cert"] = kwargs["cert"]
        if "cert_file" in kwargs:
            ssl_config_args["cert_file"] = kwargs["cert_file"]
        if "cert_key" in kwargs:
            ssl_config_args["cert_key"] = kwargs["cert_key"]
        if "cert_key_file" in kwargs:
            ssl_config_args["cert_key_file"] = kwargs["cert_key_file"]
        if logger is not None:
            ssl_config_args["logger"] = logger

        ssl_config = SSLConfig(**ssl_config_args)

        return cls(access_config, ssl_config, url_config, logger, lookup)

    def __init__(
        self,
        access: AccessConfig,
        ssl: SSLConfig,
        url: URLConfig,
        logger: Logger,
        lookup: Optional[MultiPackageLookup] = None,
    ):
        """
        Initialize an instance of :class:`Config`.
        """
        self.access = access
        self.ssl = ssl
        self.url = url
        self.logger = logger
        self.lookup = lookup
