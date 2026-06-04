# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.js_canton_error import JsCantonError
from ...models.list_known_parties_response import ListKnownPartiesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identity_provider_id: str | Unset = UNSET,
    filter_party: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["identity-provider-id"] = identity_provider_id

    params["filter-party"] = filter_party

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/parties",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JsCantonError | ListKnownPartiesResponse | str:
    if response.status_code == 200:
        response_200 = ListKnownPartiesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JsCantonError | ListKnownPartiesResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
    filter_party: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[JsCantonError | ListKnownPartiesResponse | str]:
    """List the parties known by the participant.
    The list returned contains parties whose ledger access is facilitated by
    the participant and the ones maintained elsewhere.

    Args:
        identity_provider_id (str | Unset):
        filter_party (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | ListKnownPartiesResponse | str]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
        filter_party=filter_party,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
    filter_party: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> JsCantonError | ListKnownPartiesResponse | str | None:
    """List the parties known by the participant.
    The list returned contains parties whose ledger access is facilitated by
    the participant and the ones maintained elsewhere.

    Args:
        identity_provider_id (str | Unset):
        filter_party (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | ListKnownPartiesResponse | str
    """

    return sync_detailed(
        client=client,
        identity_provider_id=identity_provider_id,
        filter_party=filter_party,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
    filter_party: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[JsCantonError | ListKnownPartiesResponse | str]:
    """List the parties known by the participant.
    The list returned contains parties whose ledger access is facilitated by
    the participant and the ones maintained elsewhere.

    Args:
        identity_provider_id (str | Unset):
        filter_party (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | ListKnownPartiesResponse | str]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
        filter_party=filter_party,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    identity_provider_id: str | Unset = UNSET,
    filter_party: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> JsCantonError | ListKnownPartiesResponse | str | None:
    """List the parties known by the participant.
    The list returned contains parties whose ledger access is facilitated by
    the participant and the ones maintained elsewhere.

    Args:
        identity_provider_id (str | Unset):
        filter_party (str | Unset):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | ListKnownPartiesResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            identity_provider_id=identity_provider_id,
            filter_party=filter_party,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
