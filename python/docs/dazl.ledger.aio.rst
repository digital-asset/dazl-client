.. Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0

:mod:`dazl.ledger.aio`
======================

.. py:currentmodule:: dazl.ledger.aio

`asyncio`-flavored protocols and base classes for connecting to a Daml ledger.

This protocol is currently implemented by the `asyncio` gRPC Ledger API implementation
:class:`dazl.ledger.grpc.conn_aio.Connection`.

.. py:class:: Connection

   .. py:method:: codec
      :property:

      The codec object.

   .. py:method:: config
      :property:

      The :class:`dazl.ledger.config.Config` that was used to initialize this connection.

   .. py:method:: open
      :async:

      Open the connection. Will also fetch the ledger ID if that information is not locally
      available.

   .. py:method:: close
      :async:

      Close the connection. Commands in-flight will be allowed to finish, but new commands will be
      rejected. All existing streams made from this connection are closed.

   .. py:method:: create(template_id, payload, /, *, workflow_id=None, command_id=None)
      :async:

      Create a contract for a given template.

      :param template_id: The template of the contract to be created.
      :type template_id: str or dazl.damlast.TypeConName
      :param payload: Template arguments for the contract to be created.
      :type payload: dict
      :param workflow_id: An optional workflow ID.
      :type workflow_id: str or None
      :param command_id: An optional command ID. If unspecified, a random one will be created.
      :type command_id: str or None
      :return:
         The :class:`dazl.ledger.CreateEvent` that describes the created contract, including its
         contract ID.

   .. py:method:: create_and_exercise(template_id, payload, choice_name, [argument], /, *, workflow_id=None, command_id=None)
      :async:

      Exercise a choice on a newly-created contract, in a single transaction.

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
      :keyword workflow_id: An optional workflow ID.
      :type workflow_id: str or None
      :keyword command_id: An optional command ID. If unspecified, a random one will be created.
      :type command_id: str or None
      :return:
         :class:`dazl.ledger.ExerciseResponse` containing the return value of the choice,
         together with a list of events that occurred as a result of exercising the choice.

   .. py:method:: exercise(contract_id, choice_name, [argument], /, *, workflow_id=None, command_id=None)
      :async:

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
      :return:
         :class:`dazl.ledger.ExerciseResponse` containing the return value of the choice,
         together with a list of events that occurred as a result of exercising the choice.

   .. py:method:: exercise_by_key(template_id, choice_name, key, [argument], /, *,  workflow_id=None, command_id=None)
      :async:

      Exercise a choice on a contract identified by its contract key.

   .. py:method:: submit(commands, /, *, workflow_id=None, command_id=None)
      :async:

      Submit one or more commands to the Ledger API.

      You should generally prefer trying to use :meth:`create`, :meth:`exercise`,
      :meth:`exercise_by_key`, or :meth:`create_and_exercise`, as they are available over both
      the gRPC Ledger API and HTTP JSON API; additionally those methods can provide more
      information about what happened.

      This method can be used to submit multiple disparate commands as a single transaction, but
      if you find yourself needing to do this, you may want to consider moving more of your logic
      into Daml so that only a single command is needed from the outside in order to satisfy your
      use case.

      :param commands: The sequence of commands to submit to the ledger.
      :type commands: dazl.ledger.Command or list[dazl.ledger.Command]
      :param workflow_id: An optional workflow ID.
      :type workflow_id: str or None
      :param command_id: An optional command ID. If unspecified, a random one will be created.
      :type command_id: str or None

   .. py:method:: query([template_id], [query], /)
                  stream([template_id], [query], /, *, offset=None)

      :param template_id:
         The name of the template for which to fetch contracts. If omitted or `"*"`, contracts for
         all templates are returned.
      :type template_id: str or :class:`dazl.damlast.TypeConName`
      :param query: A ``dict`` whose keys represent exact values to be matched.
      :param offset:
         An optional offset at which to start receiving events. If ``None``, start from the
         beginning. Can only be supplied to :meth:`stream`.
      :type offset: str or None
      :return:
         A :class:`QueryStream` over the relevant events.

         The stream returned by :meth:`query` represents a snapshot of the current state, and
         terminates when all :class:`CreateEvent` instances that represent currently active
         contracts are returned.

         The stream returned by :meth:`stream` returns the current state as :meth:`query` does, but
         afterwards the stream remains open, and subsequent :class:`CreateEvent` and
         :class:`ArchiveEvent`'s are returned until :meth:`close` is called.

   .. py:method:: query_many(*queries)
                  stream_many(*queries, offset=None)


.. py:class:: QueryStream

    Protocol for classes that provide for asynchronous reading from a stream of events from a Daml
    ledger.

    **Reading from and controlling the stream**

    The :meth:`creates`, :meth:`events`, and :meth:`items` methods are used to receive events from
    the stream; :meth:`run` can be used to consume the stream without iterating yourself, and
    :meth:`close` stops the stream. These methods consume the stream: you cannot replay a
    :class:`QueryStream`'s contents simply by trying to iterate over it again.

    .. code-block:: python

        async with conn.stream() as stream:
            async for event in stream.creates():
                # print every contract create...forever
                print(event.contract_id, event.payload)

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

    .. py:method:: creates()
         :abstractmethod:
         :async-for: event

         Return an iterator (or async iterator) over only :class:`CreateEvent` instances.

    .. py:method:: events()
         :abstractmethod:
         :async-for: event

         Return an iterator (or async iterator) over :class:`CreateEvent` and :class:`ArchiveEvent`
         instances.

    .. py:method:: items()
         :abstractmethod:
         :async-for: event_or_boundary

         Return an iterator (or async iterator) over *all* objects (:class:`CreateEvent`,
         :class:`ArchiveEvent`, and :class:`Boundary`).

    .. py:method:: run()
         :abstractmethod:
         :async:

         Block until the stream has been fully consumed. This method normally only makes sense to
         use in conjunction with callbacks (:meth:`on_create`, :meth:`on_archive`, and
         :meth:`on_boundary`).

    .. py:method:: close()
         :abstractmethod:
         :async:

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
        :type name: str or TypeConName

    .. py:method:: on_archive(fn)
                   on_archive(name, fn)
                   @on_archive
                   @on_archive(name)

        Register a callback that is triggered whenever a :class:`ArchiveEvent` is read through the
        stream.

        :param name: An optional name of a template to further filter :class:`ArchiveEvent`.
        :type name: str or TypeConName

    .. py:method:: on_boundary(fn)
                   @on_boundary

        Register a callback that is triggered whenever a :class:`Boundary` is read through the
        stream.
