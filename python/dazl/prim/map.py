# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, NoReturn

__all__ = ["FrozenDict", "to_hashable"]


class FrozenDict(dict):
    """
    A special subclass of `dict` that is immutable and hashable. Instances of this "dict" can be
    used as keys in a Python dictionary.
    """

    def __hash__(self) -> int:  # type: ignore
        return 0

    def __delitem__(self, *args, **kwargs) -> NoReturn:
        raise RuntimeError("frozendicts are immutable")

    def __setitem__(self, key, value) -> NoReturn:
        raise RuntimeError("frozendicts are immutable")

    def pop(self, *args, **kwargs) -> NoReturn:
        raise RuntimeError("frozendicts are immutable")

    def popitem(self, *args, **kwargs) -> NoReturn:
        raise RuntimeError("frozendicts are immutable")

    def setdefault(self, *args, **kwargs) -> NoReturn:
        raise RuntimeError("frozendicts are immutable")

    def update(self, *args, **kwargs) -> NoReturn:
        raise RuntimeError("frozendicts are immutable")

    def clear(self, *args, **kwargs) -> NoReturn:
        raise RuntimeError("frozendicts are immutable")


def to_hashable(obj: Any) -> Any:
    from collections.abc import Collection, Mapping

    if isinstance(obj, Mapping):
        return FrozenDict(obj)
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, Collection):
        return tuple(obj)
    else:
        return obj
