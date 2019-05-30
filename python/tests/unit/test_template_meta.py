# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import Any, Dict
from unittest import TestCase

from dazl import create, exercise, TemplateMeta, ChoiceMeta
from dazl.model.core import ContractId
from dazl.model.types import UnresolvedTypeReference
from dazl.model.types_dynamic import generated_type_proxy_root


def codegen_backends() -> Dict[str, Any]:
    class Sample(metaclass=TemplateMeta, template_name='Sample'):
        __slots__ = 'single',

        def __init__(self, single):
            self.single = single

        def _asdict(self):
            return dict(single=self.single)

        class Archive(metaclass=ChoiceMeta, template_name='Sample', choice_name='Archive'):
            __slots__ = ()

            def _asdict(self):
                return {}

    return {
        'generated': Sample,
        # This proxy type should be usable the same way as the "generated" code above is used.
        'proxy': generated_type_proxy_root(root_module_name='Sample'),
    }


class TestCodgenMetas(TestCase):
    def test_template_meta_construction(self):
        for test_name, Sample in codegen_backends().items():
            with self.subTest(test_name):
                command = create(Sample(single=1))
                self.assertEqual(command.template, UnresolvedTypeReference('Sample'))

    def test_template_meta_deconstructed(self):
        for test_name, Sample in codegen_backends().items():
            with self.subTest(test_name):
                command = create(Sample, dict(single=1))
                self.assertEqual(command.template, UnresolvedTypeReference('Sample'))

    def test_choice_meta_construction(self):
        for test_name, Sample in codegen_backends().items():
            with self.subTest(test_name):
                cid = ContractId('1:0')
                command = exercise(cid, Sample.Archive())
                self.assertEqual(command.choice, 'Archive')

    def test_choice_meta_deconstructed(self):
        for test_name, Sample in codegen_backends().items():
            with self.subTest(test_name):
                cid = ContractId('1:0')
                command = exercise(cid, Sample.Archive, {})
                self.assertEqual(command.choice, 'Archive')
