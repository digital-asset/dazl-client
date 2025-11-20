# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from typing import Any

from dazl._gen_api import AuthenticatedClient
from dazl._gen_api.openapi.api.default import (
    get_v2_state_connected_synchronizers,
    get_v2_state_latest_pruned_offsets,
    get_v2_state_ledger_end,
    get_v2_updates_transaction_tree_by_id_update_id,
    get_v2_updates_transaction_tree_by_offset_offset,
)
import httpx
import pytest


@pytest.mark.asyncio
async def test_get_transaction_tree_by_offset_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        offset = 0

        response = await get_v2_updates_transaction_tree_by_offset_offset.asyncio(
            client=client, offset=offset
        )

        logging.info(f"Transaction tree by offset response: {response}")


@pytest.mark.asyncio
async def test_get_transaction_tree_by_id_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        update_id = "test-update-id"

        response = await get_v2_updates_transaction_tree_by_id_update_id.asyncio(
            client=client, update_id=update_id
        )

        logging.info(f"Transaction tree by ID response: {response}")


@pytest.mark.asyncio
async def test_get_ledger_end_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        response = await get_v2_state_ledger_end.asyncio(client=client)

        assert response is not None
        logging.info(f"Ledger end response received")


@pytest.mark.asyncio
async def test_get_latest_pruned_offsets_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        response = await get_v2_state_latest_pruned_offsets.asyncio(client=client)

        assert response is not None
        logging.info(f"Latest pruned offsets response received")


@pytest.mark.asyncio
async def test_get_connected_synchronizers_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        response = await get_v2_state_connected_synchronizers.asyncio(client=client)

        assert response is not None
        logging.info(f"Connected synchronizers response received")
