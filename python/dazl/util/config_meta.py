# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains utilities required by :mod:`dazl.client.config`.
"""

import logging

from argparse import _ActionsContainer
from dataclasses import dataclass, field, fields, Field
from typing import Any, Callable, FrozenSet, Optional, Sequence, Tuple

from ..model.core import Party


def config_field(
        description: str,
        param_type: 'Optional[ConfigParameterType]' = None,
        default_value: Any = None,
        short_alias: Optional[str] = None,
        deprecated_alias: Optional[str] = None,
        environment_variable: Optional[str] = None) -> Field:
    return field(default=default_value, metadata={'dazl.config': ConfigParameter(
        description=description,
        param_type=param_type,
        default_value=default_value,
        short_aliases=frozenset([short_alias]) if short_alias else frozenset(),
        deprecated_aliases=frozenset([deprecated_alias]) if deprecated_alias else frozenset(),
        environment_variable=environment_variable
    )})


def config_fields(class_or_instance: Any) -> 'Sequence[Tuple[Field, ConfigParameter]]':
    return [(fld, fld.metadata.get('dazl.config')) for fld in fields(class_or_instance)]


@dataclass(frozen=True)
class ConfigParameter:
    description: str
    param_type: 'Optional[ConfigParameterType]' = None
    default_value: Any = None
    short_aliases: FrozenSet[str] = field(default_factory=frozenset)
    alternate_keys: FrozenSet[str] = field(default_factory=frozenset)
    deprecated_aliases: FrozenSet[str] = field(default_factory=frozenset)
    environment_variable: Optional[str] = None


@dataclass(frozen=True)
class ConfigParameterType:
    metavar: Optional[str]
    value_ctor: Callable[[Any], Any]


def add_argument(
        parser: '_ActionsContainer',
        key: str,
        config_param: 'ConfigParameter') -> None:
    if config_param.param_type is not None:
        aliases = ['--' + key.replace('_', '-')]
        for alias in config_param.short_aliases:
            aliases.append('-' + alias)
        for alias in config_param.alternate_keys:
            aliases.append('--' + alias.replace('_', '-'))
        for alias in config_param.deprecated_aliases:
            aliases.append('--' + alias.replace('_', '-'))

        if config_param.param_type.value_ctor == bool:
            parser.add_argument(
                *aliases,
                help=config_param.description,
                action='store_true')
        else:
            default_value = None
            if config_param.environment_variable is not None:
                import os
                default_value = os.getenv(config_param.environment_variable)
            if not default_value:
                default_value = config_param.default_value

            parser.add_argument(
                *aliases,
                type=config_param.param_type.value_ctor,
                metavar=config_param.param_type.metavar,
                help=config_param.description,
                default=default_value)


def _parse_url(obj):
    return obj


def _parse_log_level(obj) -> int:
    if not obj:
        return logging.WARNING
    if isinstance(obj, str):
        obj = obj.upper()
    p = logging.getLevelName(obj)
    return p


def _parse_str(obj: Any) -> Optional[str]:
    return str(obj) if obj is not None else None


def _parse_block_offset(obj):
    return obj


def _parse_party_list(obj) -> 'Sequence[Party]':
    if isinstance(obj, str):
        return [Party(p) for p in obj.split(',')]
    else:
        return obj


BOOLEAN_TYPE = ConfigParameterType(None, bool)
COUNT_TYPE = ConfigParameterType('COUNT', int)
BLOCK_OFFSET_TYPE = ConfigParameterType('OFFSET', _parse_block_offset)
LOG_LEVEL_TYPE = ConfigParameterType('LOG_LEVEL', _parse_log_level)
SECONDS_TYPE = ConfigParameterType('SECONDS', float)
URL_TYPE = ConfigParameterType('URL', _parse_url)
PARTIES_TYPE = ConfigParameterType('PARTIES', _parse_party_list)
PORT_TYPE = ConfigParameterType('PORT', int)
STRING_TYPE = ConfigParameterType('STRING', _parse_str)
PATH_TYPE = ConfigParameterType('PATH', _parse_str)
VERIFY_SSL_TYPE = ConfigParameterType('VERIFY_SSL', _parse_str)
