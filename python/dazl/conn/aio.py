from asyncio import Queue, get_event_loop
from threading import Thread

from .. import LOG
from .interfaces import AsyncIOLedgerConnection, BlockingLedgerConnection


class AsyncIOLedgerConnectionWrapper(AsyncIOLedgerConnection):

    def __init__(self, conn: 'BlockingLedgerConnection', executor: 'Executor'):
        self.conn = conn
        self.executor = executor

    def query(self, q: 'QueryRequest') -> 'AsyncGenerator[Trnsaction, None, None]':
        """
        Wrap a blocking :class:`Transaction` generator with an asynchronous generator.

        Note this implementation differs from the other wrapping functions because query generators
        are long-lived, and using the threads on our executor will quickly lead to thread
        starvation.

        :param q: The :class:`QueryRequest` to search on.
        :return: An asynchronous generator that returns :class:`Transaction`s as they come.
        """
        return _AsyncQueryResponseWrapper(self.conn, q)


class _AsyncQueryResponseWrapper:
    """
    Specialized wrapper over the transaction stream ``Query()`` method.

    This async wrapper is implemented with its own wrapper thread to avoid starvation of the main
    thread pool responsible for servicing shorter-lived requests.

    Instances of this class MUST be constructed on the loop for which they are intended to serve.
    """
    def __init__(self, conn, request):
        self._conn = conn  # type: BlockingLedgerConnection
        self._request = request

        self._queue = Queue()
        self._loop = get_event_loop()
        self._worker = Thread(target=self._main)

    def _main(self):
        """
        Main thread responsible for servicing this query stream request.
        """
        self._stream = self._conn.query(self._request)
        try:
            for tx in self._stream:
                self._loop.call_soon_threadsafe(self._queue.put_nowait, tx)
        finally:
            self._stream.close()

    def __aiter__(self):
        return self

    async def __anext__(self):
        tx = await self._queue.get()
        if tx is not None:
            return tx
        else:
            raise StopAsyncIteration

    async def aclose(self):
        stream = self._stream
        if stream is not None:
            try:
                stream.close()
            except Exception:  # noqa
                LOG.error("Unexpected error when trying to close the underlying stream")
