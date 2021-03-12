.. Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0
   
dazl: DA client library for Python
==================================

*Version: |release|*

Dependencies
------------

You will need Python 3.6 or later and a Daml Ledger.


Getting Started
---------------

This section assumes that you already have a running ledger with the standard `daml new` model
loaded, and have imported `dazl`.

Connect to the ledger and submit a single command::

    import dazl

    async with dazl.connect('http://localhost:6865', 'Alice') as conn:
        conn.create('Main:Asset', {'issuer': 'Alice', 'owner': 'Alice', 'name': 'hello world!'})

Connect to the ledger as a single party, print all contracts, and close::

    import dazl

    async with dazl.connect('http://localhost:6865', 'Alice') as conn:
        contracts = {}
        async for event in conn.query():
            contracts[event.cid] = event.cdata
    print(contracts)

Connect to the ledger using asynchronous callbacks::

    import dazl

    async with dazl.connect('http://localhost:6865', 'Alice') as conn:
        contracts = {}
        @conn.on_create
        def _(event):
            contracts[event.cid] = event.cdata
    print(contracts)

Code
----

Build-time dependencies are handled using `Poetry <https://python-poetry.org/>`_.


Table of Contents
-----------------

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   basics
   testing
   migrating
   dazl
   glossary
