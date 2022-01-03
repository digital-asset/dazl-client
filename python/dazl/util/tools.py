# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains miscellaneous utility methods that don't really fit anywhere else.
"""

from typing import (
    Callable,
    Collection,
    Generator,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
)
import warnings

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


__all__ = ["boundary_iter", "flatten", "as_list", "get_matches"]


def boundary_iter(obj: Iterable[T]) -> Generator[Tuple[bool, T], None, None]:
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


def flatten(obj):
    ret = []
    for sublist in obj:
        ret.extend(sublist)
    return ret


def as_list(obj: "Union[None, T, Collection[Union[None, T]]]") -> "List[T]":
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


def __key_error(key: str) -> Exception:
    return KeyError(key)


def get_matches(
    mapping: "Mapping[str, V]",
    key: "str",
    exc_class: "Optional[Callable[[str], Exception]]" = __key_error,
) -> "Collection[V]":
    """
    Return the value (as a singleton collection) associated with a key. If the key is equal to the
    special value ``"*"``, then all values are returned. If there is no mapping for the specified
    key and an exception class is provided, an exception is raised. Otherwise, an empty collection
    is returned.

    This function should NOT be used if ``"*"`` _can_ be a valid key; the behavior in this case is
    still to return all values, which could be confusing.

    :param mapping:
        A mapping to use to perform lookups.
    :param key:
        The key to lookup a value for, or the special value '*' to retrieve all values.
    :param exc_class:
        The exception to raise if this function would have returned an empty collection, or
        ``None`` to allow empty collections to be returned.
    :return:
        * An empty collection if the supplied key does not have a mapping _and_ ``exc_class is not None``;
        * A collection of one if a match is found for the supplied key;
        * All values of the mapping if the key is `""*""`.
    """
    warnings.warn("get_matches is deprecated; there is no replacement.", DeprecationWarning)
    if key == "*":
        return tuple(mapping.values())

    value = mapping.get(key)
    if value is None:
        if exc_class is not None:
            raise exc_class(key)
        else:
            return ()

    return (value,)
