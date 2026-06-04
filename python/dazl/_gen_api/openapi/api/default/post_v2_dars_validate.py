# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from __future__ import annotations

from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.js_canton_error import JsCantonError
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    body: File,
    synchronizer_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["synchronizerId"] = synchronizer_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/dars/validate",
        "params": params,
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | JsCantonError | str:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | JsCantonError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: File,
    synchronizer_id: str | Unset = UNSET,
) -> Response[Any | JsCantonError | str]:
    """Validates the DAR and checks the upgrade compatibility of the DAR's packages
    with the set of the already vetted packages on the target vetting synchronizer.
    See ValidateDarFileRequest for details regarding the target vetting synchronizer.

    The operation has no effect on the state of the participant or the Canton ledger:
    the DAR payload and its packages are not persisted neither are the packages vetted.

    Args:
        synchronizer_id (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        body=body,
        synchronizer_id=synchronizer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: File,
    synchronizer_id: str | Unset = UNSET,
) -> Any | JsCantonError | str | None:
    """Validates the DAR and checks the upgrade compatibility of the DAR's packages
    with the set of the already vetted packages on the target vetting synchronizer.
    See ValidateDarFileRequest for details regarding the target vetting synchronizer.

    The operation has no effect on the state of the participant or the Canton ledger:
    the DAR payload and its packages are not persisted neither are the packages vetted.

    Args:
        synchronizer_id (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JsCantonError | str
    """

    return sync_detailed(
        client=client,
        body=body,
        synchronizer_id=synchronizer_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: File,
    synchronizer_id: str | Unset = UNSET,
) -> Response[Any | JsCantonError | str]:
    """Validates the DAR and checks the upgrade compatibility of the DAR's packages
    with the set of the already vetted packages on the target vetting synchronizer.
    See ValidateDarFileRequest for details regarding the target vetting synchronizer.

    The operation has no effect on the state of the participant or the Canton ledger:
    the DAR payload and its packages are not persisted neither are the packages vetted.

    Args:
        synchronizer_id (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        body=body,
        synchronizer_id=synchronizer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: File,
    synchronizer_id: str | Unset = UNSET,
) -> Any | JsCantonError | str | None:
    """Validates the DAR and checks the upgrade compatibility of the DAR's packages
    with the set of the already vetted packages on the target vetting synchronizer.
    See ValidateDarFileRequest for details regarding the target vetting synchronizer.

    The operation has no effect on the state of the participant or the Canton ledger:
    the DAR payload and its packages are not persisted neither are the packages vetted.

    Args:
        synchronizer_id (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            synchronizer_id=synchronizer_id,
        )
    ).parsed
