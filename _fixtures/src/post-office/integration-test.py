# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging

import sys

from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

from dazl import create, exercise, Network, write_acs

LOG = logging.getLogger('integration_test')

POSTMAN_PARTY = 'Postman'
MEMBER_PARTY_COUNT = 6

dar_file = Path(__file__).parent / '.daml/dist/post-office-1.0.0.dar'


def address(index):
    return '{} Member Lane'.format(index)


class PartyBot:
    def __init__(self, party_name):
        self.party_name = party_name

    def send_to_five_friends(self, event):
        if self.party_name == event.cdata['author']:
            party_index = int(self.party_name.split(' ')[1])
            choices = []
            for receiver_index in map(lambda i: i % MEMBER_PARTY_COUNT, range(party_index + 1, party_index + 6)):
                receiver_address = address(receiver_index)
                choices.append(('CreateLetter', dict(
                    address=receiver_address,
                    content='I am a letter from {} to {}'.format(self.party_name, receiver_address))))
                choices.append(('CreateTimeLetter', dict(
                    address=receiver_address,
                    content=datetime(2000,1,1))))
                choices.append(('CreateListIntLetter', dict(
                    address=receiver_address,
                    content=[0, 1, 2, 3, 4])))

            return [exercise(event.cid, choice_name, choice_args)
                    for choice_name, choice_args in choices]


class PostOffice:
    """ Simulates a post office. """
    def __init__(self):
        self._addrs = dict()
        self._unknown_letters = defaultdict(list)
        self._unsorted_letter_count = 0

    def register_address(self, event):
        address = event.cdata['address']
        self._addrs[address] = event.cid
        unknown_letters = self._unknown_letters.pop(address, None)
        if unknown_letters:
            return [letter_cid.exercise('Sort', dict(receiverCid=event.cid))
                    for letter_cid in unknown_letters]
        return ()

    def sort_and_deliver_letter(self, event):
        """
        Try to sort and deliver the letter. If the address is unknown, it is held at the post office
        until ``register_address`` is called with a matching address.
        """
        address = event.cdata['address']
        receiver_cid = self._addrs.get(address)
        if receiver_cid is not None:
            return exercise(event.cid, 'Sort', dict(receiverCid=receiver_cid))
        else:
            self._unknown_letters[address].append(event.cid)
            self._unsorted_letter_count += 1
            return None


def run_test(url, keepalive=False):
    start_time = datetime.now()

    members = [dict(party=f'Member {i}', address=address(i)) for i in range(0, MEMBER_PARTY_COUNT)]

    network = Network()
    network.set_config(url=url, server_port=8105)

    postman_client = network.aio_party(POSTMAN_PARTY)
    member_clients = [network.aio_party(m['party']) for m in members]

    post_office = PostOffice()

    postman_client.add_ledger_ready(lambda event: create('Main:PostmanRole', dict(postman=POSTMAN_PARTY)))
    postman_client.add_ledger_created('Main:PostmanRole', lambda event: [exercise(event.cid, 'InviteParticipant', m) for m in members])
    postman_client.add_ledger_created('Main:UnsortedLetter', post_office.sort_and_deliver_letter)
    postman_client.add_ledger_created('Main:ReceiverRole', post_office.register_address)
    postman_client.add_ledger_created('Main:SortedLetter', lambda event: exercise(event.cid, 'Deliver'))

    @postman_client.ledger_exercised('Main:PostmanRole', 'InviteParticipant')
    def log(event):
        LOG.info('Observing the exercise of an InviteParticipant: %s', event)

    for member_client in member_clients:
        bot = PartyBot(member_client.party)
        # every member automatically accepts
        member_client.add_ledger_created('Main:InviteAuthorRole', lambda event: exercise(event.cid, 'AcceptInviteAuthorRole'))
        member_client.add_ledger_created('Main:InviteReceiverRole', lambda event: exercise(event.cid, 'AcceptInviteReceiverRole'))
        # every member, upon joining, sends messages to five of their best friends
        member_client.add_ledger_created('Main:AuthorRole', bot.send_to_five_friends)

    try:
        if not keepalive:
            network.run_until_complete()
        else:
            network.run_forever()
        ledger_run_failed = False
    except:
        LOG.exception('The run failed!')
        ledger_run_failed = True

    # Display everything, including archived contracts if we terminated for an unexpected reason.
    write_acs(sys.stdout, network, include_archived=ledger_run_failed)

    LOG.info('%s letters were received before the recipients were known.', post_office._unsorted_letter_count)
    LOG.info('Test finished in %s.', datetime.now() - start_time)


def _main():
    """
    Run this test case.

    If a URL is specified, then the integration test will run pointing to that ledger
    implementation. If a URL is _not_ supplied, then a local sandbox is spun up on a random port,
    the integration test is run, and the sandbox is shut down when it is complete.
    """
    import argparse
    import subprocess

    logging.basicConfig(level=logging.INFO)

    from dazl.util import ProcessLogger, find_free_port, kill_process_tree, wait_for_process_port

    argparser = argparse.ArgumentParser()

    backend_args = argparser.add_mutually_exclusive_group()
    backend_args.add_argument('--url', required=False, help='The URL of the *existing* server to connect to')
    backend_args.add_argument('--port', required=False, type=int, help='The port to spin up a NEW Sandbox')

    argparser.add_argument('--keep-alive', action='store_true')

    args = argparser.parse_args()

    if args.url:
        LOG.info('Running the test against an existing sandbox: %s', args.url)
        run_test(args.url)
    else:
        LOG.info('Spinning up a local sandbox as part of the test...')
        port = args.port if args.port else find_free_port()

        proc = subprocess.Popen(
            ["daml", "start", "--start-navigator=no", "--open-browser=no", f"--sandbox-port={port}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True)
        try:
            ProcessLogger(proc, logging.getLogger('sandbox')).start()
            wait_for_process_port(proc, port, timedelta(seconds=10))
            
            run_test(f'http://localhost:{port}', args.keep_alive)
        finally:
            kill_process_tree(proc)


if __name__ == '__main__':
    _main()
