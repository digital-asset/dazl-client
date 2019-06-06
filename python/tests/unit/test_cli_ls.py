# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Tests to ensure that CLI commands work properly.
"""
from pathlib import Path
from unittest import TestCase

from dazl import sandbox
from dazl.cli import _main

DAML_PATH = Path(__file__).parent.parent.parent / '_template' / 'Main.daml'


class TestCliLs(TestCase):

    def test_simple_ls(self):
        with sandbox(daml_path=DAML_PATH) as proc:
            exit_code = _main(f'dazl ls --url {proc.url} --parties=Alice'.split(' '))

        self.assertEqual(exit_code, 0)

    def test_simple_ls_two_parties(self):
        with sandbox(daml_path=DAML_PATH) as proc:
            exit_code = _main(f'dazl ls --url {proc.url} --parties=Alice,Bob'.split(' '))

        self.assertEqual(exit_code, 0)

    def test_env_ls(self):
        import os
        with sandbox(daml_path=DAML_PATH) as proc:
            os.environ['DAML_LEDGER_URL'] = proc.url
            os.environ['DAML_LEDGER_PARTY'] = 'Alice'
            exit_code = _main('dazl ls'.split(' '))

        self.assertEqual(exit_code, 0)
