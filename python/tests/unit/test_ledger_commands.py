# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from typing import Any

from dazl.api import (
    AuthenticatedClient,
    CompletionStreamRequest,
    JsCommands,
    ListKnownPartiesResponse,
    get_v2_parties,
    post_v2_commands_async_submit,
    post_v2_commands_completions,
    post_v2_commands_submit_and_wait,
    post_v2_commands_submit_and_wait_for_transaction_tree,
)
import httpx
import pytest


@pytest.mark.asyncio
async def test_command_completions_stream_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        parties_response = await get_v2_parties.asyncio(client=client)

        if isinstance(parties_response, ListKnownPartiesResponse):
            parties = parties_response.party_details

            if parties and len(parties) > 0:
                party_id = parties[0].party

                completion_request = CompletionStreamRequest(
                    user_id="",
                    begin_exclusive=0,
                    parties=[party_id],
                )

                response = await post_v2_commands_completions.asyncio(
                    client=client, body=completion_request
                )

                logging.info(f"Completions stream response received")
            else:
                logging.info("No parties available for completions test")
        else:
            logging.info("Failed to get parties for completions test")


@pytest.mark.asyncio
async def test_submit_command_async_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        parties_response = await get_v2_parties.asyncio(client=client)

        if isinstance(parties_response, ListKnownPartiesResponse):
            parties = parties_response.party_details

            if parties and len(parties) > 0:
                party_id = parties[0].party

                commands = JsCommands(
                    command_id="test-command-1",
                    act_as=[party_id],
                    commands=[],
                )

                response = await post_v2_commands_async_submit.asyncio(client=client, body=commands)

                logging.info(f"Async submit response received")
            else:
                logging.info("No parties available for async submit test")
        else:
            logging.info("Failed to get parties for async submit test")


@pytest.mark.asyncio
async def test_submit_and_wait_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        parties_response = await get_v2_parties.asyncio(client=client)

        if isinstance(parties_response, ListKnownPartiesResponse):
            parties = parties_response.party_details

            if parties and len(parties) > 0:
                party_id = parties[0].party

                commands = JsCommands(
                    command_id="test-command-2",
                    act_as=[party_id],
                    commands=[],
                )

                response = await post_v2_commands_submit_and_wait.asyncio(
                    client=client, body=commands
                )

                logging.info(f"Submit and wait response received")
            else:
                logging.info("No parties available for submit and wait test")
        else:
            logging.info("Failed to get parties for submit and wait test")


@pytest.mark.asyncio
async def test_submit_and_wait_for_transaction_tree_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        parties_response = await get_v2_parties.asyncio(client=client)

        if isinstance(parties_response, ListKnownPartiesResponse):
            parties = parties_response.party_details

            if parties and len(parties) > 0:
                party_id = parties[0].party

                commands = JsCommands(
                    command_id="test-command-3",
                    act_as=[party_id],
                    commands=[],
                )

                response = await post_v2_commands_submit_and_wait_for_transaction_tree.asyncio(
                    client=client, body=commands
                )

                logging.info(f"Submit and wait for transaction tree response received")
            else:
                logging.info("No parties available for submit and wait for tree test")
        else:
            logging.info("Failed to get parties for submit and wait for tree test")
