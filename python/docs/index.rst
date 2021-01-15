.. Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0
   
dazl: DA client library for Python
==================================

*Version: |release|*

Dependencies
------------

You will need Python 3.6 or later and a Digital Asset ledger implementation (DA Sandbox or
DA Ledger Server). 

Build-time dependencies are handled using `Poetry <https://poetry.eustace.io/>`_.


Getting Started
---------------

This section assumes that you already have a running ledger with the standard `daml new` model loaded, and have imported `dazl`.

Connect to the ledger and submit a single command::

    with dazl.simple_client('http://localhost:6865', 'Alice') as client:
        contract = { 'issuer' : 'Alice', 'owner' : 'Alice', 'name' : 'hello world!' }
        client.ready()
        client.submit_create('Main.Asset', contract)

Connect to the ledger as a single party, print all contracts, and close::

    with dazl.simple_client('http://localhost:7600', 'Alice') as client:
        # wait for the ACS to be fully read
        client.ready()
        contract_dict = client.find_active('*')
    print(contract_dict)

Connect to the ledger using asynchronous callbacks::

    from dazl.model.reading import ReadyEvent
    network = dazl.Network()
    network.set_config(url='http://localhost:6865')

    alice = network.aio_party('Alice')

    @alice.ledger_ready()
    async def onReady(event: ReadyEvent):
      contracts = await event.acs_find_one('Main.Asset')
      print(contracts)

    network.run_until_complete()

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
