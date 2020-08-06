dazl: DA client library for Python
==================================

*Version: |release|*

Dependencies
------------

You will need Python 3.6 or later and a Digital Asset ledger implementation (DA Sandbox or
DA Ledger Server). :term:`dazl` additionally requires the following libraries to be
installed:

* grpcio, version 1.18.0 or later
* PyYAML
* semver

Getting Started
---------------

This section assumes that you already have a running ledger with a DAML model loaded.

Connect to the ledger and submit a single command::

    with dazl.simple_client('http://localhost:7600', 'Alice') as client:
        client.submit_create('Alice', 'My.Template', { someField: 'someText' })

Connect to the ledger as a single party, print all contracts, and close::

    with dazl.simple_client('http://localhost:7600', 'Alice') as client:
        # wait for the ACS to be fully read
        client.ready()
        contract_dict = client.find_active('*')
    print(contract_dict)

Connect to the ledger as multiple parties::

    network = dazl.Network()
    network.set_config(url='http://localhost:7600')

    alice = network.simple_party('Alice')
    bob = network.simple_party('Bob')

    @alice.ledger_ready()
    def set_up(event):
        currency_cid, _ = await event.acs_find_one('My.Currency', {"currency": "USD"})
        return dazl.create('SomethingOf.Value', {
            'amount': 100,
            'currency': currency_cid,
            'from': 'Accept',
            'to': 'Bob' })

    @bob.ledger_created('SomethingOf.Value')
    def on_something_of_value(event):
        return dazl.exercise(event.cid, 'Accept', { 'message': 'Thanks!' })

    network.start()


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
