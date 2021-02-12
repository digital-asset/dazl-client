# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import sleep

import pytest

from dazl import Network

from .dars import UploadTest


@pytest.mark.asyncio
async def test_dar_uploads_near_startup(sandbox):
    package_ids = []

    network = Network()
    network.set_config(url=sandbox)

    async def upload_dars_and_verify():
        await upload_test_dars(network)
        metadata = await network.aio_global().metadata()
        package_ids.extend(network.lookup.package_ids())

    await network.aio_run(upload_dars_and_verify(), keep_open=False)

    # Because we use a single sandbox process, it's somewhat difficult to assert that the specific
    # DAR we are attempting to upload has indeed been uploaded, because packages are global and
    # other tests will upload packages as well. However, we know that we HAVE indeed uploaded
    # SOMETHING, and the Sandbox tests are started without any packages at all. So assume that a
    # non-zero package ID list means that DAR uploading works.
    assert len(package_ids) > 0


@pytest.mark.asyncio
@pytest.mark.skip(
    "Background package polling will soon be disabled, and packages will be loaded on an as-needed "
    "basis. When this happens, PackagesAddedEvent will be dropped. If this is still a use-case you "
    "need, please write your own poller around lookup.package_ids."
)
async def test_package_events(sandbox):
    initial_events = []
    follow_up_events = []

    network = Network()
    network.set_config(url=sandbox)
    client = network.aio_new_party()

    async def upload_dars_and_verify():
        # make sure the client is "ready" before uploading DARs, because we are explicitly
        # checking to make sure proper reporting of packages that are uploaded after a
        # client is running and # operational
        await client.ready()
        await upload_test_dars(network)
        await (await network.aio_global().metadata()).package_loader.load_all()

        # give the client some time to pick up the new packages; unfortunately there isn't
        # much more to do here except wait
        await sleep(10)

    client.add_ledger_packages_added(lambda _: initial_events.append(_), initial=True)
    client.add_ledger_packages_added(lambda _: follow_up_events.append(_))

    await network.aio_run(upload_dars_and_verify(), keep_open=False)

    assert len(initial_events) == 2
    assert len(follow_up_events) == 1


async def upload_test_dars(network: "Network"):
    g = network.aio_global()
    await g.ensure_dar(UploadTest)
