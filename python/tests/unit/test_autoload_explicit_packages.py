# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from asyncio import ensure_future
import logging

from dazl import Network, connect
from dazl.damlast.errors import PackageNotFoundError
from dazl.damlast.lookup import MultiPackageLookup
from dazl.damlast.pkgfile import DarFile
from dazl.testing import SandboxLauncher
import pytest

from .dars import Simple


@pytest.mark.asyncio
async def test_autoload_explicit_packages(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        party_info = await conn.allocate_party()

    with DarFile(Simple) as dar_file:
        lookup = MultiPackageLookup()
        lookup.add_archive(*dar_file.archives())
        fqtn = lookup.template_name("Simple:OperatorRole")

    # Start the sandbox and make sure our package is loaded.
    logging.info("Preloading the DAR...")
    network = Network()
    network.set_config(url=sandbox.url)
    await network.aio_global().ensure_dar(Simple)

    # Now start the sandbox again, but without any preloading.
    logging.info("Now running the real test...")
    network = Network()
    network.set_config(url=sandbox.url, eager_package_fetch=False)
    client = network.aio_party(party_info.party)
    fut = ensure_future(network.aio_run())
    await client.ready()

    with pytest.raises(PackageNotFoundError):
        # this call SHOULD fail because the package has not yet locally been loaded
        _ = network.lookup.template(fqtn)

    # this call should NOT fail because we tolerate searches on templates when
    # fully specified but the package has not yet been fetched
    contracts = client.find_active(fqtn)
    assert len(contracts) == 0

    # this call should nonetheless succeed because dazl fetches packages that it sees
    # it's missed
    logging.info("Submitting the create...")
    await client.create(fqtn, {"operator": client.party})

    network.shutdown()
    await fut
