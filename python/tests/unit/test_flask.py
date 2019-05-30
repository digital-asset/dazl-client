# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
from pathlib import Path
from threading import Thread
from unittest import TestCase

from dazl import simple_client, sandbox, create
from dazl.client import SimplePartyClient
from flask import Flask, jsonify


DAML_PATH = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'
SAMPLE_PARTY = 'TestParty'


class TestFlaskIntegration(TestCase):

    def test_simple_flask_integration(self):
        with sandbox(daml_path=DAML_PATH) as proc:
            with simple_client(proc.url, SAMPLE_PARTY) as client:
                # seed the ledger with some initial state
                client.add_ledger_ready(
                    lambda event: create('Main.PostmanRole', dict(postman=SAMPLE_PARTY)))
                client.ready()

                # now start a Flask app
                main_thread = Thread(target=run_flask_app, args=(client, 9999))
                main_thread.start()

                returned_data = run_flask_test(9999)
                self.assertEqual(returned_data, {'postman': SAMPLE_PARTY})

                main_thread.join(30)
                if main_thread.is_alive():
                    raise Exception('The Flask thread should have terminated, but did not.')


def run_flask_app(client: SimplePartyClient, port: int) -> None:
    app = Flask('TestFlaskIntegration')

    @app.route('/')
    def hello():
        from flask import request

        # shut down Flask as soon as this request is serviced
        func = request.environ.get('werkzeug.server.shutdown')
        func()

        cid, cdata = client.find_one('Main.PostmanRole')
        return jsonify(cdata)

    app.run(host='localhost', port=port)


def run_flask_test(port: int):
    from urllib.request import urlopen
    from time import sleep
    sleep(2)
    with urlopen(f'http://localhost:{port}') as f:
        return json.loads(f.read().decode('utf-8'))
