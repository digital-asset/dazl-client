# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from typing import Any

from dazl.api import (
    AllocateExternalPartyRequest,
    AllocateExternalPartyResponse,
    AllocatePartyRequest,
    AllocatePartyResponse,
    AuthenticatedClient,
    GenerateExternalPartyTopologyRequest,
    ListKnownPartiesResponse,
    PartyDetails,
    UpdatePartyDetailsRequest,
    get_v2_parties,
    get_v2_parties_participant_id,
    get_v2_parties_party,
    patch_v2_parties_party,
    post_v2_parties,
    post_v2_parties_external_allocate,
    post_v2_parties_external_generate_topology,
)
import httpx
import pytest


@pytest.mark.asyncio
async def test_list_parties_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        response = await get_v2_parties.asyncio(client=client)

        assert isinstance(response, ListKnownPartiesResponse)
        assert response.party_details is not None
        assert isinstance(response.party_details, list)

        for party in response.party_details:
            assert party.party is not None
            logging.info(f"Party: {party.party}")


@pytest.mark.asyncio
async def test_get_party_by_id_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        parties_response = await get_v2_parties.asyncio(client=client)
        assert isinstance(parties_response, ListKnownPartiesResponse)
        assert parties_response.party_details is not None
        assert isinstance(parties_response.party_details, list)

        if len(parties_response.party_details) > 0:
            party_id = parties_response.party_details[0].party

            response = await get_v2_parties_party.asyncio(client=client, party=party_id)

            assert response is not None
            logging.info(f"Retrieved party: {party_id}")
        else:
            logging.info("No parties available to test")


@pytest.mark.asyncio
async def test_get_parties_by_participant_id_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        response = await get_v2_parties_participant_id.asyncio(client=client)

        assert response is not None
        logging.info(f"Participant parties response received")


@pytest.mark.asyncio
async def test_allocate_party_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        allocate_request = AllocatePartyRequest(
            party_id_hint="test-party",
            identity_provider_id="",
            synchronizer_id="",
            user_id="",
        )

        response = await post_v2_parties.asyncio(client=client, body=allocate_request)

        if isinstance(response, AllocatePartyResponse):
            assert response.party_details is not None
            from dazl._gen_api.openapi.models.party_details import PartyDetails

            assert isinstance(response.party_details, PartyDetails)
            logging.info(f"Allocated party: {response.party_details.party}")
        else:
            logging.info(f"Party allocation response: {response}")


@pytest.mark.asyncio
async def test_update_party_details_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        parties_response = await get_v2_parties.asyncio(client=client)
        assert isinstance(parties_response, ListKnownPartiesResponse)
        assert parties_response.party_details is not None
        assert isinstance(parties_response.party_details, list)

        if len(parties_response.party_details) > 0:
            party_id = parties_response.party_details[0].party

            update_request = UpdatePartyDetailsRequest()

            response = await patch_v2_parties_party.asyncio(
                client=client, party=party_id, body=update_request
            )

            assert response is not None
            logging.info(f"Updated party: {party_id}")
        else:
            logging.info("No parties available to update")
