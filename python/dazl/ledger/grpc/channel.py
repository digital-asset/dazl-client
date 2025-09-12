# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from urllib.parse import urlparse

from grpc import ssl_channel_credentials
from grpc.aio import Channel, insecure_channel, secure_channel

from ..config import Config

__all__ = ["create_channel"]


def create_channel(config: Config) -> Channel:
    """
    Create a :class:`Channel` for the specified configuration.

    Note that the returned channel never carries authorization; the caller is expected to supply
    auth tokens on every request.
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

        return secure_channel(u.netloc, credentials, tuple(options))
    else:
        return insecure_channel(u.netloc, options)
