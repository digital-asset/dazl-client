import logging
from asyncio import sleep

import dazl
from dazl.protocols.core import ReadyEvent, ContractCreateEvent


logging.basicConfig(filename="app.log", level=logging.INFO)


def send(party, cid, choice_name, count):
    logging.info(
        party
        + " is exercising "
        + choice_name
        + " on "
        + str(cid)
        + " at count "
        + str(count)
    )
    return dazl.exercise(cid, choice_name)


def init_pingpong(network: dazl.Network, sender, receiver):
    sender_client = network.aio_party(sender)

    @sender_client.ledger_ready()
    async def init(event: ReadyEvent):
        pings = event.acs_find_active(
            "PingPong.Ping", match=lambda cdata: cdata["sender"] == sender
        )
        pongs = event.acs_find_active(
            "PingPong.Pong", match=lambda cdata: cdata["receiver"] == sender
        )
        if len(pings) == 0 and len(pongs) == 0:
            logging.info("Initializing Ping for " + sender)
            return dazl.create(
                "PingPong.Ping", {"sender": sender, "receiver": receiver, "count": 0}
            )


def register_pingpong_handler(network: dazl.Network, party):
    party_client = network.aio_party(party)

    @party_client.ledger_ready()
    async def init(event: ReadyEvent):
        cmds = []

        pings = event.acs_find_active(
            "PingPong.Ping", match=lambda cdata: cdata["receiver"] == party
        )
        for pingCid, pingData in pings.items():
            cmds.append(send(party, pingCid, "RespondPong", pingData["count"]))

        pongs = event.acs_find_active(
            "PingPong.Pong", match=lambda cdata: cdata["receiver"] == party
        )
        for pongCid, pongData in pongs.items():
            cmds.append(send(party, pongCid, "RespondPing", pongData["count"]))

        return cmds

    @party_client.ledger_created("PingPong.Ping")
    async def ping(event: ContractCreateEvent):
        if event.cdata["receiver"] == party:
            await sleep(1)
            return send(party, event.cid, "RespondPong", event.cdata["count"])

    @party_client.ledger_created("PingPong.Pong")
    async def pong(event: ContractCreateEvent):
        if event.cdata["receiver"] == party:
            await sleep(1)
            return send(party, event.cid, "RespondPing", event.cdata["count"])


def dazl_main(network):
    init_pingpong(network, "Alice", "Bob")
    init_pingpong(network, "Bob", "Alice")

    register_pingpong_handler(network, "Alice")
    register_pingpong_handler(network, "Bob")


def main():
    dazl.run(dazl_main)


if __name__ == "__main__":
    main()
