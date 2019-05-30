# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase

from dazl.metrics import MetricEvents
from dazl.client._party_client_impl import _PartyClientImpl
from dazl.client.api import AIOPartyClient, SimplePartyClient
from dazl.model.core import Party
from dazl.util.asyncio_util import Invoker


class TestApiConsistency(TestCase):
    def test_api_consistency(self):
        impl = _PartyClientImpl(MetricEvents(), Invoker(), Party('party'))

        apc = AIOPartyClient(impl)
        tpc = SimplePartyClient(impl)

        callable_apcs = {key: getattr(apc, key) for key in dir(apc) if not key.startswith('_') and callable(getattr(apc, key))}
        callable_tpcs = {key: getattr(tpc, key) for key in dir(tpc) if not key.startswith('_') and callable(getattr(tpc, key))}

        self.assertEqual(sorted(set(callable_apcs.keys())), sorted(set(callable_tpcs.keys())))

