# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import keyword
import re
from typing import Collection, List, Optional, Tuple

__all__ = ["as_interned_field", "strip_interning"]


SNAKE_CASE_RE = re.compile(r"(?<!^)(?=[A-Z])")


def as_interned_field(field_names: "Collection[str]") -> "Tuple[Optional[str], Optional[str]]":
    """
    Determine if the specified field names belong to a oneof that exists exclusively to support
    interning. If the oneof group exists only for interning, return the simple name of the field
    and its desired type; otherwise return ``(None, None)``.

    :param field_names:
        The names of fields in the oneof group.

    >>> as_interned_field(['var_interned_str', 'var_str'])
    ('var', 'str')
    >>> as_interned_field(['something', 'else'])
    (None, None)
    """
    # interned fields only come in pairs
    if len(field_names) != 2:
        return None, None

    # we don't particularly care what order the field names come in
    names = sorted(field_names)  # type: List[str]
    if names[0].endswith("_interned_str") and names[1].endswith("_str"):
        return names[1][:-4], "str"

    if names[0].endswith("_dname") and names[1].endswith("_interned_dname"):
        return names[0][:-6], "DottedName"

    return None, None


def strip_interning(field_name: str, field_type: str) -> "Tuple[str, str]":
    fld_name = without_suffix(field_name, "_interned_str")
    if fld_name is not None:
        return fld_name, "str"

    fld_name = without_suffix(field_name, "_interned")
    if fld_name is not None:
        return fld_name, "str"

    fld_name = without_suffix(field_name, "_str")
    if fld_name is not None:
        return fld_name, "str"

    fld_name = without_suffix(field_name, "_interned_dname")
    if fld_name is not None:
        return fld_name, "DottedName"

    fld_name = without_suffix(field_name, "_dname")
    if fld_name is not None:
        return fld_name, "DottedName"

    return field_name, field_type


def pyize_name(name: str) -> str:
    """
    Convert a name to one that is more Pythonic.
    """
    # for historical reasons, leave "Sum" upper-cased
    if name == "Sum":
        return "Sum"

    if keyword.iskeyword(name):
        return name + "_"

    return SNAKE_CASE_RE.sub("_", name).lower().replace("_non_consuming_", "_nonconsuming_")


def without_prefix(value: str, prefix: str) -> "Optional[str]":
    return value[len(prefix) :] if value.startswith(prefix) else None


def without_suffix(value: str, suffix: str) -> "Optional[str]":
    return value[: -len(suffix)] if value.endswith(suffix) else None
