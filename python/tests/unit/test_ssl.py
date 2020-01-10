# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from subprocess import run
from pathlib import Path
from typing import Tuple

from dazl import create, sandbox, Network, LOG
from dazl.model.network import SSLSettings

_DAZL_ROOT = Path(__file__).parent.parent.parent
# TODO: This utility should be fetched in a less ugly way
TLS_KEYGEN_SCRIPT = _DAZL_ROOT.parent.parent.parent / 'pipeline' / 'scripts' / 'TLS' / 'generate-certificates.sh'
TEMPLATE_DAML_FILE = _DAZL_ROOT / '_template' / 'Main.daml'


def test_ssl_not_defined():
    assert not SSLSettings(None, None, None)


@pytest.mark.skip('Still needs work')
def test_ssl_connectivity():
    client_ssl_settings, server_ssl_settings = create_ssl_test_package()
    messages_received = []
    with sandbox(TEMPLATE_DAML_FILE, ssl_settings=server_ssl_settings) as proc:
        network = Network()
        network.set_config(url=proc.url,
                           ca_file=client_ssl_settings.ca_file,
                           cert_file=client_ssl_settings.cert_file,
                           cert_key_file=client_ssl_settings.cert_key_file)

        client = network.aio_party('SOME_PARTY')
        client.add_ledger_ready(lambda e: create('Main.PostmanRole', dict(party='SOME_PARTY')))
        client.add_ledger_created('Main.PostmanRole', lambda cid, cdata: messages_received.append(cid))
        network.run_until_complete()

        assert len(messages_received) == 1


def create_ssl_test_package(force=False) -> Tuple[SSLSettings, SSLSettings]:
    """
    Generate certs and scripts for running a Sandbox.

    The contents of the directory will be reused for no longer than 24 hours. If the test package is
    older than that or not present at all, it will be (re-)created.

    :return: A tuple of client/server SSL settings.
    """
    import time
    pkg_dir = Path(_DAZL_ROOT).resolve() / '.tmp' / 'ssl'
    pkg_dir.mkdir(parents=True, exist_ok=True)
    sandbox_script = pkg_dir / 'sandbox.sh'

    client_ssl_settings = SSLSettings(ca_file=str(pkg_dir / 'ca.crt'),
                                      cert_file=str(pkg_dir / 'server.crt'),
                                      cert_key_file=str(pkg_dir / 'server.key'))
    server_ssl_settings = SSLSettings(ca_file=str(pkg_dir / 'ca.crt'),
                                      cert_file=str(pkg_dir / 'server.crt'),
                                      cert_key_file=str(pkg_dir / 'server.pem'))
    if not force:
        if sandbox_script.exists():
            if (time.time() - sandbox_script.stat().st_mtime) < 86400:
                LOG.info('Skipping package creation because we already did it')
                return client_ssl_settings, server_ssl_settings

    # wipe out the package and start over
    for p in pkg_dir.glob('**'):
        if not p.is_dir():
            p.unlink()

    # create the certs
    run(args=[str(TLS_KEYGEN_SCRIPT), '--destination', str(pkg_dir), '--common-name', 'digitalasset.com.test'], check=True)
    return client_ssl_settings, server_ssl_settings
