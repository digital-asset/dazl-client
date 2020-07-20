"""
Tests to ensure that cancelled command submissions behave correctly.
"""
from dazl import sandbox, Network
from tests.unit.dars import Pending

PARTY = 'SomeParty'


def test_cancelled_write():

    with sandbox(Pending) as proc:
        network = Network()
        network.set_config(url=proc.url)

        party_client = network.aio_party(PARTY)

        async def test_body(_):
            # Submit a command, but _immediately_ cancel it. Because there are no awaits, this code
            # cannot have possibly been interrupted by the coroutine responsible for scheduling a write
            # to the server, so the command should be cancelled.
            fut = party_client.submit_create('Pending:Counter', {'owner': PARTY, 'value': 66})
            fut.cancel()

            # Immediately afterwards, schedule another command submission; this time, we wait for it.
            fut = party_client.submit_create('Pending:Counter', {'owner': PARTY, 'value': 7})
            await fut

        party_client.add_ledger_ready(test_body)

        network.run_until_complete()

        data = party_client.find_active('Pending:Counter')

    assert len(data) == 1
    assert list(data.values())[0]['value'] == 7
