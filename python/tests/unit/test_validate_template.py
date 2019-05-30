# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from unittest import TestCase

from dazl.model.lookup import validate_template
from dazl.model.types_dynamic import generated_type_proxy_root


class TestValidateTemplate(TestCase):

    def test_generated_type_proxy_with_no_package_id(self):
        # noinspection PyPep8Naming
        Sample = generated_type_proxy_root(root_module_name='Sample')

        expected = ('*', 'Sample.Test.Template')
        actual = validate_template(Sample.Test.Template)
        self.assertEqual(expected, actual)
