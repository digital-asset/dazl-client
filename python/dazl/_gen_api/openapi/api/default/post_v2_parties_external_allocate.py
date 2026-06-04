# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.allocate_external_party_request import AllocateExternalPartyRequest
from ...models.allocate_external_party_response import AllocateExternalPartyResponse
from ...models.js_canton_error import JsCantonError
from ...types import Response


def _get_kwargs(
    *,
    body: AllocateExternalPartyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/parties/external/allocate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AllocateExternalPartyResponse | JsCantonError | str:
    if response.status_code == 200:
        response_200 = AllocateExternalPartyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AllocateExternalPartyResponse | JsCantonError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AllocateExternalPartyRequest,
) -> Response[AllocateExternalPartyResponse | JsCantonError | str]:
    """Alpha 3.3: Endpoint to allocate a new external party on a synchronizer

    Expected to be stable in 3.5

    The external party must be hosted (at least) on this node with either confirmation or observation
    permissions
    It can optionally be hosted on other nodes (then called a multi-hosted party).
    If hosted on additional nodes, explicit authorization of the hosting relationship must be performed
    on those nodes
    before the party can be used.
    Decentralized namespaces are supported but must be provided fully authorized by their owners.
    The individual owner namespace transactions can be submitted in the same call (fully authorized as
    well).
    In the simple case of a non-multi hosted, non-decentralized party, the RPC will return once the
    party is
    effectively allocated and ready to use, similarly to the AllocateParty behavior.
    For more complex scenarios applications may need to query the party status explicitly (only through
    the admin API as of now).

    Args:
        body (AllocateExternalPartyRequest): Required authorization:
              ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(identity_provider_id) OR
            IsAuthenticatedUser(user_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocateExternalPartyResponse | JsCantonError | str]
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
    body: AllocateExternalPartyRequest,
) -> AllocateExternalPartyResponse | JsCantonError | str | None:
    """Alpha 3.3: Endpoint to allocate a new external party on a synchronizer

    Expected to be stable in 3.5

    The external party must be hosted (at least) on this node with either confirmation or observation
    permissions
    It can optionally be hosted on other nodes (then called a multi-hosted party).
    If hosted on additional nodes, explicit authorization of the hosting relationship must be performed
    on those nodes
    before the party can be used.
    Decentralized namespaces are supported but must be provided fully authorized by their owners.
    The individual owner namespace transactions can be submitted in the same call (fully authorized as
    well).
    In the simple case of a non-multi hosted, non-decentralized party, the RPC will return once the
    party is
    effectively allocated and ready to use, similarly to the AllocateParty behavior.
    For more complex scenarios applications may need to query the party status explicitly (only through
    the admin API as of now).

    Args:
        body (AllocateExternalPartyRequest): Required authorization:
              ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(identity_provider_id) OR
            IsAuthenticatedUser(user_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocateExternalPartyResponse | JsCantonError | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AllocateExternalPartyRequest,
) -> Response[AllocateExternalPartyResponse | JsCantonError | str]:
    """Alpha 3.3: Endpoint to allocate a new external party on a synchronizer

    Expected to be stable in 3.5

    The external party must be hosted (at least) on this node with either confirmation or observation
    permissions
    It can optionally be hosted on other nodes (then called a multi-hosted party).
    If hosted on additional nodes, explicit authorization of the hosting relationship must be performed
    on those nodes
    before the party can be used.
    Decentralized namespaces are supported but must be provided fully authorized by their owners.
    The individual owner namespace transactions can be submitted in the same call (fully authorized as
    well).
    In the simple case of a non-multi hosted, non-decentralized party, the RPC will return once the
    party is
    effectively allocated and ready to use, similarly to the AllocateParty behavior.
    For more complex scenarios applications may need to query the party status explicitly (only through
    the admin API as of now).

    Args:
        body (AllocateExternalPartyRequest): Required authorization:
              ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(identity_provider_id) OR
            IsAuthenticatedUser(user_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocateExternalPartyResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AllocateExternalPartyRequest,
) -> AllocateExternalPartyResponse | JsCantonError | str | None:
    """Alpha 3.3: Endpoint to allocate a new external party on a synchronizer

    Expected to be stable in 3.5

    The external party must be hosted (at least) on this node with either confirmation or observation
    permissions
    It can optionally be hosted on other nodes (then called a multi-hosted party).
    If hosted on additional nodes, explicit authorization of the hosting relationship must be performed
    on those nodes
    before the party can be used.
    Decentralized namespaces are supported but must be provided fully authorized by their owners.
    The individual owner namespace transactions can be submitted in the same call (fully authorized as
    well).
    In the simple case of a non-multi hosted, non-decentralized party, the RPC will return once the
    party is
    effectively allocated and ready to use, similarly to the AllocateParty behavior.
    For more complex scenarios applications may need to query the party status explicitly (only through
    the admin API as of now).

    Args:
        body (AllocateExternalPartyRequest): Required authorization:
              ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(identity_provider_id) OR
            IsAuthenticatedUser(user_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocateExternalPartyResponse | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
