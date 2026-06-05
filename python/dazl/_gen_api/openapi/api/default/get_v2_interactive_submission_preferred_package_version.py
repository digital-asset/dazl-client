# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_preferred_package_version_response import GetPreferredPackageVersionResponse
from ...models.js_canton_error import JsCantonError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parties: list[str] | Unset = UNSET,
    package_name: str,
    vetting_valid_at: datetime.datetime | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_parties: list[str] | Unset = UNSET
    if not isinstance(parties, Unset):
        json_parties = parties

    params["parties"] = json_parties

    params["package-name"] = package_name

    json_vetting_valid_at: str | Unset = UNSET
    if not isinstance(vetting_valid_at, Unset):
        json_vetting_valid_at = vetting_valid_at.isoformat()
    params["vetting_valid_at"] = json_vetting_valid_at

    params["synchronizer-id"] = synchronizer_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/interactive-submission/preferred-package-version",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPreferredPackageVersionResponse | JsCantonError | str:
    if response.status_code == 200:
        response_200 = GetPreferredPackageVersionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    try:
        response_default = JsCantonError.from_dict(response.json())
    except (KeyError, ValueError):
        return response.text

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPreferredPackageVersionResponse | JsCantonError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    parties: list[str] | Unset = UNSET,
    package_name: str,
    vetting_valid_at: datetime.datetime | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> Response[GetPreferredPackageVersionResponse | JsCantonError | str]:
    """A preferred package is the highest-versioned package for a provided package-name
    that is vetted by all the participants hosting the provided parties.

    Ledger API clients should use this endpoint for constructing command submissions
    that are compatible with the provided preferred package, by making informed decisions on:
    - which are the compatible packages that can be used to create contracts
    - which contract or exercise choice argument version can be used in the command
    - which choices can be executed on a template or interface of a contract

    Can be accessed by any Ledger API client with a valid token when Ledger API authorization is
    enabled.

    Provided for backwards compatibility, it will be removed in the Canton version 3.4.0

    Args:
        parties (list[str] | Unset):
        package_name (str):
        vetting_valid_at (datetime.datetime | Unset):
        synchronizer_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPreferredPackageVersionResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        parties=parties,
        package_name=package_name,
        vetting_valid_at=vetting_valid_at,
        synchronizer_id=synchronizer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    parties: list[str] | Unset = UNSET,
    package_name: str,
    vetting_valid_at: datetime.datetime | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> GetPreferredPackageVersionResponse | JsCantonError | str | None:
    """A preferred package is the highest-versioned package for a provided package-name
    that is vetted by all the participants hosting the provided parties.

    Ledger API clients should use this endpoint for constructing command submissions
    that are compatible with the provided preferred package, by making informed decisions on:
    - which are the compatible packages that can be used to create contracts
    - which contract or exercise choice argument version can be used in the command
    - which choices can be executed on a template or interface of a contract

    Can be accessed by any Ledger API client with a valid token when Ledger API authorization is
    enabled.

    Provided for backwards compatibility, it will be removed in the Canton version 3.4.0

    Args:
        parties (list[str] | Unset):
        package_name (str):
        vetting_valid_at (datetime.datetime | Unset):
        synchronizer_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPreferredPackageVersionResponse | JsCantonError | str
    """

    return sync_detailed(
        client=client,
        parties=parties,
        package_name=package_name,
        vetting_valid_at=vetting_valid_at,
        synchronizer_id=synchronizer_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    parties: list[str] | Unset = UNSET,
    package_name: str,
    vetting_valid_at: datetime.datetime | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> Response[GetPreferredPackageVersionResponse | JsCantonError | str]:
    """A preferred package is the highest-versioned package for a provided package-name
    that is vetted by all the participants hosting the provided parties.

    Ledger API clients should use this endpoint for constructing command submissions
    that are compatible with the provided preferred package, by making informed decisions on:
    - which are the compatible packages that can be used to create contracts
    - which contract or exercise choice argument version can be used in the command
    - which choices can be executed on a template or interface of a contract

    Can be accessed by any Ledger API client with a valid token when Ledger API authorization is
    enabled.

    Provided for backwards compatibility, it will be removed in the Canton version 3.4.0

    Args:
        parties (list[str] | Unset):
        package_name (str):
        vetting_valid_at (datetime.datetime | Unset):
        synchronizer_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPreferredPackageVersionResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        parties=parties,
        package_name=package_name,
        vetting_valid_at=vetting_valid_at,
        synchronizer_id=synchronizer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    parties: list[str] | Unset = UNSET,
    package_name: str,
    vetting_valid_at: datetime.datetime | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> GetPreferredPackageVersionResponse | JsCantonError | str | None:
    """A preferred package is the highest-versioned package for a provided package-name
    that is vetted by all the participants hosting the provided parties.

    Ledger API clients should use this endpoint for constructing command submissions
    that are compatible with the provided preferred package, by making informed decisions on:
    - which are the compatible packages that can be used to create contracts
    - which contract or exercise choice argument version can be used in the command
    - which choices can be executed on a template or interface of a contract

    Can be accessed by any Ledger API client with a valid token when Ledger API authorization is
    enabled.

    Provided for backwards compatibility, it will be removed in the Canton version 3.4.0

    Args:
        parties (list[str] | Unset):
        package_name (str):
        vetting_valid_at (datetime.datetime | Unset):
        synchronizer_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPreferredPackageVersionResponse | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            parties=parties,
            package_name=package_name,
            vetting_valid_at=vetting_valid_at,
            synchronizer_id=synchronizer_id,
        )
    ).parsed
