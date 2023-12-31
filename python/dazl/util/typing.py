# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains helper utilities for working within the constraints of Python's type system.
"""

from __future__ import annotations

from typing import Any, Type, TypeVar

__all__ = ["safe_cast"]

K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")


def safe_cast(typ: Type[T], val: Any) -> T:
    """
    Safely casts an item to the specified type. Unlike ``typing.cast``, this method will actually
    throw an exception if types do not match.
    """
    if isinstance(typ, type):
        if isinstance(val, typ):
            return val
        else:
            raise ValueError(f"expected a value of type {typ} here (got {val} instead)")
    else:
        raise Exception(f"safe_cast can only be used with actual types (got {typ})")
