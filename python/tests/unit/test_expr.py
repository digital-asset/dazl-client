# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
from pathlib import Path
from unittest import TestCase, skip

from dazl import setup_default_logger
from dazl.util.dar import TemporaryDar

DAML_FILE = Path(__file__).parent.parent / 'resources' / 'Pending.daml'


setup_default_logger(logging.DEBUG)


class TestExpr(TestCase):
    @skip('This API does not really work yet, nor is it finalized')
    def test_calculate_signatories(self):
        tdar = TemporaryDar(DAML_FILE)
        try:
            store = tdar.store()
            template = next(iter(store.resolve_template('Pending.Counter')))
            actual = template.signatories(store, {'owner': 'Mommy', 'value': 0})
            self.assertEqual(['Mommy'], actual)
        finally:
            tdar.cleanup()
