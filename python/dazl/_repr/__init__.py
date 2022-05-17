# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Default ``repr`` rules for dazl.

THIS IS NOT A PUBLIC API, AND ITS CONTENTS ARE SUBJECT TO CHANGE AT ANY TIME!
"""

import builtins
from reprlib import Repr
from typing import Collection

REPR = Repr()

# Python's default max string length is a little too short to nicely display some common
# Ledger API constructs such as template IDs and party literals, so bump it up higher
REPR.maxstring = 255


__all__ = ["list", "str", "REPR"]


# noinspection PyShadowingBuiltins
def list(__obj: Collection) -> builtins.str:
    # the typing rules for reprlib are too strict; in reality `repr_list` takes any
    # iterable
    return REPR.repr_list(__obj, REPR.maxlevel)  # type: ignore


# noinspection PyShadowingBuiltins
def str(__obj: builtins.str) -> builtins.str:
    return REPR.repr_str(__obj, REPR.maxlevel)
