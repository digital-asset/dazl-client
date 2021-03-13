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


Migrating from dazl v6 from v7
==============================

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

Migrating from dazl v5 from v6
==============================

No major breaking API changes were introduced in the v6 release.


Migrating from dazl v5 from v4
==============================



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


