# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any, NewType

from .basic import to_str

__all__ = ["Party", "to_party"]

Party = NewType("Party", str)


def to_party(o: "Any") -> "Party":
    return Party(to_str(o))
