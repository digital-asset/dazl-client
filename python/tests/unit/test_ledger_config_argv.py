# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
from io import StringIO
import logging
import os
from typing import Any, Mapping

from dazl.ledger.config import configure_parser
from dazl.ledger.config.argv import WideHelpFormatter
from dazl.ledger.config.exc import ConfigWarning
import pytest


def _test(cmd_line: str, expected: Mapping[str, Any]):
    parser = argparse.ArgumentParser(
        "sample app",
        add_help=False,
    )
    configure_parser(parser)
    args = parser.parse_args(cmd_line.split(" "))
    actual = {k: v for k, v in vars(args).items() if v is not None}
    assert actual == expected


def test_can_configure_parser():
    os.environ["COLUMNS"] = "108"
    parser = argparse.ArgumentParser(
        "sample app", add_help=False, formatter_class=WideHelpFormatter
    )
    configure_parser(parser)
    with StringIO() as buf:
        parser.print_help(buf)
        logging.info("Sample output:\n\n" + buf.getvalue())


def test_basic_args():
    _test("--host somewhere --port 6865", {"host": "somewhere", "port": 6865})


def test_basic_short_args():
    _test("-h somewhere -p 6865", {"host": "somewhere", "port": 6865})


def test_party_compat_alias():
    _test("--party Alice", {"act_as": ["Alice"]})


def test_act_as_multiple_parties_with_comma():
    _test("--act-as Alice,Bob", {"act_as": ["Alice", "Bob"]})


def test_act_as_multiple_parties_with_space():
    _test("--act-as Alice Bob", {"act_as": ["Alice", "Bob"]})


def test_act_as_multiple_times():
    _test("--act-as Alice --act-as Bob", {"act_as": ["Alice", "Bob"]})


def test_mixed_parties():
    _test(
        "--act-as Alice --act-as Bob --read-as Carol",
        {"act_as": ["Alice", "Bob"], "read_as": ["Carol"]},
    )


def test_mixed_parties_short_form():
    _test("-u Alice -u Bob -r Carol", {"act_as": ["Alice", "Bob"], "read_as": ["Carol"]})


def test_specify_token():
    _test("--oauth-token XYZ", {"oauth_token": "XYZ"})


def test_http_proxy_flag():
    _test("--use-http-proxy", {"use_http_proxy": True})
    _test("--enable-http-proxy", {"use_http_proxy": True})
    _test("--no-use-http-proxy", {"use_http_proxy": False})


def test_warning_flags():
    with pytest.warns(ConfigWarning):
        _test("--poll-interval 30", {})


def test_dash_p_compat_alias_for_party():
    with pytest.warns(ConfigWarning):
        _test("-p Alice", {"act_as": ["Alice"]})


def test_dash_p_compat_alias_for_port():
    _test("-p 1000", {"port": 1000})
