# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains miscellaneous utility methods that don't really fit anywhere else.
"""

from __future__ import annotations

from typing import Generator, Iterable, TypeVar

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


__all__ = ["boundary_iter", "flatten"]


def boundary_iter(obj: Iterable[T], /) -> Generator[tuple[bool, T], None, None]:
    """
    Iterates over an iterable, returning a boolean and the underlying values indicating
    whether the iterator has reached its last item.

    >>> list(boundary_iter(range(0, 3)))
    [(False, 0), (False, 1), (True, 2)]

    >>> list(boundary_iter('A'))
    [(True, 'A')]

    # empty example
    >>> list(boundary_iter([]))
    []

    # iterating over an infinite iterable
    >>> import itertools
    >>> list(itertools.islice(boundary_iter(iter(lambda:0,1)), 4))
    [(False, 0), (False, 0), (False, 0), (False, 0)]
    """
    gen = iter(obj)
    prev_entry = None
    while True:
        try:
            entry = next(gen)
            if prev_entry is not None:
                yield False, prev_entry
            prev_entry = entry
        except StopIteration:
            if prev_entry is not None:
                yield True, prev_entry
            break


def flatten(obj: Iterable[Iterable[T]], /) -> list[T]:
    ret = list[T]()
    for sublist in obj:
        ret.extend(sublist)
    return ret
