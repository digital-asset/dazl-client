.. Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0

:mod:`dazl.ledger`
==================

.. py:currentmodule:: dazl.ledger

The :mod:`dazl.ledger` module provides a way of connecting to Daml ledgers via the
`gRPC Ledger API <https://docs.daml.com/app-dev/ledger-api.html>`_ or
`HTTP JSON API <https://docs.daml.com/json-api/index.html>`_.

Example
-------

.. note::

   These examples are targeted to Python 3.7+ and later, particularly the use of
   :meth:`asyncio.run`. For Python 3.6, replace calls to ``asyncio.run(main())`` with:

   .. code-block:: python

      loop = asyncio.get_event_loop()
      loop.run_until_complete(main())

Connecting to a ledger, and printing out all create events that ``Alice`` can see
(using the ``asyncio`` API):

.. code-block:: python

   import asyncio
   import dazl

   async def main():
      async with dazl.connect(url='localhost:6865', read_as='Alice') as conn:
         async with conn.query('*') as stream:
            async for event in stream.creates():
               print(event.contract_id, event.payload)

   # Python 3.7+ or later
   asyncio.run(main())

.. py:function:: connect(**kwargs)

   Create a connection from the supplied parameters. All of the parameters are optional, but you
   will have to supply at least ``read_as``, ``act_as``, ``admin``, ``oauth_token``, or
   ``oauth_token_file`` (see the section on Access config below).

   :param url:
      The URL to connect to. Can be used as an alternative to supplying ``host``, ``port``,
      and ``scheme`` as individual values. If none of of ``url``, ``host``, ``port`` or ``scheme``
      are specified, the value from the environment variable ``DAML_LEDGER_URL`` is used instead.
   :type url: str

   :param host:
      The host to connect to. Can be used as an alternative to supplying ``url`` as a combined
      value. If none of of ``url``, ``host``, ``port`` or ``scheme`` are specified, the value from
      the environment variable ``DAML_LEDGER_HOST`` is used instead.
   :type host: str

   :param port:
      The port to connect to. Can be used as an alternative to supplying ``url`` as a combined
      value. If none of of ``url``, ``host``, ``port`` or ``scheme`` are specified, the value from
      the environment variable ``DAML_LEDGER_PORT`` is used instead.
   :type port: int

   :param scheme:
      The scheme to connect to. Can be used as an alternative to supplying ``url`` as a combined
      value. If none of of ``url``, ``host``, ``port`` or ``scheme`` are specified, the value from
      the environment variable ``DAML_LEDGER_SCHEME`` is used instead.
   :type scheme: str

   :param connect_timeout:
      Length of time to wait before giving up connecting to the remote and declaring an error.
      The default value is 30 seconds. If a number is supplied instead of a ``timedelta``, it
      is assumed to mean seconds.
   :type connect_timeout: float or datetime.timedelta

   :param use_http_proxy:
      ``True`` to use an HTTP(S) proxy server if configured; ``False`` to avoid using any
      configured server. If unspecified and the host is ``localhost``, the proxy server is
      avoided; otherwise the proxy server is used.
   :type use_http_proxy: bool

   :param ca:
      A certificate authority to use to validate the server's certificate. If not supplied,
      the operating system's default trust store is used. Cannot be specified with
      ``ca_file``.
   :type ca: bytes

   :param ca_file:
      A file containing the certificate authority to use to validate the server's certificate.
      If not supplied, the operating system's default trust store is used. Cannot be specified
      with ``ca``.
   :type ca_file: os.PathLike

   :param cert:
      A client-side certificate to be used when connecting to a server that requires mutual
      TLS. Cannot be specified with ``cert_file``.
   :type cert: bytes

   :param cert_file:
      A file containing the client-side certificate to be used when connecting to a server
      that requires mutual TLS. Cannot be specified with ``cert``.
   :type cert_file: os.PathLike

   :param cert_key:
      A client-side private key to be used when connecting to a server that requires mutual
      TLS. Cannot be specified with ``cert_key_file``.
   :type cert_key: bytes

   :param cert_key_file:
      A client-side private key to be used when connecting to a server that requires mutual
      TLS. Cannot be specified with ``cert_key``.
   :type cert_key_file: os.PathLike

   :param read_as:
      A party or set of parties on whose behalf (in addition to all parties listed in ``act_as``)
      contracts can be retrieved. Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is
      specified. If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``,
      ``application_name``, ``oauth_token``, or ``oauth_token_file`` are specified, the value from
      the environment variable ``DAML_LEDGER_ACT_AS`` is used instead.
   :type read_as: str or Collection[str]

   :param act_as:
      A party or set of parties on whose behalf commands should be executed. Parties here are also
      implicitly granted ``read_as`` access as well. Cannot be specified if ``oauth_token`` or
      ``oauth_token_file`` is specified. If none of of ``read_as``, ``act_as``, ``admin``,
      ``ledger_id``, ``application_name``, ``oauth_token``, or ``oauth_token_file`` are specified,
      the value from the environment variable ``DAML_LEDGER_ACT_AS`` is used instead.
   :type act_as: str or Collection[str]

   :param admin:
      HTTP JSON API only: allow admin endpoints to be used. This flag is ignored when connecting to
      gRPC Ledger API implementations. Cannot be specified if ``oauth_token`` or
      ``oauth_token_file`` is specified.
   :type admin: bool

   :param ledger_id:
      The ledger ID to connect to. For the HTTP JSON API, this value is required. For the gRPC
      Ledger API, if this value is _not_ supplied, its value will be retrieved from the server.
      Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is specified. If none of of
      ``read_as``, ``act_as``, ``admin``, ``ledger_id``, ``application_name``, ``oauth_token``, or
      ``oauth_token_file`` are specified, the value from the environment variable ``DAML_LEDGER_ID``
      is used instead.
   :type ledger_id: str

   :param application_name:
      A string that identifies this application. This is used for tracing purposes on the
      server-side. Cannot be specified if ``oauth_token`` or ``oauth_token_file`` is specified.
      If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``, ``application_name``,
      ``oauth_token``, or ``oauth_token_file`` are specified, the value from the environment
      variable ``DAML_LEDGER_APPLICATION_NAME`` is used instead.
   :type application_name: str

   :param oauth_token:
      The OAuth bearer token to be used on all requests. Cannot be specified if ``read_as``,
      ``act_as``, ``admin``, ``ledger_id``, ``application_name``, or ``oauth_token_file`` is
      specified. If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``,
      ``application_name``, ``oauth_token``, or ``oauth_token_file`` are specified, the value from
      the environment variable ``DAML_LEDGER_OAUTH_TOKEN`` is used instead.
   :type oauth_token: bytes

   :param oauth_token_file:
      A file that contains the OAuth bearer token to be used on all requests. Cannot be specified if
      ``read_as``, ``act_as``, ``admin``, ``ledger_id``, ``application_name``, or ``oauth_token`` is
      specified. If none of of ``read_as``, ``act_as``, ``admin``, ``ledger_id``,
      ``application_name``, ``oauth_token``, or ``oauth_token_file`` are specified, the value from
      the environment variable ``DAML_LEDGER_OAUTH_TOKEN_FILE`` is used instead.
   :type oauth_token_file: os.PathLike

   :param logger:
      The logger to use for connections created from this configuration. If not supplied, a
      logger will be created.
   :type logger: logging.Logger

   :param logger_name:
      The name of the logger. Only used if ``logger`` is not provided.
   :type logger_name: str

   :param log_level:
      The logging level for the logger. The default is ``warn``. Only used if ``logger`` is
      not provided. This function accepts any valid Python `logging level
      <https://docs.python.org/3/library/logging.html#levels>`_.
   :type log_level: int or str


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

   If *no* fields are specified, this is an error unless environment variables supply an alternate
   source of configuration.

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


