# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from datetime import datetime
from typing import Iterator, Optional

# noinspection PyPackageRequirements
from grpc import RpcError, StatusCode

from ... import LOG
from .pb_parse_event import to_datetime


def maybe_grpc_time_stream(time_service: 'G.TimeServiceStub', ledger_id: str) \
        -> Optional[Iterator[datetime]]:
    """
    Return an iterator over times that monotonically increases, or ``None`` if the TimeService is
    not implemented by the remote server.

    :param time_service:
    :param ledger_id:
    :return:
    """
    from . import model as G
    request = G.GetTimeRequest(ledger_id=ledger_id)

    time_stream = time_service.GetTime(request)
    try:
        return _TimeStream(time_stream)
    except StaticTimeUnsupportedError:
        LOG.debug('Operating in real-time mode.')
        return None


class _TimeStream(Iterator[datetime]):

    def __init__(self, time_stream):
        try:
            self.time_stream_iter = iter(time_stream)
            self.time_queue = [to_datetime(next(self.time_stream_iter).current_time)]
        except RpcError as ex:
            status_code = ex.code()
            if status_code == StatusCode.UNIMPLEMENTED:
                raise StaticTimeUnsupportedError()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.time_queue.pop()
        except IndexError:
            pass

        try:
            dt = to_datetime(next(self.time_stream_iter).current_time)
            LOG.debug('Got a new time: %s', dt)
            return dt
        except RpcError as ex:
            status_code = ex.code()
            if status_code == StatusCode.CANCELLED:
                # a cancelled code is fine; that just means the underlying time stream connection is
                # closed (which also means this function is done with its work)
                raise StopIteration
            else:
                raise


class StaticTimeUnsupportedError(Exception):
    pass
