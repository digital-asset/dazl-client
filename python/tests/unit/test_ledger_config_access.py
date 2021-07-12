# Copyright (c) 2017-2023 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.ledger.auth import DamlV1ClaimName
from dazl.ledger.config import PropertyBasedAccessConfig, TokenBasedAccessConfig
from dazl.prim import Party
import jwt

ALICE = Party("Alice")


def test_access_jwts_are_valid():
    config = PropertyBasedAccessConfig(act_as=[ALICE])
    claims = jwt.decode(config.token, algorithms=["none"], options={"verify_signature": False})

    assert claims[DamlV1ClaimName]["actAs"] == ["Alice"]


def test_v1_party_claims_parse():
    # use PropertyBasedAccessConfig to create a token, which we then parse using
    # TokenBasedAccessConfig
    config = PropertyBasedAccessConfig(act_as=[ALICE])
    access = TokenBasedAccessConfig(config.token)
    assert set(access.act_as) == {ALICE}
