# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from pathlib import Path
daml_project_root = Path(__file__).parent.parent.parent.parent / '_fixtures/src/post-office'


import dazl
import subprocess
import unittest


# DOC_BEGIN: EXAMPLE
# Change this to point to your DAML project directory.
# daml_project_root = "<path to directory containing daml.yaml>"

# This field will contain t
sandbox_url = None  # type: Optional[str]
sandbox_proc = None  # type: Optional[subprocess.Popen]


def setUpModule():
    """
    Called by ``unittest`` before the tests in this module are going to be run.
    """
    global sandbox_url, sandbox_proc

    port = dazl.util.find_free_port()

    sandbox_proc = subprocess.Popen(
        ["daml", "start", "--start-navigator=no", "--open-browser=no", f"--sandbox-port={port}"],
        cwd=daml_project_root)
    sandbox_url = f"http://localhost:{port}"


def tearDownModule():
    if sandbox_proc is not None:
        sandbox_proc.terminate()


class ExampleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.network = dazl.Network()
        self.network.set_config(url=sandbox_url)
        self.network.start_in_background()

    def tearDown(self) -> None:
        self.network.shutdown()
        self.network.join()

    def test_something(self):
        client = self.network.simple_new_party()
        client.ready()

        client.submit_create('Main:PostmanRole', {'postman': client.party})
        self.assertEqual(len(client.find_active('Main:PostmanRole')), 1)

# DOC_END: EXAMPLE
