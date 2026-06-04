# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_contract_request import GetContractRequest
from ...models.get_contract_response import GetContractResponse
from ...models.js_canton_error import JsCantonError
from ...types import Response


def _get_kwargs(
    *,
    body: GetContractRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/contracts/contract-by-id",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetContractResponse | JsCantonError | str:
    if response.status_code == 200:
        response_200 = GetContractResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetContractResponse | JsCantonError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GetContractRequest,
) -> Response[GetContractResponse | JsCantonError | str]:
    """Looking up contract data by contract ID.
    This endpoint is experimental / alpha, therefore no backwards compatibility is guaranteed.
    This endpoint must not be used to look up contracts which entered the participant via party
    replication
    or repair service.

    Args:
        body (GetContractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetContractResponse | JsCantonError | str]
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
    body: GetContractRequest,
) -> GetContractResponse | JsCantonError | str | None:
    """Looking up contract data by contract ID.
    This endpoint is experimental / alpha, therefore no backwards compatibility is guaranteed.
    This endpoint must not be used to look up contracts which entered the participant via party
    replication
    or repair service.

    Args:
        body (GetContractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetContractResponse | JsCantonError | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GetContractRequest,
) -> Response[GetContractResponse | JsCantonError | str]:
    """Looking up contract data by contract ID.
    This endpoint is experimental / alpha, therefore no backwards compatibility is guaranteed.
    This endpoint must not be used to look up contracts which entered the participant via party
    replication
    or repair service.

    Args:
        body (GetContractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetContractResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GetContractRequest,
) -> GetContractResponse | JsCantonError | str | None:
    """Looking up contract data by contract ID.
    This endpoint is experimental / alpha, therefore no backwards compatibility is guaranteed.
    This endpoint must not be used to look up contracts which entered the participant via party
    replication
    or repair service.

    Args:
        body (GetContractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetContractResponse | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
