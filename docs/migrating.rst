.. Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0
   
#######
Migrate
#######

Migrating to the Daml Python bindings v8.0
==========================================

v8 does not introduce any new APIs, but drops a lot of symbols that were deprecated in v7 and earlier.
If you have been upgrading to new versions of the client bindings as they became available and have
been reacting to `DeprecationWarning` notifications as they appear, then upgrading to v8 is not
expected to break anything.

Notable symbols that have been removed:

 * dazl.setup_default_logger
   Instead, prefer to set up your own logger. This code suffices as a replacement for most use cases:

   .. code-block: python::
      import logging
      logging.basicConfig()

Migrating to the Daml Python bindings v7.5
==========================================

The Daml Python bindings v7.5.0 introduces a new API, ``dazl.connect`` for adding support to more modern features of
Daml Connect. The ``dazl.Network`` API will continue to be supported in the Daml Python bindings v8 (the next major
version of the Daml Python bindings), but you are encouraged to use ``dazl.connect`` going forward.

``dazl.connect`` embraces design patterns and technical capabilities that have been introduced to
Daml and some of the underlying Python libraries over the last few years.

* Daml Multi-party submissions (as of Daml Connect 1.9):
  https://daml.com/blog/engineering/roles-in-daml-introducing-multi-party-submissions/

  Occasionally it had been necessary for applications to listen to multiple streams as different
  parties and submit commands based on information. With multi-party submissions, relationships
  such as public information and group membership is easier to model with parties, which removes
  the need for clients to attempt to keep otherwise independent streams correlated. As such,
  :class:`dazl.Network` is deprecated in favor of a lighterweight API that is more explicitly
  focused on single connections.

* Daml HTTP JSON API (stable as of DAML SDK 1.3.0)

  While not yet directly supported (this is planned for the Daml Python bindings v8.0.0), the HTTP JSON API supports
  most use-cases for applications that need to communicate with a ledger. The new API is slightly
  restructured for both compatibility with the HTTP JSON API and parity with the JavaScript
  `@daml/ledger <https://www.npmjs.com/package/@daml/ledger>`_ library.

* Daml Authentication/authorization using JSON Web Tokens (JWT)

  The Daml Python bindings were originally built with the simple assumption that a ``Party`` exists 1:1 to a set of
  credentials. As the Daml Ledger API evolved, this assumption no longer holds. The new Daml Python bindings API
  treats tokens more as a 

* Daml return values from exercise choices

  Exercise return values have been available from the Ledger API since Daml was open sourced back
  in April 2019. The Daml Python bindings's API has finally been updated to take this feature into account.

* "Unsubscribing" from streams

  The Daml Python bindings have never had a straightforward way of abandoning event callbacks that were no longer
  needed. The new API makes stream lifecycle more explicit and the responsibility of the user of the
  library. Disposing of streams is now simpler to reason about.

* Native gRPC support for asyncio: https://github.com/grpc/proposal/pull/155

  As of gRPC 1.32.0, the Python gRPC libraries natively support ``asyncio``. This, combined with
  client streams that are no longer coupled to each other, means the internals of the Daml Python bindings are
  significantly simpler while also improving performance.


Command submission changes (``dazl.Network`` and ``dazl.connect``)
------------------------------------------------------------------

The most visible change from trying to align the Daml Python bindings to the
`@daml/ledger <https://www.npmjs.com/package/@daml/ledger>`_ library is a renaming of the properties
of the ``Command`` class hierarchy.

In general, however, you should prefer the command submission
methods on either :class:`dazl.ledger.Connection` or ``dazl.client.PartyClient``, as these methods
give you access to command-specific return values, such as exercise results for
:class:`dazl.ledger.CreateAndExerciseCommand`, :class:`dazl.ledger.ExerciseCommand`, and
:class:`dazl.ledger.ExerciseByKeyCommand`; or information about the created contract
(:class:`dazl.ledger.CreateCommand`).

.. code-block:: python

   # Avoid:
   from dazl import exercise
   # This method does not return anything meaningful
   await client.submit(exercise(cid, "SomeChoice", {"amount": 300}))

   # Instead (v7.5 and later):
   response = await client.exercise(cid, "SomeChoice", {"amount": 300}))
   # This is the result of exercising the choice;
   # available only when using specific command submission methods
   print(response.result)

