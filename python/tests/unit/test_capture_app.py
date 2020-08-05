# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime

from dazl import ContractId
from dazl.pretty.table import fmt_pretty, LedgerCapture


def test_capture_handles_unknown_templates():
    parties = list('ABC')
    capture = LedgerCapture()
    capture.capture('A',
                    ContractId('0:0', template_id='some_unknown_template'),
                    dict(some_field='some_value'), datetime.utcnow())

    lines = fmt_pretty.format_entries(capture, parties)
    output = '\n'.join(lines) + '\n'
    assert output, 'some lines of output expected'
