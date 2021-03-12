# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import warnings

from dazl import Party
from dazl.client.api import AIOPartyClient, Network as V5_Network, SimplePartyClient
from dazl.compat import Network as V8_Network, NotSupportedError


def test_api_consistency():
    from dazl.client._network_client_impl import _NetworkImpl
    from dazl.client._party_client_impl import _PartyClientImpl

    impl = _PartyClientImpl(_NetworkImpl(), Party("party"))

    apc = AIOPartyClient(impl)
    tpc = SimplePartyClient(impl)

    callable_apcs = {key for key in dir(apc) if is_public_symbol(apc, key)}
    callable_tpcs = {key for key in dir(tpc) if is_public_symbol(tpc, key)}

    assert sorted(callable_apcs) == sorted(callable_tpcs)


def test_api_consistency_v8_compat():
    """
    Ensure the dazl.compat.v8.Network class exposes the same symbols as dazl.client.api.Network.
    """
    n5 = V5_Network()
    n8 = V8_Network()

    callable_v5_symbols = {key for key in dir(n5) if is_public_symbol(n5, key)}
    callable_v8_symbols = {key for key in dir(n8) if is_public_symbol(n8, key)}

    assert sorted(callable_v5_symbols) == sorted(callable_v8_symbols)


def is_public_symbol(obj, key):
    if key.startswith("_"):
        return False

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            val = getattr(obj, key)
    except NotSupportedError:
        # we use NotSupportedError as a signal that an API is not supported, even in the
        # transitional API; however we're
        return True

    return callable(val)
