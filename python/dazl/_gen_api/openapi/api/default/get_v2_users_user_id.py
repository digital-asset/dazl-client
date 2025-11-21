# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_user_response import GetUserResponse
from ...models.js_canton_error import JsCantonError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    identity_provider_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["identity-provider-id"] = identity_provider_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/users/{user_id}".format(
            user_id=user_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetUserResponse | JsCantonError | str:
    if response.status_code == 200:
        response_200 = GetUserResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetUserResponse | JsCantonError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
) -> Response[GetUserResponse | JsCantonError | str]:
    """Get user details.

    Args:
        user_id (str):
        identity_provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        identity_provider_id=identity_provider_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
) -> GetUserResponse | JsCantonError | str | None:
    """Get user details.

    Args:
        user_id (str):
        identity_provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserResponse | JsCantonError | str
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        identity_provider_id=identity_provider_id,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
) -> Response[GetUserResponse | JsCantonError | str]:
    """Get user details.

    Args:
        user_id (str):
        identity_provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        identity_provider_id=identity_provider_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
) -> GetUserResponse | JsCantonError | str | None:
    """Get user details.

    Args:
        user_id (str):
        identity_provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserResponse | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            identity_provider_id=identity_provider_id,
        )
    ).parsed
