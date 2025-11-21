# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.allocate_party_request import AllocatePartyRequest
from ...models.allocate_party_response import AllocatePartyResponse
from ...models.js_canton_error import JsCantonError
from ...types import Response


def _get_kwargs(
    *,
    body: AllocatePartyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/parties",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AllocatePartyResponse | JsCantonError | str:
    if response.status_code == 200:
        response_200 = AllocatePartyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AllocatePartyResponse | JsCantonError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AllocatePartyRequest,
) -> Response[AllocatePartyResponse | JsCantonError | str]:
    """Allocate a new party to the participant node

    Args:
        body (AllocatePartyRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocatePartyResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AllocatePartyRequest,
) -> AllocatePartyResponse | JsCantonError | str | None:
    """Allocate a new party to the participant node

    Args:
        body (AllocatePartyRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocatePartyResponse | JsCantonError | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AllocatePartyRequest,
) -> Response[AllocatePartyResponse | JsCantonError | str]:
    """Allocate a new party to the participant node

    Args:
        body (AllocatePartyRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocatePartyResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AllocatePartyRequest,
) -> AllocatePartyResponse | JsCantonError | str | None:
    """Allocate a new party to the participant node

    Args:
        body (AllocatePartyRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocatePartyResponse | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
