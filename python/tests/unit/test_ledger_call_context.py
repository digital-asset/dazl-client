# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Tests that validate correct values are used when supplied at the call level, connection level, and/or read from a previously cached value.
"""

from __future__ import annotations

# noinspection PyProtectedMember
from dazl.ledger._call import AnyCallParameters, CachedParameters, CallContext, ConnectionParameters
from dazl.testing import encode_unsigned_token
import pytest

DEFAULT_V1_CONNECTION_PARAMETERS = ConnectionParameters(
    read_as=(),
    act_as=(),
    ledger_id=None,
    user_id_or_application_name=None,
    token=None,
    timeout=None,
)


def test_v1_token_disallows_user_id():
    token = encode_unsigned_token(ledger_id="fooledger")
    with pytest.raises(ValueError):
        CallContext.compute(
            AnyCallParameters(token="", user_id="somebody"), None, DEFAULT_V1_CONNECTION_PARAMETERS
        )
