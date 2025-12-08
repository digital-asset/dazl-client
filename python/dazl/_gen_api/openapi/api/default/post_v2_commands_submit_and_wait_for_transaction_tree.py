# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.js_canton_error import JsCantonError
from ...models.js_commands import JsCommands
from ...models.js_submit_and_wait_for_transaction_tree_response import (
    JsSubmitAndWaitForTransactionTreeResponse,
)
from ...types import Response


def _get_kwargs(
    *,
    body: JsCommands,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/commands/submit-and-wait-for-transaction-tree",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str:
    if response.status_code == 200:
        response_200 = JsSubmitAndWaitForTransactionTreeResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: JsCommands,
) -> Response[JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str]:
    """Submit a batch of commands and wait for the transaction trees response. Provided for backwards
    compatibility, it will be removed in the Canton version 3.5.0, use submit-and-wait-for-transaction
    instead.

    Args:
        body (JsCommands): A composite command that groups multiple commands together.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str]
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
    body: JsCommands,
) -> JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str | None:
    """Submit a batch of commands and wait for the transaction trees response. Provided for backwards
    compatibility, it will be removed in the Canton version 3.5.0, use submit-and-wait-for-transaction
    instead.

    Args:
        body (JsCommands): A composite command that groups multiple commands together.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: JsCommands,
) -> Response[JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str]:
    """Submit a batch of commands and wait for the transaction trees response. Provided for backwards
    compatibility, it will be removed in the Canton version 3.5.0, use submit-and-wait-for-transaction
    instead.

    Args:
        body (JsCommands): A composite command that groups multiple commands together.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: JsCommands,
) -> JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str | None:
    """Submit a batch of commands and wait for the transaction trees response. Provided for backwards
    compatibility, it will be removed in the Canton version 3.5.0, use submit-and-wait-for-transaction
    instead.

    Args:
        body (JsCommands): A composite command that groups multiple commands together.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | JsSubmitAndWaitForTransactionTreeResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