If you still have a use-case for constructing commands (for example, batch submission), the change
to your code should be as simple as changing imports:

+-------------------------------------------------+-------------------------------------------------+
| Old imports                                     | New import                                      |
+=================================================+=================================================+
| ``dazl.CreateCommand``                          | :class:``dazl.ledger.CreateCommand``            |
| ``dazl.create(...)``                            |                                                 |
| ``dazl.model.writing.CreateCommand``            |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| ``dazl.CreateAndExerciseCommand``               | :class:``dazl.ledger.CreateAndExerciseCommand`` |
| ``dazl.create_and_exercise``                    |                                                 |
| ``dazl.model.writing.CreateAndExerciseCommand`` |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| ``dazl.ExerciseCommand``                        | :class:``dazl.ledger.ExerciseCommand``          |
| ``dazl.exercise(...)``                          |                                                 |
| ``dazl.model.writing.ExerciseCommand``          |                                                 |
+-------------------------------------------------+-------------------------------------------------+
| ``dazl.ExerciseByKeyCommand``                   | :class:``dazl.ledger.ExerciseByKeyCommand``     |
| ``dazl.model.writing.ExerciseByKeyCommand``     |                                                 |
| ``dazl.model.writing.create``                   |                                                 |
+-------------------------------------------------+-------------------------------------------------+

These command classes can and should be used in both the ``dazl.Network`` API and the
``dazl.connect`` API.

The changes:

``dazl.Network``, which has been the primary entry point for the Daml Python binding's code since Daml Python bindings v5, will be
deprecated in the Daml Python bindings v8.0.0. Transitional releases (starting with v7.5.0) will include both APIs, an
``dazl.Network`` will be fully removed in the Daml Python bindings v9.0.0.


.. code-block:: python

   # dazl v5-v7
   import dazl

   network = dazl.Network()
   network.set_config(url="http://localhost:6865")
   client = network.aio_party("Alice")

   @client.on_ledger_create("Some:Request")
   def auto_accept(event):
      return dazl.exercise(event.cid, "Accept")

   network.run_forever()

   # dazl v7.5 or later, transitional API
   import dazl

   network = dazl.ConnectionFactory()
   network.set_config(url="http://localhost:6865")
   client = network.aio_party("Alice")

   @client.on_ledger_create("Some:Request")
   def auto_accept(event):
      return dazl.exercise(event.cid, "Accept")

   network.run_forever()

   # dazl v7.5 or later, new API
   import asyncio, dazl

   async def main():
      async with dazl.connect("http://localhost:6865", "Alice") as conn:
         async for event in conn.stream("Some:Request"):
            await conn.exercise(event.cid, "Accept")

   asyncio.run(main())

A multi-party example. Note that because there is no more ``Network`` to tie connections together,
there are no guarantees that ``Alice`` and ``Bob`` receive events at around the same time. You
should generally

.. code-block:: python

   # dazl v5-v7
   import dazl

   network = dazl.Network()
   network.set_config(url="http://localhost:6865")

   client_alice = network.aio_party("Alice")
   client_bob = network.aio_party("Bob")

   @client_alice.on_ledger_create("Some:Request")
   def auto_accept(event):
      return dazl.exercise(event.cid, "Accept")

   @client_bob.on_ledger_create("Some:Request")
   def auto_accept(event):
      return dazl.exercise(event.cid, "Accept"))

   network.run()

   # dazl v7.5 or later, transitional API
   import dazl

   network = dazl.ConnectionFactory()
   network.set_config(url="http://localhost:6865")

   client_alice = network.aio_party("Alice")
   client_bob = network.aio_party("Bob")

   @client_alice.on_ledger_create("Some:Request")
   def auto_accept(event):
      # changed to avoid warnings, even though it still works the old way
      # return dazl.exercise(event.cid, "Accept")
      return client_alice.submit_exercise(event.cid, "Accept")

   @client_bob.on_ledger_create("Some:Request")
   def auto_accept(event):
      # changed to avoid warnings, even though it still works the old way
      # return dazl.exercise(event.cid, "Accept"))
      return client_bob.submit_exercise(event.cid, "Accept")

   network.run()

   # dazl v7.5 or later, new API
   import asyncio, dazl

   async def main_alice():
      async with dazl.connect("http://localhost:6865", "Alice") as conn:
         async for event in conn.stream("Some:Request"):
            await conn.exercise(event.cid, "Accept")

   async def main_bob():
      async with dazl.connect("http://localhost:6865", "Bob") as conn:
         async for event in conn.stream("Some:Request"):
            await conn.exercise(event.cid, "Accept")

   # Python 3.7+
   asyncio.run(asyncio.gather(main_alice(), main_bob()))


