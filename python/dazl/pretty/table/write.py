# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains utilities for deterministically outputting contract information.
"""

from typing import TYPE_CHECKING, Optional, TextIO

from .fmt_base import get_formatter
from .model import TableBuilder

if TYPE_CHECKING:
    from ...client import Network

__all__ = ["write_acs"]


def write_acs(
    buf: "TextIO", network: "Network", fmt: "Optional[str]" = None, include_archived: bool = False
) -> None:
    """
    Write all entries tabled by the plugin to the provided buffer.

    :param buf:
        The buffer to write to.
    :param network:
        The network to write data from.
    :param fmt:
        Format of the output; currently either ``"json"`` or ``"pretty"``.
    :param include_archived:
        ``True`` to include archived contracts in the output; otherwise, ``False``.
    """
    formatter = get_formatter(fmt)
    parties = set(network.parties())

    table = TableBuilder()
    for party in parties:
        client = network.aio_party(party)

        if include_archived:
            for cxdata in client.find_historical("*"):
                table.add(party, cxdata.cid, cxdata.cdata, cxdata.effective_at)
        else:
            for cid, cdata in client.find_active("*").items():
                table.add(party, cid, cdata, None)

    for line in formatter.render(network.lookup, parties, table):
        buf.write(line + "\n")
