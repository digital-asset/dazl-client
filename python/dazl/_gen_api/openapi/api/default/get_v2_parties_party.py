from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_parties_response import GetPartiesResponse
from ...models.js_canton_error import JsCantonError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    party: str,
    *,
    identity_provider_id: str | Unset = UNSET,
    parties: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["identity-provider-id"] = identity_provider_id

    json_parties: list[str] | Unset = UNSET
    if not isinstance(parties, Unset):
        json_parties = parties

    params["parties"] = json_parties

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/parties/{party}".format(
            party=party,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPartiesResponse | JsCantonError | str:
    if response.status_code == 200:
        response_200 = GetPartiesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPartiesResponse | JsCantonError | str]:
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
    identity_provider_id: str | Unset = UNSET,
    parties: list[str] | Unset = UNSET,
) -> Response[GetPartiesResponse | JsCantonError | str]:
    """Get party details

    Args:
        party (str):
        identity_provider_id (str | Unset):
        parties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPartiesResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        party=party,
        identity_provider_id=identity_provider_id,
        parties=parties,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    party: str,
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
    parties: list[str] | Unset = UNSET,
) -> GetPartiesResponse | JsCantonError | str | None:
    """Get party details

    Args:
        party (str):
        identity_provider_id (str | Unset):
        parties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPartiesResponse | JsCantonError | str
    """

    return sync_detailed(
        party=party,
        client=client,
        identity_provider_id=identity_provider_id,
        parties=parties,
    ).parsed


async def asyncio_detailed(
    party: str,
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
    parties: list[str] | Unset = UNSET,
) -> Response[GetPartiesResponse | JsCantonError | str]:
    """Get party details

    Args:
        party (str):
        identity_provider_id (str | Unset):
        parties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPartiesResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        party=party,
        identity_provider_id=identity_provider_id,
        parties=parties,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    party: str,
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
    parties: list[str] | Unset = UNSET,
) -> GetPartiesResponse | JsCantonError | str | None:
    """Get party details

    Args:
        party (str):
        identity_provider_id (str | Unset):
        parties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPartiesResponse | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            party=party,
            client=client,
            identity_provider_id=identity_provider_id,
            parties=parties,
        )
    ).parsed
