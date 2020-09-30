# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from dazl.damlast.daml_lf_1 import DottedName, ModuleRef, PackageRef, TypeConName
from dazl.damlast import daml_types as daml
from dazl.pretty import DamlPrettyPrinter, PrettyOptions
from dazl.util.dar import DarFile
from .dars import Pending


def test_render_list_of_party_old():
    from dazl.model.types import ListType, SCALAR_TYPE_PARTY

    type_ = ListType(SCALAR_TYPE_PARTY)

    expected = '[Party]'
    actual = str(type_)

    assert expected == actual


def test_render_list_of_party_new():
    type_ = daml.List(daml.Party)

    expected = '[Party]'
    actual = str(type_)

    assert expected == actual


def test_render_list_of_contract_type_con_old():
    from dazl.model.types import ContractIdType, ListType, TypeReference

    module_ref = ModuleRef(package_id=PackageRef('00000000000000000000000000000000'), module_name=DottedName(('ABC',)))
    type_ref = TypeReference(con=TypeConName(module=module_ref, name=('DefGhi',)))
    type_ = ListType(ContractIdType(type_ref))

    expected = '[ContractId ABC:DefGhi]'
    actual = str(type_)

    assert expected == actual


def test_render_list_of_contract_type_con_new():
    module_ref = ModuleRef(package_id=PackageRef('00000000000000000000000000000000'), module_name=DottedName(('ABC',)))
    name = TypeConName(module=module_ref, name=('DefGhi',))
    type_ = daml.List(daml.ContractId(daml.con(name)))

    expected = '[ContractId ABC:DefGhi]'
    actual = str(type_)

    assert expected == actual


def test_render_update_of_contract_type_con_old():
    from dazl.model.types import ContractIdType, UpdateType, TypeReference

    module_ref = ModuleRef(package_id=PackageRef('00000000000000000000000000000000'), module_name=DottedName(('ABC',)))
    type_ref = TypeReference(con=TypeConName(module=module_ref, name=('DefGhi',)))
    type_ = UpdateType(ContractIdType(type_ref))

    expected = 'Update (ContractId ABC:DefGhi)'
    actual = str(type_)

    assert expected == actual


def test_render_update_of_contract_type_con_new():
    module_ref = ModuleRef(package_id=PackageRef('00000000000000000000000000000000'), module_name=DottedName(('ABC',)))
    name = TypeConName(module=module_ref, name=('DefGhi',))
    type_ = daml.Update(daml.ContractId(daml.con(name)))

    expected = 'Update (ContractId ABC:DefGhi)'
    actual = str(type_)

    assert expected == actual


def test_render_metadata():
    with DarFile(Pending) as dar:
        pp = DamlPrettyPrinter(store=dar.read_metadata(), context=PrettyOptions(show_hidden_types=True))
        pp.render_store()
