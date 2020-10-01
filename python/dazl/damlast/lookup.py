# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
DAML-LF fast lookups
--------------------
"""

from .daml_lf_1 import TypeConName, ModuleRef, DottedName


__all__ = ['parse_type_con_name']


def parse_type_con_name(val: str) -> 'TypeConName':
    """
    Parse the given string as a type constructor.
    """
    # TODO: validate_template should be deprecated and some of its remaining bits be moved in-line
    #  but it's used too heavily in its current form at the moment. This is a local import to avoid
    #  import cycles between dazl.damlast and dazl.model.
    from ..model.lookup import validate_template

    pkg, name = validate_template(val)
    module_name, _, entity_name = name.rpartition(':')
    module_ref = ModuleRef(pkg, DottedName(module_name.split('.')))
    return TypeConName(module_ref, entity_name.split('.'))
