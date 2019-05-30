# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from typing import Optional, Sequence

from ..damlast.daml_lf_1 import Expr, FieldWithType
from .types import ModuleRef


class DamlDeclaration:
    """

    """
    module: ModuleRef
    name: Sequence[str]


class DamlDataType(DamlDeclaration):
    """

    """
    module: ModuleRef
    name: Sequence[str]
    fields: 'Sequence[FieldWithType]'
    eq_instance: 'Optional[Expr]'
    ord_instance: 'Optional[Expr]'
    show_instance: 'Optional[Expr]'


class DamlTemplate(DamlDataType):
    signatories: 'Expr'
    observers: 'Expr'
    agreement: 'Expr'
    precondition: 'Expr'
    choices: 'Sequence[DamlChoice]'


class DamlChoice:
    name: str
