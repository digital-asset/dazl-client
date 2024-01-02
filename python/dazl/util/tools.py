# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains miscellaneous utility methods that don't really fit anywhere else.
"""

from __future__ import annotations

from typing import Collection, Generator, Iterable, List, Tuple, TypeVar, Union

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


__all__ = ["boundary_iter", "flatten", "as_list"]


def boundary_iter(obj: Iterable[T], /) -> Generator[Tuple[bool, T], None, None]:
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


def flatten(obj, /):
    ret = []
    for sublist in obj:
        ret.extend(sublist)
    return ret


def as_list(obj: Union[None, T, Collection[Union[None, T]]], /) -> List[T]:
    """
    Convert an object that is either nothing, a single object, or a collection, to a list of type
    of that object.
    """
    from collections.abc import Iterable

    if obj is None:
        return []
    elif isinstance(obj, str):
        # strings are iterable, but it's almost never intended to be used in place of a list; if
        # we're given a string, then assume what is wanted is a single list containing the full
        # string instead of a list containing every character as an individual item
        return [obj]  # type: ignore
    elif isinstance(obj, Iterable):
        return [o for o in obj if o is not None]
    else:
        # assume we're dealing with a single object of the requested type
        return [obj]
