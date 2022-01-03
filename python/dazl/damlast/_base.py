# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import TypeVar


class _Missing:
    """
    Sentinel object used to denote that a value was unspecified in a sum type in the AST.
    """

    __slots__ = ()

    def __repr__(self):
        return "MISSING"


MISSING = _Missing()
T = TypeVar("T")
