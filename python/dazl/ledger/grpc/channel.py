# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
from typing import List, Tuple, Union, cast, overload
from urllib.parse import urlparse

from grpc import (
    AuthMetadataContext,
    AuthMetadataPlugin,
    AuthMetadataPluginCallback,
    Channel,
    ChannelCredentials,
    composite_channel_credentials,
    insecure_channel,
    metadata_call_credentials,
    secure_channel,
    ssl_channel_credentials,
)
from grpc.aio import (
    Channel as AioChannel,
    insecure_channel as insecure_aio_channel,
    secure_channel as secure_aio_channel,
)

from ..config import Config

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ["create_channel"]


@overload
def create_channel(config: "Config", *, blocking: Literal[False] = ...) -> "AioChannel":
    ...


@overload
def create_channel(config: "Config", *, blocking: Literal[True]) -> "Channel":
    ...


def create_channel(config: "Config", blocking: bool = False) -> "Channel":
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
        credentials = ssl_channel_credentials(
            root_certificates=config.ssl.ca,
            private_key=config.ssl.cert_key,
            certificate_chain=config.ssl.cert,
        )
        if config.access.token:
            # The grpc Credential objects do not actually define a formal interface, and are
            # used interchangeably in the code.
            #
            # Additionally there are some incorrect rules in the grpc-stubs typing rules that force
            # us to work around the type system.
            credentials = cast(
                ChannelCredentials,
                composite_channel_credentials(
                    credentials, metadata_call_credentials(GrpcAuth(config))
                ),
            )
        if blocking:
            return secure_channel(u.netloc, credentials, options)
        else:
            return secure_aio_channel(u.netloc, credentials, options)
    else:
        if blocking:
            return insecure_channel(u.netloc, options)
        else:
            return insecure_aio_channel(u.netloc, options)


class GrpcAuth(AuthMetadataPlugin):
    def __init__(self, config: "Config"):
        self._config = config

    def __call__(self, context: "AuthMetadataContext", callback: "AuthMetadataPluginCallback"):
        # This overly verbose type signature is here to satisfy mypy and grpc-stubs
        options = []  # type: List[Tuple[str, Union[str, bytes]]]

        # TODO: Add support here for refresh tokens
        token = self._config.access.token
        if token:
            # note: gRPC headers MUST be lowercased
            options.append(("authorization", "Bearer " + self._config.access.token))

        callback(tuple(options), None)
