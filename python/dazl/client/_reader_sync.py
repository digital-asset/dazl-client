# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Functions for ensuring that readers across different parties remain as close in sync to each other
as practical.
"""

from asyncio import Future, ensure_future, gather, sleep
from typing import TYPE_CHECKING, Collection, List, Optional, Tuple

from .. import LOG
from ..util.asyncio_util import completed, named_gather

if TYPE_CHECKING:
    from ._party_client_impl import _PartyClientImpl


async def run_iteration(
    party_impls: "Collection[_PartyClientImpl]",
) -> "Tuple[Optional[str], Collection[Future]]":
    """
    Read the next set of transactions for the set of parties. This coroutine ends when all
    parties are caught up to the same offset.

    :param party_impls:
        A collection of :class:`_PartyClientImpl` will have scheduled invocations.
    :return:
        A tuple of the current ending offset and Futures that represent completions for commands
        that were submitted as a direct result of these events.
    """
    read_coroutines = []  # type: List[Future]

    # have every client read as far ahead as they can
    offsets, event_fut = await read_transactions(party_impls, None, True)
    if not event_fut.done():
        read_coroutines.append(event_fut)

    final_offset = max_offset(offsets)
    if len(offsets) > 1:
        # now have every client catch up to the agreed-upon HEAD
        _, event_fut = await read_transactions(party_impls, final_offset, True)
        if not event_fut.done():
            read_coroutines.append(event_fut)

    await sleep(0)

    return final_offset, [fut for fut in read_coroutines if not fut.done()]


async def read_initial_acs(party_impls: "Collection[_PartyClientImpl]") -> "Optional[str]":
    """
    Perform the initial synchronization of the Active Contract Set with the server, using the
    Active Contract Set service.

    :param party_impls:
        A collection of _PartyClientImpl's whose offset and ACS state need to be updated.
    :return:
        The ending offset that all parties have reached, or ``None`` if no calls were actually
        made.
    """
    LOG.info("Reading current ledger state...")

    # Fetch the ACS as every single client.
    if not party_impls:
        return None

    offset = max_offset(
        [
            offset
            for offset, _ in await gather(
                *[party_impl.read_acs(None, False) for party_impl in party_impls]
            )
        ]
    )

    # Find the most recent offset among all of those clients, and use the transaction stream
    # to catch up all clients to the same point.
    LOG.info("Catching up...")
    await gather(*[party_impl.read_transactions(offset, False) for party_impl in party_impls])
    LOG.info("Finished catching up.")

    LOG.info("Finished reading current ledger state.")
    return offset


async def read_transaction_event_stream(
    party_impls: "Collection[_PartyClientImpl]",
) -> "Optional[str]":
    LOG.info("Reading current ledger state...")
    if not party_impls:
        return None

    party_impl = next(iter(party_impls))
    offset = await party_impl.read_end()

    await gather(*[party_impl.read_transactions(offset, False) for party_impl in party_impls])
    return offset


async def read_transactions(
    party_impls: "Collection[_PartyClientImpl]", until_offset: "Optional[str]", raise_events: bool
) -> "Tuple[Collection[str], Future]":
    """
    Read transactions from a collection of PartyImpls.

    :param party_impls:
    :param until_offset:
    :param raise_events:
    :return:
        A tuple containing:
         * a set of the offsets returned from all readers, and
         * a Future that is resolved when all events across all readers have resolved either
           successfully or unsuccessfully.
    """
    tuples = await gather(*(pi.read_transactions(until_offset, raise_events) for pi in party_impls))
    offsets = sorted({t[0] for t in tuples})
    futures = [ensure_future(t[1]) for t in tuples]
    futures = [fut for fut in futures if not fut.done()]
    if not futures:
        return offsets, completed(None)
    elif len(futures):
        return offsets, futures[0]
    else:
        return offsets, named_gather(repr(futures), *futures, return_exceptions=True)


def max_offset(offsets: "Collection[Optional[str]]") -> "Optional[str]":
    """
    Return the most "recent" offset from a collection of offsets.

    :param offsets: A collection of offsets to examine.
    :return: The largest offset, or ``None`` if unknown.
    """
    non_none_offsets = [offset for offset in offsets if offset is not None]
    return max(non_none_offsets) if non_none_offsets else None
