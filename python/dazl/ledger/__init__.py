# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
:mod:`dazl.ledger` — gRPC Ledger API / HTTP JSON API client
===========================================================
.. autofunction:: connect

This module contains the types needed to submit commands to and read events from a
Daml `gRPC Ledger API <https://docs.daml.com/app-dev/ledger-api.html>`_ or
`HTTP JSON API <https://docs.daml.com/json-api/index.html>`_.

Example:

+-----------------------------------+--------------------------------------------------------------+
| Commands                                                                                         |
+-----------------------------------+--------------------------------------------------------------+
| :class:`Command`                  | abstract base class of all commands                          |
+-----------------------------------+--------------------------------------------------------------+
| :class:`CreateCommand`            | create a contract                                            |
+-----------------------------------+--------------------------------------------------------------+
| :class:`CreateAndExerciseCommand` | create a contract and immediately exercise a choice on the   |
|                                   | newly created contract in a single transaction               |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ExerciseCommand`          | exercise a choice on a contract identified by its contract   |
|                                   | ID                                                           |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ExerciseByKeyCommand`     | exercise a choice on a contract identified by its contract   |
|                                   | key                                                          |
+-----------------------------------+--------------------------------------------------------------+
| Events and Responses                                                                             |
+-----------------------------------+--------------------------------------------------------------+
| :class:`CreateEvent`              | event raised when a contract is created, either as part of   |
|                                   | the active contract set or on the transaction stream         |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ArchiveEvent`             | event raised when a contract is archived on the transaction  |
|                                   | stream                                                       |
+-----------------------------------+--------------------------------------------------------------+
| :class:`ExerciseResponse`         | the response from an exercise, including the choice's return |
|                                   | value (if any)                                               |
+-----------------------------------+--------------------------------------------------------------+
| :class:`Boundary`                 | indicates a point where an event stream can be subsequently  |
|                                   | resumed                                                      |
+-----------------------------------+--------------------------------------------------------------+
| Other                                                                                            |
+-----------------------------------+--------------------------------------------------------------+
| :class:`PartyInfo`                | metadata about a party                                       |
+-----------------------------------+--------------------------------------------------------------+

Write-side types
----------------

Daml ledger state can be updated by submitting commands to the ledger. You should prefer using
:meth:`Connection.create`, :meth:`Connection.create_and_exercise`, :meth:`Connection.exercise`, and
:meth:`Connection.exercise_by_key` over constructing instances of these commands, as those methods
can give you more information about what happened.

.. autoclass:: Command

.. autoclass:: CreateCommand
   :members:

.. autoclass:: CreateAndExerciseCommand
   :members:

.. autoclass:: ExerciseCommand
   :members:

.. autoclass:: ExerciseByKeyCommand
   :members:

Read-side types
---------------

An ``Event`` in a transaction is either a :class:`CreateEvent` or an `ArchiveEvent``.

You can resume a stream of events from a previous point by using ``stream.items()`` and looking for
``Boundary`` objects.

More detailed information about exercises, including the return value and events that occurred as
a result of an exercise, is available from ``ExerciseResponse`` objects as returned from
:meth:`Connection.create_and_exercise`, :meth:`Connection.exercise`, and
:meth:`Connection.exercise_by_key`.

.. autoclass:: CreateEvent
   :members:

.. autoclass:: ArchiveEvent
   :members:

.. autoclass:: Boundary
   :members:

.. autoclass:: ExerciseResponse
   :members:

Other
-----

.. autoclass:: PartyInfo
    :members:

