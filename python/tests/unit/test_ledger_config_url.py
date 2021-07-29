# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from urllib.parse import urlparse

from dazl.ledger.config import create_url
import pytest

testdata = [
    # TODO: figure out a way to test the blank default in pytest while also ignoring environment
    #  variables; right now our tests set DAML_LEDGER_URL for integration tests but this screws
    #  up the test for the "no values specified" case
    # ({}, "grpc://localhost:6865"),
    ({"url": "somewhere"}, "https://somewhere:443"),
    ({"url": "http://somewhere"}, "http://somewhere:80"),
    ({"url": "https://somewhere"}, "https://somewhere:443"),
    ({"url": "somewhere:443"}, "https://somewhere:443"),
    ({"port": 6865}, "grpc://localhost:6865"),
    ({"port": 7575}, "http://localhost:7575"),
    ({"host": "localhost"}, "grpc://localhost:6865"),
    ({"host": "somewhere"}, "https://somewhere:443"),
]


@pytest.mark.parametrize("kwargs,expected_url", testdata)
def test_ledger_config_url_all_defaults(kwargs, expected_url):
    actual = urlparse(create_url(**kwargs).url)
    expected = urlparse(expected_url)
    assert expected == actual


def test_ledger_config_rejects_overspecified_values():
    with pytest.raises(ValueError):
        create_url(url="localhost:6865", host="localhost", port=6865)
