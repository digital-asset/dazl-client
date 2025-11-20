from __future__ import annotations

from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.js_canton_error import JsCantonError
from ...models.upload_dar_file_response import UploadDarFileResponse
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    body: File,
    vet_all_packages: bool | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["vetAllPackages"] = vet_all_packages

    params["synchronizerId"] = synchronizer_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/packages",
        "params": params,
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JsCantonError | UploadDarFileResponse | str:
    if response.status_code == 200:
        response_200 = UploadDarFileResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JsCantonError | UploadDarFileResponse | str]:
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
    vet_all_packages: bool | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> Response[JsCantonError | UploadDarFileResponse | str]:
    """Upload a DAR to the participant node

    Args:
        vet_all_packages (bool | Unset):
        synchronizer_id (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | UploadDarFileResponse | str]
    """

    kwargs = _get_kwargs(
        body=body,
        vet_all_packages=vet_all_packages,
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
    vet_all_packages: bool | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> JsCantonError | UploadDarFileResponse | str | None:
    """Upload a DAR to the participant node

    Args:
        vet_all_packages (bool | Unset):
        synchronizer_id (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | UploadDarFileResponse | str
    """

    return sync_detailed(
        client=client,
        body=body,
        vet_all_packages=vet_all_packages,
        synchronizer_id=synchronizer_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: File,
    vet_all_packages: bool | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> Response[JsCantonError | UploadDarFileResponse | str]:
    """Upload a DAR to the participant node

    Args:
        vet_all_packages (bool | Unset):
        synchronizer_id (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | UploadDarFileResponse | str]
    """

    kwargs = _get_kwargs(
        body=body,
        vet_all_packages=vet_all_packages,
        synchronizer_id=synchronizer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: File,
    vet_all_packages: bool | Unset = UNSET,
    synchronizer_id: str | Unset = UNSET,
) -> JsCantonError | UploadDarFileResponse | str | None:
    """Upload a DAR to the participant node

    Args:
        vet_all_packages (bool | Unset):
        synchronizer_id (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | UploadDarFileResponse | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            vet_all_packages=vet_all_packages,
            synchronizer_id=synchronizer_id,
        )
    ).parsed
