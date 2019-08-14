# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase

from dazl.pretty import DamlPrettyPrinter, PrettyOptions
from dazl.util.dar import DarFile
from .dars import Pending


class TestDamlPrettyPrinter(TestCase):

    # region Basic type rendering

    def test_render_list_of_party_old(self):
        from dazl.model.types import ListType, SCALAR_TYPE_PARTY

        type_ = ListType(SCALAR_TYPE_PARTY)

        expected = '[Party]'
        actual = str(type_)

        self.assertEqual(expected, actual)

    def test_render_list_of_party_new(self):
        from dazl.damlast.daml_lf_1 import PrimType, Type

        type_ = Type(prim=Type.Prim(prim=PrimType.LIST, args=(Type(prim=Type.Prim(prim=PrimType.PARTY, args=())),)))

        expected = '[Party]'
        actual = str(type_)

        self.assertEqual(expected, actual)

    def test_render_list_of_contract_type_con_old(self):
        from dazl.model.types import ContractIdType, ListType, ModuleRef, TypeReference

        module_ref = ModuleRef(package_id='00000000000000000000000000000000', module_name=('ABC',))
        type_ref = TypeReference(module=module_ref, name=('DefGhi',))
        type_ = ListType(ContractIdType(type_ref))

        expected = '[ContractId ABC:DefGhi]'
        actual = str(type_)

        self.assertEqual(expected, actual)

    def test_render_list_of_contract_type_con_new(self):
        from dazl.damlast.daml_lf_1 import PrimType, Type
        from dazl.model.types import ModuleRef, TypeReference

        module_ref = ModuleRef(package_id='00000000000000000000000000000000', module_name=('ABC',))
        con_type = Type(con=Type.Con(tycon=TypeReference(module=module_ref, name=('DefGhi',)), args=()))
        cid_type = Type(prim=Type.Prim(prim=PrimType.CONTRACT_ID, args=(con_type,)))
        type_ = Type(prim=Type.Prim(prim=PrimType.LIST, args=(cid_type,)))

        expected = '[ContractId ABC:DefGhi]'
        actual = str(type_)

        self.assertEqual(expected, actual)

    def test_render_update_of_contract_type_con_old(self):
        from dazl.model.types import ContractIdType, UpdateType, ModuleRef, TypeReference

        module_ref = ModuleRef(package_id='00000000000000000000000000000000', module_name=('ABC',))
        type_ref = TypeReference(module=module_ref, name=('DefGhi',))
        type_ = UpdateType(ContractIdType(type_ref))

        expected = 'Update (ContractId ABC:DefGhi)'
        actual = str(type_)

        self.assertEqual(expected, actual)

    def test_render_update_of_contract_type_con_new(self):
        from dazl.damlast.daml_lf_1 import PrimType, Type
        from dazl.model.types import ModuleRef, TypeReference

        module_ref = ModuleRef(package_id='00000000000000000000000000000000', module_name=('ABC',))
        con_type = Type(con=Type.Con(tycon=TypeReference(module=module_ref, name=('DefGhi',)), args=()))
        cid_type = Type(prim=Type.Prim(prim=PrimType.CONTRACT_ID, args=(con_type,)))
        type_ = Type(prim=Type.Prim(prim=PrimType.UPDATE, args=(cid_type,)))

        expected = 'Update (ContractId ABC:DefGhi)'
        actual = str(type_)

        self.assertEqual(expected, actual)

    # endregion

    def test_render_metadata(self):
        with DarFile(Pending) as dar:
            pp = DamlPrettyPrinter(store=dar.read_metadata(), context=PrettyOptions(show_hidden_types=True))
            pp.render_store()
