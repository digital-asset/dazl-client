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
from ...models.list_vetted_packages_request import ListVettedPackagesRequest
from ...models.list_vetted_packages_response import ListVettedPackagesResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ListVettedPackagesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/package-vetting/list",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JsCantonError | ListVettedPackagesResponse | str:
    if response.status_code == 200:
        response_200 = ListVettedPackagesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JsCantonError | ListVettedPackagesResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ListVettedPackagesRequest,
) -> Response[JsCantonError | ListVettedPackagesResponse | str]:
    """Lists which participant node vetted what packages on which synchronizer.
    Can be called by any authenticated user.

    Args:
        body (ListVettedPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | ListVettedPackagesResponse | str]
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
    body: ListVettedPackagesRequest,
) -> JsCantonError | ListVettedPackagesResponse | str | None:
    """Lists which participant node vetted what packages on which synchronizer.
    Can be called by any authenticated user.

    Args:
        body (ListVettedPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | ListVettedPackagesResponse | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ListVettedPackagesRequest,
) -> Response[JsCantonError | ListVettedPackagesResponse | str]:
    """Lists which participant node vetted what packages on which synchronizer.
    Can be called by any authenticated user.

    Args:
        body (ListVettedPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | ListVettedPackagesResponse | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ListVettedPackagesRequest,
) -> JsCantonError | ListVettedPackagesResponse | str | None:
    """Lists which participant node vetted what packages on which synchronizer.
    Can be called by any authenticated user.

    Args:
        body (ListVettedPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | ListVettedPackagesResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
