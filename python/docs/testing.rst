.. Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0
   
#######
Testing
#######

Code that you write against `dazl` will typically need a Sandbox to be running. You can use a setup
similar to what ``dazl`` does for its own tests.

``dazl`` starts a single Sandbox process for all of its tests, because starting and stopping Sandbox
instances repeatedly can greatly slow down the test suite. To achieve good isolation between tests,
use freshly-allocated ``Party`` in instances instead. Because of DAML's privacy model, islands of
``Party`` s that are mutually unaware of each other are guaranteed to never see unintended
contracts.

``unittest``
############

You can use a module-based setup fixture in ``unittest``:

.. literalinclude:: ../tests/unittest_example/unittest_example.py
    :language: python
    :start-after: # DOC_BEGIN: EXAMPLE
    :end-before: # DOC_END: EXAMPLE
    :name: unittest_example

pytest
######

``dazl`` uses pytest internally, which supports session-scoped fixtures and avoids the need for
globals:

.. code-block:: python

    import dazl
    import pytest

    # Change this to point to your DAML project directory.
    # daml_project_root = "<path to directory containing daml.yaml>"

    @pytest.fixture(scope="session")
    def sandbox():
        port = dazl.util.find_free_port()

        sandbox_proc = subprocess.Popen(
            ["daml", "start", "--start-navigator=no", "--open-browser=no", f"--sandbox-port={port}"],
            cwd=daml_project_root)
        try:
            yield "http://localhost:{port}"
        finally:
            sandbox_proc.terminate()


    def test_something(sandbox):
        network = dazl.Network()
        network.set_config(url=sandbox_url)
        network.start_in_background()
        try:
            client = self.network.simple_new_party()
            client.ready()

            client.submit_create('Main:PostmanRole', {'postman': client.party})
            assert len(client.find_active('Main:PostmanRole') == 1

        finally:
            network.shutdown()
            network.join()
