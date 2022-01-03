# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import NamedTuple, Optional, Tuple, Union
from urllib.parse import urlparse

from ..prim import Party


class HTTPConnectionSettings(NamedTuple):
    """
    Defines the unique settings that determine whether an HTTP connection can be shared across
    multiple clients.
    """

    scheme: str
    host: str
    port: int
    verify_ssl: str
    ssl_settings: "SSLSettings"
    oauth: "OAuthSettings"
    enable_http_proxy: bool

    def url(self, *path_components: str):
        """
        Return the base URL string for this settings, optionally appending path strings to the end
        of it.
        """
        base_url = "{}://{}:{}".format(self.scheme, self.host, self.port)
        for component in path_components:
            cmp = component.lstrip("/")
            base_url = base_url.rstrip("/") + "/" + cmp
        return base_url

    def __repr__(self):
        url = f"{self.scheme}://{self.host}:{self.port}"
        ssl_args = {}
        if self.verify_ssl:
            ssl_args["verify_ssl"] = self.verify_ssl
        if self.ssl_settings:
            ssl_args.update(self.ssl_settings._asdict())
        if ssl_args:
            return f"{url} ({ssl_args})"
        else:
            return url


class SSLSettings(NamedTuple):
    ca_file: Optional[str]
    cert_file: Optional[str]
    cert_key_file: Optional[str]

    def __bool__(self):
        return bool(self.ca_file or self.cert_file or self.cert_key_file)


class OAuthSettings(NamedTuple):
    token: Optional[str]
    refresh_token: Optional[str]
    id_token: Optional[str]
    token_uri: Optional[str]
    client_id: Optional[str]
    client_secret: Optional[str]
    redirect_uri: Optional[str]
    auth_url: Optional[str]
    auth_ca_file: Optional[str]
    auth_audience: Optional[str]


def connection_settings(
    url: str,
    party: "Union[None, str, Party]",
    oauth=None,
    default_scheme=None,
    verify_ssl=None,
    ca_file=None,
    cert_file=None,
    cert_key_file=None,
    enable_http_proxy=True,
) -> "Tuple[HTTPConnectionSettings, str]":
    if url is None:
        if party is not None:
            raise ValueError("URL is required for party %s" % party)
        else:
            raise ValueError("URL is required")
    try:
        # relative URLs have no meaning in this context; enforce that all URLs passed to us are
        # absolute so that things parse properly
        if "//" not in url:
            url = "//" + url

        if not default_scheme:
            default_scheme = "https" if ca_file or cert_file or cert_key_file else "http"

        components = urlparse(url, scheme=default_scheme, allow_fragments=False)
        if components.port is None:
            port = 443 if components.scheme in ("https", "grpcs") else 80
        else:
            port = components.port

        if components.hostname is None:
            raise ValueError("missing hostname")

        settings = HTTPConnectionSettings(
            scheme=components.scheme,
            host=components.hostname,
            port=port,
            verify_ssl=verify_ssl,
            oauth=oauth,
            ssl_settings=SSLSettings(
                ca_file=ca_file, cert_file=cert_file, cert_key_file=cert_key_file
            ),
            enable_http_proxy=enable_http_proxy,
        )
        return (settings, components.path.rstrip("/"))
    except ValueError:
        raise ValueError("Could not parse {}".format(url))
