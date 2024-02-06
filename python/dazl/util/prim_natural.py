# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

__all__ = ["n_things"]


def n_things(count: int, plural_noun: str, singular_noun: Optional[str] = None) -> str:
    if count == 1:
        if singular_noun is None:
            return f"1 {plural_noun[0:-1]}"
        else:
            return f"1 {singular_noun}"
    else:
        return f"{count} {plural_noun}"
