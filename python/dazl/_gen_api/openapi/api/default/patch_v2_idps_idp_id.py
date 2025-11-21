# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.js_canton_error import JsCantonError
from ...models.update_identity_provider_config_request import (
    UpdateIdentityProviderConfigRequest,
)
from ...models.update_identity_provider_config_response import (
    UpdateIdentityProviderConfigResponse,
)
from ...types import Response


def _get_kwargs(
    idp_id: str,
    *,
    body: UpdateIdentityProviderConfigRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/idps/{idp_id}".format(
            idp_id=idp_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JsCantonError | UpdateIdentityProviderConfigResponse | str:
    if response.status_code == 200:
        response_200 = UpdateIdentityProviderConfigResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JsCantonError | UpdateIdentityProviderConfigResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    idp_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateIdentityProviderConfigRequest,
) -> Response[JsCantonError | UpdateIdentityProviderConfigResponse | str]:
    """Update identity provider config

    Args:
        idp_id (str):
        body (UpdateIdentityProviderConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | UpdateIdentityProviderConfigResponse | str]
    """

    kwargs = _get_kwargs(
        idp_id=idp_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    idp_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateIdentityProviderConfigRequest,
) -> JsCantonError | UpdateIdentityProviderConfigResponse | str | None:
    """Update identity provider config

    Args:
        idp_id (str):
        body (UpdateIdentityProviderConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | UpdateIdentityProviderConfigResponse | str
    """

    return sync_detailed(
        idp_id=idp_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    idp_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateIdentityProviderConfigRequest,
) -> Response[JsCantonError | UpdateIdentityProviderConfigResponse | str]:
    """Update identity provider config

    Args:
        idp_id (str):
        body (UpdateIdentityProviderConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | UpdateIdentityProviderConfigResponse | str]
    """

    kwargs = _get_kwargs(
        idp_id=idp_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    idp_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateIdentityProviderConfigRequest,
) -> JsCantonError | UpdateIdentityProviderConfigResponse | str | None:
    """Update identity provider config

    Args:
        idp_id (str):
        body (UpdateIdentityProviderConfigRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | UpdateIdentityProviderConfigResponse | str
    """

    return (
        await asyncio_detailed(
            idp_id=idp_id,
            client=client,
            body=body,
        )
    ).parsed
