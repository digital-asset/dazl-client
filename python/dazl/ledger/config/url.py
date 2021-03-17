# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import timedelta
import ipaddress
from logging import Logger
from reprlib import repr
import sys
from types import MappingProxyType
from typing import TYPE_CHECKING, Optional
from urllib.parse import urlparse
import warnings

from ...prim import TimeDeltaLike, to_timedelta
from ._validate import Validator
from .exc import ConfigError, ConfigWarning

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable


__all__ = ["URLConfig", "create_url", "KNOWN_SCHEME_PORTS", "DEFAULT_CONNECT_TIMEOUT"]

if TYPE_CHECKING:
    # We refer to the Config class in a docstring and
    # without this import, Sphinx can't resolve the reference
    # noinspection PyUnresolvedReferences
    from . import Config

DEFAULT_CONNECT_TIMEOUT = timedelta(seconds=30)

# The set of schemes we understand, and the known ports that map to those schemes. The first port
# in the list is the default value for the scheme.
KNOWN_SCHEME_PORTS = MappingProxyType(
    {"http": (80, 7575, 8080), "https": (443, 8443), "grpc": (6865,), "grpcs": ()}
)

# some environment variables that we frequently refer to
DAML_LEDGER_URL = "DAML_LEDGER_URL"
DAML_LEDGER_HOST = "DAML_LEDGER_HOST"
DAML_LEDGER_PORT = "DAML_LEDGER_PORT"
DAML_LEDGER_SCHEME = "DAML_LEDGER_SCHEME"


def create_url(
    *,
    url: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[int] = None,
    scheme: Optional[str] = None,
    connect_timeout: Optional[TimeDeltaLike] = None,
    use_http_proxy: Optional[bool] = None,
    logger: Optional[Logger] = None,
):
    """
    Create an instance of :class:`URLConfig`, possibly with values taken from environment variables,
    or defaulted if otherwise unspecified.

    See :meth:`Config.create` for a more detailed description of these parameters.
    """
    validator = Validator(logger)

    with validator.new_case("URL") as case:
        url_field = case.string("url", url, "DAML_LEDGER_URL")

    with validator.new_case("URL parts") as case:
        host_field = case.string("host", host, "DAML_LEDGER_HOST")
        port_field = case.int("port", port, "DAML_LEDGER_PORT")
        scheme_field = case.string("scheme", scheme, "DAML_LEDGER_SCHEME")

    case_name = validator.validate()
    if case_name == "URL":
        url = sanitize_url(url_field.value)
    elif case_name == "URL parts":
        url = build_url(host_field.value, port_field.value, scheme_field.value)
    else:
        url = build_url("localhost", None, None)

    if use_http_proxy is None:
        hostname = urlparse(url).hostname
        if hostname is None:
            # this shouldn't have happened because we validate hostnames above
            raise ValueError("hostname of None unexpected here")

    cfg = SimpleURLConfig(
        url=url,
        connect_timeout=to_timedelta(connect_timeout)
        if connect_timeout is not None
        else DEFAULT_CONNECT_TIMEOUT,
        use_http_proxy=use_http_proxy,
    )
    validator.logger.debug("Created config: %r", cfg)
    return cfg


@runtime_checkable
class URLConfig(Protocol):
    """
    Configuration parameters for the remote host, including basic connection parameters that do not
    belong in :class:`AccessConfig`.
    """

    @property
    def url(self) -> str:
        """
        The full URL to connect to, including a protocol (scheme), host, and port.
        """
        raise NotImplementedError

    @property
    def use_http_proxy(self) -> bool:
        """
        Whether to allow the use of HTTP proxies.
        """
        raise NotImplementedError

    @property
    def connect_timeout(self) -> timedelta:
        """
        How long to wait for a connection before giving up.

        The default is 30 seconds.
        """
        raise NotImplementedError


class SimpleURLConfig:
    """
    Trivial implementation of the :class:`URLConfig` protocol.
    """

    def __init__(self, url: str, connect_timeout: timedelta, use_http_proxy: bool):
        self.url = url
        self.connect_timeout = connect_timeout
        self.use_http_proxy = use_http_proxy


def sanitize_url(url: str) -> str:
    """
    Perform some basic sanitization on a URL string (see :meth:`build_url`):
     * Supply a default protocol according to our general rules
     * Supply a port, even if one wasn't specified
     * Strip out any trailing slashes

    >>> sanitize_url("somewhere:1000")
    '//somewhere:1000'

    >>> sanitize_url("http://somewhere:1000")
    'http://somewhere:1000'

    >>> sanitize_url("http://somewhere:1000/")
    'http://somewhere:1000/'
    """
    first_slash = url.find("/")
    if first_slash == -1 or first_slash != url.find("//"):
        url = "//" + url

    original = urlparse(url)
    sanitized = urlparse(build_url(original.hostname, original.port, original.scheme))
    return original._replace(
        netloc=f"{sanitized.hostname}:{sanitized.port}", scheme=sanitized.scheme
    ).geturl()


def build_url(host: Optional[str], port: Optional[int], scheme: Optional[str]) -> str:
    """
    Build a URL from host/port/scheme components.

    :param host:
        The host to connect to. If unspecified, ``"localhost"`` is assumed.
    :param port:
        The port to connect to. If provided, must be a valid port number
        (between 1 and 65535 inclusive).
    :param scheme:
        The scheme to use (must be ``"http"``, ``"https"``, ``"grpc"``, ``"grpcs"`` or ``None``).
    :raises ConfigError: One or more of the passed parameters had invalid values.
    """

    if not host:
        host = "localhost"

    if port is not None and port != "":
        port = int(port)
        if not 1 <= port <= 65535:
            raise ConfigError(f"not a valid port number: {repr(port)}")

    if scheme:
        # Scheme specified; if a port is _not_ specified, the we'll try to figure out a
        # default from the scheme.
        scheme = scheme.lower()
        known_ports = KNOWN_SCHEME_PORTS.get(scheme)
        if known_ports is None:
            raise ConfigError(f"not a valid scheme: {repr(scheme)}")
        if port:
            return f"{scheme}://{host}:{port}"
        elif not known_ports:
            raise ConfigError(
                f"there is no default port for {scheme} URLs; you must specify a port"
            )
        else:
            return f"{scheme}://{host}:{known_ports[0]}"

    if port:
        # No scheme provided, but a port was provided.
        # See if we can infer the scheme from the provided port.
        for proposed_scheme, ports in KNOWN_SCHEME_PORTS.items():
            if port in ports:
                return f"{proposed_scheme}://{host}:{port}"

        warnings.warn(
            f"A port ({port}) was specified without supplying a scheme (http/https); "
            "will attempt connecting with https. Unless you are using a standard port, "
            "you should specify a scheme explicitly.",
            ConfigWarning,
        )

    # Neither scheme nor port are provided. If the host is localhost, then assume we're targeting
    # a sandbox; otherwise prefer an SSL/TLS connection.
    return f"grpc://{host}:6865" if is_localhost(host) else f"https://{host}:443"


def is_localhost(host: str) -> bool:
    if host == "localhost":
        return True
    try:
        addr = ipaddress.ip_address(host)
        return addr.is_loopback
    except ValueError:
        return False