Command-line changes
--------------------

The standard set of command line options provided by ``dazl.run`` has changed. This also impacts any
 Daml Python bindings commands (``dazl ls``, ``dazl tail``, etc.) as well as any custom commands that use
``dazl.run``:

* ``-p`` is now used to denote the Ledger API port and **not** ``Party``. In the Daml Python bindings v8,
  supplying a string argument to ``-p`` will be still interpreted as a ``Party`` but you will get a warning;
  switch to ``--act-as`` or ``--read-as`` instead. This backwards compatible behavior will be
  removed in the Daml Python bindings v9.0.0.

* ``--party``/``--parties`` has been renamed to ``--act-as`` (``-u``); ``--party-groups`` has been
  renamed to ``--read-as`` (``-r``). Both ``--act-as`` and ``--read-as`` take a comma-separated list
  of parties, or as an alternative can be specified multiple times. This matches the terminology
  used in multi-party submissions as added in Daml Connect 1.9. The older forms of these flags will
  be removed in the Daml Python bindings v9.0.0.

* ``--package-fetch-poll-interval`` replaces ``--eager-package-fetch``.
  If unspecified or zero, package polling is disabled. Note that the Daml Python bindings will still generally
  discover packages as it needs to. This is really only of value if you are explicitly interested
  in keeping metadata up-to-date because you are using package metadata, and you should generally
  NOT use this for performance reasons.

  Setting ``-eager-package-fetch`` is the same as specifying ``--package-fetch-poll-interval=1``,
  as the Daml Python bindings previously polled for package updates once a second.

* ``--enable-http-proxy`` has been renamed to ``--use-http-proxy``; the old flag will be removed in
  the Daml Python bindings v9.0.0.

* The following flags have no effect in the Daml Python bindings v8 and will be removed in the Daml Python bindings v8.0.0::
   - ``--idle-timeout``
   - ``--max-command-batch-timeout``
   - ``--max-connection-batch-size``
   - ``--max-connection-count``
   - ``--max-consequence-depth``
   - ``--max-event-block-size``
   - ``--poll-interval``
   - ``--quiet-count``
   - ``--use-acs-service``



Migrating to the Daml Python bindings v7
========================================

Template formats
----------------

Versions of the Daml Python bindings prior to version 7 understood previously-used conventions for template names
other than the form ``package_ref:module_name:entity_name``. As of version 7, this is the only
understood format, and other forms are now unrecognized.

Concretely, this will mean you need to change code usages such as::

    @client.ledger_create('MyModule.MyTemplate')
    def handle_something(event): ...

to::

    @client.ledger_create('MyModule:MyTemplate')
    def handle_something(event): ...

Sandbox Wrapper
---------------

The ``dazl.sandbox()`` function has been removed. In order to set up tests around applications that
use the Daml Python bindings as a library, see the testing guide.

Time Model changes
------------------

`DAML SDK 1.0 <https://github.com/digital-asset/daml/releases/tag/v1.0.0>`_ brought some changes to
the way that time works over the Ledger API. Clients no longer need to behave differently for
ledgers that run in static time vs. real time mode.

The default time model for the DAML SDK Sandbox has changed to real time. Consequently, the Daml Python bindings
APIs for manipulating static time have been removed and no replacement API is available. Static time
is generally only useful in non-production contexts and use cases that require static time are
better addressed with DAML scenarios.

Deprecated symbols removal
--------------------------

Deprecated symbols in the `dazl.damlast` and `dazl.model` packages have been removed:

