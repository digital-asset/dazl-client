from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_identity_provider_config_response import (
    DeleteIdentityProviderConfigResponse,
)
from ...models.js_canton_error import JsCantonError
from ...types import Response


def _get_kwargs(
    idp_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v2/idps/{idp_id}".format(
            idp_id=idp_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteIdentityProviderConfigResponse | JsCantonError | str:
    if response.status_code == 200:
        response_200 = DeleteIdentityProviderConfigResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteIdentityProviderConfigResponse | JsCantonError | str]:
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
) -> Response[DeleteIdentityProviderConfigResponse | JsCantonError | str]:
    """Delete identity provider config

    Args:
        idp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteIdentityProviderConfigResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        idp_id=idp_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    idp_id: str,
    *,
    client: AuthenticatedClient,
) -> DeleteIdentityProviderConfigResponse | JsCantonError | str | None:
    """Delete identity provider config

    Args:
        idp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteIdentityProviderConfigResponse | JsCantonError | str
    """

    return sync_detailed(
        idp_id=idp_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    idp_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteIdentityProviderConfigResponse | JsCantonError | str]:
    """Delete identity provider config

    Args:
        idp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteIdentityProviderConfigResponse | JsCantonError | str]
    """

    kwargs = _get_kwargs(
        idp_id=idp_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    idp_id: str,
    *,
    client: AuthenticatedClient,
) -> DeleteIdentityProviderConfigResponse | JsCantonError | str | None:
    """Delete identity provider config

    Args:
        idp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteIdentityProviderConfigResponse | JsCantonError | str
    """

    return (
        await asyncio_detailed(
            idp_id=idp_id,
            client=client,
        )
    ).parsed
