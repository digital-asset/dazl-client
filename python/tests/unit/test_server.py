# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from asyncio import sleep
import logging

from aiohttp import ClientSession
from dazl import Network, Party, async_network, connect
from dazl.testing import SandboxLauncher
import pytest

from .dars import TestServer as TestServerDar

LOG = logging.getLogger("test_server")


@pytest.mark.asyncio
async def test_server_endpoint(sandbox: SandboxLauncher) -> None:
    SERVER_PORT = 53390

    async with connect(url=sandbox.url, admin=True) as conn:
        alice = (await conn.allocate_party()).party
        bob = (await conn.allocate_party()).party
        carol = (await conn.allocate_party()).party

    async with async_network(url=sandbox.url, dars=TestServerDar) as network:
        network.set_config(server_port=SERVER_PORT)

        _ = network.aio_party(alice)
        bob_client = network.aio_party(bob)
        carol_client = network.aio_party(carol)

        # create Person contracts for each party
        for party in [alice, bob, carol]:
            ensure_person_contract(network, party)

        # have Bob start up "suspended"; we'll start up Bob from the outside
        bob_bot = bob_client._impl.bots.add_new("Bob's Bot")
        bob_bot.pause()

        @bob_bot.ledger_created("TestServer:Person")
        async def bob_sends_a_message(_):
            await bob_client.exercise_by_key(
                "TestServer:Person",
                "SayHello",
                bob,
                {"receiver": alice, "text": "Bob's ultra secret message"},
            )

        @carol_client.ledger_created("TestServer:Person")
        async def carol_sends_a_message(_):
            await carol_client.exercise_by_key(
                "TestServer:Person",
                "SayHello",
                carol,
                {"receiver": alice, "text": "Carol's gonna Carol"},
            )

        # Carol will start Bob only once Alice has processed three events
        await network.aio_run(client_main(network, SERVER_PORT, alice, bob, carol), keep_open=False)


def ensure_person_contract(network: Network, party: Party) -> None:
    client = network.aio_party(party)
    client.add_ledger_ready(lambda _: client.create("TestServer:Person", dict(party=party)))  # type: ignore


async def client_main(network: Network, server_port: int, alice: Party, bob: Party, carol: Party):
    """
    The main method of a client running against the server endpoint exposed by the dazl app above.
    """
    LOG.info("client_main: started.")
    try:
        async with ClientSession() as session:
            await wait_for_ready(session, server_port, [alice, bob, carol])

            # start Bob from the administration endpoint
            bots_response = await session.get(f"http://localhost:{server_port}/bots")
            bots = await bots_response.json()
            bobs_bots = [bot for bot in bots["bots"] if bot["party"] == bob]
            for bobs_bot in bobs_bots:
                await session.post(
                    f'http://localhost:{server_port}/bots/{bobs_bot["id"]}/state/resume'
                )

            # now make sure Alice received Bob's message, and not Carol's (because Carol was never started)
            alice_client = network.aio_party(alice)
            _, cdata = await alice_client.find_one("TestServer:Message")
            LOG.info("Received message from %r: %r", cdata["sender"], cdata["text"])

            all_messages = alice_client.find("TestServer:Message")
            LOG.info("Alice has a total of %d message(s).", len(all_messages))

            if len(all_messages) > 1:
                raise AssertionError("Alice was only supposed to have one message")

        LOG.info("client_main: finished.")
    except Exception:
        LOG.exception("client_main: failed.")


async def wait_for_ready(session, server_port, parties):
    """
    Block until the dazl server reports these parties as all being ready.
    """
    while True:
        response = await session.get(f"http://localhost:{server_port}/readyz")
        if response.status == 200:
            body = await response.json()
            ready_parties = [key for key, value in body["parties"].items() if value["ready"]]
            if set(ready_parties) == set(parties):
                LOG.info("Everyone is now ready.")
                return
        else:
            LOG.warning("readyz returned a non-200 error code: %r", response.status)
        await sleep(0.2)
