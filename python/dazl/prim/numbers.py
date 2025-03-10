# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from decimal import Decimal
from typing import Any, Optional

__all__ = ["to_int", "to_decimal", "decimal_to_str"]


def to_int(obj: Any) -> int:
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return int(obj)
    elif isinstance(obj, Decimal):
        return int(obj)
    raise ValueError(f"Could not parse as an int: {obj!r}")


def to_decimal(obj: Optional[Any]) -> Optional[Decimal]:
    """
    Convert any of the common wire representations of a ``Decimal`` to a ``Decimal``.
    """
    if obj is None:
        # noinspection PyTypeChecker
        return None

    if isinstance(obj, Decimal):
        return obj
    elif isinstance(obj, (int, float)):
        return Decimal(str(obj))
    elif isinstance(obj, str):
        return Decimal(obj)
    raise ValueError(f"Could not parse as a Decimal: {obj!r}")


def decimal_to_str(d: Decimal) -> str:
    """
    Return a string representation of a :class:`Decimal` that is safe to be used over the
    Ledger API. Concretely, this means staying away from scientific notation.
    """
    exponent = d.as_tuple().exponent
    if isinstance(exponent, int):
        precision = max(0, -exponent)
        return format(d, f".{precision}f")
    else:
        raise ValueError(f"Not a legal Decimal: {d!r})")
