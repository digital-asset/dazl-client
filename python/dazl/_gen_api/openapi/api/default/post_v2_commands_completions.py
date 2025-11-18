from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.completion_stream_request import CompletionStreamRequest
from ...models.js_canton_error import JsCantonError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CompletionStreamRequest,
    limit: int | Unset = UNSET,
    stream_idle_timeout_ms: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["stream_idle_timeout_ms"] = stream_idle_timeout_ms

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/commands/completions",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JsCantonError | str:
    if response.status_code == 400:
        response_400 = response.text
        return response_400

    response_default = JsCantonError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[JsCantonError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CompletionStreamRequest,
    limit: int | Unset = UNSET,
    stream_idle_timeout_ms: int | Unset = UNSET,
) -> Response[JsCantonError | str]:
    """Query completions list (blocking call)
    Notice: This endpoint should be used for small results set.
    When number of results exceeded node configuration limit (`http-list-max-elements-limit`)
    there will be an error (`413 Content Too Large`) returned.
    Increasing this limit may lead to performance issues and high memory consumption.
    Consider using websockets (asyncapi) for better efficiency with larger results.

    Args:
        limit (int | Unset):
        stream_idle_timeout_ms (int | Unset):
        body (CompletionStreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | str]
    """

    kwargs = _get_kwargs(
        body=body,
        limit=limit,
        stream_idle_timeout_ms=stream_idle_timeout_ms,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CompletionStreamRequest,
    limit: int | Unset = UNSET,
    stream_idle_timeout_ms: int | Unset = UNSET,
) -> JsCantonError | str | None:
    """Query completions list (blocking call)
    Notice: This endpoint should be used for small results set.
    When number of results exceeded node configuration limit (`http-list-max-elements-limit`)
    there will be an error (`413 Content Too Large`) returned.
    Increasing this limit may lead to performance issues and high memory consumption.
    Consider using websockets (asyncapi) for better efficiency with larger results.

    Args:
        limit (int | Unset):
        stream_idle_timeout_ms (int | Unset):
        body (CompletionStreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | str
    """

    return sync_detailed(
        client=client,
        body=body,
        limit=limit,
        stream_idle_timeout_ms=stream_idle_timeout_ms,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CompletionStreamRequest,
    limit: int | Unset = UNSET,
    stream_idle_timeout_ms: int | Unset = UNSET,
) -> Response[JsCantonError | str]:
    """Query completions list (blocking call)
    Notice: This endpoint should be used for small results set.
    When number of results exceeded node configuration limit (`http-list-max-elements-limit`)
    there will be an error (`413 Content Too Large`) returned.
    Increasing this limit may lead to performance issues and high memory consumption.
    Consider using websockets (asyncapi) for better efficiency with larger results.

    Args:
        limit (int | Unset):
        stream_idle_timeout_ms (int | Unset):
        body (CompletionStreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsCantonError | str]
    """

    kwargs = _get_kwargs(
        body=body,
        limit=limit,
        stream_idle_timeout_ms=stream_idle_timeout_ms,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CompletionStreamRequest,
    limit: int | Unset = UNSET,
    stream_idle_timeout_ms: int | Unset = UNSET,
) -> JsCantonError | str | None:
    """Query completions list (blocking call)
    Notice: This endpoint should be used for small results set.
    When number of results exceeded node configuration limit (`http-list-max-elements-limit`)
    there will be an error (`413 Content Too Large`) returned.
    Increasing this limit may lead to performance issues and high memory consumption.
    Consider using websockets (asyncapi) for better efficiency with larger results.

    Args:
        limit (int | Unset):
        stream_idle_timeout_ms (int | Unset):
        body (CompletionStreamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsCantonError | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            limit=limit,
            stream_idle_timeout_ms=stream_idle_timeout_ms,
        )
    ).parsed