+-----------------------------------------------------------------------+------------------------------------------------+
| Removed symbol                                                        | Replacement                                    |
+=======================================================================+================================================+
| ``dazl.damlast.daml_lf_1.ModuleRef.package_id`` property              | :func:`dazl.damlast.util.package_ref()`        |
+-----------------------------------------------------------------------+------------------------------------------------+
| ``dazl.damlast.daml_lf_1.ModuleRef.module_name`` property             | :func:`dazl.damlast.util.module_name()`        |
+-----------------------------------------------------------------------+------------------------------------------------+
| ``dazl.damlast.daml_lf_1.TypeConName.module`` property                | :func:`dazl.damlast.util.module_ref()`         |
+-----------------------------------------------------------------------+------------------------------------------------+
| ``dazl.damlast.daml_lf_1.TypeConName.name`` property                  | :func:`dazl.damlast.util.module_local_name()`  |
+-----------------------------------------------------------------------+------------------------------------------------+
| ``dazl.damlast.daml_lf_1.TypeConName.full_name`` property             | no replacement                                 |
+-----------------------------------------------------------------------+------------------------------------------------+
| ``dazl.damlast.daml_lf_1.TypeConName.full_name_unambiguous`` property | :func:`dazl.damlast.util.package_local_name()` |
+-----------------------------------------------------------------------+------------------------------------------------+
| ``dazl.model.types.TypeReference.module`` property                    | :func:`dazl.damlast.util.module_ref()`         |
+-----------------------------------------------------------------------+------------------------------------------------+
| ``dazl.model.types.TypeReference.name`` property                      | :func:`dazl.damlast.util.module_local_name()`  |
+-----------------------------------------------------------------------+------------------------------------------------+
| ``dazl.model.types.TypeReference.full_name`` property                 | no replacement                                 |
+-----------------------------------------------------------------------+------------------------------------------------+
| ``dazl.model.types.TypeReference.full_name_unambiguous`` property     | :func:`dazl.damlast.util.package_local_name()` |
+-----------------------------------------------------------------------+------------------------------------------------+

Migrating to v6
===============

No major breaking API changes were introduced in the v6 release.


Migrating to v5
===============

Library Initialization
----------------------

Old API::

    # original Daml Python bindings API
    with create_client(participant_url='http://localhost:7600', parties=['Alice', 'Bob']) as manager:
        alice_client = manager.client('Alice')
        bob_client = manager.client('Bob')
        # register some event handlers for Alice and Bob
        manager.run_forever()

New API::

    # asyncio-based API
    network = Network()
    network.set_config(url='http://localhost:7600')

    alice_client = network.aio_party('Alice')
    bob_client = network.aio_party('Bob')

    # run
    alice_client.run_forever()

Initialization Event Listeners
------------------------------

Arguments to event listeners have changed in order to provide more information about events and
for consistency across event handlers.

Initialization has been collapsed into a single event, where formerly, there were two events
(``on_init`` and ``on_init_metadata``):

Old API::

    # original Daml Python bindings API
    client = manager.client('Some Party')
    client.on_init(lambda: print('Ledger initialization is happening')
    client.on_init_metadata(lambda store: print(f'Ledger package store: {store}'))

New API::

    # asyncio-based API
    client.add_ledger_init(lambda event: print(f'Ledger initialization with package store: {event.store}'))

Ready Event Listeners
---------------------

Old API::

    # original Daml Python bindings API
    client = manager.client('Some Party')
    client.on_ready(lambda party_name, client\_: print(f'Party {party_name} is ready'))

New API::

    # asyncio-based API
    client = network.aio_party('Some Party')
    client.add_ledger_ready(lambda event: print(f'Party {event.party} is ready'))

Create/Archive Event Listeners
------------------------------

Create and archive events now take a single parameter, called ``event`` by convention, that contain
the contract ID, contract data, and additional metadata about the event, such as the time of
execution, ledger ID, and access to the active contract set.

Old API::

    # original Daml Python bindings API
    client = manager.client('Some Party')
    client.on_created('Some.Asset', lambda cid, cdata: print(cid, cdata))
    client.on_archived('Some.Asset', lambda cid: print(cid))

New API::

    # asyncio-based API
    client = network.aio_party('Some Party')
    client.add_ledger_created('Some.Asset', lambda event: print(event.cid, event.cdata))
    client.add_ledger_archived('Some.Asset', lambda event: print(event.cid))


