# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime

from dazl.damlast.daml_lf_1 import TypeConName, ModuleRef, PackageRef, DottedName
from dazl.model.types import dotted_name
from dazl.model.types_store import PackageStore
from dazl.pretty.table.fmt_pretty import PrettyFormatter
from dazl.pretty.table.model import TableBuilder
from dazl.prim import ContractId


def test_capture_handles_unknown_templates():
    store = PackageStore.empty()
    formatter = PrettyFormatter()
    parties = {'ABC'}

    name = TypeConName(
        ModuleRef(PackageRef("00"), DottedName(dotted_name("SomeModule"))),
        dotted_name("SomeUnknownTemplate"))

    table = TableBuilder()
    table.add('A', ContractId(name, '0:0'), dict(some_field='some_value'), datetime.utcnow())

    lines = formatter.render(store, parties, table)
    output = '\n'.join(lines) + '\n'
    assert output, 'some lines of output expected'
