Migrate
=======

Migrating from dazl v5 from v4



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


