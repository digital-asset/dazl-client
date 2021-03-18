# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse

from grpc import (
    AuthMetadataContext,
    AuthMetadataPlugin,
    AuthMetadataPluginCallback,
    composite_channel_credentials,
    metadata_call_credentials,
    ssl_channel_credentials,
)
from grpc.aio import Channel, insecure_channel, secure_channel

from ..config import Config

__all__ = ["create_channel"]


def create_channel(config: "Config") -> "Channel":
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
            credentials = composite_channel_credentials(
                credentials, metadata_call_credentials(GrpcAuth(config))
            )
        return secure_channel(u.netloc, credentials, options)
    else:
        return insecure_channel(u.netloc, options)


class GrpcAuth(AuthMetadataPlugin):
    def __init__(self, config: "Config"):
        self._config = config

    def __call__(self, context: "AuthMetadataContext", callback: "AuthMetadataPluginCallback"):
        options = []

        # TODO: Add support here for refresh tokens
        token = self._config.access.token
        if token:
            options.append(("Authorization", "Bearer " + self._config.access.token))

        callback(options, None)
