# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections import defaultdict
from types import MappingProxyType
from typing import Any, Collection, DefaultDict, Mapping, Optional, Protocol, Set, TypeVar

__all__ = ["merge"]


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


K = TypeVar("K")
V = TypeVar("V", bound=SupportsLessThan)  # noqa: Y001


def merge(*m: Optional[Mapping[K, Collection[V]]]) -> Mapping[K, Collection[V]]:
    """
    Combine multiple key-values mappings into a single key-values mapping.
    """
    ret = defaultdict(set)  # type: DefaultDict[K, Set[V]]
    for mapping in m:
        if mapping:
            for k, v in mapping.items():
                ret[k].update(v)
    return MappingProxyType({k: tuple(sorted(v)) for k, v in ret.items()})
