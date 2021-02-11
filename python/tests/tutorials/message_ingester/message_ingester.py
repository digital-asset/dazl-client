# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import create, exercise
from dazl.client import create_client
from dazl.plugins import LedgerCapturePlugin

parties = ["Alice", "Bob"]
url = "http://localhost:7600/"


def genesis_contract(_, __):
    return create("MessageIngester.OperatorRole", {"operator": "Alice"})


# DOC_BEGIN: FUNCTION_INGEST_THE_MESSAGE
def ingest_the_message(cid, cdata):
    ingest_message = [exercise(cid, "IngestMessage", {"requestProcessingParty": "Bob"})]
    return ingest_message
    # DOC_BEGIN: FUNCTION_INGEST_THE_MESSAGE


def accept_the_message(cid, cdata):
    accept_message_action = [exercise(cid, "AcceptMessage", {"acknowledgingParty": "alice"})]
    return accept_message_action


def acknowledge_the_message(cid, cdata):
    acknowledge_message_action = [exercise(cid, "Acknowledge", {})]
    return acknowledge_message_action


def register_event_handlers(client_mgr):
    # define a sandbox client, associated with the 'operator' party, and how it reacts to events
    alice_client = client_mgr.new_client("Alice")
    alice_client.on_ready(genesis_contract)
    # DOC_BEGIN: SAMPLE_CALLBACK_ONCREATED
    alice_client.on_created("MessageIngester.OperatorRole", ingest_the_message)
    # DOC_END: SAMPLE_CALLBACK_ONCREATED
    alice_client.on_created("MessageIngester.TradeResponse", acknowledge_the_message)

    # define a sandbox client, associated with the 'requestor' party, and how it reacts to events
    bob_client = client_mgr.new_client("Bob")
    bob_client.on_created("MessageIngester.TradeRequest", accept_the_message)


def run():
    with create_client(parties=parties, participant_url=url) as client_mgr:
        inspector = LedgerCapturePlugin.stdout()
        try:
            client_mgr.register(inspector)
            register_event_handlers(client_mgr)
            ledger_run = client_mgr.run_until_complete()
            return ledger_run.exit_code
        finally:
            inspector.dump_all()


if __name__ == "__main__":
    run()
