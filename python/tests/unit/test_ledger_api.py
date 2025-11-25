# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging
from typing import Any

from dazl.api import (
    AuthenticatedClient,
    GetUserResponse,
    ListUsersResponse,
    UpdateUserIdentityProviderIdRequest,
    UpdateUserRequest,
    User,
    delete_v2_users_user_id,
    get_v2_authenticated_user,
    get_v2_users,
    get_v2_users_user_id,
    get_v2_users_user_id_rights,
    patch_v2_users_user_id,
    patch_v2_users_user_id_identity_provider_id,
)
import httpx
import pytest


@pytest.mark.asyncio
async def test_list_users_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        response = await get_v2_users.asyncio(client=client)

        assert isinstance(response, ListUsersResponse)
        assert response.users is not None
        assert isinstance(response.users, list)

        for user in response.users:
            assert user.id is not None
            logging.info(f"User: {user.id} Party: {user.primary_party}")


@pytest.mark.asyncio
async def test_get_authenticated_user_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        response = await get_v2_authenticated_user.asyncio(client=client)

        if isinstance(response, str):
            logging.info(f"Expected auth failure with test token: {response}")
            assert "authenticated" in response.lower() or "token" in response.lower()
        else:
            assert isinstance(response, GetUserResponse)
            assert response.user is not None
            assert isinstance(response.user, User)
            logging.info(f"Authenticated user: {response.user.id}")


@pytest.mark.asyncio
async def test_get_user_by_id_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        users_response = await get_v2_users.asyncio(client=client)
        assert isinstance(users_response, ListUsersResponse)
        assert users_response.users is not None
        assert isinstance(users_response.users, list)
        assert len(users_response.users) > 0
        user_id = users_response.users[0].id

        response = await get_v2_users_user_id.asyncio(client=client, user_id=user_id)

        assert isinstance(response, GetUserResponse)
        assert response.user is not None
        assert isinstance(response.user, User)
        assert response.user.id == user_id
        logging.info(f"Retrieved user: {response.user.id}")


@pytest.mark.asyncio
async def test_get_user_rights_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        users_response = await get_v2_users.asyncio(client=client)
        assert isinstance(users_response, ListUsersResponse)
        assert users_response.users is not None
        assert isinstance(users_response.users, list)
        assert len(users_response.users) > 0
        user_id = users_response.users[0].id

        httpx_client = client.get_async_httpx_client()
        response = await httpx_client.get(f"/v2/users/{user_id}/rights")

        assert response.status_code == 200
        assert response.content is not None
        logging.info(f"User rights for {user_id}: {response.text}")


@pytest.mark.asyncio
async def test_update_user_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        users_response = await get_v2_users.asyncio(client=client)
        assert isinstance(users_response, ListUsersResponse)
        assert users_response.users is not None
        assert isinstance(users_response.users, list)
        assert len(users_response.users) > 0
        user_id = users_response.users[0].id
        existing_user = users_response.users[0]

        update_request = UpdateUserRequest(
            user=existing_user,
        )

        response = await patch_v2_users_user_id.asyncio(
            client=client, user_id=user_id, body=update_request
        )

        assert response is not None
        logging.info(f"Updated user: {user_id}")


@pytest.mark.asyncio
async def test_update_user_identity_provider_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        users_response = await get_v2_users.asyncio(client=client)
        assert isinstance(users_response, ListUsersResponse)
        assert users_response.users is not None
        assert isinstance(users_response.users, list)
        assert len(users_response.users) > 0
        user_id = users_response.users[0].id
        current_idp = users_response.users[0].identity_provider_id

        update_request = UpdateUserIdentityProviderIdRequest(
            user_id=user_id,
            source_identity_provider_id=current_idp or "",
            target_identity_provider_id=current_idp or "",
        )

        response = await patch_v2_users_user_id_identity_provider_id.asyncio(
            client=client, user_id=user_id, body=update_request
        )

        assert response is not None
        logging.info(f"Updated identity provider for user: {user_id}")


@pytest.mark.asyncio
async def test_delete_user_via_api(sandbox_v3: Any) -> None:
    timeout = httpx.Timeout(10.0, connect=5.0)
    async with AuthenticatedClient(
        base_url=sandbox_v3.url, token="test-token", timeout=timeout
    ) as client:
        users_response = await get_v2_users.asyncio(client=client)
        assert isinstance(users_response, ListUsersResponse)
        assert users_response.users is not None
        assert isinstance(users_response.users, list)
        initial_count = len(users_response.users)

        if initial_count > 1:
            user_id_to_delete = users_response.users[-1].id

            response = await delete_v2_users_user_id.asyncio(
                client=client, user_id=user_id_to_delete
            )

            assert response is not None
            logging.info(f"Deleted user: {user_id_to_delete}")

            users_after = await get_v2_users.asyncio(client=client)
            assert isinstance(users_after, ListUsersResponse)
            assert users_after.users is not None
            assert isinstance(users_after.users, list)
            assert len(users_after.users) == initial_count - 1
        else:
            logging.info("Skipping delete test - only one user available")
