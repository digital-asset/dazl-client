import pytest

from dazl import async_network, create

from .dars import AllParty, PostOffice


@pytest.mark.asyncio
async def test_template_filtering(sandbox):
    # First, create a few contracts stretching across two DARs and validate that all of those
    # contracts show up in the active contract set. async_network will supply the list of DARs to
    # dazl.
    async with async_network(url=sandbox, dars=[AllParty, PostOffice]) as network:
        client = network.aio_new_party()

        # Remember the party, because we're going to reconnect as this party, but with a restricted
        # set of DARs.
        party = client.party

        network.start()
        await client.submit(
            [
                create("AllParty:PrivateContract", {"someParty": party}),
                create("AllParty:PrivateContract", {"someParty": party}),
                create("AllParty:PrivateContract", {"someParty": party}),
                create("Main:PostmanRole", {"postman": party}),
                create("Main:PostmanRole", {"postman": party}),
            ]
        )

        # The ACS should only contain the five contracts we created: two from Post Office, and three
        # from AllKindsOf.
        contracts = client.find_active("*")
        assert len(contracts) == 5

    # Now create a new client to the same sandbox, but with less DARs
    async with async_network(url=sandbox, dars=[PostOffice]) as network:
        client = network.aio_party(party)
        network.start()

        await client.ready()

        # The ACS should only contain the two contracts we created that were part of the Post Office
        # model.
        contracts = client.find_active("*")
        assert len(contracts) == 2
