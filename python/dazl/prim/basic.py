# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import re
from typing import Any, Optional

__all__ = [
    "LEDGER_STRING_REGEX",
    "NAME_STRING_REGEX",
    "PACKAGE_ID_STRING_REGEX",
    "PARTY_ID_STRING_REGEX",
    "to_bool",
    "to_str",
]

# Standard string regexes as defined here:
# https://github.com/digital-asset/daml/blob/a6da995ecb71004c34c88a4f4211543868cfde15/ledger-api/grpc-definitions/com/daml/ledger/api/v1/value.proto#L18-L21
NAME_STRING_REGEX = re.compile(r"[A-Za-z$_][A-Za-z0-9$_]*")
PACKAGE_ID_STRING_REGEX = re.compile(r"[A-Za-z0-9\-_ ]+")
PARTY_ID_STRING_REGEX = re.compile(r"[A-Za-z0-9:\-_ ]")
LEDGER_STRING_REGEX = re.compile(r"[A-Za-z0-9#:\-_/ ]")


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
