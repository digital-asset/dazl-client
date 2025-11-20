from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.js_canton_error import JsCantonError
from ...models.js_get_transaction_tree_response import JsGetTransactionTreeResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    update_id: str,
    *,
    parties: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_parties: list[str] | Unset = UNSET
    if not isinstance(parties, Unset):
        json_parties = parties

    params["parties"] = json_parties

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/updates/transaction-tree-by-id/{update_id}".format(
            update_id=update_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JsCantonError | JsGetTransactionTreeResponse | str:
    if response.status_code == 200:
        response_200 = JsGetTransactionTreeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JsCantonError | JsGetTransactionTreeResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    update_id: str,
    *,
    client: AuthenticatedClient,
    parties: list[str] | Unset = UNSET,
) -> Response[JsCantonError | JsGetTransactionTreeResponse | str]:
    """Get transaction tree by id. Provided for backwards compatibility, it will be removed in the Canton
    version 3.5.0, use v2/updates/update-by-id instead.

    Args:
        update_id (str):
        parties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | JsGetTransactionTreeResponse | str]
    """

    kwargs = _get_kwargs(
        update_id=update_id,
        parties=parties,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    update_id: str,
    *,
    client: AuthenticatedClient,
    parties: list[str] | Unset = UNSET,
) -> JsCantonError | JsGetTransactionTreeResponse | str | None:
    """Get transaction tree by id. Provided for backwards compatibility, it will be removed in the Canton
    version 3.5.0, use v2/updates/update-by-id instead.

    Args:
        update_id (str):
        parties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | JsGetTransactionTreeResponse | str
    """

    return sync_detailed(
        update_id=update_id,
        client=client,
        parties=parties,
    ).parsed


async def asyncio_detailed(
    update_id: str,
    *,
    client: AuthenticatedClient,
    parties: list[str] | Unset = UNSET,
) -> Response[JsCantonError | JsGetTransactionTreeResponse | str]:
    """Get transaction tree by id. Provided for backwards compatibility, it will be removed in the Canton
    version 3.5.0, use v2/updates/update-by-id instead.

    Args:
        update_id (str):
        parties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | JsGetTransactionTreeResponse | str]
    """

    kwargs = _get_kwargs(
        update_id=update_id,
        parties=parties,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    update_id: str,
    *,
    client: AuthenticatedClient,
    parties: list[str] | Unset = UNSET,
) -> JsCantonError | JsGetTransactionTreeResponse | str | None:
    """Get transaction tree by id. Provided for backwards compatibility, it will be removed in the Canton
    version 3.5.0, use v2/updates/update-by-id instead.

    Args:
        update_id (str):
        parties (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | JsGetTransactionTreeResponse | str
    """

    return (
        await asyncio_detailed(
            update_id=update_id,
            client=client,
            parties=parties,
        )
    ).parsed
