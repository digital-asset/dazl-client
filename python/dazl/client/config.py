# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains configuration parameters used by the rest of the library.
"""

import warnings
from argparse import Namespace

from dataclasses import dataclass, field, fields, asdict
from typing import Any, Collection, List, Mapping, Optional, Sequence

from .. import LOG
from ..model.core import ConfigurationError, Party
from ..util.config_meta import config_field, \
    COUNT_TYPE, LOG_LEVEL_TYPE, PARTIES_TYPE, PATH_TYPE, PORT_TYPE, SECONDS_TYPE, STRING_TYPE, \
    URL_TYPE, VERIFY_SSL_TYPE, config_fields, add_argument

# If this environment variable is set, is used in place of a configuration file if none is supplied
# on the command-line.
DAZL_CONFIG_ENV = 'DAZL_CONFIG'


@dataclass(frozen=True)
class _PartyConfig:
    """
    Configuration for a specific party's client.
    """

    url: str = config_field(
        'URL where the Ledger API is hosted',
        param_type=URL_TYPE,
        short_alias='u',
        environment_variable='DAML_LEDGER_URL',
        deprecated_alias='participant_url')

    admin_url: Optional[str] = config_field(
        'URL where administrative functions are exposed',
        param_type=URL_TYPE,
        environment_variable='DAML_LEDGER_ADMIN_URL',
        default_value=None)

    ca_file: Optional[str] = config_field(
        'server certificate authority file',
        param_type=PATH_TYPE,
        default_value=None)

    cert_file: Optional[str] = config_field(
        'client certificate file',
        param_type=PATH_TYPE)

    cert_key_file: Optional[str] = config_field(
        'client certificate and key file',
        param_type=PATH_TYPE)

    verify_ssl: Optional[str] = config_field(
        'level of verification to use for SSL',
        param_type=VERIFY_SSL_TYPE)

    poll_interval: Optional[float] = config_field(
        'polling interval for receiving new events',
        param_type=SECONDS_TYPE,
        default_value=0.1)

    connect_timeout: Optional[float] = config_field(
        'number of seconds before giving up on a connection',
        param_type=SECONDS_TYPE,
        default_value=120)

    application_name: Optional[str] = config_field(
        'The name that this application uses to identify itself to the ledger.',
        param_type=STRING_TYPE,
        default_value='DAZL-Client')

    max_event_block_size: Optional[int] = config_field(
        'Maximum number of blocks to read in a single call.',
        param_type=COUNT_TYPE,
        default_value=100)

    max_command_batch_size: Optional[int] = config_field(
        'Maximum number of commands to batch up in a single transaction',
        param_type=COUNT_TYPE,
        default_value=100)

    max_command_batch_timeout: Optional[float] = config_field(
        'Maximum number of seconds to wait before sending out a command',
        param_type=SECONDS_TYPE,
        default_value=0.25)

    party_groups: Optional[Collection[str]] = config_field(
        'comma-separated list of broadcast parties',
        param_type=PARTIES_TYPE)


@dataclass(frozen=True)
class _NetworkConfig:
    """
    Configuration for the entire client library and all connected parties.
    """

    log_level: Optional[int] = config_field(
        'logging level for events for this party',
        param_type=LOG_LEVEL_TYPE,
        environment_variable='DAZL_LOG_LEVEL',
        short_alias='l')

    max_connection_count: Optional[int] = config_field(
        'Number of concurrent HTTP connections to have outstanding.',
        param_type=COUNT_TYPE,
        default_value=20)

    quiet_timeout: Optional[float] = config_field(
        'Number of seconds to wait after the client "thinks" it\'s done to hang around for',
        param_type=SECONDS_TYPE,
        default_value=1)

    idle_timeout: Optional[float] = config_field(
        'Maximum number of seconds of idle activity before automatically closing the client',
        param_type=SECONDS_TYPE,
        default_value=120)

    max_consequence_depth: Optional[int] = config_field(
        'The maximum number of times to wait for all parties to arrive at the same offset' +
        'before failing with an error',
        param_type=COUNT_TYPE,
        default_value=50)

    server_host: Optional[str] = config_field(
        'Server listening host. Used for OAuth web application flow callbacks.',
        param_type=STRING_TYPE)

    server_port: Optional[int] = config_field(
        'Server listening port. Used for OAuth web application flow callbacks.',
        param_type=PORT_TYPE)

    oauth_client_id: Optional[str] = config_field(
        'OAuth client ID',
        param_type=STRING_TYPE)

    oauth_client_secret: Optional[str] = config_field(
        'OAuth client secret (implies web application flow or backend application flow)',
        param_type=STRING_TYPE)

    oauth_token: Optional[str] = config_field(
        'OAuth token',
        param_type=STRING_TYPE)

    oauth_refresh_token: Optional[str] = config_field(
        'OAuth refresh token',
        param_type=STRING_TYPE)

    oauth_id_token: Optional[str] = config_field(
        'OpenID token (JWT formatted)',
        param_type=STRING_TYPE)

    oauth_token_uri: Optional[str] = config_field(
        'OAuth token URL',
        param_type=STRING_TYPE)

    oauth_redirect_uri: Optional[str] = config_field(
        'OAuth redirect URI (implies web application flow)',
        param_type=STRING_TYPE)

    oauth_auth_url: Optional[str] = config_field(
        'OAuth auth URL (implies mobile application flow)',
        param_type=STRING_TYPE)

    oauth_legacy_username: Optional[str] = config_field(
        'OAuth username (implies legacy application flow)',
        param_type=STRING_TYPE)

    oauth_legacy_password: Optional[str] = config_field(
        'OAuth password (implies legacy application flow)',
        param_type=STRING_TYPE)


@dataclass(frozen=True)
class _FlatConfig(_NetworkConfig, _PartyConfig):
    """
    A configuration object that assumes a single flat key-value structure suitable for parsing
    command-line or environment variable-based values.

    This configuration object is used as an intermediate holding object when parsing parameters
    from environment variables or command-line arguments.
    """
    parties: Collection[Party] = config_field(
        'comma-separated list of parties serviced by a participant node',
        param_type=PARTIES_TYPE,
        short_alias='p',
        environment_variable='DAML_LEDGER_PARTY',
        default_value=())


@dataclass(frozen=True)
class PartyConfig(_PartyConfig):
    party: Optional[Party] = None


@dataclass(frozen=True)
class NetworkConfig(_NetworkConfig):
    parties: 'Sequence[PartyConfig]' = field(default_factory=tuple)


def configure_parser(arg_parser, config_file_support=False):
    """
    Add standard options to an arg parser (later to be extracted out by ``get_config``).
    """
    if config_file_support:
        from os import environ
        default_config = environ.get(DAZL_CONFIG_ENV)
        group = arg_parser.add_argument_group('Configuration Settings')
        group.add_argument('--config', help='path to a YAML config file', default=default_config)

    party_config_fields = [fld.name for fld, _ in config_fields(_PartyConfig)]

    group = arg_parser.add_argument_group('Overall Settings')
    for fld, param in config_fields(_FlatConfig):
        if fld.name not in party_config_fields:
            add_argument(group, fld.name, param)

    group = arg_parser.add_argument_group('Per-Party Settings')
    for fld, param in config_fields(_PartyConfig):
        add_argument(group, fld.name, param)

    return arg_parser


def unflatten_config(config: '_FlatConfig') -> 'NetworkConfig':
    """
    Convert a :class:`_FlatConfig` to a :class:`NetworkConfig`.
    """
    config_dict = {k: v for k, v in asdict(config).items() if v is not None}
    network_dict = {fld.name: config_dict.get(fld.name) for fld in fields(_NetworkConfig)}
    party_dict = {fld.name: config_dict.get(fld.name) for fld in fields(_PartyConfig)}
    parties = tuple(PartyConfig(party=party, **party_dict) for party in config.parties)
    return NetworkConfig(parties=parties, **network_dict)


def parse_kwargs(*config: 'NetworkConfig', **kwargs) -> 'NetworkConfig':
    """
    Create a :class:`NetworkConfig` for the configuration settings.

    :param config:
        Instances of :class:`NetworkConfig`` objects to merge together.
    :param kwargs:
        Configuration options that are accepted either at the global level or at the party level.
    :return:
        An instance of :class:`NetworkConfig`.
    """
    configurations = list(config)  # type: List[NetworkConfig]
    if kwargs:
        args_dict = dict(_get_env_defaults())
        args_dict.update(_parse_args_dict(kwargs))
        flat_config = _FlatConfig(**args_dict)
        configurations.append(unflatten_config(flat_config))
    network_config = merge_configurations(*configurations)
    return validate_config(network_config)


def get_config(args: 'Namespace', config_file_support: bool = False) -> 'NetworkConfig':
    """
    Convert an ``argparse.Namespace`` to a fully-formed and valid :class:`NetworkConfig`.
    """
    args_dict = dict(_get_env_defaults())
    args_dict.update(_parse_args_ns(args))
    flat_config = _FlatConfig(**args_dict)
    network_config = unflatten_config(flat_config)
    return validate_config(network_config)


def fetch_config(path_or_url: Optional[str]) -> Optional[str]:
    """
    Attempts to fetch a config file from what looks like either a path or a URL.

    :param path_or_url: A file path or a URL.
    :return: The body of the config file.
    """
    if not path_or_url:
        return None

    from urllib.error import URLError, HTTPError
    from urllib.parse import urlparse
    from urllib.request import urlopen

    u = urlparse(path_or_url)
    if not u.scheme or u.scheme == 'file':
        try:
            with open(u.path, 'r') as buf:
                config_str = buf.read()
        except FileNotFoundError:
            raise ConfigurationError([f'Config file not found: {u.path}'])
    else:
        try:
            with urlopen(path_or_url) as buf:
                config_str = buf.read().decode('utf8')
        except HTTPError as error:
            raise ConfigurationError([f'HTTP {error.code}: {path_or_url}'])
        except URLError as error:
            if isinstance(error.args[0], ConnectionRefusedError):
                raise ConfigurationError([f'HTTP unreachable: {path_or_url}'])
            else:
                raise ConfigurationError([error.args[0]])

    return config_str


def _get_env_defaults() -> 'Mapping[str, Any]':
    from os import getenv
    kwargs = {}
    for fld, param in config_fields(_FlatConfig):
        if param.environment_variable:
            value = getenv(param.environment_variable)
            if value:
                kwargs[fld.name] = param.param_type.value_ctor(value)
    return kwargs


def _parse_args_ns(args: 'Namespace') -> 'Mapping[str, Any]':
    """
    Convert the values
    :param args:
    :return:
    """
    return {fld.name: getattr(args, fld.name)
            for fld in fields(_FlatConfig) if hasattr(args, fld.name)}


def _parse_args_dict(d: 'Mapping[str, Any]') -> 'Mapping[str, Any]':
    """
    Convert the key-value pairs in this mapping to keys that are defined on :class:`_FlatConfig`.

    :param d:
    :return:
    """
    kwargs = {}
    unknown_fields = set()
    for fld, param in config_fields(_FlatConfig):
        value = d.get(fld.name)
        if value is None:
            for key in param.alternate_keys:
                if d.get(key) is not None:
                    value = d.get(key)
                    break

        if value is None:
            for key in param.deprecated_aliases:
                if d.get(key) is not None:
                    warnings.warn(f'The {key} option is deprecated. Please use {fld.name} instead.',
                                  DeprecationWarning)
                    value = d.get(key)
                    break

        if value is not None:
            if param.param_type.value_ctor is not None:
                try:
                    value = param.param_type.value_ctor(value)
                except:
                    LOG.exception('Config key: %r; could not parse value: %r', fld.name, value)

            kwargs[fld.name] = value

    if unknown_fields:
        raise ValueError(f'unknown kwargs: {sorted(unknown_fields)}')
    return kwargs


def validate_config(config: 'NetworkConfig') -> 'NetworkConfig':
    failures = set()

    LOG.debug('Configuration: %s', config)

    if config.parties:
        for party_config in config.parties:
            if not party_config.url:
                failures.add(f'Party {party_config.party} has no Ledger API URL')
    else:
        failures.add('At least one party and a URL must be specified')

    if failures:
        raise ConfigurationError(failures)

    return config


def merge_configurations(*configurations: 'NetworkConfig') -> 'NetworkConfig':
    return configurations[0]
