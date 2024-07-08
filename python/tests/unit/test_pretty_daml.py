# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.damlast import DarFile, daml_types as daml
from dazl.damlast.daml_lf_1 import DottedName, ModuleRef, PackageRef, TypeConName
from dazl.damlast.lookup import MultiPackageLookup
from dazl.pretty import DamlPrettyPrinter, PrettyOptions

from .dars import Pending


def test_render_list_of_party():
    type_ = daml.List(daml.Party)

    expected = "[Party]"
    actual = str(type_)

    assert expected == actual


def test_render_list_of_contract_type_con():
    module_ref = ModuleRef(
        package_id=PackageRef("00000000000000000000000000000000"), module_name=DottedName(("ABC",))
    )
    name = TypeConName(module=module_ref, name=("DefGhi",))
    type_ = daml.List(daml.ContractId(daml.con(name)))

    expected = "[ContractId ABC:DefGhi]"
    actual = str(type_)

    assert expected == actual


def test_render_update_of_contract_type_con():
    module_ref = ModuleRef(
        package_id=PackageRef("00000000000000000000000000000000"), module_name=DottedName(("ABC",))
    )
    name = TypeConName(module=module_ref, name=("DefGhi",))
    type_ = daml.Update(daml.ContractId(daml.con(name)))

    expected = "Update (ContractId ABC:DefGhi)"
    actual = str(type_)

    assert expected == actual


def test_render_metadata():
    with DarFile(Pending) as dar:
        pp = DamlPrettyPrinter(
            lookup=MultiPackageLookup(dar.archives()), context=PrettyOptions(show_hidden_types=True)
        )
        pp.render_store()
