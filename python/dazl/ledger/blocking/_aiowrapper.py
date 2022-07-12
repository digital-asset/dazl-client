# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from asyncio import new_event_loop, run_coroutine_threadsafe, set_event_loop, sleep
from queue import Queue
from threading import Thread
from typing import Callable, Optional

from ..aio import Connection, QueryStream

__all__ = ["ConnectionThunk", "QueryStreamThunk"]


class ConnectionThunk:
    """
    A blocking Connection wrapper around an asynchronous connection.
    """

    def __init__(self, conn_fn: "Callable[[], Connection]", *, name: "Optional[str]" = None):
        self._conn_fn = conn_fn
        self._conn = None
        self._thread = Thread(target=self._main, name=name, daemon=True)
        self._loop = new_event_loop()
        self._fut = self._loop.create_future()

    def _main(self) -> None:
        """
        The "main" thread that runs the event loop where operations for this connection are scheduled.
        """
        set_event_loop(self._loop)
        self._loop.run_until_complete(self._fut)

    def open(self):
        # start the main thread
        self._thread.start()

        fut = run_coroutine_threadsafe(self._create_conn(), self._loop)
        fut.result()

    async def _create_conn(self):
        await sleep(0)
        self._conn = self._conn_fn()
        await self._conn.open()

    def close(self):
        run_coroutine_threadsafe(self._conn.close(), self._loop).result()
        self._loop.call_soon_threadsafe(self._fut.set_result, None)
        self._thread.join()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def create(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.create(*args, **kwargs), self._loop)
        return fut.result()

    def create_and_exercise(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.create_and_exercise(*args, **kwargs), self._loop)
        return fut.result()

    def exercise(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.exercise(*args, **kwargs), self._loop)
        return fut.result()

    def exercise_by_key(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.exercise_by_key(*args, **kwargs), self._loop)
        return fut.result()

    def submit(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.submit(*args, **kwargs), self._loop)
        return fut.result()

    def archive(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.archive(*args, **kwargs), self._loop)
        return fut.result()

    def archive_by_key(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.archive_by_key(*args, **kwargs), self._loop)
        return fut.result()

    def get_ledger_end(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.get_ledger_end(*args, **kwargs), self._loop)
        return fut.result()

    def query(self, *args, **kwargs):
        return QueryStreamThunk(self._conn.query(*args, **kwargs), self._loop)

    def query_many(self, *args, **kwargs):
        return QueryStreamThunk(self._conn.query_many(*args, **kwargs), self._loop)

    def stream(self, *args, **kwargs):
        return QueryStreamThunk(self._conn.stream(*args, **kwargs), self._loop)

    def stream_many(self, *args, **kwargs):
        return QueryStreamThunk(self._conn.stream_many(*args, **kwargs), self._loop)

    def get_user(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.get_user(*args, **kwargs), self._loop)
        return fut.result()

    def list_users(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.list_users(*args, **kwargs), self._loop)
        return fut.result()

    def allocate_party(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.allocate_party(*args, **kwargs), self._loop)
        return fut.result()

    def list_known_parties(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.list_known_parties(*args, **kwargs), self._loop)
        return fut.result()

    def upload_package(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.upload_package(*args, **kwargs), self._loop)
        return fut.result()

    def get_package(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.get_package(*args, **kwargs), self._loop)
        return fut.result()

    def list_package_ids(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.list_package_ids(*args, **kwargs), self._loop)
        return fut.result()

    def get_metering_report(self, *args, **kwargs):
        fut = run_coroutine_threadsafe(self._conn.get_metering_report(*args, **kwargs), self._loop)
        return fut.result()


class QueryStreamThunk:
    """
    A blocking QueryStream wrapper around an asynchronous query stream.
    """

    def __init__(self, stream: "QueryStream", loop):
        self._loop = loop
        self._stream = stream
        self._q = Queue()  # type: ignore
        self._fut = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # try to abort an existing iteration if one is running
        if self._fut is not None:
            try:
                self._fut.cancel()
            except Exception:  # noqa
                pass
        self.close()

    def on_create(self, *args):
        return self._stream.on_create(*args)

    def on_archive(self, *args):
        return self._stream.on_archive(*args)

    def on_boundary(self, *args):
        return self._stream.on_boundary(*args)

    def close(self):
        self._q.put_nowait(None)

    def run(self):
        self._fut = run_coroutine_threadsafe(self._stream.run(), self._loop)
        self._fut.result()

    def creates(self):
        self._fut = run_coroutine_threadsafe(self._producer(self._stream.creates), self._loop)
        return self._consume_queue()

    def events(self):
        self._fut = run_coroutine_threadsafe(self._producer(self._stream.events), self._loop)
        return self._consume_queue()

    def items(self):
        self._fut = run_coroutine_threadsafe(self._producer(self._stream.items), self._loop)
        return self._consume_queue()

    def __iter__(self):
        return self.items()

    async def _producer(self, source):
        async with self._stream:
            async for item in source():
                self._q.put_nowait(item)
            self._q.put_nowait(None)

    def _consume_queue(self):
        while True:
            item = self._q.get()
            if item is not None:
                yield item
            else:
                break
