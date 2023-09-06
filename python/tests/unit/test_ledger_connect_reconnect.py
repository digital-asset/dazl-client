# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from asyncio import create_task, sleep
from datetime import timedelta
import logging

from dazl import connect
from dazl.testing import SandboxLauncher
from grpc import RpcError, StatusCode
import pytest

ONE_MINUTE = timedelta(minutes=1)


@pytest.mark.asyncio
async def test_deadline_does_not_abort_query_stream(sandbox: SandboxLauncher) -> None:
    async with connect(url=sandbox.url, admin=True) as conn:
        party_info = await conn.allocate_party()

        async with conn.stream_many(read_as=party_info.party, timeout=0.1) as stream:
            task = create_task(stream.run())
        await sleep(1.0)

        # a query stream should NOT abort naturally on its own; if it did, that means we failed somehow
        if task.done():
            await task
            raise AssertionError("did not expect the query stream to terminate naturally")
        else:
            # clean up after the task to avoid leaking coroutines
            try:
                task.cancel()
            except Exception:  # noqa
                pass


@pytest.mark.asyncio
async def test_reconnect_party_allocation() -> None:
    sandbox = SandboxLauncher()
    try:
        sandbox.start()
        async with connect(url=sandbox.url, admin=True) as conn:
            await conn.allocate_party()

            logging.info("Stopping our sandbox...")
            sandbox.stop()

            logging.info("Waiting a bit for things to really be gone.")
            await sleep(5)

            # this is expected to fail, since our ledger is now down
            try:
                logging.info("Trying to intentionally fail to allocate a party...")
                await conn.allocate_party(timeout=ONE_MINUTE)
            except RpcError as ex:
                assert ex.code() == StatusCode.UNAVAILABLE
                logging.info("Got the expected error.")

            logging.info("Starting the sandbox up again...")
            sandbox.start()

            # # a call using a brand new connection will definitely work...
            # async with connect(url=sandbox.url, admin=True) as conn2:
            #     party_info = await conn2.allocate_party()

            retry_count = 0
            while retry_count < 10:
                try:
                    # ...but a call using the old connection should still work too
                    logging.info("Allocating another party...")
                    await conn.allocate_party()
                    break
                except RpcError as ex:
                    if ex.code() in (StatusCode.DEADLINE_EXCEEDED, StatusCode.UNAVAILABLE):
                        # this is retryable
                        await sleep(1)
                    else:
                        raise

            assert retry_count < 10

    finally:
        sandbox.stop()


@pytest.mark.asyncio
async def test_reconnect_query_stream() -> None:
    sandbox = SandboxLauncher()
    try:
        sandbox.start()
        async with connect(url=sandbox.url, admin=True) as conn:
            party_info = await conn.allocate_party()

            async with conn.stream_many(read_as=party_info.party, timeout=ONE_MINUTE) as stream:
                task = create_task(stream.run())

            logging.info("Stopping our sandbox...")
            sandbox.stop()

            logging.info("Waiting a bit for things to really be gone.")
            await sleep(5)

            did_die = False
            try:
                await task
            except RpcError as ex:
                assert ex.code() == StatusCode.UNAVAILABLE
                logging.info(
                    "Got the expected error--the query stream died like it was supposed to."
                )
                did_die = True
            assert did_die

            # this is expected to fail, since our ledger is now down
            did_die = False
            try:
                logging.info("Trying to intentionally fail to query contracts...")
                async with conn.stream_many(read_as=party_info.party, timeout=ONE_MINUTE) as stream:
                    await stream.run()

            except RpcError as ex:
                assert ex.code() == StatusCode.UNAVAILABLE
                logging.info("Got the expected error.")
                did_die = True
            assert did_die

            sandbox.start()

            # note that because the sandbox does not preserve state, when we "restart" the sandbox,
            # we need to reallocate parties and open a query stream over a new party
            party_info = await conn.allocate_party()

            async with conn.stream_many(read_as=party_info.party, timeout=ONE_MINUTE) as stream:
                task = create_task(stream.run())

            logging.info("Giving the query stream a chance to terminate improperly")
            await sleep(2)

            # query streams never terminate naturally; we should still be running
            assert not task.done()

            try:
                task.cancel()
            except Exception:  # noqa
                pass

    finally:
        sandbox.stop()
