# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from dazl import create, exercise, sandbox, Network

DAML_PATH = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'


def test_parties_can_be_added_after_run_forever():
    with sandbox(daml_path=DAML_PATH) as proc:
        network = Network()
        network.set_config(url=proc.url)

        operator = network.aio_party('Operator')
        party_a = network.aio_party('Party A')
        party_b = network.aio_party('Party B')

        @operator.ledger_ready()
        def _(event):
            return create('Main.PostmanRole', {'postman': 'Operator'})

        @operator.ledger_created('Main.PostmanRole')
        def __(event):
            return [exercise(event.cid, 'InviteParticipant', {'party': party, 'address': 'whatevs'})
                    for party in ('Party A', 'Party B', 'Party C')]

        @party_a.ledger_created('Main.InviteAuthorRole')
        async def _(event):
            party_c = network.aio_party('Party C')

            @party_c.ledger_created('Main.AuthorRole')
            def ___(event):
                network.shutdown()

            cid, cdata = await party_c.find_one('Main.InviteAuthorRole')
            party_c.submit_exercise(cid, 'AcceptInviteAuthorRole')

        network.run_forever()