Data Model
----------

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

Connections
-----------

.. py:class:: Connection

   Protocol that describes a connection to a ledger. You will typically work with the more specific
   protocols :class:`dazl.ledger.aio.Connection` or :class:`dazl.ledger.blocking.Connection` that
   are tailored towards connections with ``asyncio`` or thread-blocking semantics, respectively.

   On *asynchronous* connections:

    * the command submission methods :meth:`create`, :meth:`exercise`, :meth:`submit` are coroutines.
    * the stream methods :meth:`query`, :meth:`query_many`, :meth:`stream`, and :meth:`stream_many`,
      return asynchronous context managers and asynchronous iterators

   On *blocking* connections:

    * the command submission methods :meth:`create`, :meth:`exercise`, :meth:`submit` block the
      current thread until the command submission succeeds or fails.
    * the stream methods :meth:`query`, :meth:`query_many`, :meth:`stream`, and :meth:`stream_many`,
      return context managers and blocking iterators.

   .. py:function:: exercise(contract_id, choice_name, [argument], /, *, workflow_id=None, command_id=None)

      Exercise a choice on a contract identified by its contract ID.

      :param contract_id: The contract ID of the contract to exercise.
      :type contract_id: dazl.prim.ContractId
      :param choice_name: The name of the choice to exercise.
      :type choice_name: str
      :param argument: The choice arguments. Can be omitted for choices that take no argument.
      :type argument: dict or None
      :param workflow_id: An optional workflow ID.
      :type workflow_id: str or None
      :param command_id: An optional command ID. If unspecified, a random one will be created.
      :type command_id: str or None

   .. py:function:: archive(contract_id, /, *, workflow_id=None, command_id=None)

      Archive a choice on a contract identified by its contract ID.

      :param contract_id: The contract ID of the contract to archive.
      :type contract_id: dazl.prim.ContractId
      :param workflow_id: An optional workflow ID.
      :type workflow_id: str or None
      :param command_id: An optional command ID. If unspecified, a random one will be created.
      :type command_id: str or None

