# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, Collection, NewType, Sequence, Union, overload

from .basic import to_str

__all__ = ["Party", "to_party", "to_parties"]

Party = NewType("Party", str)


def to_party(o: Any, /) -> Party:
    return Party(to_str(o))


@overload
def to_parties(o: None, /) -> None:
    ...


@overload
def to_parties(o: Union[str, Party, Collection[str], Collection[Party]], /) -> Sequence[Party]:
    ...


def to_parties(
    o: Union[None, str, Party, Collection[str], Collection[Party]], /
) -> Union[None, Sequence[Party]]:
    """
    Return the specified object as a collection of parties.

    :param o:
        The object to convert to a set of parties.
    """
    if o is None:
        return None
    elif isinstance(o, str):
        return (Party(o),)
    else:
        return tuple(Party(p) for p in o)
