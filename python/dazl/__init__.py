# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains the Python API for interacting with the Ledger API.
"""
from ._logging import LOG

from .client import run, simple_client, async_network, Network, SimplePartyClient, AIOPartyClient
from .model.core import ContractId, ContractData, DazlError, Party
from .model.writing import create, exercise, exercise_by_key, create_and_exercise, \
    Command, CreateCommand, ExerciseCommand, ExerciseByKeyCommand, CreateAndExerciseCommand
from .util.logging import setup_default_logger
from .prim import FrozenDict as frozendict
from .pretty.table import write_acs


try:
    # This method is undocumented, but is required to read large size of model files when using
    # the C++ implementation.
    # noinspection PyPackageRequirements,PyUnresolvedReferences,PyProtectedMember
    from google.protobuf.pyext import _message
    _message.SetAllowOversizeProtos(True)

except ImportError:
    # ImportError for the Protobuf libraries is likely fatal, but this would not be the most helpful
    # place to throw an ImportError.
    pass


def _get_version() -> str:
    """
    Used to make the version of this library easily accessible programmatically.
    Two techniques are tried:
     1. Try to read it from the current package definition. This is what is used
        when trying to look up version information if dazl is installed via a
        wheel file.
     2. Use the value from the local pyproject.toml file (this is used when
        running dazl from source).
    """
    import pkg_resources
    from ast import literal_eval
    from configparser import ConfigParser
    from pathlib import Path
    try:
        return pkg_resources.require('dazl')[0].version
    except pkg_resources.DistributionNotFound:
        pass
    except Exception:
        return 'unknown'

    try:
        config = ConfigParser()
        config.read(Path(__file__).parent.parent / 'pyproject.toml')
        if 'tool.poetry' in config:
            poetry_section = config['tool.poetry']
            return literal_eval(poetry_section['version'])
    except Exception:  # noqa
        return 'unknown'


__version__ = _get_version()
