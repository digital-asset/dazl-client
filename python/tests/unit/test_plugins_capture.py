# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest
from datetime import datetime

from dazl.model.core import ContractId
from dazl.plugins.capture import fmt_pretty
from dazl.plugins.capture.model_capture import LedgerCapture


class PluginsCaptureTest(unittest.TestCase):

    def test_capture_handles_unknown_templates(self):
        parties = list('ABC')
        capture = LedgerCapture()
        capture.capture('A',
                        ContractId('0:0', template_id='some_unknown_template'),
                        dict(some_field='some_value'), datetime.utcnow())

        lines = fmt_pretty.format_entries(capture, parties)
        output = '\n'.join(lines) + '\n'
        self.assertTrue(output, 'some lines of output expected')
