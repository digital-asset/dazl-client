# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import defaultdict
import sys
from types import MappingProxyType
from typing import Any, Collection, DefaultDict, Mapping, Optional, Set, TypeVar

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

__all__ = ["merge"]


class SupportsLessThan(Protocol):
    def __lt__(self, __other: Any) -> bool:
        ...


K = TypeVar("K")
V = TypeVar("V", bound=SupportsLessThan)  # noqa: Y001


def merge(*m: "Optional[Mapping[K, Collection[V]]]") -> "Mapping[K, Collection[V]]":
    """
    Combine multiple key-values mappings into a single key-values mapping.
    """
    ret = defaultdict(set)  # type: DefaultDict[K, Set[V]]
    for mapping in m:
        if mapping:
            for k, v in mapping.items():
                ret[k].update(v)
    return MappingProxyType({k: tuple(sorted(v)) for k, v in ret.items()})
