# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Utilities for working with ledger offsets.

This API is _not_ public!
"""
from __future__ import annotations

from typing import Any, Optional, Union

__all__ = [
    "LedgerOffsetRange",
]


class End:
    """
    Marker object that denotes the current end of the ledger.
    """

    def __hash__(self):
        return 0

    def __repr__(self):
        return "END"


END = End()


class LedgerOffsetRange:
    """
    Denotes an offset range on a ledger. This API is _not_ considered public.

    The gRPC Ledger API and HTTP JSON API do not expose ledger offsets with the same semantics,
    so this class actually represents the commonality between these two interfaces.
    """

    def __init__(self, begin: Union[None, str], end: Union[None, END], /):
        """
        Initialize a :class:`LedgerOffsetRange`.

        :param begin:
            The start of the stream. If ``None``, then read from the beginning of the ledger.
            Otherwise, must be a legal ledger offset.
        :param end:
            The end of the stream. If ``None``, then keep reading from the stream forever; if
            ``END``, then terminate when reaching the _current_ end of stream. Note that offsets
            are *not* allowed here, as the HTTP JSON API does not provide a mechanism for reading
            *to* a specific transaction offset.
        """
        self.begin = begin
        self.end = end

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, LedgerOffsetRange)
            and self.begin == other.begin
            and self.end == other.end
        )

    def __hash__(self):
        return hash(self.begin) ^ hash(self.end)


UNTIL_END = LedgerOffsetRange(None, END)
FROM_BEGINNING_UNTIL_FOREVER = LedgerOffsetRange(None, None)


def from_offset_until_forever(offset: Optional[str]) -> LedgerOffsetRange:
    return LedgerOffsetRange(offset, None)