# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, AsyncIterable, Callable, Iterable, Tuple, TypeVar, Union, cast
from urllib.parse import urlparse

from grpc import (
    AuthMetadataContext,
    AuthMetadataPlugin,
    AuthMetadataPluginCallback,
    ChannelCredentials,
    composite_channel_credentials,
    metadata_call_credentials,
    ssl_channel_credentials,
)
from grpc.aio import (
    Channel,
    ClientCallDetails,
    ClientInterceptor,
    StreamStreamCall,
    StreamStreamClientInterceptor,
    StreamUnaryCall,
    StreamUnaryClientInterceptor,
    UnaryStreamCall,
    UnaryStreamClientInterceptor,
    UnaryUnaryCall,
    UnaryUnaryClientInterceptor,
    insecure_channel,
    secure_channel,
)

from ..config import Config

__all__ = ["create_channel"]

RequestType = TypeVar("RequestType")
RequestIterableType = Union[Iterable[Any], AsyncIterable[Any]]
ResponseIterableType = AsyncIterable[Any]


def create_channel(config: Config) -> Channel:
    """
    Create a :class:`Channel` for the specified configuration.
    """
    u = urlparse(config.url.url)

    options = [
        ("grpc.max_send_message_length", -1),
        ("grpc.max_receive_message_length", -1),
    ]
    if not config.url.use_http_proxy:
        options.append(("grpc.enable_http_proxy", 0))

    if (u.scheme in ("https", "grpcs")) or config.ssl:
        if config.ssl.ca is None and config.ssl.cert is not None:
            credentials = ssl_channel_credentials(root_certificates=config.ssl.cert)
        else:
            credentials = ssl_channel_credentials(
                root_certificates=config.ssl.ca,
                private_key=config.ssl.cert_key,
                certificate_chain=config.ssl.cert,
            )
        if config.access.token_version is not None:
            # The grpc Credential objects do not actually define a formal interface, and are
            # used interchangeably in the code.
            #
            # Additionally there are some incorrect rules in the grpc-stubs typing rules that force
            # us to work around the type system.
            credentials = cast(
                ChannelCredentials,
                composite_channel_credentials(
                    credentials, metadata_call_credentials(GrpcAuth(config), name="auth gateway")
                ),
            )
        return secure_channel(u.netloc, credentials, tuple(options))

    elif config.access.token_version is not None:
        # Python/C++ libraries refuse to allow "credentials" objects to be passed around on
        # non-TLS channels, but they don't check interceptors; use an interceptor to inject
        # an Authorization header instead
        #
        # There must be a distinct interceptor instance for each of
        # the four Request/Response arities. There is a known issue in
        # the underlying gRPC code that prevents reuse of a single
        # multiply-inherited interceptor.
        #
        # https://github.com/grpc/grpc/issues/31442
        return insecure_channel(
            u.netloc,
            options,
            interceptors=[
                cast(ClientInterceptor, GrpcAuthUnaryUnaryClientInterceptor(config)),
                cast(ClientInterceptor, GrpcAuthUnaryStreamClientInterceptor(config)),
                cast(ClientInterceptor, GrpcAuthStreamUnaryClientInterceptor(config)),
                cast(ClientInterceptor, GrpcAuthStreamStreamClientInterceptor(config)),
            ],
        )  # type: ignore

    else:
        # no TLS, no tokens--simply create an insecure channel with no adornments
        return insecure_channel(u.netloc, options)


class GrpcAuth(AuthMetadataPlugin):
    def __init__(self, config: Config):
        self._config = config

    def __call__(self, context: AuthMetadataContext, callback: AuthMetadataPluginCallback):
        # This overly verbose type signature is here to satisfy mypy and grpc-stubs
        options = list[Tuple[str, Union[str, bytes]]]()

        # TODO: Add support here for refresh tokens
        token = self._config.access.token
        if token:
            # note: gRPC headers MUST be lowercased
            options.append(("authorization", "Bearer " + self._config.access.token))

        callback(tuple(options), None)


class GrpcAuthInterceptor:
    """
    An interceptor that injects "Authorization" metadata into a request.

    This works around the fact that the C++ gRPC libraries (which Python is built on) highly
    discourage sending authorization data over the wire unless the connection is protected with TLS.
    """

    # NOTE: There are a number of typing errors in the grpc.aio classes, so we're ignoring a handful
    #  of lines until those problems are addressed.

    def __init__(self, config: Config):
        self._config = config

    def _modify_client_call_details(self, client_call_details: ClientCallDetails):
        if (
            client_call_details.metadata is not None
            and "authorization" not in client_call_details.metadata
            and self._config.access.token_version is not None
        ):
            client_call_details.metadata.add("authorization", f"Bearer {self._config.access.token}")

        return client_call_details


class GrpcAuthUnaryUnaryClientInterceptor(GrpcAuthInterceptor, UnaryUnaryClientInterceptor):
    async def intercept_unary_unary(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], UnaryUnaryCall],
        client_call_details: ClientCallDetails,
        request: RequestType,
    ) -> Union[UnaryUnaryCall, RequestType]:
        return await continuation(self._modify_client_call_details(client_call_details), request)


class GrpcAuthUnaryStreamClientInterceptor(GrpcAuthInterceptor, UnaryStreamClientInterceptor):
    async def intercept_unary_stream(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], UnaryStreamCall],
        client_call_details: ClientCallDetails,
        request: RequestType,
    ) -> Union[ResponseIterableType, UnaryStreamCall]:
        return await continuation(  # type: ignore
            self._modify_client_call_details(client_call_details), request
        )


class GrpcAuthStreamUnaryClientInterceptor(GrpcAuthInterceptor, StreamUnaryClientInterceptor):
    async def intercept_stream_unary(  # type: ignore
        self,
        continuation: Callable[[ClientCallDetails, RequestType], StreamUnaryCall],
        client_call_details: ClientCallDetails,
        request_iterator: RequestIterableType,
    ) -> StreamUnaryCall:
        return await continuation(
            self._modify_client_call_details(client_call_details), request_iterator  # type: ignore
        )


class GrpcAuthStreamStreamClientInterceptor(GrpcAuthInterceptor, StreamStreamClientInterceptor):
    async def intercept_stream_stream(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], StreamStreamCall],
        client_call_details: ClientCallDetails,
        request_iterator: RequestIterableType,
    ) -> Union[ResponseIterableType, StreamStreamCall]:
        return await continuation(  # type: ignore
            self._modify_client_call_details(client_call_details), request_iterator  # type: ignore
        )
