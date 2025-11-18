from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.js_canton_error import JsCantonError
from ...models.update_user_request import UpdateUserRequest
from ...models.update_user_response import UpdateUserResponse
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: UpdateUserRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/users/{user_id}".format(
            user_id=user_id,
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JsCantonError | UpdateUserResponse | str:
    if response.status_code == 200:
        response_200 = UpdateUserResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JsCantonError | UpdateUserResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateUserRequest,
) -> Response[JsCantonError | UpdateUserResponse | str]:
    """Update  user.

    Args:
        user_id (str):
        body (UpdateUserRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(user.identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | UpdateUserResponse | str]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateUserRequest,
) -> JsCantonError | UpdateUserResponse | str | None:
    """Update  user.

    Args:
        user_id (str):
        body (UpdateUserRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(user.identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | UpdateUserResponse | str
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateUserRequest,
) -> Response[JsCantonError | UpdateUserResponse | str]:
    """Update  user.

    Args:
        user_id (str):
        body (UpdateUserRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(user.identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | UpdateUserResponse | str]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateUserRequest,
) -> JsCantonError | UpdateUserResponse | str | None:
    """Update  user.

    Args:
        user_id (str):
        body (UpdateUserRequest): Required authorization: ``HasRight(ParticipantAdmin) OR
            IsAuthenticatedIdentityProviderAdmin(user.identity_provider_id)``

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | UpdateUserResponse | str
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
