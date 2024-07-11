# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl import Party
from dazl.client.api import AIOPartyClient, SimplePartyClient


def test_api_consistency():
    from dazl.client._network_client_impl import _NetworkImpl
    from dazl.client._party_client_impl import _PartyClientImpl

    impl = _PartyClientImpl(_NetworkImpl(), Party("party"))

    apc = AIOPartyClient(impl)
    tpc = SimplePartyClient(impl)

    callable_apcs = {
        key: getattr(apc, key)
        for key in dir(apc)
        if not key.startswith("_") and callable(getattr(apc, key))
    }
    callable_tpcs = {
        key: getattr(tpc, key)
        for key in dir(tpc)
        if not key.startswith("_") and callable(getattr(tpc, key))
    }

    assert sorted(set(callable_apcs.keys())) == sorted(set(callable_tpcs.keys()))