"""
from logging import Logger
from os import PathLike
from typing import Collection, Optional, Union

from ..prim import Party, TimeDeltaLike
from .api_types import (
    ArchiveEvent,
    Boundary,
    Command,
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    ExerciseByKeyCommand,
    ExerciseCommand,
    ExerciseResponse,
    PartyInfo,
)

__all__ = [
    "ArchiveEvent",
    "Boundary",
    "Command",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "CreateEvent",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "ExerciseResponse",
    "PartyInfo",
]


def connect(
    url: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[int] = None,
    scheme: Optional[str] = None,
    read_as: Union[None, Party, Collection[Party]] = None,
    act_as: Union[None, Party, Collection[Party]] = None,
    admin: Optional[bool] = False,
    ledger_id: Optional[str] = None,
    application_name: Optional[str] = None,
    oauth_token: Optional[str] = None,
    oauth_token_file: Optional[str] = None,
    ca: Optional[bytes] = None,
    ca_file: Optional[PathLike] = None,
    cert: Optional[bytes] = None,
    cert_file: Optional[PathLike] = None,
    cert_key: Optional[bytes] = None,
    cert_key_file: Optional[PathLike] = None,
    connect_timeout: Optional[TimeDeltaLike] = None,
    use_http_proxy: bool = True,
    logger: Optional[Logger] = None,
    logger_name: Optional[str] = None,
    log_level: Optional[str] = None,
):
    """
    Create a connection from the supplied parameters.

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
    to the ledger. (Note that you cannot specify both ``oauth_token`` and ``oauth_token_file``.)

    If other fields are specified, then *property-based access* is used. At least one of
    ``read_as``, ``act_as``, or ``admin`` must be supplied. For the HTTP JSON API,
    ``ledger_id`` MUST be supplied.

    If _no_ fields are specified, this is an error unless environment variables supply an
    alternate source of configuration.

    +----------------------+----------------------+------------------------------------------------+
    | function argument    | environment variable | default value                                  |
    +======================+======================+================================================+
    | **Connection config**                                                                        |
    |                                                                                              |
    | Specifying *any* of ``url``, ``host``, ``port``, or ``scheme`` causes *all* of these         |
    | environment variables to be ignored                                                          |
    +----------------------+----------------------+------------------------------------------------+
    | ``url``              | DAML_LEDGER_URL      | localhost:6865                                 |
    +----------------------+----------------------+------------------------------------------------+
    | ``host``             | DAML_LEDGER_HOST     | localhost                                      |
    +----------------------+----------------------+------------------------------------------------+
    | ``port``             | DAML_LEDGER_PORT     | | 6865, unless ``scheme`` is specified:        |
    |                      |                      | | • 80 for ``http``                            |
    |                      |                      | | • 443 for ``https``                          |
    |                      |                      | | • 6865 for ``grpc``                          |
    +----------------------+----------------------+------------------------------------------------+
    | ``scheme``           | DAML_LEDGER_SCHEME   | | ``https`` for port 443 or 8443               |
    |                      |                      | | ``http`` for port 80, 7575 or 8080           |
    |                      |                      | | ``grpc`` for port 6865                       |
    |                      |                      | | ``https`` for all other ports                |
    +----------------------+----------------------+------------------------------------------------+
    | **Access config**                                                                            |
    |                                                                                              |
    | Specifying *any* of ``act_as``, ``read_as``, ``admin``, ``ledger_id``, ``application_name``, |
    | ``oauth_token``, or ``oauth_token_file`` causes *all* of these environment variables to be   |
    | ignored                                                                                      |
    +----------------------+-----------------------------------------------------------------------+
    | ``act_as``           | ``DAML_LEDGER_ACT_AS`` (as a comma-separated list of parties)         |
    +----------------------+-----------------------------------------------------------------------+
    | ``read_as``          | ``DAML_LEDGER_READ_AS`` (as a comma-separated list of parties)        |
    +----------------------+-----------------------------------------------------------------------+
    | ``ledger_id``        | ``DAML_LEDGER_ID``                                                    |
    +----------------------+-----------------------------------------------------------------------+
    | ``application_name`` | ``DAML_LEDGER_APPLICATION_NAME``                                      |
    +----------------------+-----------------------------------------------------------------------+
    | ``oauth_token``      | ``DAML_LEDGER_OAUTH_TOKEN``                                           |
    +----------------------+-----------------------------------------------------------------------+
    | ``oauth_token_file`` | ``DAML_LEDGER_OAUTH_TOKEN_FILE``                                      |
    +----------------------+-----------------------------------------------------------------------+

    .. note::

        When connecting to the gRPC Ledger API, note that
        `gRPC environment variables
        <https://grpc.github.io/grpc/cpp/md_doc_environment_variables.html>`_ are also respected.
        You can configure the gRPC client in much more detail with these flags.

    :param url:
        The URL to connect to. Can be used as an alternative to supplying ``host``, ``port``,
        and ``scheme`` as individual values.

        If none of of ``url``, ``host``, ``port`` or ``scheme`` are specified, the value from the
        environment variable ``DAML_LEDGER_URL`` is used instead.

    :param host:
        The host to connect to. Can be used as an alternative to supplying ``url`` as a combined
        value.

        If none of of ``url``, ``host``, ``port`` or ``scheme`` are specified, the value from the
        environment variable ``DAML_LEDGER_HOST`` is used instead.

    :param port:
        The port to connect to. Can be used as an alternative to supplying ``url`` as a combined
        value.

        If none of of ``url``, ``host``, ``port`` or ``scheme`` are specified, the value from the
        environment variable ``DAML_LEDGER_PORT`` is used instead.

    :param scheme:
        The scheme to connect to. Can be used as an alternative to supplying ``url`` as a
        combined value.

        If none of of ``url``, ``host``, ``port`` or ``scheme`` are specified, the value from the
        environment variable ``DAML_LEDGER_SCHEME`` is used instead.

    :param connect_timeout:
        Length of time to wait before giving up connecting to the remote and declaring an error.
        The default value is 30 seconds.

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
        ``act_as``) contracts can be retrieved.

        Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is specified.

        If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``, ``application_name``,
        ``oauth_token``, or ``oauth_token_file`` are specified, the value from the environment
        variable ``DAML_LEDGER_ACT_AS`` is used instead.

    :param act_as:
        A party or set of parties on whose behalf commands should be executed. Parties here are
        also implicitly granted ``read_as`` access as well.

        Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is specified.

        If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``, ``application_name``,
        ``oauth_token``, or ``oauth_token_file`` are specified, the value from the environment
        variable ``DAML_LEDGER_ACT_AS`` is used instead.

    :param admin:
        HTTP JSON API only: allow admin endpoints to be used. This flag is ignored when
        connecting to gRPC Ledger API implementations.

        Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is specified.

    :param ledger_id:
        The ledger ID to connect to. For the HTTP JSON API, this value is required. For the gRPC
        Ledger API, if this value is _not_ supplied, its value will be retrieved from the
        server.

        Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is specified.

        If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``, ``application_name``,
        ``oauth_token``, or ``oauth_token_file`` are specified, the value from the environment
        variable ``DAML_LEDGER_ID`` is used instead.

    :param application_name:
        A string that identifies this application. This is used for tracing purposes on the
        server-side.

        Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is specified.

        If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``, ``application_name``,
        ``oauth_token``, or ``oauth_token_file`` are specified, the value from the environment
        variable ``DAML_LEDGER_APPLICATION_NAME`` is used instead.

    :param oauth_token:
        The OAuth bearer token to be used on all requests.

        Cannot be specified if ``read_as``, ``act_as``, ``admin``, ``ledger_id``,
        ``application_name``, or ``oauth_token_file`` is specified.

        If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``, ``application_name``,
        ``oauth_token``, or ``oauth_token_file`` are specified, the value from the environment
        variable ``DAML_LEDGER_OAUTH_TOKEN`` is used instead.

    :param oauth_token_file:
        A file that contains the OAuth bearer token to be used on all requests.

        Cannot be specified if ``read_as``, ``act_as``, ``admin``, ``ledger_id``,
        ``application_name``, or ``oauth_token`` is specified.

        If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``, ``application_name``,
        ``oauth_token``, or ``oauth_token_file`` are specified, the value from the environment
        variable ``DAML_LEDGER_OAUTH_TOKEN_FILE`` is used instead.

    :param logger:
        The logger to use for connections created from this configuration. If not supplied, a
        logger will be created.

    :param logger_name:
        The name of the logger. Only used if ``logger`` is not provided.

    :param log_level:
        The logging level for the logger. The default is ``warn``. Only used if ``logger`` is
        not provided.
    """
    # TODO: Ideally we could _define_ the function as taking all of these parameters, but implement
    #  it with kwargs passing; unfortunately Sphinx doesn't seem to allow this.
    from .config import Config

    _ = Config.create(
        url=url,
        host=host,
        port=port,
        scheme=scheme,
        read_as=read_as,
        act_as=act_as,
        admin=admin,
        ledger_id=ledger_id,
        application_name=application_name,
        oauth_token=oauth_token,
        oauth_token_file=oauth_token_file,
        ca=ca,
        ca_file=ca_file,
        cert=cert,
        cert_file=cert_file,
        cert_key=cert_key,
        cert_key_file=cert_key_file,
        connect_timeout=connect_timeout,
        use_http_proxy=use_http_proxy,
        logger=logger,
        logger_name=logger_name,
        log_level=log_level,
    )
    # TODO: Implement when the v8 connection code fully lands
    raise NotImplementedError
