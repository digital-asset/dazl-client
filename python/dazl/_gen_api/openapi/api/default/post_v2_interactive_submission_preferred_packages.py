# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_preferred_packages_request import GetPreferredPackagesRequest
from ...models.get_preferred_packages_response import GetPreferredPackagesResponse
from ...models.js_canton_error import JsCantonError
from ...types import Response


def _get_kwargs(
    *,
    body: GetPreferredPackagesRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/interactive-submission/preferred-packages",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPreferredPackagesResponse | JsCantonError | str:
    if response.status_code == 200:
        response_200 = GetPreferredPackagesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPreferredPackagesResponse | JsCantonError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GetPreferredPackagesRequest,
) -> Response[GetPreferredPackagesResponse | JsCantonError | str]:
    """Compute the preferred packages for the vetting requirements in the request.
    A preferred package is the highest-versioned package for a provided package-name
    that is vetted by all the participants hosting the provided parties.

    Ledger API clients should use this endpoint for constructing command submissions
    that are compatible with the provided preferred packages, by making informed decisions on:
    - which are the compatible packages that can be used to create contracts
    - which contract or exercise choice argument version can be used in the command
    - which choices can be executed on a template or interface of a contract

    If the package preferences could not be computed due to no selection satisfying the requirements,
    a `FAILED_PRECONDITION` error will be returned.

    Can be accessed by any Ledger API client with a valid token when Ledger API authorization is
    enabled.

    Experimental API: this endpoint is not guaranteed to provide backwards compatibility in future
    releases

    Args:
        body (GetPreferredPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPreferredPackagesResponse | JsCantonError | str]
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
    body: GetPreferredPackagesRequest,
) -> GetPreferredPackagesResponse | JsCantonError | str | None:
    """Compute the preferred packages for the vetting requirements in the request.
    A preferred package is the highest-versioned package for a provided package-name
    that is vetted by all the participants hosting the provided parties.

    Ledger API clients should use this endpoint for constructing command submissions
    that are compatible with the provided preferred packages, by making informed decisions on:
    - which are the compatible packages that can be used to create contracts
    - which contract or exercise choice argument version can be used in the command
    - which choices can be executed on a template or interface of a contract

    If the package preferences could not be computed due to no selection satisfying the requirements,
    a `FAILED_PRECONDITION` error will be returned.

    Can be accessed by any Ledger API client with a valid token when Ledger API authorization is
    enabled.

    Experimental API: this endpoint is not guaranteed to provide backwards compatibility in future
    releases

    Args:
        body (GetPreferredPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPreferredPackagesResponse | JsCantonError | str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GetPreferredPackagesRequest,
) -> Response[GetPreferredPackagesResponse | JsCantonError | str]:
    """Compute the preferred packages for the vetting requirements in the request.
    A preferred package is the highest-versioned package for a provided package-name
    that is vetted by all the participants hosting the provided parties.

    Ledger API clients should use this endpoint for constructing command submissions
    that are compatible with the provided preferred packages, by making informed decisions on:
    - which are the compatible packages that can be used to create contracts
    - which contract or exercise choice argument version can be used in the command
    - which choices can be executed on a template or interface of a contract

    If the package preferences could not be computed due to no selection satisfying the requirements,
    a `FAILED_PRECONDITION` error will be returned.

    Can be accessed by any Ledger API client with a valid token when Ledger API authorization is
    enabled.

    Experimental API: this endpoint is not guaranteed to provide backwards compatibility in future
    releases

    Args:
        body (GetPreferredPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPreferredPackagesResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GetPreferredPackagesRequest,
) -> GetPreferredPackagesResponse | JsCantonError | str | None:
    """Compute the preferred packages for the vetting requirements in the request.
    A preferred package is the highest-versioned package for a provided package-name
    that is vetted by all the participants hosting the provided parties.

    Ledger API clients should use this endpoint for constructing command submissions
    that are compatible with the provided preferred packages, by making informed decisions on:
    - which are the compatible packages that can be used to create contracts
    - which contract or exercise choice argument version can be used in the command
    - which choices can be executed on a template or interface of a contract

    If the package preferences could not be computed due to no selection satisfying the requirements,
    a `FAILED_PRECONDITION` error will be returned.

    Can be accessed by any Ledger API client with a valid token when Ledger API authorization is
    enabled.

    Experimental API: this endpoint is not guaranteed to provide backwards compatibility in future
    releases

    Args:
        body (GetPreferredPackagesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPreferredPackagesResponse | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
