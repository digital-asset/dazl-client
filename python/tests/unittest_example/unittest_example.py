# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

daml_project_root = Path(__file__).parent.parent.parent.parent / "_fixtures/src/post-office"

# DOC_BEGIN: EXAMPLE
# Change this to point to your DAML project directory.
# daml_project_root = "<path to directory containing daml.yaml>"

import unittest

from dazl import Network, testing

sandbox_proc = testing.sandbox(project_root=daml_project_root)


def setUpModule():
    """
    Called by ``unittest`` before the tests in this module are going to be run.
    """
    global sandbox_proc
    sandbox_proc.start()


def tearDownModule():
    if sandbox_proc is not None:
        sandbox_proc.stop()


class ExampleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.network = Network()
        self.network.set_config(url=sandbox_proc.url)
        self.network.start_in_background()

    def tearDown(self) -> None:
        self.network.shutdown()
        self.network.join()

    def test_something(self):
        client = self.network.simple_new_party()
        client.ready()

        client.create("Main:PostmanRole", {"postman": client.party})
        self.assertEqual(len(client.find_active("Main:PostmanRole")), 1)


# DOC_END: EXAMPLE
