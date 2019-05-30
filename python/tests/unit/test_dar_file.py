# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from unittest import TestCase, skip

from dazl.util.dar import TemporaryDar, DarFile

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'AllKindsOf.daml'


class TestDarFile(TestCase):
    @skip('Something about the way dazl compiles DARs currently causes this field to be blank')
    def test_get_sdk_version(self):
        with TemporaryDar(DAML_FILE, damlc_component='damlc:0.12.20') as outputs:
            for output in outputs:
                if output.endswith('.dar'):
                    with DarFile(output) as dar:
                        print(dar.get_manifest())
                        self.assertEqual('0.12.20', dar.get_sdk_version())

