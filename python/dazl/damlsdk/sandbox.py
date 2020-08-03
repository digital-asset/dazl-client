# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains utilities for starting up a local instance of the Ledger Sandbox,
either through the Sandbox or one local to the build tree of the project.
"""

import logging
import warnings
from pathlib import Path
from typing import Collection, Sequence, Optional, Type, Union

from ._process import SandboxProcessOptions, SandboxProcessWatcher
from ..model.core import DazlError
from ..model.ledger import TimeModel, StaticTimeModel, RealTimeModel
from ..model.network import SSLSettings


# TODO: This is currently 0.13.32 simply because that's what it was already set to, and we're trying
#  to preserve the existing behavior as much as can before we fully drop sandbox launching support.
DEFAULT_SDK_VERSION = '0.13.32'


def sandbox(dar_path: 'Union[str, Path, Collection[str], Collection[Path]]',
            port: 'Optional[int]' = None,
            time_model_type: 'Type[TimeModel]' = StaticTimeModel,
            sdk_version: 'str' = DEFAULT_SDK_VERSION,
            ssl_settings: 'Optional[SSLSettings]' = None,
            extra_args: 'Optional[Sequence[str]]' = None) \
        -> 'SandboxProcessWatcher':
    """
    Run an instance of the Sandbox.

    :param dar_path:
        The path to the DAML file or DAR file to open, or a list of files.
    :param port:
        The port to bind the server to, or ``None`` to pick a port at random and use it.
    :param time_model_type:
        The mode in which to run the Sandbox clock. Defaults to static time.
    :param sdk_version:
        The version of the SDK that specifies the Sandbox that is to be launched.
    :param ssl_settings:
        Settings that configure how the Sandbox is to start in HTTPS mode. If not supplied, the
        Sandbox starts up in HTTP.
    :param extra_args:
        Extra arguments to pass to the Sandbox.
    :return:
        A ``SandboxRunner`` that can be used as a context object to end the process.
    """
    warnings.warn(
        "The sandbox wrapper is deprecated; you should start the sandbox outside of dazl.",
        DeprecationWarning)

    # provide default values for backend and port if they were not provided
    if dar_path is None:
        raise ValueError('dar_path is required')

    if port is None:
        from ..util.io import find_free_port
        port = find_free_port()

    full_extra_args = [] if not extra_args else list(extra_args)
    if time_model_type == StaticTimeModel:
        pass
    elif time_model_type == RealTimeModel:
        full_extra_args.append('-w')

    if ssl_settings:
        if ssl_settings.cert_file:
            full_extra_args.extend(('--crt', ssl_settings.cert_file))
        if ssl_settings.cert_key_file:
            full_extra_args.extend(('--pem', ssl_settings.cert_key_file))
        if ssl_settings.ca_file:
            full_extra_args.extend(('--cacrt', ssl_settings.ca_file))

    args = ['daml', 'sandbox', *full_extra_args, '--port', port, *_validate_dar_path(dar_path)]
    return SandboxProcessWatcher(
        SandboxProcessOptions(args, logger=logging.getLogger('sandbox'), watch_port=port),
        f'http://localhost:{port}',
        sdk_version if sdk_version else DEFAULT_SDK_VERSION)


class SandboxError(DazlError):
    """
    Error raised when the Sandbox aborts abnormally.
    """
    def __init__(self, exit_code: int):
        self.exit_code = exit_code


def _validate_dar_path(dar_path: 'Union[str, Path, Collection[str], Collection[Path]]') \
        -> 'Collection[Path]':
    if isinstance(dar_path, str):
        paths = [Path(dar_path)]
    elif isinstance(dar_path, Path):
        paths = [dar_path]
    else:
        paths = [Path(p) for p in dar_path]

    for p in paths:
        ext = p.suffix.lower()
        if ext != '.dar':
            raise ValueError(f'unknown file type: {ext}')

    return paths
