# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from typing import Any

from dazl._gen_api import AuthenticatedClient
from dazl._gen_api.openapi.api.default import get_v2_users
from dazl._gen_api.openapi.models.list_users_response import ListUsersResponse
import httpx
import pytest


@pytest.mark.asyncio
async def test_list_users_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        response = await get_v2_users.asyncio(client=client)

        for user in response.users:
            assert user.id is not None
            logging.info(f"User: {user.id} Party: {user.primary_party}")

        assert isinstance(response, ListUsersResponse)
        assert response.users is not None
        assert isinstance(response.users, list)
