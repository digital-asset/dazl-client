.. Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0
   
#######
Migrate
#######

Migrating to dazl v8
====================

Command-line changes
--------------------

Commands such as ``dazl ls``, ``dazl tail``, or options provided for your application by calling
``dazl.run`` have changed:

* ``-p`` is now used to denote the Ledger API port and **not** ``Party``. In dazl v8, supplying a
  string argument to ``-p`` will be still interpreted as a ``Party`` but you will get a warning;
  switch to ``--act-as`` or ``--read-as`` instead. This backwards compatible behavior will be
  removed in dazl v9.

* ``--party``/``--parties`` has been renamed to ``--act-as`` (``-u``); ``--party-groups`` has been
  renamed to ``--read-as`` (``-r``). Both ``--act-as`` and ``--read-as`` take a comma-separated list
  of parties, or as an alternative can be specified multiple times. This matches the terminology
  used in multi-party submissions as added in Daml Connect 1.9. The older forms of these flags will
  be removed in dazl v9.

* ``--package-fetch-poll-interval`` replaces ``--eager-package-fetch``.
  If unspecified or zero, package polling is disabled. Note that ``dazl`` will still generally
  discover packages as it needs to. This is really only of value if you are explicitly interested
  in keeping metadata up-to-date because you are using package metadata, and you should generally
  NOT use this for performance reasons.

  Setting ``-eager-package-fetch`` is the same as specifying ``--package-fetch-poll-interval=1``,
  as dazl previously polled for package updates once a second.

* ``--enable-http-proxy`` has been renamed to ``--use-http-proxy``; the old flag will be removed in
  dazl v9.

* The following flags have no effect in dazl v8 and will be removed in dazl v9::
   - ``--idle-timeout``
   - ``--max-command-batch-timeout``
   - ``--max-connection-batch-size``
   - ``--max-connection-count``
   - ``--max-consequence-depth``
   - ``--max-event-block-size``
   - ``--poll-interval``
   - ``--quiet-count``
   - ``--use-acs-service``


Migrating to dazl v7.5
======================

dazl 7.5 introduced a new API for connecting to the Ledger API that embraces design patterns and
technical capabilities that have been introduced to Daml and some of the underlying Python libraries
over the last few years.

* Daml Multi-party submissions (as of Daml Connect 1.9):
  https://daml.com/blog/engineering/roles-in-daml-introducing-multi-party-submissions/

  Occasionally it had been necessary for applications to listen to multiple streams as different
  parties and submit commands based on information. With multi-party submissions, relationships
  such as public information and group membership is easier to model with parties, which removes
  the need for clients to attempt to keep otherwise independent streams correlated. As such,
  :class:`dazl.Network` is deprecated in favor of a lighterweight API that is more explicitly
  focused on single connections.

* Daml HTTP JSON API (stable as of DAML SDK 1.3.0)

  While not yet directly supported (this is planned for dazl v8), the HTTP JSON API supports most
  use-cases for applications that need to communicate with a ledger. The new API is slightly
  restructured for both compatibility with the HTTP JSON API and parity with the JavaScript
  `@daml/ledger <https://www.npmjs.com/package/@daml/ledger>`_ library.

* Daml Authentication/authorization using JSON Web Tokens (JWT)

  dazl was originally built with the simple assumption that a ``Party`` exists 1:1 to a set of
  credentials. As the Daml Ledger API evolved, this assumption no longer holds. The new dazl API
  treats tokens more as a

* Daml return values from exercise choices

  Exercise return values have been available from the Ledger API since Daml was open sourced back
  in April 2019. dazl's API has finally been updated to take this feature into account.

* "Unsubscribing" from streams

  ``dazl`` has never had a straightforward way of abandoning event callbacks that were no longer
  needed. The new API makes stream lifecycle more explicit and the responsibility of the user of the
  library. Disposing of streams is now simpler to reason about.

* Native gRPC support for asyncio: https://github.com/grpc/proposal/pull/155

  As of gRPC 1.32.0, the Python gRPC libraries natively support ``asyncio``. This, combined with
  client streams that are no longer coupled to each other, means the internals of ``dazl`` are
  significantly simpler while also improving performance.

The changes:

``dazl.Network``, which has been the primary entry point for dazl code since dazl v5, is now
deprecated. Transitional releases (starting with v7.5) will include both APIs, and ``dazl.Network``
will be fully removed in dazl v8.

To ease the transition, you can simply replace ``dazl.Network`` with ``dazl.ConnectionFactory``,
but there are some important semantic differences between these APIs:

* Old-style template names are not supported with ``dazl.ConnectionFactory``. If you were using
  template names such as "Some.Module.Contract" instead of "Some.Module:Contract", this is the time
  to change.
* Callbacks from a ``dazl.ConnectionFactory`` that _return_ commands will raise warnings
  (though they will still function as expected). These warnings are raised to help you find
  examples of callbacks that will need to be reworked when transitioning to the new API.
* Multiple calls to aio_party or simple_party for the same ``Party`` will still share an underlying
  connection, but a warning will be raised. These warnings are raised to help you find examples of
  places where you may be relying on connection sharing; connections are no longer automatically
  shared in the new API.
* Data streams will no longer be synchronized across Parties. If you were building up state from the
  perspective of one party and using that information as a different party, you will experience
  different behavior. This behavior is anyway generally frowned upon, but prior to the introduction
  of multi-party submissions, occasionally necessary.


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



Migrating to dazl v7
====================

Template formats
----------------

Versions of `dazl` prior to version 7 understood previously-used conventions for template names
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
use ``dazl`` as a library, see the testing guide.

Time Model changes
------------------

`DAML SDK 1.0 <https://github.com/digital-asset/daml/releases/tag/v1.0.0>`_ brought some changes to
the way that time works over the Ledger API. Clients no longer need to behave differently for
ledgers that run in static time vs. real time mode.

The default time model for the DAML SDK Sandbox has changed to real time. Consequently, the `dazl`
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

    # original dazl API
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

    # original dazl API
    client = manager.client('Some Party')
    client.on_init(lambda: print('Ledger initialization is happening')
    client.on_init_metadata(lambda store: print(f'Ledger package store: {store}'))

New API::

    # asyncio-based API
    client.add_ledger_init(lambda event: print(f'Ledger initialization with package store: {event.store}'))

Ready Event Listeners
---------------------

Old API::

    # original dazl API
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

    # original dazl API
    client = manager.client('Some Party')
    client.on_created('Some.Asset', lambda cid, cdata: print(cid, cdata))
    client.on_archived('Some.Asset', lambda cid: print(cid))

New API::

    # asyncio-based API
    client = network.aio_party('Some Party')
    client.add_ledger_created('Some.Asset', lambda event: print(event.cid, event.cdata))
    client.add_ledger_archived('Some.Asset', lambda event: print(event.cid))


