# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Contains functions for working with "native" Python types as they correspond to types over the
Ledger API.
"""

from typing import Any, Dict, Mapping, Tuple

__all__ = ["to_record", "to_variant"]

VARIANT_KEYS = frozenset(["tag", "value"])


def to_record(obj: "Any") -> "Mapping[str, Any]":
    """
    "Unflattens" fields of a dict to support nested records.
    """
    from collections.abc import Mapping

    if not isinstance(obj, Mapping):
        raise ValueError("a mapping is required")

    # pull out any specialized dotted-field mappings
    reformatted = dict()  # type: Dict[str, Any]
    for key, value in obj.items():
        k1, d, k2 = key.partition(".")
        if d:
            v = reformatted.get(k1)
            if v is None:
                v = dict()
                reformatted[k1] = v
            v[k2] = value
        else:
            reformatted[key] = value

    return reformatted


def to_variant(obj: "Any") -> "Tuple[str, Any]":
    """
    Return the constructor and value that is represented by the given object.
    """
    from collections.abc import Mapping

    if not isinstance(obj, Mapping):
        raise ValueError(f"cannot coerce {obj!r} to a variant")

    if VARIANT_KEYS == obj.keys():
        return obj["tag"], obj["value"]
    if len(obj) != 1:
        raise ValueError(f"variants must be encoded as single-key dicts (got {obj!r} instead)")
    key = list(obj)[0]
    value = obj.get(key)
    return key, value
