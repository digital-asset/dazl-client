# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains functions for testing contract data against a match object.
"""

from ..model.core import ContractData, ContractMatch


def is_match(predicate: ContractMatch, cdata: ContractData) -> bool:
    """
    Determine whether a contract matches a predicate expression.
    """
    if predicate is None:
        return True

    if callable(predicate):
        return predicate(cdata)

    for key, predicate_value in predicate.items():
        cdata_value = cdata.get(key)
        if cdata_value is None:
            # None only matches with None
            if predicate_value is not None:
                return False

        elif callable(predicate_value):
            # support lambdas as predicate values
            if not predicate_value(cdata_value):
                return False

        elif isinstance(predicate_value, dict):
            # deep dictionaries are for variants or records
            return is_match(predicate_value, cdata_value)

        elif predicate_value != cdata_value:
            # exact matches are, of course, supported
            return False

        else:
            # TODO: think of convenient ways to deal with lists
            pass

    return True
