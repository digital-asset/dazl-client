# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Test of two clients operating simultaneously.
"""

import asyncio
import logging
from pathlib import Path
from unittest import TestCase, skip

from dazl import create_client, sandbox
from dazl.rules import Application, ApplicationBuilder, register_application, from_, init, \
    TemplateExpr

TEMPLATE_DAML_FILE = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'


LOG = logging.getLogger('test_duplicate_ledger')

MEMBERS = [dict(
    party_address='{} Member Lane'.format(i),
    party_name='Member{}'.format(i),
    party_index=i) for i in range(0, 9)]


InviteAuthorRole = TemplateExpr('Main.InviteAuthorRole')
InviteReceiverRole = TemplateExpr('Main.InviteReceiverRole')
AuthorRole = TemplateExpr('Main.AuthorRole')
ReceiverRole = TemplateExpr('Main.ReceiverRole')
UnsortedLetter = TemplateExpr('Main.UnsortedLetter')
PostmanRole = TemplateExpr('Main.PostmanRole')


def set_up() -> Application:
    """
    Create the application.
    """
    app_builder = ApplicationBuilder()

    app_builder.as_party('POSTMAN'). \
        add(init().update(PostmanRole(postman='POSTMAN'))). \
        add(invite_members()). \
        add(sort_and_deliver())

    for member in MEMBERS:
        party = member['party_name']
        app_builder.as_party(party). \
            add(InviteAuthorRole.Accept()). \
            add(InviteReceiverRole.Accept()). \
            add(send_to_five_friends(member))

    return app_builder.build()


def invite_members():
    """
    Invite member as an initialization step after a `PostmanRole` contract is seen.
    """
    postman = PostmanRole
    return init(). \
        from_(postman). \
        update([postman.InviteParticipant(
                    party=member['party_name'],
                    address=member['party_address']) \
                for member in MEMBERS])


def sort_and_deliver():
    """
    Sort and deliver a letter for all pairs of receivers and unsorted letters
    where the address for the receiver matches the address of the letter.
    """
    letter = UnsortedLetter
    receiver = ReceiverRole
    return from_(letter, receiver). \
        where(letter['address'] == receiver['address']). \
        update(letter.Sort(receiverCid=receiver))


def send_to_five_friends(member):
    """
    Send letters to five friends for the given member.
    """
    # This is just a demonstration; in a real system, this interaction would
    # likely have to happen "outside" the ledger program.
    party_index = member['party_index']
    party_address = member['party_address']

    return init(). \
        from_(AuthorRole). \
        update([AuthorRole.CreateLetter(
            address=party_address,
            content='I am a letter from {} to {}.'.format(party_index, friend_index))
            for friend_index in
            [i % len(MEMBERS) for i in range(party_index + 1, party_index + 6)]])


class TestDuplicateLedger(TestCase):

    @skip('This test requires a working rules API')
    def test_duplicate_ledger(self):
        """
        Main method.
        """
        with sandbox(TEMPLATE_DAML_FILE) as damli_proc_1, \
             sandbox(TEMPLATE_DAML_FILE) as damli_proc_2, \
             create_client(participant_url=damli_proc_1.url,
                           parties=['POSTMAN'] + [m['party_name'] for m in MEMBERS]) as client_1, \
             create_client(participant_url=damli_proc_2.url,
                           parties=['POSTMAN'] + [m['party_name'] for m in MEMBERS]) as client_2:
            app = set_up()

            register_application(client_1, app)
            register_application(client_2, app)

            # Expect program that is expected to terminate. It will be considered done
            # only once all pending commands have been completed (including any of their
            # follow-ups)
            event_loop = asyncio.get_event_loop()
            event_loop.run_until_complete(asyncio.gather(client_1.main(False), client_2.main(False)))

            LOG.info('Application finished.')

