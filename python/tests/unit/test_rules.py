# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Rules-based API.

This API is experimental and not guaranteed to remain stable between releases.
"""

from pathlib import Path

from dazl import setup_default_logger, sandbox
from dazl.client import create_client
from dazl.rules import from_, init, TemplateExpr, Application, ApplicationBuilder, register_application
from dazl.plugins import LedgerCapturePlugin

setup_default_logger()

MEMBERS = [dict(
    party_address='{} Member Lane'.format(i),
    party_name='Member{}'.format(i),
    party_index=i) for i in range(0, 50)]

daml_file = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'

PostmanRole = TemplateExpr('Main.PostmanRole')


def set_up() -> Application:
    """
    Create the application.
    """
    InviteAuthorRole = TemplateExpr('Main.InviteAuthorRole')
    InviteReceiverRole = TemplateExpr('Main.InviteReceiverRole')

    app_builder = ApplicationBuilder()

    app_builder.as_party('POSTMAN'). \
        add(init().update(PostmanRole(postman='POSTMAN'))). \
        add(invite_members()). \
        add(sort_()). \
        add(deliver())

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
    return init(). \
        from_(PostmanRole). \
        update([PostmanRole.InviteParticipant(
                    party=member['party_name'],
                    address=member['party_address'])
                for member in MEMBERS])


def sort_():
    """
    Sort and deliver a letter for all pairs of receivers and unsorted letters
    where the address for the receiver matches the address of the letter.
    """
    letter = TemplateExpr('Main.UnsortedLetter')
    receiver = TemplateExpr('Main.ReceiverRole')
    return from_(letter, receiver). \
        where(letter['address'] == receiver['address']). \
        update(letter.Sort(receiverCid=receiver))


def deliver():
    sl = TemplateExpr('Main.SortedLetter')
    return from_(sl).update(sl.Deliver())


def send_to_five_friends(member):
    """
    Send letters to five friends for the given member.
    """
    author = TemplateExpr('Main.AuthorRole')
    # This is just a demonstration; in a real system, this interaction would
    # likely have to happen "outside" the ledger program.
    party_index = member['party_index']
    party_address = member['party_address']

    return init(). \
        from_(author). \
        update([author.CreateLetter(
            address=party_address,
            content='I am a letter from {} to {}.'.format(party_index, friend_index)) \
            for friend_index in \
            [i % len(MEMBERS) for i in range(party_index + 1, party_index + 6)]])


def main():
    """
    Main method.
    """
    with sandbox(daml_file) as damli_proc, \
         create_client(participant_url=damli_proc.url,
                       parties=['POSTMAN'] + [m['party_name'] for m in MEMBERS]) \
    as client:
        app = set_up()

        # Print the "app" on the command line.
        print(app)

        register_application(client, app)

        # Set up a plugin that will simply capture all data for later output on
        # the console.
        inspector = LedgerCapturePlugin.stdout()
        client.register(inspector)

        # Expect program that is expected to terminate. It will be considered done
        # only once all pending commands have been completed (including any of their
        # follow-ups)
        try:
            client.run_until_complete()
        finally:
            inspector.dump_all()
            pass

        # Run the program until the process is killed.
        # client.run_forever()

        # Run the program until a certain ledger query is true or a non-empty set.
        # client.run_until(len(Main.receivedLetters) == len(MEMBERS * 5))


if __name__ == '__main__':
    main()
