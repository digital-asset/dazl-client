# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Optional, Union

from ..damlast import TypeConName
from ..ledger import CreateEvent
from ..ledger.aio import Connection
from ..query import Query


async def fetch_first(
    __conn: Connection, __template_id: Union[str, TypeConName], __query: Query = None
) -> Optional[CreateEvent]:
    """
    Return the first (earliest) :class:`CreateEvent` from the Active Contract Set (ACS), or ``None``
    if no contract is currently a part of the ACS.

    :param __conn: The connection to use to fetch results.
    :param __template_id: The ID of the template to fetch.
    :param __query: An optional query to further filter results.
    :return:
        The first :class:`CreateEvent`, or ``None`` if no matching :class:`CreateEvent` currently
        exists.
    """
    async with __conn.query(__template_id, __query) as stream:
        async for event in stream.creates():
            return event

    return None


async def fetch_last(
    __conn: Connection, __template_id: Union[str, TypeConName], __query: Query = None
) -> Optional[CreateEvent]:
    """
    Return the last (most recent) :class:`CreateEvent` from the Active Contract Set (ACS), or
    ``None`` if no contract is currently a part of the ACS.

    :param __conn: The connection to use to fetch results.
    :param __template_id: The ID of the template to fetch.
    :param __query: An optional query to further filter results.
    :return:
        The last :class:`CreateEvent`, or ``None`` if no matching :class:`CreateEvent` currently
        exists.
    """
    last_event = None
    async with __conn.query(__template_id, __query) as stream:
        async for event in stream.creates():
            last_event = event

    return last_event
