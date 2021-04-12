# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Optional

__all__ = ["to_bool", "to_str"]


def to_bool(obj: "Optional[Any]") -> "Optional[bool]":
    """
    Convert any of the common wire representations of a ``bool`` to a ``bool``.
    """
    if obj is None:
        # noinspection PyTypeChecker
        return None

    if isinstance(obj, bool):
        return obj
    elif isinstance(obj, str):
        lobj = obj.lower().strip()
        if lobj == "true":
            return True
        elif lobj == "false":
            return False
        else:
            raise ValueError(f"Could not parse a string as a boolean: {obj!r}")
    raise ValueError(f"Could not parse as a boolean: {obj!r}")


def to_str(obj: "Any") -> str:
    """
    Convert any object to a string. This simply calls ``str`` on the object to produce a string
    representation.
    """
    return obj if isinstance(obj, str) else str(obj)
