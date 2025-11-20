from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_connected_synchronizers_response import GetConnectedSynchronizersResponse
from ...models.js_canton_error import JsCantonError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    party: str | Unset = UNSET,
    participant_id: str | Unset = UNSET,
    identity_provider_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["party"] = party

    params["participantId"] = participant_id

    params["identityProviderId"] = identity_provider_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/state/connected-synchronizers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetConnectedSynchronizersResponse | JsCantonError | str:
    if response.status_code == 200:
        response_200 = GetConnectedSynchronizersResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetConnectedSynchronizersResponse | JsCantonError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    party: str | Unset = UNSET,
    participant_id: str | Unset = UNSET,
    identity_provider_id: str | Unset = UNSET,
) -> Response[GetConnectedSynchronizersResponse | JsCantonError | str]:
    """Get connected synchronizers

    Args:
        party (str | Unset):
        participant_id (str | Unset):
        identity_provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConnectedSynchronizersResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        party=party,
        participant_id=participant_id,
        identity_provider_id=identity_provider_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    party: str | Unset = UNSET,
    participant_id: str | Unset = UNSET,
    identity_provider_id: str | Unset = UNSET,
) -> GetConnectedSynchronizersResponse | JsCantonError | str | None:
    """Get connected synchronizers

    Args:
        party (str | Unset):
        participant_id (str | Unset):
        identity_provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConnectedSynchronizersResponse | JsCantonError | str
    """

    return sync_detailed(
        client=client,
        party=party,
        participant_id=participant_id,
        identity_provider_id=identity_provider_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    party: str | Unset = UNSET,
    participant_id: str | Unset = UNSET,
    identity_provider_id: str | Unset = UNSET,
) -> Response[GetConnectedSynchronizersResponse | JsCantonError | str]:
    """Get connected synchronizers

    Args:
        party (str | Unset):
        participant_id (str | Unset):
        identity_provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConnectedSynchronizersResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        party=party,
        participant_id=participant_id,
        identity_provider_id=identity_provider_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    party: str | Unset = UNSET,
    participant_id: str | Unset = UNSET,
    identity_provider_id: str | Unset = UNSET,
) -> GetConnectedSynchronizersResponse | JsCantonError | str | None:
    """Get connected synchronizers

    Args:
        party (str | Unset):
        participant_id (str | Unset):
        identity_provider_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConnectedSynchronizersResponse | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            party=party,
            participant_id=participant_id,
            identity_provider_id=identity_provider_id,
        )
    ).parsed
