# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
All of the snippets for the Postman tutorial. Executing this file as a module will test as many of
the snippets as possible in the way that they are intended to be used.

This file should not be modified without also carefully looking at ``tutorials_post_office.rst``
in the documentation folder.
"""


import unittest
from dazl import setup_default_logger
from dazl.client import ExitCode  # noqa
from dazl.client.config import LedgerNodeConfiguration

# These imports are included in the documentation EXACTLY AS IS.
# Only add imports here if they are used as part of the tutorial's documentation.
# DOC_BEGIN: IMPORTS_CONSTANTS
from os import path

from dazl import create, sandbox
from dazl.client import create_client

DAML_FILE = path.realpath(path.join(path.dirname(__file__), './Main.daml'))

POSTMAN_PARTY = 'Postman'
MEMBER_PARTY_COUNT = 10
# DOC_END: IMPORTS_CONSTANTS


setup_default_logger()
LedgerNodeConfiguration._defaults['poll_interval'] = 1.0


def create_postman():
    # DOC_BEGIN: CREATE_POSTMAN
    def run_test(url):
        all_parties = [POSTMAN_PARTY]

        with create_client(parties=all_parties, participant_url=url) as client_mgr:
            postman_client = client_mgr.new_client(POSTMAN_PARTY)
            postman_client.on_ready(
                lambda _, __: create('Main:PostmanRole', dict(postman=POSTMAN_PARTY)))

            ledger_run = client_mgr.run_until_complete()
            return ledger_run.exit_code
    # DOC_END: CREATE_POSTMAN
    return run_test


def inspect_ledger():
    # DOC_BEGIN: INSPECT_LEDGER
    from dazl.plugins import LedgerCapturePlugin

    def run_test(url):
        all_parties = [POSTMAN_PARTY]

        with create_client(parties=all_parties, participant_url=url) as client_mgr:
            inspector = LedgerCapturePlugin.stdout()
            try:
                postman_client = client_mgr.new_client(POSTMAN_PARTY)
                postman_client.on_ready(
                    lambda _, __: create('Main:PostmanRole', dict(postman=POSTMAN_PARTY)))

                client_mgr.register(inspector)

                ledger_run = client_mgr.run_until_complete()
                return ledger_run.exit_code
            finally:
                inspector.dump_all()
    # DOC_END: INSPECT_LEDGER
    return run_test


def invite_participants():
    from dazl.plugins import LedgerCapturePlugin

    # DOC_BEGIN: INVITE_PARTICIPANTS
    def run_test(url):
        members = [dict(party=f'Member {i}', address=address(i)) for i in
                   range(0, MEMBER_PARTY_COUNT)]
        all_parties = [POSTMAN_PARTY] + [member['party'] for member in members]

        with create_client(parties=all_parties, participant_url=url) as client_mgr:
            inspector = LedgerCapturePlugin.stdout()
            try:
                set_up(client_mgr, members)
                client_mgr.register(inspector)

                ledger_run = client_mgr.run_until_complete()
                return ledger_run.exit_code
            finally:
                inspector.dump_all()

    def set_up(client_mgr, members):
        postman_client = client_mgr.new_client(POSTMAN_PARTY)
        postman_client.on_ready(
            lambda _, __: create('Main:PostmanRole', dict(postman=POSTMAN_PARTY)))
        postman_client.on_created(
            'Main:PostmanRole',
            lambda cid, cdata: [cid.exercise('InviteParticipant', m) for m in members])

    def address(index):
        return '{} Member Lane'.format(index)
    # DOC_END: INVITE_PARTICIPANTS
    return run_test


def final_run_test(set_up):
    from dazl.plugins import LedgerCapturePlugin

    def address(index):
        return f'{index} Member Lane'

    def run_test(url):
        members = [dict(party=f'Member {i}', address=address(i))
                   for i in range(0, MEMBER_PARTY_COUNT)]
        all_parties = [POSTMAN_PARTY] + [member['party'] for member in members]

        with create_client(parties=all_parties, participant_url=url) as client_mgr:
            inspector = LedgerCapturePlugin.stdout()
            try:
                set_up(client_mgr, members)
                client_mgr.register(inspector)

                ledger_run = client_mgr.run_until_complete()
                return ledger_run.exit_code
            finally:
                inspector.dump_all()

    return run_test


def accept_invites():
    # DOC_BEGIN: ACCEPT_INVITES
    def set_up(client_mgr, members):
        postman_client = client_mgr.new_client(POSTMAN_PARTY)
        postman_client.on_ready(
            lambda _, __: create('Main:PostmanRole', dict(postman=POSTMAN_PARTY)))
        postman_client.on_created(
            'Main:PostmanRole',
            lambda cid, cdata: [cid.exercise('InviteParticipant', m) for m in members])

        member_clients = [client_mgr.new_client(m['party']) for m in members]
        for member_client in member_clients:
            # every member automatically accepts
            member_client.on_created(
                'Main:InviteAuthorRole', lambda cid, cdata: cid.exercise('AcceptInviteAuthorRole'))
            member_client.on_created(
                'Main:InviteReceiverRole', lambda cid, cdata: cid.exercise('AcceptInviteReceiverRole'))
    # DOC_END: ACCEPT_INVITES
    return final_run_test(set_up)


def send_letters():
    def address(index):
        return f'{index} Member Lane'

    # DOC_BEGIN: SEND_LETTERS
    from functools import partial

    def set_up(client_mgr, members):
        postman_client = client_mgr.new_client(POSTMAN_PARTY)
        postman_client.on_ready(
            lambda _, __: create('Main:PostmanRole', dict(postman=POSTMAN_PARTY)))
        postman_client.on_created(
            'Main:PostmanRole',
            lambda cid, cdata: [cid.exercise('InviteParticipant', m) for m in members])

        member_clients = [client_mgr.new_client(m['party']) for m in members]
        for member_client in member_clients:
            # every member automatically accepts
            member_client.on_created(
                'Main:InviteAuthorRole', lambda cid, cdata: cid.exercise('AcceptInviteAuthorRole'))
            member_client.on_created(
                'Main:InviteReceiverRole', lambda cid, cdata: cid.exercise('AcceptInviteReceiverRole'))
            member_client.on_created(
                'Main:AuthorRole', partial(send_five_letters, member_client.party_name))

    def send_five_letters(party_name, cid, cdata):
        if party_name == cdata['author']:
            party_index = int(party_name.split(' ')[1])
            addresses = map(lambda i: address(i % MEMBER_PARTY_COUNT), range(party_index + 1, party_index + 6))

            # exercise the same non-consuming choice repeatedly
            return [cid.exercise(
                'CreateLetter',
                dict(address=address, content=f'I am a letter from {party_name} to {address}'))
                for address in addresses]

    # DOC_END: SEND_LETTERS
    return final_run_test(set_up)


def main_boilerplate(globals_, run_test):
    __name__ = globals_['__name__']

    # DOC_BEGIN: MAIN-BOILERPLATE
    if __name__ == '__main__':
        import sys

        with sandbox(DAML_FILE) as server:
            exit_code = run_test(server.url)
            sys.exit(int(exit_code))
    # DOC_END: MAIN-BOILERPLATE


class TutorialTest(unittest.TestCase):
    def test_create_postman(self):
        run_test = create_postman()
        with sandbox(DAML_FILE) as server:
            self.assertEqual(run_test(server.url), ExitCode.SUCCESS)

    def test_inspect_ledger(self):
        run_test = inspect_ledger()
        with sandbox(DAML_FILE) as server:
            self.assertEqual(run_test(server.url), ExitCode.SUCCESS)

    def test_invite_participants(self):
        run_test = invite_participants()
        with sandbox(DAML_FILE) as server:
            self.assertEqual(run_test(server.url), ExitCode.SUCCESS)

    def test_accept_invites(self):
        run_test = accept_invites()
        with sandbox(DAML_FILE) as server:
            self.assertEqual(run_test(server.url), ExitCode.SUCCESS)

    def test_send_letters(self):
        run_test = send_letters()
        with sandbox(DAML_FILE) as server:
            self.assertEqual(run_test(server.url), ExitCode.SUCCESS)