.. py:class:: QueryStream

   Protocol for classes that provide for reading from a stream of events from a Daml ledger. Like
   :class:`Connection`, there are async query streams (:class:`dazl.ledger.aio.QueryStream`) and
   blocking query streams (:class:`dazl.ledger.blocking.QueryStream`).

   The methods of :class:`QueryStream` consume the stream: you cannot replay a
   :class:`QueryStream`'s contents simply by trying to iterate over it again.

   On *asynchronous* connections, the methods on :class:`QueryStream` return asynchronous
   iterators: use ``async for`` to iterate over their contents.

   On *blocking* connections, the methods on :class:`QueryStream` return blocking iterators:
   use ``for`` to iterate over their contents.

   Note that the :meth:`events` and :meth:`items` streams may return :class:`ArchiveEvent` objects
   that had no :class:`CreateEvent` predecessor. This may happen for a number of reasons:

    * You started requesting a stream at a specific offset. When resuming from an offset, no
      events (:class:`CreateEvent` or :class:`ArchiveEvent`) that preceded the specified offset are
      returned.
    * You are filtering events; event filtering only applies to :class:`CreateEvent` instances and
      *not* :class:`ArchiveEvent`.
    * You are learning of an archive of a `divulged contract
      <https://docs.daml.com/concepts/ledger-model/ledger-privacy.html#divulgence-when-non-stakeholders-see-contracts>`_.
      Note that ``dazl`` does not have an API for retrieving divulged contracts.

   **Reading from and controlling the stream**

   The :meth:`creates`, :meth:`events`, and :meth:`items` methods are used to receive events from
   the stream; :meth:`run` can be used to consume the stream without iterating yourself, and
   :meth:`close` stops the stream.

   .. code-block:: python

      # asynchronous connections
      async with conn.stream() as stream:
         async for event in stream.creates():
            # print every contract create...forever
            print(event.contract_id, event.payload)

      # blocking connections
      with conn.stream() as stream:
         for event in stream.creates():
            # print every contract create...forever
            print(event.contract_id, event.payload)

   .. py:method:: creates()

      Return an iterator (or async iterator) over only :class:`CreateEvent` instances.

   .. py:method:: events()

      Return an iterator (or async iterator) over :class:`CreateEvent` and :class:`ArchiveEvent`
      instances.

   .. py:method:: items()

      Return an iterator (or async iterator) over *all* objects (:class:`CreateEvent`,
      :class:`ArchiveEvent`, and :class:`Boundary`).

   .. py:method:: run()

      Block until the stream has been fully consumed. This method normally only makes sense to
      use in conjunction with callbacks (:meth:`on_create`, :meth:`on_archive`, and
      :meth:`on_boundary`). For async connections, this is a coroutine.

   .. py:method:: close()

      Stops the iterator and aborts the stream. For async connections, this is a coroutine.

   **Registering Callbacks**

   Callbacks can be used as an alternative to reading events from the stream.

   The callable must take a :class:`CreateEvent`, :class:`ArchiveEvent`, or :class:`Boundary` as
   its only parameter and should generally return ``None``. However the callback can also return
   :class:`CreateEvent` or :class:`ExerciseResponse`, mostly so that one-line lambdas that call
   ledger methods can be used:

   .. code-block:: python

      # registering a callback as a lambda
      stream.on_create("My:Tmpl", lambda event: conn.exercise(event.cid, "Accept"))

      # registering a callback using a decorator
      @stream.on_create("My:Tmpl")
      def handle(event):
          conn.exercise(event.cid, "Accept")

   .. py:method:: on_create(fn)
                  on_create(name, fn)
                  @on_create
                  @on_create(name)

      Register a callback that is triggered whenever a :class:`CreateEvent` is read through the
      stream.

      :param name: An optional name of a template to further filter :class:`CreateEvent`.
      :type name: str or dazl.damlast.TypeConName

   .. py:method:: on_archive(fn)
                  on_archive(name, fn)
                  @on_archive
                  @on_archive(name)

      Register a callback that is triggered whenever a :class:`ArchiveEvent` is read through the
      stream.

      :param name: An optional name of a template to further filter :class:`ArchiveEvent`.
      :type name: str or dazl.damlast.TypeConName

   .. py:method:: on_boundary(fn)
                   @on_boundary

      Register a callback that is triggered whenever a :class:`Boundary` is read through the
      stream.


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
