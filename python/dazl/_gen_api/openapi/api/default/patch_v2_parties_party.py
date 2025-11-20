from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.js_canton_error import JsCantonError
from ...models.update_party_details_request import UpdatePartyDetailsRequest
from ...models.update_party_details_response import UpdatePartyDetailsResponse
from ...types import Response


def _get_kwargs(
    party: str,
    *,
    body: UpdatePartyDetailsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/parties/{party}".format(
            party=party,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JsCantonError | UpdatePartyDetailsResponse | str:
    if response.status_code == 200:
        response_200 = UpdatePartyDetailsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JsCantonError | UpdatePartyDetailsResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    party: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePartyDetailsRequest,
) -> Response[JsCantonError | UpdatePartyDetailsResponse | str]:
    """Allocate a new party to the participant node

    Args:
        party (str):
        body (UpdatePartyDetailsRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(party_details.identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | UpdatePartyDetailsResponse | str]
    """

    kwargs = _get_kwargs(
        party=party,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    party: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePartyDetailsRequest,
) -> JsCantonError | UpdatePartyDetailsResponse | str | None:
    """Allocate a new party to the participant node

    Args:
        party (str):
        body (UpdatePartyDetailsRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(party_details.identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | UpdatePartyDetailsResponse | str
    """

    return sync_detailed(
        party=party,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    party: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePartyDetailsRequest,
) -> Response[JsCantonError | UpdatePartyDetailsResponse | str]:
    """Allocate a new party to the participant node

    Args:
        party (str):
        body (UpdatePartyDetailsRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(party_details.identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | UpdatePartyDetailsResponse | str]
    """

    kwargs = _get_kwargs(
        party=party,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    party: str,
    *,
    client: AuthenticatedClient,
    body: UpdatePartyDetailsRequest,
) -> JsCantonError | UpdatePartyDetailsResponse | str | None:
    """Allocate a new party to the participant node

    Args:
        party (str):
        body (UpdatePartyDetailsRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(party_details.identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | UpdatePartyDetailsResponse | str
    """

    return (
        await asyncio_detailed(
            party=party,
            client=client,
            body=body,
        )
    ).parsed
